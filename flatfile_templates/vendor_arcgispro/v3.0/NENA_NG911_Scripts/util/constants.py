# ==============================================================================
# Spatial Reference Constants
# ==============================================================================

SR_WGS84_HORIZONTAL = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",' \
                      'SPHEROID["WGS_1984",6378137.0,298.257223563]],' \
                      'PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];' \
                      '-400 -400 1000000000;-100000 10000;' \
                      '-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision'

# ==============================================================================
# METADATA Constants
# ==============================================================================
MD_TITLE = 'Next Generation 9-1-1 GIS Data Template'
MD_SUMMARY = 'GIS data model template that is conformant with the NG9-1-1 Data Model Standard (NENA-STA-006.3-2026). This data template is a National Emergency Number Association (NENA) working group-approved representation of the data model outlined in NENA Standard for NG9-1-1 GIS Data Model (NENA-STA-006.3-2026)'
MD_DESCRIPTION = 'The purpose of the template is to serve as a reference implementation of the current National Emergency Number Association\'s NG9-1-1 GIS Data Model (NENA-STA-006.3-2026). While the template can be used as a data structure for local GIS data, it is not a requirement. An entity which builds and maintains GIS data for NG9-1-1 need only be able to transform their internally-managed GIS data into a format which matches this template in preparation for data exchange with an external entity. For more information on the specifics of each field, attribute, relationship, etc. please refer to the "NENA Standard for NG9-1-1 GIS Data Model (NENA-STA-006.3-2026)"  This standard can be found at https://www.nena.org/page/standards and database templates can be found at https://github.com/NENA911/NG911GISDataModel. This metadata is provided to give the end user a high level overview of the template.  End users who use this template are encouraged to provide their own metadata in accordance with their internal data distribution policies.'
MD_CREDIT = 'This template was prepared by a National Emergency Number Association (NENA) working group called the "GIS Data Model Working Group". The working group operated under the Data Structures Committee; a NENA committee that maintains interoperable 9-1-1 data formats.'
MD_KEYWORDS = 'NENA, NG9-1-1, GIS, Data Model'
