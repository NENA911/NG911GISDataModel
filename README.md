# NG9-1-1 GIS Data Model Templates

The 
[NENA Standard for NG9-1-1 GIS Data Model, NENA-STA-006](https://www.nena.org/page/NG911GISDataModel), supports the NENA Next Generation 9-1-1 (NG9-1-1) Core Services (NGCS) of location validation and geospatial call routing to the appropriate agency for dispatch. This model also defines several GIS data layers (hereinafter "layers") used in local Public Safety Answering Point (PSAP) and response agency mapping applications for handling and responding to 9-1-1 calls.

The objective of the templates in this repository is to provide a common transport format of NG9-1-1 data layers between GIS Data Providers and an NGCS Spatial Interface (SI). While the following scripts and tools may be used by GIS Data Providers as a template for the management of their own NG9-1-1 data, it is expected that each GIS Data Provider will adapt the scripts and extend the schema to meet their specific organization's needs and requirements. 

With the v3.0 release, this repository has undergone a major refactor t0 support two parallel approaches to template generation: the long‑standing “flatfile” model and a new relational data model. This restructuring was driven by the need to maintain backward compatibility with existing workflows while enabling more robust, normalized database implementations aligned with modern NG9‑1‑1 data management practices. To make these paths clear and maintainable, the repository is now organized into two primary template directories:

- [flatfile_templates](flatfile_templates) – Traditional, single-table templates designed for desktop GIS applications and workflows that rely on the classic flatfile representation of the NENA NG9-1-1 GIS Data Model.
- [relational_templates](relational_templates) – A new, normalized relational schema that reflects the logical structure of the NENA NG9‑1‑1 GIS Data Model and supports more advanced enterprise database implementations.

This dual‑template structure ensures that implementers, tool developers and public safety GIS practitioners can choose the model that best fits their operational environment while benefiting from a unified, version‑aware codebase.

---

## Table of Contents

* [Folders and Files](#folders-and-files)
* [Usage](#usage)
* [Owner](#owner)
* [Version History](#version-history)
* [Issues](#issues)
* [Contributing](#contributing)
* [Associated Documents](#associated-documents)
* [Other References](#other-references)
* [NENA Ethics & Code of Conduct Policy](#nena-ethics--code-of-conduct-policy)
* [NENA Intellectual Property Rights & Antitrust Policy](#nena-intellectual-property-rights--antitrust-policy)
* [License](#license)

---

## Folders and Files
* [docs](docs/README.md) - Folder containing PDF files with the NENA-STA-006.x NG9-1-1 GIS Data Model standards for reference by version.
* [flatfile_templates](flatfile_templates) - Folder containing the pre-built flat-file templates, schema, and vendor code repositories.
  * [prebuilt_templates](flatfile_templates/prebuilt_templates/README.md) - Folder containing the pre-built flat-file templates.
  * [schema](flatfile_templates/schema/README.md) - Folder containing the schema definitions by version.
  * [vendor_arcgispro](flatfile_templates/vendor_arcgispro/) - Folder containing example code to create the flat-file templates in Esri ArcGIS Pro.
  * [vendor_qgis](flatfile_templates/vendor_qgis/README.md) - Folder for future example code to create the flat-file templates in QGIS.
* [relational_templates](relational_templates/README.md) - Folder containing information regarding the relational data model, introduced in v3.0.
  * [schema](relational_templates/schema) - Folder containing the schema definitions by version.
* .gitignore
* [CHANGELOG.md](CHANGELOG.md) - All notable changes to this project will be documented in this file.
* [LICENSE.md](LICENSE.md) - License file for the project.
* [README.md](README.md) - This document.

---

## Usage

In Version 3 of the NG9-1-1 GIS Data Model, a major structural change introduced the addition of a relational data structure to the previous flat-file data structure in previous versions of the GIS Data templates. 

There are three data structures provided as part of the NG9-1-1 GIS data model template package: an open source version based on the GeoPackage specification, a version based on the Esri File Geodatabase, and a relational data structure. The templates are meant to represent what NG9-1-1 GIS data should look like when it is being exchanged between two parties or to the SI (Spatial Interface) according to the NENA NG9-1-1 GIS Data Model Standard (NENA-STA-006.3-2026).

While preparing these templates, the Data Model Templates Working Subgroup developed a set of scripts to assist in the creation of the template files. The scripts were originally intended to serve only as a method to help develop the template files. However, it was felt the that scripts could also prove useful to the GIS community, so they are included for reference purposes only.

It is IMPORTANT to note that the NENA NG9-1-1 GIS Data Model templates are ONLY meant for the interchange of data between organizations and the SI (Spatial Interface). While they may be utilized for NG9-1-1 data management, it is expected that each GIS Data Provider will utilize ETL (Extract-Transform-Load) processes to migrate their organization-unique data into the NENA NG9-1-1 GIS Data Model.

### GIS Data Provider Specific Domains

Within the templates, there are domains that have no entries. These domains include:

* Additional Code (`AddCode`, `AddCode_L` and `AddCode_R`)
* Discrepancy Agency ID (`DiscrpAgID`) 
* Administrative Level 2 (`A2`, `A2_L`, `A2_R`)
* ESN (`ESN`, `ESN_L`, and `ESN_R`)
* Postal Code (`Post_Code`, `PostCode_L`, and `PostCode_R`)
* Postal Community Name (`PostComm`, `PostComm_L`, and `PostComm_R`)
* Service URI (`ServiceURI`) 

The GIS Data Provider is expected to populate these domains, in accordance with guidelines specified within the NG9-1-1 GIS Data Model standard, based on the needs within their jurisdiction.

For domains that have entries but do not completely meet the GIS Data Provider's needs, the GIS Data Provider is encouraged to find the proper channel through which those domains can be extended. In the case of the **Street Name Pre/Post Types**, **Street Name Pre Type Separator**, and **Placement Method** domains, those entries are maintained by NENA through the [NENA Registry System](http://technet.nena.org/nrs/registry/_registries.xml), and new entries can be requested through that system. In the case of **Country**, **Place Type**, and **Service URN**, the GIS Data Provider is encouraged to contact the Owner to seek more direction for requesting new entries. The ESN domain is also commented out, as it will not be used in every implementation. If it is needed in their implementation, the GIS Data Provider is expected to uncomment the domain and populate it.

Lastly, there are some domains where extension is not anticipated. Those include domains such as **Location Marker Indicator** (`LM_Ind`),**Legacy Street Name Pre/Post Directional**, **Street Name Pre/Post Directional**, **One-Way**, **Parity**, **Road Class**, and **Validation**. However, if a GIS Data Provider believes changes are needed for these domains, the entity is encouraged to contact the Owner 
to seek more direction for requesting new entries.

### Miscellaneous Notes

#### PlaceType Domain

The **SiteStructureAddressPoint** layer **PlaceType** domain specifies the values of the IANA [Location Types Registry](https://www.iana.org/assignments/location-type-registry/location-type-registry.xml). The Location Types defined in this registry include vehicles (e.g., "aircraft","automobile", "bus", "bicycle", etc.). Upon discussion of the working group, it was agreed that it is uncommon to address a vehicle but rather the space the vehicle occupies. Therefore, the vehicle location types were excluded from the templates as it is unusual to address a location that moves.

---

## Owner

The owner of this repository approves all changes to the repository.

This repository is owned by the 
[NENA Data Structures & Management Committee](https://www.nena.org/page/DevelopmentGroup), 
DSM-NG GIS Data Model working group.

**Contact:**

[NENA Data Stuctures & Management Committee](https://www.nena.org/page/DevelopmentGroup)

---

# Version History
All notable changes to the NG9-1-1 GIS Data Model Templates will be documented in this file. This project adheres to the[NENA Rules for Code Repositories](https://github.com/babley/NENA-Rules-for-Code-Repositories/blob/main/NENA-ADM-012-2021.md). For a more detailed Change Log, please visit the [CHANGE_LOG](CHANGELOG.md).

### [v3.0 - 2026-03-24](https://github.com/NENA911/NG911GISDataModel/releases/tag/3.0)

### [v2.0a - 2023-05-07](https://github.com/NENA911/NG911GISDataModel/releases/tag/2.0a)

### [v2.0 - 2023-03-21](https://github.com/NENA911/NG911GISDataModel/releases/tag/2.0)

### [v1.0 - 2019-11-20](https://github.com/NENA911/NG911GISDataModel/releases/tag/1.0.0)


---

## Issues
Found a bug or want to suggest an enhancement? Check out previously logged 
[Issues](https://github.com/NENA911/NG911GISDataModel/issues). If you don't see 
what you're looking for, feel free to submit a new issue.

---

## Contributing

The NENA GIS Data Model Working Group welcomes contributions from anyone and everyone. There are many ways you can contribute to this repository.

* Suggest enhancements or code changes as GitHub issues.
* Report potential bugs to GitHub issues.
* Contribute code, as pull requests, to the repository. If you are new
  to GitHub, [Git and GitHub Tutorials #4](https://www.youtube.com/watch?v=nT8KGYVurIU) 
  provides a good overview of creating forks and pulls to contribute.

### Contribute code improvements

1. Make sure you have a [GitHub account](https://github.com/signup/free).
2. [Fork](https://help.github.com/articles/fork-a-repo) the repo on GitHub.
3. Clone this repository to your local machine.
4. Create a new feature branch on your local machine.
    * The name of the branch doesn't matter, but as a best practice use a 
      descriptive name like "Updated PrePostStreetName domain".
5. Write code to add an enhancement or fix a problem.
    * Document your code.
    * Make commits of logical units.
    * Use [clear and descriptive commit messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).
6. Test your code.

### Submitting changes
1. Push the changes in your feature branch to your repository.
2. Submit a [pull request](https://help.github.com/articles/using-pull-requests).  
   Submitting a pull request will open a GitHub issue.
    * Clearly describe the issue including steps to reproduce; or if an 
      enhancement, indicate the functionality you built.

### License of contributed code
By contributing your code, you agree to license your contribution under the 
terms of the [Apache License 2.0](LICENSE.md).

---

## Associated Documents

- **NENA Standard for NG9-1-1 GIS Data Model**
  - NENA-STA-006.3-2026
  - [NENA-STA-006.2a-2023](docs/nena-sta-006.2a-2023_ng9-1-1.pdf)
  - [NENA-STA-006.2-2022](docs/nena-sta-006.2-2022_ng9-1-1.pdf)
  - [NENA-STA-006.1.1-2020](docs/nena-sta-006.1.1-2020_ng9-1-1.pdf)
  - [NENA-STA-006.1-2018](docs/nena-sta-006.1-2018_ng9-1-1.pdf)

---

## Other References

- [NENA Knowledge Base Glossary](https://kb.nena.org/wiki/Category:Glossary)
- [NENA-INF-028 - NENA Information Document for GIS Data Stewardship for Next Generation 9-1-1 (NG9-1-1)](https://cdn.ymaws.com/www.nena.org/resource/resmgr/standards/NENA_INF_028.1_2020_GISDataS.pdf)
- [NENA Standards & Other Documents](https://www.nena.org/page/standards)
  - NENA-STA-004 - NENA Next Generation 9-1-1 United States Civic Location Data Exchange Format (CLDXF-US) Standard
  - NENA-STA-008 - NENA Registry System (NRS) Standard
  - NENA-STA-010 - NENA i3 Standard for Next Generation 9-1-1
  - NENA-STA-015 - NENA Standard Data Formats for E9-1-1 Data Exchange & GIS Mapping
  - NENA-STA-029 - NENA Next Generation 9-1-1 (NG9-1-1) Canadian Civic Location Data Exchange Format (CLDXF-CA) Standard
  - NENA-REQ-003 - NENA Requirements for 3D GIS for E9-1-1 and NG9-1-1
  - NENA-INF-014 - NENA Information Document for Development of Site/Structure Address Point GIS Data for 9-1-1
  - NENA-INF-028 - NENA Information Document for GIS Data Stewardship for NG9-1-1
  - NENA-INF-046 - NENA GIS Data Transition Information Document

---

## NENA Ethics & Code of Conduct Policy

By contributing to this repository, you agree to adhere to NENA's Ethics and Code of Conduct Policy available 
[here](https://www.nena.org/page/codeofconduct).

---

## NENA Intellectual Property Rights & Antitrust Policy


NENA requires an explicit Intellectual Property Rights & Antitrust Policy to 
conduct its daily work. The objectives of this policy are to:

1. Ensure that Members' and participating Entities’ IPR are protected;
2. Promote awareness of IPR issues among NENA Committees so as to permit 
   informed decision-making about the trade-offs associated with technical 
   alternatives encountered in committee work; and
3. Ensure that implementers producing products or services based on NENA 
   standards are not unreasonably inhibited by IPR licensing requirements.

See the full policy [here](https://www.nena.org/page/ipr).

---

## License
Copyright © 2018-2026 National Emergency Number Association. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not 
use these files except in compliance with the License. You may obtain a copy 
of the License at http://www.apache.org/licenses/LICENSE-2.0. A copy of the 
License is available in the repository's [LICENSE](LICENSE.md) file.

Unless required by applicable law or agreed to in writing, software 
distributed under the License are distributed on an "AS IS" BASIS, WITHOUT 
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 

See the License for the specific language governing permissions and limitations 
under the License.

---

## Contributors

* v3.0
  * [Tom Neer](https://github.com/tomneer), Digital Data Services, Inc.
  * Matt Gerike, PhD, GISP, Virginia Department of Emergency Management
  * Robert Harris, GISP, ENP, Esri Canada
* v2.0
  * [Tom Neer](https://github.com/tomneer), Digital Data Services, Inc.
  * [Jason Horning](https://github.com/jasonhorning), ENP, North Dakota Association of Counties
* v1.0

---

# Acknowledgements

Trademarks provided under license from Esri. 
Other companies and products mentioned are trademarks of their respective owners. 
