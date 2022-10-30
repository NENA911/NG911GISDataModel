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

* Corrected `longitude` check error from `CHECK ( -90 <= Longitude AND Longitude <= 90 )` 
  to `CHECK ( -180 <= Longitude AND Longitude <= 180 )` in multiple tables.
* ServiceURN was never hooked up

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

## Changes from v1 to v2

* 

## Questions for WG

* Should the script include indexes?
* Should lookup tables include a prefix to identify them more easily?
* Should the script include a trigger to create the NGUID?
* Should the `id` field be replaced by a UUID?
* Should the data model template be migrated to an ORM that would support 
  deployment to multiple databases? This would require a rewrite into Python.
* Need to discuss the use of Service URI in Service Boundary layers.
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
	County VARCHAR(75) PRIMARY KEY
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


-- directional as data type 
DROP DOMAIN IF EXISTS nena.Directional CASCADE;
CREATE DOMAIN nena.Directional AS VARCHAR(9) 
CHECK ( VALUE IN ('North', 'South', 'East', 'West', 'Northeast', 'Northwest', ' Southeast', 'Southwest') );

-- legacy directional as lookup
DROP TABLE IF EXISTS nena.LegacyDirectionals CASCADE;
CREATE TABLE nena.LegacyDirectionals (
	LegacyDirectional VARCHAR(2) PRIMARY KEY
,	Legacy1Directional_lookup VARCHAR(9)
);
INSERT INTO nena.LegacyDirectionals VALUES
	('N','North')
, 	('S','Southwest')
, 	('E','East')
, 	('W','West')
, 	('NE','Northeast')
,	('NW','Northwest')
,	('SE','Southeast')
,	('SW','Southwest')
;

-- Legacy Street Name Types table
-- this is limited  to Pub 28 main abbrev. lookup 
-- Production DB would have similar table with much longer list 
-- of abbreviation lookups e.g. for parsing 
DROP TABLE IF EXISTS nena.LegacyStreetNameTypes CASCADE;
CREATE TABLE nena.LegacyStreetNameTypes (
	LegacyStreetNameType  VARCHAR(4) PRIMARY KEY	
,	LegacyStreetNameType_lookup VARCHAR(20) 
);
INSERT INTO nena.LegacyStreetNameTypes VALUES 
	('ALY','ALLEY')
,	('ANX','ANEX')
,	('ARC','ARCADE')
,	('AVE','AVENUE')
,	('BYU','BAYOU')
,	('BCH','BEACH')
,	('BND','BEND')
,	('BLF','BLUFF')
,	('BLFS','BLUFFS')
,	('BTM','BOTTOM')
,	('BLVD','BOULEVARD')
,	('BR','BRANCH')
,	('BRG','BRIDGE')
,	('BRK','BROOK')
,	('BRKS','BROOKS')
,	('BG','BURG')
,	('BGS','BURGS')
,	('BYP','BYPASS')
,	('CP','CAMP')
,	('CYN','CANYON')
,	('CPE','CAPE')
,	('CSWY','CAUSEWAY')
,	('CTR','CENTER')
,	('CTRS','CENTERS')
,	('CIR','CIRCLE')
,	('CIRS','CIRCLES')
,	('CLF','CLIFF')
,	('CLFS','CLIFFS')
,	('CLB','CLUB')
,	('CMN','COMMON')
,	('CMNS','COMMONS')
,	('COR','CORNER')
,	('CORS','CORNERS')
,	('CRSE','COURSE')
,	('CT','COURT')
,	('CTS','COURTS')
,	('CV','COVE')
,	('CVS','COVES')
,	('CRK','CREEK')
,	('CRES','CRESCENT')
,	('CRST','CREST')
,	('XING','CROSSING')
,	('XRD','CROSSROAD')
,	('XRDS','CROSSROADS')
,	('CURV','CURVE')
,	('DL','DALE')
,	('DM','DAM')
,	('DV','DIVIDE')
,	('DR','DRIVE')
,	('DRS','DRIVES')
,	('EST','ESTATE')
,	('ESTS','ESTATES')
,	('EXPY','EXPRESSWAY')
,	('EXT','EXTENSION')
,	('EXTS','EXTENSIONS')
,	('FALL','FALL')
,	('FLS','FALLS')
,	('FRY','FERRY')
,	('FLD','FIELD')
,	('FLDS','FIELDS')
,	('FLT','FLAT')
,	('FLTS','FLATS')
,	('FRD','FORD')
,	('FRDS','FORDS')
,	('FRST','FOREST')
,	('FRG','FORGE')
,	('FRGS','FORGES')
,	('FRK','FORK')
,	('FRKS','FORKS')
,	('FT','FORT')
,	('FWY','FREEWAY')
,	('GDN','GARDEN')
,	('GDNS','GARDENS')
,	('GTWY','GATEWAY')
,	('GLN','GLEN')
,	('GLNS','GLENS')
,	('GRN','GREEN')
,	('GRNS','GREENS')
,	('GRV','GROVE')
,	('GRVS','GROVES')
,	('HBR','HARBOR')
,	('HBRS','HARBORS')
,	('HVN','HAVEN')
,	('HTS','HEIGHTS')
,	('HWY','HIGHWAY')
,	('HL','HILL')
,	('HLS','HILLS')
,	('HOLW','HOLLOW')
,	('INLT','INLET')
,	('IS','ISLAND')
,	('ISS','ISLANDS')
,	('ISLE','ISLE')
,	('JCT','JUNCTION')
,	('JCTS','JUNCTIONS')
,	('KY','KEY')
,	('KYS','KEYS')
,	('KNL','KNOLL')
,	('KNLS','KNOLLS')
,	('LK','LAKE')
,	('LKS','LAKES')
,	('LAND','LAND')
,	('LNDG','LANDING')
,	('LN','LANE')
,	('LGT','LIGHT')
,	('LGTS','LIGHTS')
,	('LF','LOAF')
,	('LCK','LOCK')
,	('LCKS','LOCKS')
,	('LDG','LODGE')
,	('LOOP','LOOP')
,	('MALL','MALL')
,	('MNR','MANOR')
,	('MNRS','MANORS')
,	('MDW','MEADOW')
,	('MDWS','MEADOWS')
,	('MEWS','MEWS')
,	('ML','MILL')
,	('MLS','MILLS')
,	('MSN','MISSION')
,	('MTWY','MOTORWAY')
,	('MT','MOUNT')
,	('MTN','MOUNTAIN')
,	('MTNS','MOUNTAINS')
,	('NCK','NECK')
,	('ORCH','ORCHARD')
,	('OVAL','OVAL')
,	('OPAS','OVERPASS')
,	('PARK','PARK(S)')
,	('PKWY','PARKWAY(S)')
,	('PASS','PASS')
,	('PSGE','PASSAGE')
,	('PATH','PATH')
,	('PIKE','PIKE')
,	('PNE','PINE')
,	('PNES','PINES')
,	('PL','PLACE')
,	('PLN','PLAIN')
,	('PLNS','PLAINS')
,	('PLZ','PLAZA')
,	('PT','POINT')
,	('PTS','POINTS')
,	('PRT','PORT')
,	('PRTS','PORTS')
,	('PR','PRAIRIE')
,	('RADL','RADIAL')
,	('RAMP','RAMP')
,	('RNCH','RANCH')
,	('RPD','RAPID')
,	('RPDS','RAPIDS')
,	('RST','REST')
,	('RDG','RIDGE')
,	('RDGS','RIDGES')
,	('RIV','RIVER')
,	('RD','ROAD')
,	('RDS','ROADS')
,	('RTE','ROUTE')
,	('ROW','ROW')
,	('RUE','RUE')
,	('RUN','RUN')
,	('SHL','SHOAL')
,	('SHLS','SHOALS')
,	('SHR','SHORE')
,	('SHRS','SHORES')
,	('SKWY','SKYWAY')
,	('SPG','SPRING')
,	('SPGS','SPRINGS')
,	('SPUR','SPUR(S)')
,	('SQ','SQUARE')
,	('SQS','SQUARES')
,	('STA','STATION')
,	('STRA','STRAVENUE')
,	('STRM','STREAM')
,	('ST','STREET')
,	('STS','STREETS')
,	('SMT','SUMMIT')
,	('TER','TERRACE')
,	('TRWY','THROUGHWAY')
,	('TRCE','TRACE')
,	('TRAK','TRACK')
,	('TRFY','TRAFFICWAY')
,	('TRL','TRAIL')
,	('TRLR','TRAILER')
,	('TUNL','TUNNEL')
,	('TPKE','TURNPIKE')
,	('UPAS','UNDERPASS')
,	('UN','UNION')
,	('UNS','UNIONS')
,	('VLY','VALLEY')
,	('VLYS','VALLEYS')
,	('VIA','VIADUCT')
,	('VW','VIEW')
,	('VWS','VIEWS')
,	('VLG','VILLAGE')
,	('VLGS','VILLAGES')
,	('VL','VILLE')
,	('VIS','VISTA')
,	('WALK','WALK(S)')
,	('WALL','WALL')
,	('WAY','WAY')
,	('WAYS','WAYS')
,	('WL','WELL')
,	('WLS','WELLS')
;




-- lookup table for one way codes 
DROP TABLE IF EXISTS nena.OneWays CASCADE;
CREATE TABLE nena.OneWays (
	OneWay VARCHAR(2) PRIMARY KEY 
,	OneWay_lookup VARCHAR(50)
);
INSERT INTO nena.OneWays VALUES 
	('B', 'Travel in both directions allowed')
,	('FT','One-way traveling from FROM node to TO node')
,	('TF','One way traveling from TO node to FROM node')
; 

-- lookup table for parity codes 
DROP TABLE IF EXISTS nena.Parities CASCADE;
CREATE TABLE nena.Parities (
	Parity VARCHAR(1) PRIMARY KEY 
,	Parity_lookup VARCHAR(20)
); 
INSERT INTO nena.Parities VALUES 
	('O','Odd')
,	('E', 'Even')
,	('B','Both')
,	('Z','Address Range 0-0')
; 

-- table listing for placement methods - could be expanded 
DROP TABLE IF EXISTS nena.PlacementMethods CASCADE;
CREATE TABLE nena.PlacementMethods (
	PlacementMethod VARCHAR(25) PRIMARY KEY 
); 
INSERT INTO nena.PlacementMethods VALUES 
	('Geocoding')
,	('Parcel')
,	('Property Access')
,	('Structure')
,	('Site')
,	('Unknown')
;

-- lookup table for placetypes 
DROP TABLE IF EXISTS nena.PlaceTypes CASCADE;
CREATE TABLE nena.PlaceTypes (
	PlaceType VARCHAR(50) PRIMARY KEY 
,	PlaceType_lookup TEXT 
); 
INSERT INTO nena.PlaceTypes VALUES 
	('airport','A place from which aircrafts operate, such as an airport or heliport.')
,	('arena','Enclosed area used for sports events.')
,	('bank','Business establishment in which money is kept for saving, commercial purposes, is invested, supplied for loans, or exchanged.')
,	('bar','A bar or saloon.')
,	('bus-station','Terminal that serves bus passengers, such as a bus depot or bus terminal.')
,	('cafe','Usually a small and informal establishment that serves various refreshments (such as coffee); coffee shop.')
,	('classroom','Academic classroom or lecture hall.')
,	('club','Dance club, nightclub, or discotheque.')
,	('construction','Construction site.')
,	('convention-center','Convention center or exhibition hall.')
,	('government','Government building, such as those used by the legislative, executive, or judicial branches of governments, including court houses, police stations, and military installations.')
,	('hospital','Hospital, hospice, medical clinic, mental institution, or doctor''s office.')
,	('hotel','Hotel, motel, inn, or other lodging establishment.')
,	('industrial','Industrial setting, such as a manufacturing floor or power plant.')
,	('library','Library or other public place in which literary and artistic materials, such as books, music, periodicals, newspapers, pamphlets, prints, records, and tapes, are kept for reading, reference, or lending.')
,	('office','Business setting, such as an office.')
,	('other','A place without a registered place type representation.')
,	('outdoors','Outside a building, in or into the open air, such as a park or city streets.')
,	('parking','A parking lot or parking garage.')
,	('place-of-worship','A religious site where congregations gather for religious observances, such as a church, chapel, meetinghouse, mosque, shrine, synagogue, or temple.')
,	('prison','Correctional institution where persons are confined while on trial or for punishment, such as a prison, penitentiary, jail, brig.')
,	('public','Public area such as a shopping mall, street, park, public building, train station, or airport or in public conveyance such as a bus, train, plane, or ship. This general description encompasses the more precise descriptors ''street'', ''public-transport'', ''airport'' and so on.')
,	('residence','A private or residential setting, not necessarily the personal residence of the entity, e.g., including a friend''s home.')
,	('restaurant','Restaurant, coffee shop, or other public dining establishment.')
,	('school','School or university property, but not necessarily a classroom or library.')
,	('shopping-area','Shopping mall or shopping area. This area is a large, often enclosed, shopping complex containing various stores, businesses, and restaurants usually accessible by common passageways.')
,	('stadium','Large, usually open structure for sports events, including a racetrack.')
,	('store','Place where merchandise is offered for sale, such as a shop.')
,	('street','A public thoroughfare, such as an avenue, street, alley, lane, or road, including any sidewalks.')
,	('theater','Theater, lecture hall, auditorium, classroom, movie theater, or similar facility designed for presentations, talks, plays, music performances, and other events involving an audience.')
,	('train-station','Terminal where trains load or unload passengers or goods; railway station, railroad station, railroad terminal, train depot.')
,	('unknown','The type of place is unknown.')
,	('warehouse','Place in which goods or merchandise are stored, such as a storehouse or self-storage facility.')
,	('water','In, on, or above bodies of water, such as an ocean, lake, river, canal, or other waterway.')
;

-- postal code listing with regular expression match for US and Canadian codes 
DROP TABLE IF EXISTS nena.PostalCodes CASCADE; 
CREATE TABLE nena.PostalCodes (
	PostalCode VARCHAR(7) PRIMARY KEY CHECK ( PostalCode ~* '(\d{5})|([A-Z][0-9][A-Z] [0-9][A-Z][0-9])' )
); 

-- table list of postal communities will be locally populated 
DROP TABLE IF EXISTS nena.PostalCommunities CASCADE;
CREATE TABLE nena.PostalCommunities (
	PostalCommunity VARCHAR(40) PRIMARY KEY 
) ;

-- table list of road classes 
DROP TABLE IF EXISTS nena.RoadClasses CASCADE;
CREATE TABLE nena.RoadClasses (
	RoadClass VARCHAR(15) PRIMARY KEY 
,	RoadClass_lookup TEXT
);
INSERT INTO nena.RoadClasses VALUES 
	('Primary','Primary roads are limited-access highways that connect to other roads only at interchanges and not at at-grade intersections')
,	('Secondary','Secondary roads are main arteries that are not limited access, usually in the U.S. highway, state highway, or county highway systems.')
,	('Local','Generally a paved non-arterial street, road, or byway that usually has a single lane of traffic in each direction.')
,	('Ramp','A road that allows controlled access from adjacent roads onto a limited access highway, often in the form of a cloverleaf interchange.')
,	('Service Drive','A road, usually paralleling a limited access highway, that provides access to structures and/or service facilities along the highway')
,	('Vehicular Trail','An unpaved dirt trail where a four-wheel drive vehicle is required. These vehicular trails are found almost exclusively in very rural areas.')
,	('Walkway','A path that is used for walking, being either too narrow for or legally restricted from vehicular traffic.')
,	('Stairway','A pedestrian passageway from one level to another by a series of steps.')
,	('Alley','A service road that does not generally have associated addressed structures and is usually unnamed. It is located at the rear of buildings and properties and is used for deliveries.')
,	('Private','A road within private property that is privately maintained for service, extractive, or other purposes. These roads are often unnamed.')
,	('Parking Lot','The main travel route for vehicles through a paved parking area. This may include unnamed roads through apartment/condominium/office complexes where pull-in parking spaces line the road.')
,	('Trail','(Ski, Bike, Walking/Hikding Trail) is generally a path used by human powered modes of transportation.')
,	('Bridle Path','A path that is used for horses, being either too narrow for or legally restricted from vehicular traffic.')
,	('Other','Any road or path type that does not fit into the above categories')
;





-- table listing of street name pre type separators 
DROP TABLE IF EXISTS nena.StreetNamePreTypeSeparators CASCADE;
CREATE TABLE nena.StreetNamePreTypeSeparators (
	StreetNamePreTypeSeparator VARCHAR(20) PRIMARY KEY 
);
INSERT INTO nena.StreetNamePreTypeSeparators VALUES 
	('of the')
,	('at')
,	('de las')
,	('in the')
,	('des')
,	('to the')
,	('of')
,	('on the')
,	('to')
;

-- list of street name types - will likely be expanded locally 
DROP TABLE IF EXISTS nena.StreetNameTypes CASCADE;
CREATE TABLE nena.StreetNameTypes (
	StreetNameType VARCHAR(50) PRIMARY KEY
);
INSERT INTO nena.StreetNameTypes VALUES 
	('Access Road')
,	('Acres')
,	('Alcove')
,	('Alley')
,	('Annex')
,	('Approach')
,	('Arcade')
,	('Arch')
,	('Avenida')
,	('Avenue')
,	('Avenue Court')
,	('Bank')
,	('Bay')
,	('Bayou')
,	('Bayway')
,	('Beach')
,	('Bend')
,	('Bluff')
,	('Bluffs')
,	('Bottom')
,	('Boardwalk')
,	('Boulevard')
,	('Branch')
,	('Bridge')
,	('Brook')
,	('Brooks')
,	('Bureau of Indian Affairs Route')
,	('Burg')
,	('Burgs')
,	('Bypass')
,	('Calle')
,	('Camino')
,	('Camp')
,	('Canyon')
,	('Cape')
,	('Causeway')
,	('Center')
,	('Centers')
,	('Chase')
,	('Circle')
,	('Circles')
,	('Circus')
,	('Cliff')
,	('Cliffs')
,	('Close')
,	('Club')
,	('Cluster')
,	('Common')
,	('Commons')
,	('Concourse')
,	('Connect')
,	('Connector')
,	('Corner')
,	('Corners')
,	('Corridor')
,	('County Forest Road')
,	('County Highway')
,	('County Road')
,	('County Route')
,	('Course')
,	('Court')
,	('Courts')
,	('Cove')
,	('Coves')
,	('Creek')
,	('Crescent')
,	('Crest')
,	('Cross')
,	('Crossing')
,	('Crossroad')
,	('Crossroads')
,	('Crossway')
,	('Curve')
,	('Custer County Road')
,	('Cutoff')
,	('Cutting')
,	('Dale')
,	('Dam')
,	('Dawson County Road')
,	('Dell')
,	('Divide')
,	('Down')
,	('Downs')
,	('Drift')
,	('Drive')
,	('Drives')
,	('Driveway')
,	('End')
,	('Esplanade')
,	('Estate')
,	('Estates')
,	('Exchange')
,	('Exit')
,	('Expressway')
,	('Extension')
,	('Extensions')
,	('Fall')
,	('Falls')
,	('Fare')
,	('Farm')
,	('Federal-Aid Secondary Highway')
,	('Ferry')
,	('Field')
,	('Fields')
,	('Flat')
,	('Flats')
,	('Flyway')
,	('Ford')
,	('Fords')
,	('Forest')
,	('Forge')
,	('Forges')
,	('Fork')
,	('Forks')
,	('Fort')
,	('Freeway')
,	('Front')
,	('Garden')
,	('Gardens')
,	('Garth')
,	('Gate')
,	('Gates')
,	('Gateway')
,	('Glade')
,	('Glen')
,	('Glens')
,	('Gorge')
,	('Green')
,	('Greens')
,	('Grove')
,	('Groves')
,	('Harbor')
,	('Harbors')
,	('Harbour')
,	('Haven')
,	('Heights')
,	('Highway')
,	('Hill')
,	('Hills')
,	('Hollow')
,	('Horseshoe')
,	('Inlet')
,	('Interstate')
,	('Interval')
,	('Island')
,	('Islands')
,	('Isle')
,	('Junction')
,	('Junctions')
,	('Keep')
,	('Key')
,	('Keys')
,	('Knoll')
,	('Knolls')
,	('Lair')
,	('Lake')
,	('Lakes')
,	('Land')
,	('Landing')
,	('Lane')
,	('Lateral')
,	('Ledge')
,	('Light')
,	('Lights')
,	('Loaf')
,	('Lock')
,	('Locks')
,	('Lodge')
,	('Lookout')
,	('Loop')
,	('Mall')
,	('Manor')
,	('Manors')
,	('Market')
,	('Meadow')
,	('Meadows')
,	('Mews')
,	('Mill')
,	('Mills')
,	('Mission')
,	('Montana Highway')
,	('Motorway')
,	('Mount')
,	('Mountain')
,	('Mountains')
,	('Narrows')
,	('National Forest Development Road')
,	('Neck')
,	('Nook')
,	('Orchard')
,	('Oval')
,	('Overlook')
,	('Overpass')
,	('Park')
,	('Parke')
,	('Parks')
,	('Parkway')
,	('Parkways')
,	('Pass')
,	('Passage')
,	('Path')
,	('Pathway')
,	('Pike')
,	('Pine')
,	('Pines')
,	('Place')
,	('Plain')
,	('Plains')
,	('Plaza')
,	('Point')
,	('Pointe')
,	('Points')
,	('Port')
,	('Ports')
,	('Prairie')
,	('Promenade')
,	('Quarter')
,	('Quay')
,	('Ramp')
,	('Radial')
,	('Ranch')
,	('Rapid')
,	('Rapids')
,	('Reach')
,	('Rest')
,	('Ridge')
,	('Ridges')
,	('Rise')
,	('River')
,	('River Road')
,	('Road')
,	('Roads')
,	('Round')
,	('Route')
,	('Row')
,	('Rue')
,	('Run')
,	('Runway')
,	('Shoal')
,	('Shoals')
,	('Shore')
,	('Shores')
,	('Skyway')
,	('Slip')
,	('Spring')
,	('Springs')
,	('Spur')
,	('Spurs')
,	('Square')
,	('Squares')
,	('State Highway')
,	('State Parkway')
,	('State Road')
,	('State Route')
,	('State Secondary')
,	('Station')
,	('Strand')
,	('Strasse')
,	('Stravenue')
,	('Stream')
,	('Street')
,	('Street Court')
,	('Streets')
,	('Strip')
,	('Summit')
,	('Taxiway')
,	('Tern')
,	('Terrace')
,	('Throughway')
,	('Thruway')
,	('Trace')
,	('Track')
,	('Trafficway')
,	('Trail')
,	('Trailer')
,	('Triangle')
,	('Tunnel')
,	('Turn')
,	('Turnpike')
,	('United States Forest Service Road')
,	('United States Highway')
,	('Underpass')
,	('Union')
,	('Unions')
,	('Valley')
,	('Valleys')
,	('Via')
,	('Viaduct')
,	('View')
,	('Views')
,	('Villa')
,	('Village')
,	('Villages')
,	('Ville')
,	('Vista')
,	('Walk')
,	('Walks')
,	('Wall')
,	('Way')
,	('Ways')
,	('Weeg')
,	('Well')
,	('Wells')
,	('Woods')
,	('Wye')
;


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
, Parity_L VARCHAR(1)  NOT NULL  REFERENCES nena.Parities(Parity)
, Parity_R VARCHAR(1)  NOT NULL  REFERENCES nena.Parities(Parity)
, St_PreMod VARCHAR(15)   
, St_PreDir nena.DIRECTIONAL
, St_PreTyp VARCHAR(50)  REFERENCES nena.StreetNameTypes(StreetNameType)
, St_PreSep VARCHAR(20)  REFERENCES nena.StreetNamePreTypeSeparators(StreetNamePreTypeSeparator)
, St_Name VARCHAR(254)   
, St_PosTyp VARCHAR(50)  REFERENCES nena.StreetNameTypes(StreetNameType)
, St_PosDir nena.DIRECTIONAL   
, St_PosMod VARCHAR(25) 
, LSt_PreDir VARCHAR(2)  REFERENCES nena.LegacyDirectionals(LegacyDirectional)
, LSt_Name VARCHAR(75)   
, LSt_Type VARCHAR(4)  REFERENCES nena.LegacyStreetNameTypes(LegacyStreetNameType)
, LSt_PosDir VARCHAR(2)  REFERENCES nena.LegacyDirectionals(LegacyDirectional)
, ESN_L VARCHAR(5)  CHECK ( ESN_L ~* '\w{3,5}' )
, ESN_R VARCHAR(5)  CHECK ( ESN_R ~* '\w{3,5}' )
, MSAGComm_L VARCHAR(30)   
, MSAGComm_R VARCHAR(30)  
, Country_L nena.Country  NOT NULL  
, Country_R nena.Country  NOT NULL 
, State_L VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
, State_R VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
, County_L VARCHAR(40)  NOT NULL  REFERENCES nena.Counties(County)
, County_R VARCHAR(40)  NOT NULL  REFERENCES nena.Counties(County)
, AddCode_L VARCHAR(6)  REFERENCES nena.AdditionalCodes(AddCode)
, AddCode_R VARCHAR(6)  REFERENCES nena.AdditionalCodes(AddCode)
, IncMuni_L VARCHAR(100)  NOT NULL  
, IncMuni_R VARCHAR(100)  NOT NULL  
, UnincCom_L VARCHAR(100)   
, UnincCom_R VARCHAR(100)
, NbrhdCom_L VARCHAR(100)   
, NbrhdCom_R VARCHAR(100)
, PostCode_L VARCHAR(7)  REFERENCES nena.PostalCodes(PostalCode)
, PostCode_R VARCHAR(7)  REFERENCES nena.PostalCodes(PostalCode)
, PostComm_L VARCHAR(40)  REFERENCES nena.PostalCommunities(PostalCommunity)
, PostComm_R VARCHAR(40)  REFERENCES nena.PostalCommunities(PostalCommunity)
, RoadClass VARCHAR(15)  REFERENCES nena.RoadClasses(RoadClass)
, OneWay VARCHAR(2)  REFERENCES nena.OneWays(OneWay)
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
, ASt_PreDir nena.DIRECTIONAL
, ASt_PreTyp VARCHAR(50)  REFERENCES nena.StreetNameTypes(StreetNameType)
, ASt_PreSep VARCHAR(20)  REFERENCES nena.StreetNamePreTypeSeparators(StreetNamePreTypeSeparator)
, ASt_Name VARCHAR(254)  NOT NULL  
, ASt_PosTyp VARCHAR(50)  REFERENCES nena.StreetNameTypes(StreetNameType)
, ASt_PosDir nena.DIRECTIONAL   
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
, County VARCHAR(40)  NOT NULL  REFERENCES nena.Counties(County)
, AddCode VARCHAR(6)  REFERENCES nena.AdditionalCodes(AddCode)
, AddDataURI VARCHAR(254)
, Inc_Muni VARCHAR(100)  NOT NULL  
, Uninc_Comm VARCHAR(100)   
, Nbrhd_Comm VARCHAR(100)   
, AddNum_Pre VARCHAR(15)   
, Add_Number INTEGER   
, AddNum_Suf VARCHAR(15)
, St_PreMod VARCHAR(15)   
, St_PreDir nena.DIRECTIONAL   
, St_PreTyp VARCHAR(50)  REFERENCES nena.StreetNameTypes(StreetNameType)
, St_PreSep VARCHAR(20)  REFERENCES nena.StreetNamePreTypeSeparators(StreetNamePreTypeSeparator)
, St_Name VARCHAR(254)
, St_PosTyp VARCHAR(50)  REFERENCES nena.StreetNameTypes(StreetNameType) 
, St_PosDir nena.DIRECTIONAL   
, St_PosMod VARCHAR(25)
, LSt_PreDir VARCHAR(2)  REFERENCES nena.LegacyDirectionals(LegacyDirectional)
, LSt_Name VARCHAR(75)
, LSt_Type VARCHAR(4)  REFERENCES nena.LegacyStreetNameTypes(LegacyStreetNameType)   
, LSt_PosDir VARCHAR(2)  REFERENCES nena.LegacyDirectionals(LegacyDirectional)
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
, Place_Type VARCHAR(50)  REFERENCES nena.PlaceTypes(PlaceType)
, Placement VARCHAR(25)  REFERENCES nena.PlacementMethods(PlacementMethod)
, Longitude REAL  CHECK ( -180 <= Longitude AND Longitude <= 180 )
, Latitude REAL  CHECK ( -90 <= Latitude AND Latitude <= 90 )
, Elev INTEGER
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
, Country nena.Country  NOT NULL  
, State VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
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
, Country nena.Country  NOT NULL  
, State VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
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
, Country nena.Country  NOT NULL  
, State VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
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
, Country nena.Country  NOT NULL  
, State VARCHAR(2)  NOT NULL  REFERENCES nena.States(State)
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
, RLOWN VARCHAR(100)
, RLNAME VARCHAR(100)
, RLOP VARCHAR(100)
, RMPH REAL
, RMPL REAL
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
, County VARCHAR(75)  NOT NULL   REFERENCES nena.Counties(County)
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