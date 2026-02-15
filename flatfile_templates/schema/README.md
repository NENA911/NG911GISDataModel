# NG9-1-1 GIS Data Model Schemas

The **schema** folder contains the NENA NG9-1-1 GIS Data Model schemas in 
sub-folders by version.

Starting with Version 3, the flat-file schema is defined in a YAML file to be language agnostic and consistent with other NENA code definitions. The Version 2 schema is defined as JSON dictionaries in Python file. Usage in other programming languages should only require minor modifications.

> **IMPORTANT!** 
> 
>NENA NG9-1-1 GIS Data Model schemas are directly associated to their associated NENA document (NENA-STA-006.x-YYYY). They are ONLY updated when the associated document is released.
> 
> **Domains are only accurate at time of publication.** Some domains rely on external resources that can be updated separately. URLs are provided to the sources for these domains in the comments of the schema for end-user updates.

---

## Folders and Files
* [v2.0a](v2.0a) - Folder containing the NENA NG9-1-1 GIS Data Model v2 schema.
  * [schema_fgdb_v2.py](v2.0a/schema_fgdb_v2.py) - Python file containing the NENA NG9-1-1 GIS Data Model as JSON dictionaries.
* [v3.0](v3.0) - Folder containing the NENA NG9-1-1 GIS Data Model v3 schema.
  * [nena_sta_006_v3.py](v3.0/nena_sta_006_v3.py) - Python file containing the field definitions from **Section: 5 Detailed Description of Field Names and associated attribute data** and the **GIS Data Layers Registry**. 
  * [flatfile_schema_v3.yaml](v3.0/flatfile_schema_v3.yaml) - YAML file containing the layer and domain definitions from **Section: 4 GIS Data Model Layers**.