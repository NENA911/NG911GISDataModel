# PostgreSQL/PostGIS Change Log

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