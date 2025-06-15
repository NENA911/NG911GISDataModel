# Relational GIS Data Model Template

The relational data model adopted in NENA-STA-006.3-202Y supercedes the 
PostgreSQL/PostGIS "flat-file" template provided in previous versions.

**Section 15 Appendix E** outlines the relational data model utilized in the 
SI (Spatial Interface). While this model is essential for data exchange, it can 
optionally be used for data maintenance, providing a standardized structure 
that supports consistency and efficiency. Data maintainers 
may apply additional normalization to meet local needs; however, the structure 
specified in Appendix E must be followed for data exchange purposes. Apart 
from primary and foreign keys, the Descriptive Names used in Appendix E align 
with those listed in **Section 5 Detailed Description of Field Names and 
Associated Attribute Data**.

Due to the dialects of relational databases, please refer to **NENA-STA-006.3-202Y 
Section 15 Appendix E - Relational Data Model** for a tabular description of 
the schema.

---

## Change Log

* v3.0
  * Updated for NENA-STA-006.3-202Y
* v2.0
    * Updated for [NENA-STA-006.2-2022](https://github.com/NENA911/NG911GISDataModel/blob/main/docs/nena-sta-006.2-2022_ng9-1-1.pdf)
    * Various bug fixes and optimizations
    * See [commit change](https://github.com/NENA911/NG911GISDataModel/commits/main) 
      or [release history](https://github.com/NENA911/NG911GISDataModel/releases)
* v1.0
    * Based on [NENA-STA-006.1.1-2020](https://github.com/NENA911/NG911GISDataModel/blob/main/docs/nena-sta-006.1.1-2020_ng9-1-1.pdf)
    * Initial Release

---

## Contributors

* v3.0
  * [Tom Neer](https://github.com/tomneer), Digital Data Services, Inc.
  * Matt Gerike, Virginia Department of Emergency Management
  * Robb Harris, GISP, ENP, Esri Canada
* v2.0
  * [Tom Neer](https://github.com/tomneer), Digital Data Services, Inc.
  * [Jason Horning](https://github.com/jasonhorning), North Dakota Association of Counties
* v1.0
