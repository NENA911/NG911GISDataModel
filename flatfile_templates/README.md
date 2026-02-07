# Flat-File GIS Data Model Template

The portion of this repository has undergone a significant refactor in the v3.0 release to better support long‑term maintainability and multiple NENA model versions. What began as a single, monolithic structure has been reorganized into a clearer, modular layout that separates core schema definitions from vendor‑specific tooling and prebuilt deliverables.

To make the project easier to navigate, and to streamline future updates, the repository is now organized into the following directories:

- [prebuilt_templates](prebuilt_templates) – Ready‑to‑use File Geodatabase (FGDB) and GeoPackage (GPKG) templates generated from the NENA schema organized by version subfolders.
- [schema](schema) – The canonical, versioned logical schema definitions that drive all template generation organized by version subfolders.
- [vendor_arcgispro](vendor_arcgispro) – ArcGIS Pro–specific example code
- [vendor_qgis](vendor_qgis) – Placeholder for future QGIS‑specific example code.

This structure provides a clean foundation for contributors, tool developers, and public safety GIS practitioners who need a consistent, version‑aware implementation of the NENA NG9‑1‑1 data model.

---

* [Folders and Files](#folders-and-files)
* [Help](#help)
* [Known Issues](#known-issues)
* [Change Log](#change-log)
* [Contributors](#contributors)
* [Acknowledgements](#acknowledgements)

---

## Folders and Files

* [prebuilt_templates](prebuilt_templates/) - The **prebuilt_templates** folder contains the NENA NG9-1-1 GIS Data Model 
pre-built templates in sub-folders by version.
  - [v2.0a](prebuilt_templates/v2.0a) - Folder containing the NENA NG9-1-1 GIS Data Model v2.0a pre-built FGDB templates.
  - [v3.0](prebuilt_templates/3.0) - Folder containing the NENA NG9-1-1 GIS Data Model v3 pre-built FGDB & GPKG templates.
* [schema](schema/) - The **schema** folder contains the NENA NG9-1-1 GIS Data Model schemas in 
sub-folders by version. 
  - [v2.0a](schema/v2.0a) - Folder containing the NENA NG9-1-1 GIS Data Model v2.0a schema definitions.
  - [v3.0](schema/v3.0) - Folder containing the NENA NG9-1-1 GIS Data Model v3.0 schema definitions.
* [vendor_arcgispro](vendor_arcgispro/) - Folder containing example template-generation code for Esri's ArcGIS Pro.
  - [.imgs](vendor_arcgispro/.imgs) - Folder containing documentation images.
  - [v2.0a](vendor_arcgispro/v2.0a) - Folder containing example code to generate the v2.0a version of NENA NG9-1-1 GIS Data Model.
  - [v3.0](vendor_arcgispro/v3.0) - Folder containing example code to generate the v3.0 version of NENA NG9-1-1 GIS Data Model.
* [vendor_qgis](vendor_qgis/) - This folder currently serves as a placeholder for future QGIS template‑generation code.
* [README.md](README.md) - This document.

---

## Help

For assistance not provided within this repositories documentation, please visit https://www.nena.org/page/DataStructures where contact information for the leadership of the Data Structures Committee can be found.  

---

## Known Issues

---

## Change Log

* v3.0
    * Initial release

---

## Acknowledgements

* v3.0
  * Relational Data Model Sub-Working Group

Other companies and products mentioned are trademarks of their respective owners. 