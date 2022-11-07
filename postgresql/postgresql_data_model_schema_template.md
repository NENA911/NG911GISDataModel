# NG9-1-1 Data Model PostGIS Template Script

The following SQL script is used to create the NG9-1-1 GIS Data Model template 
in PostgreSQL. This script is designed for PostgreSQL/PostGIS but may be 
adapted for other platforms.

## Instructions

Run the following lines of code in the Query tool on the database.

NOTE: The following script uses a SCHEMA "nena". If you chose to use a different 
domain replace "nena." with "<your schema>." in a text editor.

## Notes on Domains

Domains are based on WA state ArcPy script for ESRI file geodatabase as edited 
by NENA workgroup.

Domains are implemented in various ways based on their characteristics in some 
cases a new data type is created with CREATE DOMAIN and a short, fixed list in 
other cases a table is created with domain values as the primary key to support 
a foreign key constraint on matching columns some domain tables also have a 
lookup column to document code values just like  ESRI coded domains in WA 
state script additionally some domain tables implement pattern matching, 
ranges or other check constraints and finally individual check constraints on 
columns are used for minimal situations where only one table is involved.

## Fixes from v1.0

* Added missing `St_PreDir` and `St_PosDir` field missing from the v1.0 
  RoadCenterlines schema
* Corrected `longitude` check error from `CHECK ( -90 <= Longitude AND Longitude <= 90 )` 
  to `CHECK ( -180 <= Longitude AND Longitude <= 180 )` in multiple tables.
* Fixed typo `('PARK":"PARK(S)')` to `('PARK","PARK(S)')` in LegacyStreetTypes
  lookup table.
* Added missing relationship to ServiceURN. v1.0 included the look up table but 
  did not define the relationship.

## Schema Changes from v1.0

* Changed all `DOUBLE PRECISION` datatypes to `REAL` to reflect the `FLOAT`
  value defined in NENA-STA-006.2-2022
* Changed all `TIMESTAMP WITH TIME ZONE` datatypes to `TIMESTAMPTZ` which is the 
  proper datatype which is a time zone-aware data and time datatype. PostgreSQL 
  converts the `TIMESTAMPTZ` value into a UTC value and stores the UTC value in 
  the table.
* Changed all `CHARACTER VARYING` to `VARCHAR` which is the more common alias.
* Added `id` field otherwise editing is slow and open to error. Not part of the 
  standard but it best practice to have a `SERIAL` or `UUID` as the Primary Key. 
  The NGUID could fill this position but it would require creating a TRIGGER.
* Changed domain and reference tables to follow NENA table and field naming 
  conventions
* Improved documentation
* Reordered fields in schema to the same order as GIS Data Model documentation 
  for ease of quality assurance and control.

## Changes from v1 to v2

* Combined the Street Name and Legacy Directionals into a single lookup table 
  and added additional language directionals per NENA-STA-006.2-2022.

## Questions for WG

* Should the script include the creation of indexes on appropriate fields?
* Should lookup tables include a prefix to identify them more easily?
* Should the script include a trigger to create the NGUID?
* Should the `id` field be replaced by a UUID?
* Should the data model template be migrated to an ORM that would support 
  deployment to multiple databases? This would require a rewrite into Python.
* Need to discuss the use of Service URI in Service Boundary layers.
* Should we define dafaults such as Inc_Muni defaults to 'Unicorporated' or
  DiscrepAgencyID = 'subdomain.domain.tld'
* [v1.0] Should there be an ESN table or domain?

```sql
-- #############################################################################
-- Support tables
-- #############################################################################


/* *****************************************************************************
   DOMAIN:   nena.Agencies
   Used by:  All tables
   Source:   NENA-STA-006.2-2022, Section 5.9, p.51
   Notes:    Lookup table for discrepancy agencies values. This is used as a 
             PK/FK relationship in all layers. Agencies will need to be
             manually added later. The AgencyID field uses a regex check 
             constraing to ensure the proper format of the domain name.
   TODOS:    * Verify the regex expression works for all domain formats.
   ************************************************************************** */
DROP TABLE IF EXISTS nena.Agencies CASCADE;
CREATE TABLE nena.Agencies (
	AgencyID VARCHAR(75) PRIMARY KEY CHECK ( AgencyID ~* '(\w+\.)*\w+$' )
); 


/* *****************************************************************************
   DOMAIN:   nena.Country
   Used by:  ServiceBoundaryPolygons, A1Polygon - A5Polygon, CellSectorPoint
   Source:   NENA-STA-006.2-2022, Section 5.24, p.55
   Notes:    Domain for country creates a new data type 
   ************************************************************************** */
DROP DOMAIN IF EXISTS nena.Country CASCADE;
CREATE DOMAIN nena.Country AS VARCHAR(2)
CHECK ( VALUE IN ('US', 'CA', 'MX') ); 


/* *****************************************************************************
   TABLE:    nena.States
   Used by:  ServiceBoundaryPolygons, A1Polygon - A5Polygon, CellSectorPoint
   Source:   NENA-STA-006.2-2022, Section 5.107, p.77
   Notes:    If states or equivalents layer exists, then this should be dropped 
             as well local domain will probably be limited so this is best 
             maintained as a table
   ************************************************************************** */
DROP TABLE IF EXISTS nena.States CASCADE;
CREATE TABLE nena.States (
	State VARCHAR(2) PRIMARY KEY
, 	State_Name VARCHAR(50) NOT NULL 
);


/* *****************************************************************************
   TABLE:    nena.counties
   Used By:  A1Polygon - A5Polygon, CellSectorPoint
   Source:   NENA-STA-006.2-2022, Section 5.28, p.56
   Notes:    If counties or equivalents boundary layer is created then this should 
             be dropped and the layer should be used as the domain with pk/fk 
             constraint local listing will likely be limited to state or region 
   ************************************************************************** */
DROP TABLE  IF EXISTS nena.Counties CASCADE;
CREATE TABLE nena.Counties (
	County VARCHAR(100) PRIMARY KEY
); 


/* *****************************************************************************
   TABLE:    nena.AdditionalCodes
   Used By:  A1Polygon - A5Polygon
   Source:   NENA-STA-006.2-2022, Section 5.1, p.49
   Notes:    [v1.0 comment] Additional code is pk/fk
   ************************************************************************** */
DROP TABLE IF EXISTS nena.AdditionalCodes CASCADE;
CREATE TABLE nena.AdditionalCodes (
	AddCode VARCHAR(6) PRIMARY KEY
);


/* *****************************************************************************
   TABLE:    nena.StreetName_Parities
   Used By:  RoadCenterLine, StreetNameAliasTable, SiteStructureAddressPoint
   Source:   NENA-STA-006.2-2022, Sections 5.56, 5.57, 5.111, and 5.114. 
   Notes:    Combined both the NG9-1-1 and Legacy Directional loopups into a 
             single lookup table.
   ************************************************************************** */
-- lookup table for parity codes 
DROP TABLE IF EXISTS nena.StreetName_Parities CASCADE;
CREATE TABLE nena.StreetName_Parities (
	Parity VARCHAR(1) PRIMARY KEY 
,	Parity_lookup VARCHAR(20)
); 


/* *****************************************************************************
   TABLE:    nena.StreetName_Directionals
   Used By:  RoadCenterLine, StreetNameAliasTable, SiteStructureAddressPoint
   Source:   NENA-STA-006.2-2022, Sections 5.56, 5.57, 5.111, and 5.114. 
   Notes:    Combined both the NG9-1-1 and Legacy Directional loopups into a 
             single lookup table.
   ************************************************************************** */
-- directional as data type 
DROP DOMAIN IF EXISTS nena.StreetName_Directionals CASCADE;
CREATE DOMAIN nena.StreetName_Directionals AS CHARACTER VARYING (10) 
CHECK ( 
  VALUE IN (
    'North', 'South', 'East', 'West', 'Northeast', 'Northwest', ' Southeast', 
    'Southwest', 'Nord', 'Sud', 'Est', 'Ouest', 'Nord-Est', 'Nord-Ouest',
    'Sud-Est', 'Sud-Ouest'
  )
);


/* *****************************************************************************
   TABLE:    nena.StreetName_Types
   Used By:  RoadCenterLine, StreetNameAliasTable, SiteStructureAddressPoint
   Source:   NENA-STA-006.2-2022, Sections 5.113 and 5.117
   Notes:    This may be split into a PreType and PostType in the future and 
             may be expanded locally.
   ************************************************************************** */
DROP TABLE IF EXISTS nena.StreetName_Types CASCADE;
CREATE TABLE nena.StreetName_Types (
	StreetNameType VARCHAR(50) PRIMARY KEY
);


/* *****************************************************************************
   TABLE:    nena.StreetName_PreTypeSeparators
   Used By:  RoadCenterLine, StreetNameAliasTable, SiteStructureAddressPoint
   Source:   NENA-STA-006.2-2022, Sections 5.117, p.80
   ************************************************************************** */
DROP TABLE IF EXISTS nena.StreetName_PreTypeSeparators CASCADE;
CREATE TABLE nena.StreetName_PreTypeSeparators (
	Separator VARCHAR(20) PRIMARY KEY 
);


/* *****************************************************************************
   TABLE:    nena.StreetName_LegacyDirectionals
   Used By:  RoadCenterLine, StreetNameAliasTable, SiteStructureAddressPoint
   Source:   NENA-STA-006.2-2022, Sections 5.56, 5.57, 5.111, and 5.114. 
   Notes:    legacy directional as lookup
   ************************************************************************** */
DROP TABLE IF EXISTS nena.StreetName_LegacyDirectionals CASCADE;
CREATE TABLE nena.StreetName_LegacyDirectionals (
	Directional VARCHAR(2) PRIMARY KEY
,	Directional_lookup VARCHAR(10)
);


/* *****************************************************************************
   TABLE:    nena.StreetName_LegacyTypes
   Used By:  RoadCenterLine, SiteStructureAddressPoint
   Source:   NENA-STA-006.2-2022, Sections 5.58, p.64
   Notes:    This is limited to USPS Publication 28 main abbreviation lookup and 
             may be expanded locally.
   ************************************************************************** */
DROP TABLE IF EXISTS nena.StreetName_LegacyTypes CASCADE;
CREATE TABLE nena.StreetName_LegacyTypes (
	Abbreviation  VARCHAR(4) PRIMARY KEY	
,	Description VARCHAR(20) 
);


/* *****************************************************************************
   TABLE:    nena.PostalCodes
   Used By:  RoadCenterLines, SiteStructureAddressPoint
   Source:   NENA-STA-006.2-2022, Section 5.80, p.69
   Notes:    Postal code listing with regular expression match for US and 
             Canadian codes 
   ************************************************************************** */
DROP TABLE IF EXISTS nena.PostalCodes CASCADE; 
CREATE TABLE nena.PostalCodes (
	PostalCode CHARACTER VARYING (7) PRIMARY KEY CHECK ( PostalCode ~* '(\d{5})|([A-Z][0-9][A-Z] [0-9][A-Z][0-9])' )
); 


/* *****************************************************************************
   TABLE:    nena.PostalCommunities
   Used By:  RoadCenterLines, SiteStructureAddressPoint
   Source:   NENA-STA-006.2-2022, Section 5.84, p.70
   Notes:    Table list of postal communities will be locally populated 
   ************************************************************************** */
DROP TABLE IF EXISTS nena.PostalCommunities CASCADE;
CREATE TABLE nena.PostalCommunities (
	PostalCommunity CHARACTER VARYING (40) PRIMARY KEY 
) ;


/* *****************************************************************************
   TABLE:    nena.RoadCenterLine_RoadClasses
   Used By:  RoadCenterLines
   Source:   NENA-STA-006.2-2022, Section 5.96, p.96
   Notes:    Table listing of road classes
   ************************************************************************** */
DROP TABLE IF EXISTS nena.RoadCenterLine_RoadClasses CASCADE;
CREATE TABLE nena.RoadCenterLine_RoadClasses (
	RoadClass VARCHAR(24) PRIMARY KEY 
,	RoadClass_lookup TEXT
);


/* *****************************************************************************
   TABLE:    nena.RoadCenterLine_OneWays
   Used By:  RoadCenterLines
   Source:   NENA-STA-006.2-2022, Section 5.96, p.96
   Notes:    Lookup table for one way codes 
   ************************************************************************** */
DROP TABLE IF EXISTS nena.RoadCenterLine_OneWays CASCADE;
CREATE TABLE nena.RoadCenterLine_OneWays (
	OneWay VARCHAR(2) PRIMARY KEY 
,	OneWay_lookup VARCHAR(50)
);


/* *****************************************************************************
   TABLE:    nena.SiteStructureAddressPoint_PlaceTypes
   Used By:  SiteStructureAddressPoint
   Source:   NENA-STA-006.2-2022, Section 5.78, p.69
   Notes:    Lookup table for placetypes  
   ************************************************************************** */
DROP TABLE IF EXISTS nena.SiteStructureAddressPoint_PlaceTypes CASCADE;
CREATE TABLE nena.SiteStructureAddressPoint_PlaceTypes (
	PlaceType VARCHAR(50) PRIMARY KEY 
,	PlaceType_lookup TEXT 
); 


/* *****************************************************************************
   TABLE:    nena.SiteStructureAddressPoint_PlacementMethods
   Used By:  SiteStructureAddressPoint
   Source:   NENA-STA-006.2-2022, Section 5.79, p.69
   Notes:    Table listing for placement methods - could be expanded  
   ************************************************************************** */
DROP TABLE IF EXISTS nena.SiteStructureAddressPoint_PlacementMethods CASCADE;
CREATE TABLE nena.SiteStructureAddressPoint_PlacementMethods (
	PlacementMethod VARCHAR(25) PRIMARY KEY 
); 


/* *****************************************************************************
   TABLE:    nena.URIs
   Used By:  ServiceBoundaryPolygons
   Source:   NENA-STA-006.2-2022, Section 5.102, p.76
   Notes:    [v1.0 comment] There is a data type uri in the data model - what 
             is the pattern? Should this be implemented globally for service 
             uris, av card uris, and addl data or should there be individual 
             domains for the various URI fields?
             
             [TN Comment] The current implementation is messy and not well 
             thought out. This is an excellent example where a true relational 
             database implementation should be considered. A better solution 
             would be to implement a ServiceProvider table that contained 
             multiple fields currently in the ServiceBoundary layer fields with 
             the Agency Identifier, Service URI, Service Number, Agency vCard 
             URI, and Display Name. However, it may be a v3 decision as there 
             are changes occuring NENA-STA-010 that would negate several of 
             these fields.
   ************************************************************************** */
DROP TABLE IF EXISTS nena.URIs CASCADE;
CREATE TABLE nena.URIs (
	URI VARCHAR(254) PRIMARY KEY 
); 


/* *****************************************************************************
   TABLE:    nena.ServiceBoundary_URNs
   Used By:  ServiceBoundaryPolygons
   Source:   NENA-STA-006.2-2022, Section 5.103, p.76
   Notes:    Table listing of URNs
   TODO:     * Add Source URL
             * Verify values
   ************************************************************************** */
DROP TABLE IF EXISTS nena.ServiceBoundary_URNs CASCADE;
CREATE TABLE nena.ServiceBoundary_URNs (
	ServiceURN VARCHAR(254) PRIMARY KEY
,	ServiceURN_lookup TEXT
);


/* *****************************************************************************
   TABLE:    LocationMarker_Indicators
   Used By:  LocationMarkerPoints
   Source:   NENA-STA-006.2-2022, Section 5.59, p.64
   Notes:    Lookup table for LocationMarkerPoints
   ************************************************************************** */
DROP TABLE IF EXISTS nena.LocationMarker_Indicators CASCADE;
CREATE TABLE nena.LocationMarker_Indicators (
	Code VARCHAR(1) PRIMARY KEY 
,	Description VARCHAR(20)
);


/* *****************************************************************************
   TABLE:    LocationMarker_Units
   Used By:  LocationMarkerPoints
   Source:   NENA-STA-006.2-2022, Section 5.64, p.65
   Notes:    Lookup table for LocationMarkerPoints
   ************************************************************************** */
DROP TABLE IF EXISTS nena.LocationMarker_Units CASCADE;
CREATE TABLE nena.LocationMarker_Units (
  Unit VARCHAR(15) PRIMARY KEY
);


-- #############################################################################
-- NG9-1-1 Table Definitions
-- #############################################################################


/* *****************************************************************************
   TABLE:  nena.RoadCenterLine (Road Centerlines - REQUIRED)
   Source: NENA-STA-006.2-2022, Section 4.1.1, p.23
  *************************************************************************** */
DROP TABLE  IF EXISTS nena.RoadCenterline;
CREATE TABLE nena.RoadCenterline (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('LineString',4326)  NOT NULL  
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL
, Effective TIMESTAMPTZ
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, AdNumPre_L VARCHAR(15)
, AdNumPre_R VARCHAR(15)
, FromAddr_L INTEGER  NOT NULL  CHECK ( 0 <= FromAddr_L AND FromAddr_L <= 999999 )
, ToAddr_L INTEGER  NOT NULL  CHECK ( 0 <= ToAddr_L AND ToAddr_L <= 999999 )
, FromAddr_R INTEGER  NOT NULL  CHECK ( 0 <= FromAddr_R AND FromAddr_R <= 999999 )
, ToAddr_R INTEGER  NOT NULL  CHECK ( 0 <= ToAddr_R AND ToAddr_R <= 999999 )
, Parity_L VARCHAR(1)  NOT NULL  REFERENCES nena.StreetName_Parities(Parity)
, Parity_R VARCHAR(1)  NOT NULL  REFERENCES nena.StreetName_Parities(Parity)
, St_PreMod VARCHAR(15)   
, St_PreDir nena.StreetName_Directionals
, St_PreTyp VARCHAR(50)  REFERENCES nena.StreetName_Types(StreetNameType)
, St_PreSep VARCHAR(20)  REFERENCES nena.StreetName_PreTypeSeparators(Separator)
, St_Name VARCHAR(254)   
, St_PosTyp VARCHAR(50)  REFERENCES nena.StreetName_Types(StreetNameType)
, St_PosDir nena.StreetName_Directionals
, St_PosMod VARCHAR(25) 
, LSt_PreDir VARCHAR(2)  REFERENCES nena.StreetName_LegacyDirectionals(Directional)
, LSt_Name VARCHAR(75)   
, LSt_Typ VARCHAR(4)  REFERENCES nena.StreetName_LegacyTypes(Abbreviation)
, LSt_PosDir VARCHAR(2)  REFERENCES nena.StreetName_LegacyDirectionals(Directional)
, ESN_L VARCHAR(5)  CHECK ( ESN_L ~* '\w{3,5}' )
, ESN_R VARCHAR(5)  CHECK ( ESN_R ~* '\w{3,5}' )
, MSAGComm_L VARCHAR(30)   
, MSAGComm_R VARCHAR(30)  
, Country_L nena.Country  NOT NULL  
, Country_R nena.Country  NOT NULL 
, State_L VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
, State_R VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
, County_L VARCHAR(100)  NOT NULL  REFERENCES nena.Counties(County)
, County_R VARCHAR(100)  NOT NULL  REFERENCES nena.Counties(County)
, AddCode_L VARCHAR(6)  REFERENCES nena.AdditionalCodes(AddCode)
, AddCode_R VARCHAR(6)  REFERENCES nena.AdditionalCodes(AddCode)
, IncMuni_L VARCHAR(100)  NOT NULL  
, IncMuni_R VARCHAR(100)  NOT NULL  
, UnincCom_L VARCHAR(100)   
, UnincCom_R VARCHAR(100)
, NbrhdCom_L VARCHAR(100)   
, NbrhdCom_R VARCHAR(100)
, PostComm_L VARCHAR(40)  REFERENCES nena.PostalCommunities(PostalCommunity)
, PostComm_R VARCHAR(40)  REFERENCES nena.PostalCommunities(PostalCommunity)
, PostCode_L VARCHAR(7)  REFERENCES nena.PostalCodes(PostalCode)
, PostCode_R VARCHAR(7)  REFERENCES nena.PostalCodes(PostalCode)
, RoadClass VARCHAR(15)  REFERENCES nena.RoadCenterLine_RoadClasses(RoadClass)
, OneWay VARCHAR(2)  REFERENCES nena.RoadCenterLine_OneWays(OneWay)
, SpeedLimit INTEGER CHECK ( 1 <= SpeedLimit AND SpeedLimit <= 100 )
, Valid_L VARCHAR(1)  CHECK ( Valid_L  in ('Y','N') ) 
, Valid_R VARCHAR(1)  CHECK ( Valid_R  in ('Y','N') ) 
);


/* *****************************************************************************
   TABLE:  nena.StreetNameAliasTable (Street Name Aliases - Strongly Recommended)
   Source: NENA-STA-006.2-2022, Section 4.1.2.2, p.28
  *************************************************************************** */
DROP TABLE  IF EXISTS nena.StreetNameAliasTable;
CREATE TABLE nena.StreetNameAliasTable (
  id SERIAL  PRIMARY KEY
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ  
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, RCL_NGUID VARCHAR(254)  NOT NULL
, ASt_PreMod VARCHAR(15)
, ASt_PreDir nena.StreetName_Directionals
, ASt_PreTyp VARCHAR(50)  REFERENCES nena.StreetName_Types(StreetNameType)
, ASt_PreSep VARCHAR(20)  REFERENCES nena.StreetName_PreTypeSeparators(Separator)
, ASt_Name VARCHAR(254)  NOT NULL  
, ASt_PosTyp VARCHAR(50)  REFERENCES nena.StreetName_Types(StreetNameType)
, ASt_PosDir nena.StreetName_Directionals  
, ASt_PosMod VARCHAR(25)   
);


/* *****************************************************************************
   TABLE:  nena.SiteStructureAddressPoint (Site/Structure Address Points - REQUIRED)
   Source: NENA-STA-006.2-2022, Section 4.2.1, p.29
  *************************************************************************** */
DROP TABLE  IF EXISTS nena.SiteStructureAddressPoint;
CREATE TABLE nena.SiteStructureAddressPoint (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('Point',4326)  NOT NULL  
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ  
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, Country nena.Country  NOT NULL  
, State VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
, County VARCHAR(100)  NOT NULL  REFERENCES nena.Counties(County)
, AddCode VARCHAR(6)  REFERENCES nena.AdditionalCodes(AddCode)
, AddDataURI VARCHAR(254)
, Inc_Muni VARCHAR(100)  NOT NULL  
, Uninc_Comm VARCHAR(100)   
, Nbrhd_Comm VARCHAR(100)   
, AddNum_Pre VARCHAR(15)   
, Add_Number INTEGER   
, AddNum_Suf VARCHAR(15)
, St_PreMod VARCHAR(15)   
, St_PreDir nena.StreetName_Directionals 
, St_PreTyp VARCHAR(50)  REFERENCES nena.StreetName_Types(StreetNameType)
, St_PreSep VARCHAR(20)  REFERENCES nena.StreetName_PreTypeSeparators(Separator)
, St_Name VARCHAR(254)
, St_PosTyp VARCHAR(50)  REFERENCES nena.StreetName_Types(StreetNameType) 
, St_PosDir nena.StreetName_Directionals
, St_PosMod VARCHAR(25)
, LSt_PreDir VARCHAR(2)  REFERENCES nena.StreetName_LegacyDirectionals(Directional)
, LSt_Name VARCHAR(75)
, LSt_Typ VARCHAR(4)  REFERENCES nena.StreetName_LegacyTypes(Abbreviation)   
, LSt_PosDir VARCHAR(2)  REFERENCES nena.StreetName_LegacyDirectionals(Directional)
, ESN VARCHAR(5)
, MSAGComm VARCHAR(30)
, Post_Comm VARCHAR(40)  REFERENCES nena.PostalCommunities(PostalCommunity)
, Post_Code VARCHAR(7)  REFERENCES nena.PostalCodes(PostalCode)
, Post_Code4 VARCHAR(4)   
, Building VARCHAR(75)   
, Floor VARCHAR(75)   
, Unit VARCHAR(75)   
, Room VARCHAR(75)   
, Seat VARCHAR(75)   
, Addtl_Loc VARCHAR(225)   
, LandmkName VARCHAR(150)   
, Milepost VARCHAR(150)   
, Place_Type VARCHAR(50)  REFERENCES nena.SiteStructureAddressPoint_PlaceTypes(PlaceType)
, Placement VARCHAR(25)  REFERENCES nena.SiteStructureAddressPoint_PlacementMethods(PlacementMethod)
, Longitude REAL  CHECK ( -180 <= Longitude AND Longitude <= 180 )
, Latitude REAL  CHECK ( -90 <= Latitude AND Latitude <= 90 )
, Elevation INTEGER
);


/* *****************************************************************************
   TABLE:  nena.LandmarkNamePartTable (Landmark Name Parts - Strongly Recommended)
   Source: NENA-STA-006.2-2022, Section 4.2.2.2, p.35
  *************************************************************************** */
DROP TABLE  IF EXISTS nena.LandmarkNamePartTable;
CREATE TABLE nena.LandmarkNamePartTable (
  id SERIAL  PRIMARY KEY
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ NOT NULL 
, Effective TIMESTAMPTZ  
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, SSAP_NGUID VARCHAR(254)
, CLNA_NGUID VARCHAR(254) 
, LMNamePart VARCHAR(150)  NOT NULL   
, LMNP_Order INTEGER  NOT NULL  CHECK ( 1 <= LMNP_Order AND LMNP_Order <= 99 )
);


/* *****************************************************************************
   TABLE:  nena.LandmarkNameCompleteAliasTable (Complete Landmark Name Aliases - Strongly Recommended)
   Source: NENA-STA-006.2-2022, Section 4.2.3.2, p.39
  *************************************************************************** */
DROP TABLE IF EXISTS nena.LandmarkNameCompleteAliasTable;
CREATE TABLE nena.LandmarkNameCompleteAliasTable (
  id SERIAL  PRIMARY KEY
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ 
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, SSAP_NGUID VARCHAR(254)
, CLNAlias VARCHAR(150)
);


/* *****************************************************************************
   Service Boundaries - REQUIRED and optional
   Source: NENA-STA-006.2-2022, Section 4.3, p.39
   
   NOTE:   The table schema of each Service Boundary layer is identical. Only 
           the REQUIRED Service Boundary layers are included. If you wish to 
           use additional Service Boundary layers as defined in 
           NENA-STA-006.2-2002, Section 7.2, p. 82, copy a table below and 
           change the table name to the "Name" column in the "GIS Data Layers" 
           Registry.
     
   Questions: * How many shall we make? 
              * Should Service URN be a default value?
              * The use of nena.URIs is confusing and involves 
  *************************************************************************** */

DROP TABLE IF EXISTS nena.PsapPolygon;
CREATE TABLE nena.PsapPolygon (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('POLYGON', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ   
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, Country nena.Country  NULL  
, State VARCHAR(2)  NULL  REFERENCES nena.States(State)
, Agency_ID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, ServiceURI VARCHAR(254)  NOT NULL
, ServiceURN VARCHAR(50)  NOT NULL  REFERENCES nena.ServiceBoundary_URNs(ServiceURN)
, ServiceNum VARCHAR(15)
, AVcard_URI VARCHAR(254)  NOT NULL
, DsplayName VARCHAR(60)  NOT NULL
);

DROP TABLE IF EXISTS nena.PolicePolygon;
CREATE TABLE nena.PolicePolygon (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('POLYGON', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ  
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, Country nena.Country  NULL  
, State VARCHAR(2)  NULL  REFERENCES nena.States(State)
, Agency_ID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, ServiceURI VARCHAR(254)  NOT NULL
, ServiceURN VARCHAR(50)  NOT NULL  REFERENCES nena.ServiceBoundary_URNs(ServiceURN)
, ServiceNum VARCHAR(15)
, AVcard_URI VARCHAR(254)  NOT NULL
, DsplayName VARCHAR(60)  NOT NULL
);

DROP TABLE IF EXISTS nena.FirePolygon;
CREATE TABLE nena.FirePolygon (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('POLYGON', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ   
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, Country nena.Country  NULL  
, State VARCHAR(2)  NULL  REFERENCES nena.States(State)
, Agency_ID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, ServiceURI VARCHAR(254)  NOT NULL
, ServiceURN VARCHAR(50)  NOT NULL  REFERENCES nena.ServiceBoundary_URNs(ServiceURN)
, ServiceNum VARCHAR(15)
, AVcard_URI VARCHAR(254)  NOT NULL
, DsplayName VARCHAR(60)  NOT NULL
);

DROP TABLE IF EXISTS nena.EmsPolygon;
CREATE TABLE nena.EmsPolygon (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('POLYGON', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, Country nena.Country  NULL  
, State VARCHAR(2)  NULL  REFERENCES nena.States(State)
, Agency_ID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, ServiceURI VARCHAR(254)  NOT NULL
, ServiceURN VARCHAR(50)  NOT NULL  REFERENCES nena.ServiceBoundary_URNs(ServiceURN)
, ServiceNum VARCHAR(15)
, AVcard_URI VARCHAR(254)  NOT NULL
, DsplayName VARCHAR(60)  NOT NULL
);


/* *****************************************************************************
   TABLE:  nena.ProvisioningPolygon (Provisioning Boundaries - REQUIRED)
   Source: NENA-STA-006.2-2022, Section 4.4, p.42
  *************************************************************************** */
DROP TABLE  IF EXISTS nena.ProvisioningPolygon;
CREATE TABLE nena.ProvisioningPolygon (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('POLYGON', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ 
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE 
);


/* *****************************************************************************
   TABLE:  nena.A1Polygon (States or Equivalents - Strongly Recommended)
   Source: NENA-STA-006.2-2022, Section 4.5.1, p.43
  *************************************************************************** */
DROP TABLE  IF EXISTS nena.A1Polygon;
CREATE TABLE nena.A1Polygon (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('POLYGON', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ   
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE 
, Country nena.Country  NOT NULL   
, State VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
);


/* *****************************************************************************
   TABLE:  nena.A2Polygon (Counties or Equivalents - Strongly Recommended)
   Source: NENA-STA-006.2-2022, Section 4.5.2, p.43
  *************************************************************************** */
DROP TABLE  IF EXISTS nena.A2Polygon;
CREATE TABLE nena.A2Polygon (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('POLYGON', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ   
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE 
, Country nena.Country  NOT NULL   
, State VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
, County VARCHAR(100)  NOT NULL   REFERENCES nena.Counties(County)
);


/* *****************************************************************************
   TABLE:  nena.A3Polygon (Incorporated Municipalties - Strongly Recommended)
   Source: NENA-STA-006.2-2022, Section 4.5.3, p.43
  *************************************************************************** */
DROP TABLE  IF EXISTS nena.A3Polygon;
CREATE TABLE nena.A3Polygon (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('POLYGON', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ 
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE 
, Country nena.Country  NOT NULL   
, State VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
, County VARCHAR(100)  NOT NULL  REFERENCES nena.Counties(County)
, AddCode VARCHAR(6)  REFERENCES nena.AdditionalCodes(AddCode)
, Inc_Muni VARCHAR(100)  NOT NULL  
);


/* *****************************************************************************
   TABLE:  nena.A4Polygon (Unincorporated Communities - Strongly Recommended)
   Source: NENA-STA-006.2-2022, Section 4.5.4, p.44
  *************************************************************************** */
DROP TABLE  IF EXISTS nena.A4Polygon;
CREATE TABLE nena.A4Polygon (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('POLYGON', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ NOT NULL 
, Effective TIMESTAMPTZ  
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE 
, Country nena.Country  NOT NULL   
, State VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
, County VARCHAR(100)  NOT NULL  REFERENCES nena.Counties(County)
, AddCode VARCHAR(6)  REFERENCES nena.AdditionalCodes(AddCode)
, Inc_Muni VARCHAR(100)  NOT NULL
, Uninc_Comm VARCHAR(100) NOT NULL
);


/* *****************************************************************************
   TABLE:  nena.A5Polygon (Neighborhood Communities - Strongly Recommended)
   Source: NENA-STA-006.2-2022, Section 4.5.5, p.45
  *************************************************************************** */
DROP TABLE  IF EXISTS nena.A5Polygon;
CREATE TABLE nena.A5Polygon (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('POLYGON', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE 
, Country nena.Country  NOT NULL   
, State VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
, County VARCHAR(100)  NOT NULL  REFERENCES nena.Counties(County)
, AddCode VARCHAR(6)  REFERENCES nena.AdditionalCodes(AddCode)
, Inc_Muni VARCHAR(100)  NOT NULL
, Uninc_Comm VARCHAR(100) NOT NULL
, Nbrhd_Comm VARCHAR(100)  NOT NULL  
);


/* *****************************************************************************
   TABLE:  nena.RailroadCenterLine (Railroads - Recommended)
   Source: NENA-STA-006.2-2022, Section 4.6, p.45
  *************************************************************************** */
DROP TABLE  IF EXISTS nena.RailroadCenterLine;
CREATE TABLE nena.RailroadCenterLine (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('LineString', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ  
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE 
, RLOwn VARCHAR(100)
, RLOp VARCHAR(100)
, RLName VARCHAR(100)
, RMPL REAL
, RMPH REAL
);


/* *****************************************************************************
   TABLE:  nena.HydrologyLine (Hydrology Line - Recommended)
   Source: NENA-STA-006.2-2022, Section 4.7.1, p.46
  *************************************************************************** */
DROP TABLE IF EXISTS nena.HydrologyLine;
CREATE TABLE nena.HydrologyLine (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('LineString', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ  
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, HS_Name VARCHAR(100)   
, HS_Type VARCHAR(100)
);


/* *****************************************************************************
   TABLE:  nena.HydrologyPolygon (Hydrology Line - Recommended)
   Source: NENA-STA-006.2-2022, Section 4.7.2, p.46
  *************************************************************************** */
DROP TABLE IF EXISTS nena.HydrologyPolygon;
CREATE TABLE nena.HydrologyPolygon (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('LineString', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ 
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, HP_Name VARCHAR(100)   
, HP_Type VARCHAR(100)
);


/* *****************************************************************************
   TABLE:  nena.CellSectorPoint (Cell Sectors - Recommended)
   Source: NENA-STA-006.2-2022, Section 4.8, p.47
  *************************************************************************** */
DROP TABLE IF EXISTS nena.CellSectorPoint;
CREATE TABLE nena.CellSectorPoint (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('POINT', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ   
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, Country nena.Country  NOT NULL
, State VARCHAR(2)  NOT NULL   REFERENCES nena.States(State)
, County VARCHAR(100)  NOT NULL   REFERENCES nena.Counties(County)
, Site_ID VARCHAR(10)   
, Sector_ID VARCHAR(4)  NOT NULL  
, Switch_ID VARCHAR(10)   
, CMarket_ID VARCHAR(10)   
, CSite_Name VARCHAR(10)   
, ESRD_ESRK INTEGER   
, ESRK_Last INTEGER
, CSctr_Ornt VARCHAR(4)  NOT NULL  
, Technology VARCHAR(10)  NOT NULL
, SSAP_NGUID VARCHAR(254)
, Longitude REAL  CHECK ( -180 <= Longitude AND Longitude <= 180 ) 
, Latitude REAL  CHECK ( -90 <= Latitude AND Latitude <= 90 )
);


/* *****************************************************************************
   TABLE:  nena.LocationMarkerPoint (Location Markers - Recommended)
   Source: NENA-STA-006.2-2022, Section 4.9, p.48
  *************************************************************************** */
DROP TABLE  IF EXISTS nena.LocationMarkerPoint;
CREATE TABLE nena.LocationMarkerPoint (
  id SERIAL  PRIMARY KEY
, geom GEOMETRY ('POINT', 4326)  NOT NULL 
, DiscrpAgID VARCHAR(100)  NOT NULL  REFERENCES nena.Agencies(AgencyID)
, DateUpdate TIMESTAMPTZ  NOT NULL 
, Effective TIMESTAMPTZ 
, Expire TIMESTAMPTZ
, NGUID VARCHAR(254)  NOT NULL  UNIQUE
, LM_Unit VARCHAR(15)  REFERENCES nena.LocationMarker_Units(Unit)
, LM_Value REAL  
, LM_Rte VARCHAR(100)
, LM_Label VARCHAR(100)
, LM_Type VARCHAR(15)   
, LM_Ind VARCHAR(1)  NOT NULL  REFERENCES nena.LocationMarker_Indicators(Code)
);
```
