# Change Log
All notable changes to this project will be documented in this file.

---
 
## v3.0 - YYYY-MM-DD
 
This release of the **NENA NG9-1-1 GIS Data Model Templates** is in alignment with NENA's NG9-1-1 GIS Data Model ([NENA-STA-006.3-YYYY](https://github.com/NENA911/NG911GISDataModel/blob/main/docs/nena-sta-006.3-2026_ng9-1-1.pdf)) approved by the NENA Board of Directors on YYYY-MM-DD.
 
### Changed
- Created the SiteStructureAddressPolygon layer.
- Created the Site/Structure Address Polygon Extent Method registry.
- Created the DistanceMarkerPoint layer.
- Removed the StreetNameAliasTable.
- Removed the CellSectorPoint layer.
- Removed the LandmarkNamePartTable.
- Removed the LandmarkNameCompleteAliasTable.
- Redefined “Type” column that indicates the data type of the attribute columns in all layers.
  - TEXT(Length) field type replaces field types P and U.
  - DATETIME field type replaces field type D.
  - INTEGER field type replaces field type N.
  - REAL (Precision, Scale) field type replaces field type F.
- Administrative Levels (A1-A5) changes
  - Changed descriptive names and field names for State, County, Incorporated Municipality, Unincorporated Municipality, and Neighborhood Community in all layers.
  - Increased field length for all A2-A5 fields in all layers.
  - Added Additional Code field in A2Polygon layer.
  - Removed Additional Code field in A5Polygon layer.
- RoadCenterLine layer changes
  - Changed descriptive name of “Left FROM Address” to “Left FROM Address Number”.
  - Changed descriptive name of “Right FROM Address” to “Right FROM Address Number”.
  - Changed descriptive name of “Left TO Address” to “Left TO Address Number”.
  - Changed descriptive name of “Right TO Address ” to “Right TO Address Number”.
  - Added Direction of Travel field.
  - Added Legacy County ID Left field.
  - Added Legacy County ID Right field.
  - Increased field length of Street Name Pre Modifier field. 
- SiteStructureAddressPoint layer changes
  - Added Address Number Complete field.
  - Added Altitude field.
  - Added Distance Marker field.
  - Added Direction of Travel field.
  - Added Floor Index field.
  - Added Height field.
  - Added Legacy County ID field.
  - Added Location Marker field.
  - Added Row field.
  - Added Section field.
  - Added Site field.
  - Added SubSite field.
  - Added Unit Pre Type field.
  - Added Unit Value field.
  - Added Wing field.
  - Removed the Complete Landmark Name field.
  - Changed descriptive name and field name of Building to Structure.
  - Changed descriptive name of Floor to Floor Label.
  - Increased field length of Street Name Pre Modifier field.
  - Changed type for Latitude field.
  - Changed type for Longitude field.
- Service Boundary layers changes
  - Increased the field length of Service URN field.
  - Removed the Country field.
  - Removed the State or Equivalent field.
- RailroadCenterLine layer
  - Changed type for Rail Mile Post Low field.
  - Changed type for Rail Mile Post High field.
- LocationMarkerPoint layer changes
  - Increased the field length of Location Marker Type field.
  - Removed the Location Marker Unit of Measurement field.
  - Removed the Location Marker Measurement Value field.
  - Removed the Location Marker Route Name field.
- Domain values have been removed for the following fields:
  - Additional Code
  - Additional Code Left
  - Additional Code Right
  - Additional Data URI
  - Address Number
  - Administrative Level 3
  - Administrative Level 3 Left
  - Administrative Level 3 Right
  - Date Updated
  - Effective Date
  - Expiration Date
  - Left FROM Address Number
  - Left TO Address Number
  - Right FROM Address Number
  - Right TO Address Number
- Domain values have been changed for the following fields:
  - Administrative Level 1
  - Administrative Level 1 Left
  - Administrative Level 1 Right
  - Administrative Level 2
  - Administrative Level 2 Left
  - Administrative Level 2 Right
  - Elevation
  - Latitude
  - Location Marker Indicator
  - Longitude
  - Place Type
  - Placement Method
  - Postal Code
  - Postal Code Left
  - Postal Code Right
  - Postal Community Name
  - Postal Community Name Left
  - Postal Community Name Right
  - Rail Mile Post High
  - Rail Mile Post Low

---


## v2.0a - 2023-05-07
 
This release of the **NENA NG9-1-1 GIS Data Model Templates** is in alignment with NENA's NG9-1-1 GIS Data Model ([NENA-STA-006.2a-2023](https://github.com/NENA911/NG911GISDataModel/blob/main/docs/nena-sta-006.2a-2023_ng9-1-1.pdf)) approved by the NENA DSC on 2023-05-02. There was only one minor code change in the PostgreSQL template due to an invalid domain range in the Speed Limit field as the majority of the errata changes documented in NENA-STA-006.2a were already corrected in the v2.0 release of the Templates.

---

## v2.0 - 2023-03-21
 
This release of the **NENA NG9-1-1 GIS Data Model Templates** is based on NENA's NG9-1-1 GIS Data Model ([NENA-STA-006.2-2022](https://github.com/NENA911/NG911GISDataModel/blob/main/docs/nena-sta-006.2-2022_ng9-1-1.pdf)). This release includes most of the errata changes to NENA-STA-006.2-2022 that would later be adopted in NENA-STA-006.2a-2023.

### Enhancements

- Migrated GIS Data Model Templates to GitHub.
- [ArcGIS] Added ArcGIS Toolboxes for both ArcGIS Pro and ArcGIS Desktop 10.x
- [ArcGIS] Refactored Python script to operate in multiple versions of ArcGIS Desktop
 
### Changed

- Updated layer names, table names, domain names, descriptions, & field names to align with the v2 standard.
- Addressed Items identified in [NENA-STA-006.2-2022](https://github.com/NENA911/NG911GISDataModel/blob/main/docs/nena-sta-006.2-2022_ng9-1-1.pdf) **Reason for Issue / Reissue** section

  - Redefined “P” field type and changed all “E” field type values to “P” field type in all layers. 
  - Changed Discrepancy Agency ID field width from 75 to 100 in all layers. 
  - Changed Street Name field width from 60 to 254 in the RoadCenterLine layer and the SiteStructureAddressPoint layer. 
  - Changed Alias Street Name field width from 60 to 254 in StreetNameAliasTable. 
  - Changed field name for Longitude from “Long” to “Longitude” in the SiteStructureAddressPoint layer and CellSectorPoint layer. 
  - Changed field name for Latitude from “Lat” to “Latitude” in the SiteStructureAddressPoint layer and CellSectorPoint layer. 
  - Changed field name for Elevation from “Elev” to “Elevation” in SiteStructureAddressPoint layer. 
  - Changed County Left and County Right field width from 40 to 100 in the RoadCenterLine layer. 
  - Changed County field width from 40 to 100 in the SiteStructureAddressPoint layer, the A2-A5 Administrative Unit layers, and the CellSectorPoint layer. 
  - Changed field name for primary key NGUIDs to just “NGUID” (i.e., removed “RCL” from RCL_NGUID) in all layers. 
  - Changed field name for Site NENA Globally Unique ID (Foreign Key) from “Site_NGUID” to “SSAP_NGUID” in the LandmarkNamePartTable, the LandmarkNameCompleteAliasTable, and the CellSectorPoint layer. 
  - Changed field name for Complete Landmark Name Alias NENA Globally Unique ID (Foreign Key) from “ACLMNNGUID” to “CLNA_NGUID” in the LandmarkNamePartTable.
  - Changed field name for Legacy Street Name Type from “LSt_Type” to “LSt_Typ” in the RoadCenterLine layer and the SiteStructureAddressPoint layer. 
  - Changed descriptive name “Mile Post” to “Milepost” and changed associated field name “Mile_Post” to “Milepost” in the SiteStructureAddressPoint layer. 
  - Changed field name for Rail Line Name from “RLNameE” to “RLName” in the RailroadCenterLine layer.  
  - Changed “State” field to Not Required in all service boundary layers. 
  - Added “Country” field as a Not Required field to all service boundary layers. 
  - Added “Incorporated Municipality” field as a Required field to the A4Polygon layer. 
  - Removed Alias Legacy Street Name Pre Directional field, Alias Legacy Street Name field, Alias Legacy Street Name Type field, and Alias Legacy Street Name Post Directional field from the StreetNameAliasTable.
  - Made many changes to the descriptive names, the field names, and the M/C/O categorization in the LocationMarkerPoint layer (previously named Mile Marker Location). Also added the Location Marker Label field as a Conditional field.

- Update domain values based on current registry / source values.

  - Updated StreetNamePreTypesAndStreetNamePostTypes domain.
  - Updated StreetNamePreTypeSeparators domain.
  - Updated Alias Street Name Pre/Post Directional domains (added French values).
  - Updated Street Name Pre/Post Directional domains (added French values).
  - Updated Road Class domain.
  - Updated PlaceType domain (intentionally left vehicles out of the domain)
  - Updated ServiceURN domain.
  - Update administrative area (state, county, etc.) domain names to include Canadian equivalents.
  - Increased Street Name Pre and Post Directionals (not Legacy Directionals) to 10 characters to support new French domain values.
  - Increased "RoadClass" to 24 characters to support new domain values.
  - Removed Legacy Street Name Type Domain and association with fields.
  - Updated "PropertyAccess" domain value (from "Property Access").
  - Increase length of ServiceURN to 55 characters to support URN registry entries.
  - Removed the 'AdditionalCodes' domain requirement for `AddCode`, `AddCode_L`, and `AddCode_R` fields in both versions.

- [PostgreSQL] Added missing `St_PreDir` and `St_PosDir` field missing from the v1.0 RoadCenterlines schema.
- [PostgreSQL] Corrected longitude check error from `CHECK ( -90 <= Longitude AND Longitude <= 90 )` to `CHECK ( -180 <= Longitude AND Longitude <= 180 )` in multiple tables.
- [PostgreSQL] Changed domain and reference tables to follow NENA table and field naming conventions.
- [PostgreSQL] Reordered fields in schema to the same order as GIS Data Model documentation for ease of quality assurance and control.
- [PostgreSQL] Changed all `DOUBLE PRECISION` datatypes to `REAL` to reflect the `FLOAT` value defined in NENA-STA-006.2-2022.
- [PostgreSQL] Changed all `TIMESTAMP WITH TIME ZONE` datatypes to `TIMESTAMPTZ` which is the proper datatype that is a time zone-aware data and time datatype. PostgreSQL converts the `TIMESTAMPTZ` value into a UTC value and stores the UTC value in the table.
- [PostgreSQL] Changed all `CHARACTER VARYING` to `VARCHAR`, which is the more common alias.
- [PostgreSQL] Added `id` field; otherwise, editing is slow and open to error. Not part of the standard, but it is best practice to have a `SERIAL` or `UUID` as the Primary Key. The NGUID could fulfill this requirement, but it would require creating a TRIGGER.
- [PostgreSQL] Changed 'POLYGON' geometry datatypes to 'MULTIPOLYGON'.
 

---

## v1.0 - 2020-02-18
  
Initial release is a direct import of the **NG911_GIS_TEMPLATE_FILES_20200521** from the [NG9-1-1 GIS Data Model](https://www.nena.org/page/NG911GISDataModel). It was used as the initial baseline for this repository.
 
### New
- GIS Data Model Templates are based on NENA's NG9-1-1 GIS Data Model [NENA-STA-006.1.1-2020](https://github.com/NENA911/NG911GISDataModel/blob/main/docs/nena-sta-006.1.1-2020_ng9-1-1.pdf).
