# Relational GIS Data Model Template

**Section 15, Appendix E-Relational Data Model** outlines the relational data model utilized in the SI (Spatial Interface). Apart from primary and foreign keys, the Descriptive Names used in Appendix E align with those listed in **Section 5 Detailed Description of Field Names and Associated Attribute Data**.

Due to various SQL dialects, the relational database model is currently represented as an logical, rather than a physical, data model. A logical model focuses on structure, relationships, and rules, independent of any specific database technology, where a physical model focuses on how the database will actually be implemented on a specific platform. 

**NOTE**: The relational data model adopted in NENA-STA-006.3-202Y supercedes the PostgreSQL/PostGIS "flat-file" template provided in previous versions.

---

* [Folders and Files](#folders-and-files)
* [Data Type Mapping](#data-type-mapping)
* [Help](#help)
* [Contributors](#contributors)
* [Acknowledgements](#acknowledgements)

---

## Folders and Files

* [schema](schema) - Folder containing the NENA GIS relational data model schema organized by version.
  * [v3.0](schema/v3.0) - Folder containing the v3.0 release of the NENA GIS relational data model.
    * [.imgs](schema/v3.0/.imgs) - Folder containing documentation images and screen shots.
    * [README.md](schema/v3.0/README.md) - README file for v3.0 release.
* [README.md](README.md) - This document.

---

## Data Type Mapping

The relational data model is a logical data model, not a physical data model and will require mapping data types to database specific datatypes. The following table provides an example of cross‑platform data type equivalency for reference purposes only.

| NENA-STA-006 | Relational Data Model | PostgreSQL        | MS SQL Server        | Esri FGDB | geoPackage |
|--------------|-----------------------|-------------------|----------------------|-----------|------------|
| TEXT(Length) | TEXT(n)               | VARCHAR(n)        | VARCHAR(n)           | TEXT(n)   | TEXT       |
| DATETIME     | DATETIME              | TIMESTAMPZ        | DATETIMEOFFSET       | DATE      | DATETIME   |
| INTEGER      | INTEGER               | INTEGER           | INTEGER              | LONG      | INTEGER    |
| REAL(p,s)    | REAL(p,s)             | NUMERIC(p,s)      | NUMERIC(p,s)         | DOUBLE    | REAL       | 
| Not Defined  | BIGINT<sup>1</sup>    | BIGSERIAL/BIGINT  | BIGINT               | OBJECTID  | INTEGER    | 
| Not Defined  | GEOMETRY(POINT)       | GEOMETRY(POINT)   | GEOMETRY::POINT      | POINT     | POINT      | 
| Not Defined  | GEOMETRY(LINESTRING)  | GEOMETRY(LINE)    | GEOMETRY::LINESTRING | POLYLINE  | LINESTRING | 
| Not Defined  | GEOMETRY(POLGYON)     | GEOMETRY(POLYGON) | GEOMETRY::POLYGON    | POLYGON   | POLYGON    | 

<sup>1</sup> The BIGINT data type is used to identify primary and foreign key fields. When a BIGINT is used as a primary key, it should implement a sequencer or increment function. It is recommended BIGINT data types are defined as 8-byte integers. 

---

## Help

For assistance not provided within this repositories documentation, please visit https://www.nena.org/page/DataStructures where contact information for the leadership of the Data Structures Committee can be found.

---

## Contributors

* v3.0
  * Relational Data Model Sub-Working Group

---

## Acknowledgements

* v3.0
  * Relational Data Model Sub-Working Group

Other companies and products mentioned are trademarks of their respective owners. 