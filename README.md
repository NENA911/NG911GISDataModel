# NG9-1-1 GIS Data Model Templates

This repository defines the 
[Geographic Information Systems (GIS) Data Model](https://www.nena.org/page/NG911GISDataModel), 
which supports the NENA Next Generation 9-1-1 (NG9-1-1) Core Services (NGCS) of 
location validation and routing, both geospatial call routing or to the 
appropriate agency for dispatch. This model also defines the GIS data 
layers (layers) used in local Public Safety Answering Point (PSAP) and 
response agency mapping applications for handling and responding to 9-1-1 calls.

The objective of this repository is to provide a common transport format of 
NG9-1-1 data layers between GIS Data Providers and the SI. While the following 
scripts may be used by GIS Data Providers as a template for the management of 
their own NG9-1-1 data, it is expected that each GIS Data Provider will modify 
the schema to meet their specific organizations needs and requirements. 

---
## Table of Contents

* [Folders and Files](#folders-and-files)
* [About](#about)
* [Owner](#owner)
* [Version History](#version-history)
* [Issues](#issues)
* [Contributing](#contributing)
* [NENA Ethics & Code of Conduct Policy](#nena-ethics--code-of-conduct-policy)
* [NENA Intellectual Property Rights & Antitrust Policy](#nena-intellectual-property-rights--antitrust-policy)
* [License](#license)

---

## Folders and Files
* [docs](docs) - Folder containing PDF files with the NENA-STA-00G.x GIS Data 
  Model standards for reference by version.
* [esri_geodatabase](esri_geodatabase/README.md) - Folder containing instructions, 
  example file geodatabase, ArcGIS Toolbox and associated Python scripts to 
  create the NENA NG9-1-1 Data Model template.
* [postgresql](postgresql/README.md) - Folder containing instructions and SQL 
  scripts for creating the NENA NG9-1-1 Data Model template in PostgreSQL/PostGIS.
* .gitignore
* [LICENSE.md](LICENSE.md) - License file for the project.
* [README.md](README.md) - This document.

---

## About

There are two data structures (templates) provided as part of the 
NG9-1-1 GIS Data Model Templates package; an open source version based on a 
PostgreSQL/PostGIS database and a version based on the Esri File GeoDatabase. 
The templates are meant to represent what NG9-1-1 GIS data should look like 
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

The current templates include:

* [esri_geodatabase](esri_geodatabase/README.md) - Folder containing a sample 
  file geodatabase, ArcGIS Toolbox and associated Python scripts to create the 
  file geodatabase.
* [postgresql](postgresql/README.md) - Folder containing documentation and SQL 
  scripts to create a NENA NG9-1-1 GIS Data Model template in PostgreSQL.

### GIS Data Provider Specific Domains

Within the templates there are domains that have no entries. These domains include:

* Additional Code (`AddCode`, `AddCode_L` and `AddCode_R`)
* Discrepancy Agency ID (`DiscrpAgID`) 
* County or Equivalent (A2) (`County`, `County_L`, and `County_R`)
* ESN (`ESN`, `ESN_L`, and `ESN_R`)
* Postal Code (`PostCode`, `PostCode_L`, and `PostCode_R`)
* Postal Community Name (`PostComm`, `PostComm_L` and `PostComm_R`)
* Service URI (`ServiceURI`) 

The GIS Data Provider is expected to populate these domains, in accordance with 
guidelines specified within the NG9-1-1 GIS Data Model standard, based on the 
needs within their jurisdiction.

For domains that have entries, but do not completely meet the GIS Data Provider's 
needs, the GIS Data Provider is encouraged to find the proper channel through 
which those domains can be extended. For example, in the case of the 
**Legacy Street Name Type** (`LSt_Typ[_L\_R]`) , the owner of those entries is 
the United States Postal Service; to extend that domain requires a change in 
[USPS Publication 28 Appendix C1](https://pe.usps.com/text/pub28/28apc_002.htm). 
In the case of the **Street Name Pre/Post Types**, **Street Name Pre Type Separator** 
and **Placement Method** domains, those entries are maintained by NENA through the 
[NENA Registry System](http://technet.nena.org/nrs/registry/_registries.xml) and 
new entries can be requested through that system. In the case of 
**Country**, **Place Type** and **Service URN** the GIS Data Provider 
is encouraged to contact NENA to seek more direction for requesting new entries.

Lastly, there are some domains where extension is not anticipated. Those 
include domains such as **Location Marker Indicator** (`LM_Ind`), 
**Location Marker Unit of Measurement** (`LM_Unit`), 
**Legacy Street Name Pre/Post Directional**, **Street Name Pre/Post Directional**, 
**One Way**, **Parity**, **Road Class**, **State or Equivalent (A1)** and **Validation**. However, if an GIS Data Provider believes 
changes are needed for these domains the entity is encouraged to contact NENA 
to seek more direction for requesting new entries.

### Miscellaneous Notes

#### PlaceType Domain

The **SiteStructureAddressPoint** layer **PlaceType** domain specifies the 
values of the IANA [Location Types Registry](https://www.iana.org/assignments/location-type-registry/location-type-registry.xml). 
The Location Types defined in this registry include vehicles (e.g., "aircraft", 
"automobile", "bus", "bicycle", etc.). Upon discussion of the working group, it 
was agreed that it is uncommon to address a vehicle but rather the space the 
vehicle occupies. Therefore, the vehicle location types were excluded as it is 
unusal to address a location that moves.

#### LandmarkNameCompleteAliasTable and LandmarkNamePartTable 

In future version of NENA-STA-006 it is expected that the 
**LandmarkNameCompleteAliasTable** and **LandmarkNamePartTable** will be removed.

---

## Owner

The owner of this repository approves all changes to the repository.

This repository is owned by the 
[NENA Data Stuctures Committee](https://www.nena.org/page/DataStructures), 
DS-GIS Template working group.

**Contact:**

[NENA Data Stuctures Committee](https://www.nena.org/page/DataStructures)

---

# Version History
All notable changes to NG9-1-1 GIS Data Model Templates will be 
documented in this file. This project adheres to the 
[NENA Rules for Code Repositories](https://github.com/babley/NENA-Rules-for-Code-Repositories/blob/main/NENA-ADM-012-2021.md). 
For a more detailed, Change Log, please visit each packages respective CHANGE_LOG.


## [1.0 - 2019-11-20](https://github.com/NENA911/NG911GISDataModel/releases/tag/1.0.0)

- Initial public release

---

## Issues
Found a bug or want to suggest an enhancement? Check out previously logged 
[Issues](https://github.com/NENA911/NG911GISDataModel/issues). If you don't see 
what you're looking for, feel free to submit a new issue.

---

## Contributing

The NENA Data Model Working Group welcomes contributions from anyone and 
everyone. There are many ways you can contribute to this repository.

* Suggest enhancements or code changes as GitHub issues.
* Report potential bugs to GitHub issues.
* Contribute code, as pull requests, to the respository. If you are new
  to GitHub, [Git and GitHub Tutorials #4](https://www.youtube.com/watch?v=nT8KGYVurIU) 
  provides a good overview of creating forks and pulls to contribute.

### Contribute code improvements

1. Make sure you have a [GitHub account](https://github.com/signup/free).
2. [Fork](https://help.github.com/articles/fork-a-repo) the repo on GitHub.
3. Clone this repository to your local machine.
4. Create a new feature branch on your local machine.
    * The name of the branch doesn't matter, but as a best practice use a 
      descriptive name like "Updated PrePostStreetName domain".
5. Write code to add an enhancement or fix the problem.
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

## NENA Ethics & Code of Conduct Policy

To work in 9-1-1 is to be part of one of the most important institutions in 
America and across the globe. Since the first 9-1-1 call was placed in 
February 1968, untold millions of lives have been saved because of 9-1-1 
professionals’ dedication to public safety and service. NENA: The 9-1-1 
Association – comprised of its members, board, staff, volunteers, and event 
participants – is a community for all who are devoted to carrying this legacy 
forward and setting the standard for excellence in the industry. To do so, 
NENA strives to exemplify and embody the core values of respect, integrity, 
commitment, and cooperation.

Each association member, volunteer, and event attendee shall:

1. Represent the association honestly and professionally and refuse to 
   surrender any responsibility to special-interest or partisan political groups;
2. Avoid any conflict of interest or impropriety which could result from her or 
   his position, and refrain from using her or his status as an association 
   member for personal gain or publicity;
3. Take no public or private action that might compromise the actions, mission, 
   reputation, or integrity of NENA, and respect the confidentiality of 
   confidential information obtained in the representation of the association;
4. Only exercise that authority which is lawful;
5. Abide by the bylaws, policies, and procedures of the association;
6. Foster an environment of cooperation and collaboration that engenders trust, 
   openness and confidence – one where diverse perspectives and views are 
   encouraged and valued;
7. Encourage the free expression, through proper channels and means, of 
   opinions held by others;
8. Faithfully and diligently perform all duties properly assigned;
9. Disclose and refuse any gift, loan, reward, or promise of future employment 
   offered in exchange for a commitment to vote or take any other action 
   affecting association business;
10. Follow all accounting rules and financial controls imposed by the association;
11. Follow all laws relative to the ethical conduct of a not-for-profit 
    corporation;
12. Conduct herself or himself in a fair, honest, responsible, trustworthy and 
    unbiased manner;
13. Conduct the business of the association without respect of persons, keeping 
    deliberations and actions free from bias, prejudice, harassment, and 
    discrimination on the basis of race, color, sex, sexual orientation, gender 
    identity, religion, disability, age, political affiliation, genetic 
    information, veteran status, ancestry, or national or ethnic origin.
14. Remain professional and respectful to others in both word and deed at all 
    times;
15. Be protective of NENA, its brands, services, and reputation in all 
    communications;
16. Be committed to excelling in her or his role and support her or his peers’ 
    efforts to do the same; and
17. Share the association’s goals of improving 9-1-1 and the 9-1-1 industry; 
    facilitating growth, change, and innovation; developing leaders; driving 
    diversity; and creating community.

Individuals determined by the CEO, the Board of Directors, or its designee, to 
have violated the terms of this policy may, at NENA’s sole discretion, be 
subject to the application of measures that may include notification of the 
person’s agency or employer, forfeiture of event attendance, or revocation of 
membership. Should the NENA Board, or its designee, determine to remove an 
attendee from a NENA event or revoke membership, then it shall provide the 
affected person with an opportunity to respond to NENA’s concerns or allegations.

The above has been edited for clarity and is an abridged version of the 
board-approved Ethics & Code of Conduct Policy. See the full policy 
[here](https://cdn.ymaws.com/www.nena.org/resource/resmgr/membership/Ethics_and_Code_of_Conduct_2.pdf).

---

## NENA Intellectual Property Rights & Antitrust Policy


NENA requires an explicit Intellectual Property Rights & Antitrust Policy to 
conduct its daily work. The objectives of this policy are to:

1. Ensure that Members’ and participating Entities’ IPR are protected;
2. Promote awareness of IPR issues among NENA Committees so as to permit 
   informed decision-making about the trade-offs associated with technical 
   alternatives encountered in committee work; and
3. Ensure that implementers producing products or services based on NENA 
   standards are not unreasonably inhibited by IPR licensing requirements.

See the full policy [here](https://www.nena.org/general/custom.asp?page=ipr).

---

## License
Copyright 2019-2022 National Emergency Number Association

Licensed under the Apache License, Version 2.0 (the "License"); you may not 
use these files except in compliance with the License. You may obtain a copy 
of the License at http://www.apache.org/licenses/LICENSE-2.0. A copy of the 
License is available in the repository's [LICENSE](LICENSE.md) file.

Unless required by applicable law or agreed to in writing the tools 
distributed under the License are distributed on an "AS IS" BASIS, WITHOUT 
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the 
License for the specific language governing permissions and limitations 
under the License.
