# NG9-1-1 GIS Data Model Schemas

The **schema** folder contains the NENA NG9-1-1 GIS Data Model schemas in 
sub-folders by version. The schemas are defined as JSON dictionaries in 
Python files to support code integration within this repository. Usage in 
other programming languages should only require minor modifications.

These schemas are directly tied to their associated NENA document
(NENA-STA-006.x-YYYY). They are only updated when the associated document is 
released.

**Domains are only accurate at time of publication.**

---

## Folders and Files
* [v2.0a](v2.0a) - Folder containing the NENA NG9-1-1 GIS Data Model v2 schema.
  * [schema_fgdb_v2.py](v2.0a/schema_fgdb_v2.py) - Python file containing the NENA NG9-1-1 GIS Data Model as JSON dictionaries.
* [v3.0](v3.0) - Folder containing the NENA NG9-1-1 GIS Data Model v3 schema.
  * [nena_sta_006_v3.py](v3.0/nena_sta_006_v3.py) - Python file containing the field definitions from **Section: 5 Detailed Description of Field Names and associated attribute data** and the **GIS Data Layers Registry**. 
  * [schema_fgdb_v3.py](v3.0/schema_fgdb_v3.py) - Python file containing the layer definitions from **Section: 4 GIS Data Model Layers**.

---

## Change Log

* 2025-06-17
  * Created for v3.0 release to support multiple versions