# NG9-1-1 GIS Data Model Templates
#### Developed by: GIS Data Model Template Working Group
##### Updated: 5/20/2020 (Added Additional Notes section and content for said section)

<hr>

This repository defines the Geographic Information Systems (GIS) Data Model, 
which supports the NENA Next Generation 9-1-1 (NG9-1-1) Core Services (NGCS) of 
location validation and routing, both geospatial call routing or to the 
appropriate agency for dispatch. This model also defines several GIS data 
layers (layers) used in local Public Safety Answering Point (PSAP) and 
response agency mapping applications for handling and responding to 9-1-1 calls.

The data structures defined in this repository are related to, but different 
from the data structures defined in the NENA i3 Standard for Next Generation 
9-1-1, NENA-STA-010, Appendix B. Appendix B describes the 
Spatial Interface (SI). The purpose of the SI is to provision a functional 
element (e.g., the Emergency Call Routing Function) and GIS data. In contrast, 
this Data Model document describes the structure (e.g., field names, field data 
types, domains) of GIS data. Care has been taken to ensure that this Data Model 
is compatible with the SI provisioning process.

https://www.nena.org/page/NG911GISDataModel

<hr>

There are two data structures (templates) provided as part of the 
NG9-1-1 GIS Data Model Templates package; an open source version based on a 
PostgreSQL/PostGIS database and a version based on the Esri File GeoDatabase.  
These templates are meant to represent what NG9-1-1 GIS data should look like 
when it is being exchanged between two parties. 

While preparing these templates, the Working Group developed two sets of 
scripts (Python and SQL) to help in creation of the template files.  The 
scripts were originally intended only to serve as a method to help the 
Working Group develop the template files.  However, the Working Group felt 
that the scripts could also prove useful to the GIS community, so they have 
been included in this package.  While the scripts may prove useful, the 
Working Group does urge caution in using these scripts directly as it presents 
some potential for an entity to diverge from, and become incompatible with, 
the official NENA template files.  

ISO-compliant high-level metadata has been provided as a convenience and to 
describe what the templates represent.  The entity is not expected to use the 
provided metadata content when exchanging GIS data with another party.  
Rather, the entity should prepare metadata that is specific and relevant to 
their transaction with another entity.  The Working Group felt that high-level 
metadata was appropriate because the actual data exchanged between two parties 
would ultimately contain metadata that is specific to the party sharing the 
data when it came to contacts, use constraints, etc.  Also, there was a 
feeling that copying and pasting content from the NG9-1-1 GIS Data Model into 
the GIS template was onerous and unnecessary.  

At the conclusion of their work, the Working Group was left with a few issues 
that were not covered completely in the standard.  For those, the working 
group offers the following guidance:

### Domain Use
Within the templates there are some domains that have no entries.  These 
domains include AdditionalCode, AgencyID, County, ESN, PostalCode, 
PostalCommunityName and ServiceURI.  The entity is expected to populate these 
domains, in accordance with guidelines specified within the NG9-1-1 GIS Data 
Model standard, based on the needs within their jurisdiction.

For domains that have entries, but do not completely meet the entity's needs, 
the entity is encouraged to find the proper channel through which those domains 
can be extended. For example, in the case of the LegacyStreetNameType, the 
owner of those entries is the United States Postal Service; to extend that 
domain requires a change in USPS Publication 28 Appendix C1. In the case of 
the StreetNameType, StreetNamePreTypeSeparator and PlacementMethod domains, 
those entries are maintained by NENA through the NENA Registry System and 
new entries can be requested through that system.  In the case of Country, 
PlaceType and ServiceURN the entity is encouraged to contact NENA to seek more 
direction for requesting new entries.

Lastly, there are some domains where extension is not anticipated. Those 
include domains such as MilePostIndicator, MilePostUnitOfMeasurement, 
LegacyStreetNameDirectional, StreetNameDirectional, OneWay, Parity, RoadClass, 
State and Validation.  However, if an entity believes changes are needed for 
these domains the entity is encouraged to contact NENA to seek more direction 
for requesting new entries.

### UTC
Within the NG9-1-1 GIS Data Model Standard the domain associated with dates 
states the following: "Date and Time may be stored in the local database 
date/time format with the proviso that local time zone MUST be recorded and 
time MUST be recorded to a precision of at least 1 second and MAY be recorded 
to a precision of 0.1 second.  If the local database date/time format does not 
meet these specifications, the database SHOULD record both the local date/time 
format and a string conforming to W3C dateTime format as described in XML 
Schema Part 2: Datatypes Second Edition."

The Working Group felt that it was ideal to take advantage of built-in database 
date/time mechanisms for managing time rather than populating a W3C dateTime 
manually.  To address the intent of the domain, the working group determined 
that coordinated universal time (UTC) was an appropriate way to address the 
requirements.  Because UTC time is universal, it is also locally relevant while 
not requiring an offset or consideration of daylight savings time.  While 
entities are not expected to store UTC-based date/time in their locally 
maintained GIS data, they are expected to convert their date/time values into 
UTC when using these templates for sharing information with other parties.

## Additional Notes
When using this template solely for importing data as part of an 
extract/transform/load process, consideration should be given to turning off 
the Editor Tracking feature for each feature class so as not to unintentionally 
overwrite actual DateUpdate values from a source datasets.  When using this 
template as the primary local data structure, the strategy of turning off 
Editor Tracking should be considered as a temporary measure for an initial load.
