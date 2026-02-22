# create_ng11_fgdb.py
"""
| Name:      Create NG9-1-1 File Geodatabase v3
| Purpose:   Creates a GIS data model template that is conformant with the
|            NG9-1-1 Data Model Standard (NENA-STA-006.3-2026). This data
|            template is a National Emergency Number Association (NENA) working
|            group-approved representation of the data model outlined in NENA
|            Standard for NG9-1-1 GIS Data Model (NENA-STA-006.3-2026)
|
| Notes:     This code is written using the default Python library for
|            ArcGIS Pro's "arcgispro-py3" conda environment. This code is not
|            dependent on ArcGIS Pro, but is part of a larger package of
|            Python scripts which are.
|
| Author:    NENA Data Structures Committee, DS-GIS Template Working Group
|
| TODO: Resolve issue with Esri not recognizing EPSG 4979
| TODO: Create ArcGIS Toolbox
| TODO: Add code support to generate File Geodatabase and/or GeoPackage in code
| TODO: Add code support for CDLXF dialects
| TODO: Add code support for field level metadata. Blocked by Esri.
| TODO: Add code to check if user has ArcGIS Pro license and to refresh if necessary.
"""
import arcpy
import os
import yaml
from six import iteritems
from sys import exit
from util import CreateLogger

# ==============================================================================
# Import Constants
# ==============================================================================

import util.constants as CONSTANTS

DOMAINS = None
FEATURE_CLASSES = None
FIELDS = None
GIS_DATA_LAYERS_REGISTRY = None

# ==============================================================================
# Functions
# ==============================================================================

def messages(msgs, msg_lvl, msg_type, log, progress=True):
    """
    Distributes code messages to file logger and ArcPy Messages and Progressor.

    :param msgs:
    :param msg_lvl:
    :param msg_type:
    :param log:
    :param progress:
    :return:
    """
    for msg in msgs:
        if msg_lvl == 'ERROR':
            log.error(msg)
            if msg_type == 'TOOLBOX':
                # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/adderror.htm
                arcpy.AddError(msg)
            exit()
        elif msg_lvl == 'WARN':
            log.warning(msg)
            if msg_type == 'TOOLBOX':
                # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/addwarning.htm
                arcpy.AddWarning(msg)
        else:
            log.info(msg)
            if msg_type == 'TOOLBOX':
                # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/addmessage.htm
                arcpy.AddMessage(msg)
                if progress:
                    # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/setprogressor.htm
                    arcpy.SetProgressorLabel(msg)
                    arcpy.SetProgressorPosition()


def convert_datatype(in_data_type, params, log):
    """
    Converts Data Model Schema data types to Esri data types.

    :param in_data_type:
    :param params:
    :param log:
    :return:
    """
    esri_data_type = None
    if in_data_type == "TEXT":
        esri_data_type = "TEXT"
    elif in_data_type == "DATETIME":
        esri_data_type = "DATE"
    elif in_data_type == "INTEGER":
        esri_data_type = "LONG"
    elif in_data_type == "REAL":
        esri_data_type = "DOUBLE"
    else:
        messages(
            msgs=[
                f'ERROR: {in_data_type} not recognized domain data type.'
            ],
            msg_lvl='ERROR',
            msg_type=params["params_type"],
            log=log
        )
    return esri_data_type


# ==============================================================================
# Functions
# ==============================================================================
def main(**params):
    """
    Main module
    :param params    Dictionary of script parameters from the
    """
    # =========================================================================
    # Module Initialization
    # =========================================================================

    # Create log file
    log, logfile = CreateLogger(logname=os.path.splitext(os.path.basename(__file__))[0])
    log.info('============================================================')
    log.info(f'Base Path: {__file__}')
    log.info(' ')

    # ==========================================================================
    # Load YAML
    # ==========================================================================
    relative_yaml_path = os.path.join('..', '..', '..', 'schema', 'v3.0', 'flatfile_schema_v3.yaml')
    absolute_yaml_path = os.path.abspath(relative_yaml_path)
    with open(absolute_yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        DOMAINS = data['domains']
        FEATURE_CLASSES = data['feature_classes']

    # Get version of ArcPy
    #   Required to several functional differences in ArcPy between ArcMap and ArcGIS Pro
    #   https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/getinstallinfo.htm
    install_info = arcpy.GetInstallInfo()

    # Parse the FEATURE_CLASSES for primary vs non-primary layers
    # This differentiates primary Service Boundaries from non-primary Service Boundaries
    primary = True if params["primary"] == "true" else False
    primary_layers = []
    if primary:
        for layer in FEATURE_CLASSES:
            if layer["primary"] == primary:
                primary_layers.append(layer)
    else:
        primary_layers = FEATURE_CLASSES

    # Initialize the Progressor, if running through ArcGIS Toolbox
    if params["params_type"] == 'TOOLBOX':
        # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/setprogressor.htm
        max_steps = 1 + len(DOMAINS) + len(primary_layers)
        arcpy.SetProgressor(
            type='step',
            min_range=0,
            max_range=max_steps,
            step_value=1
        )

    # Verify that the code is running in ArcGIS Pro 3.x or later
    if install_info['Version'].startswith('10.'):
        messages(
            msgs=[
                'This tool requires an ArcGIS Pro 3.x or later.'
            ],
            msg_lvl='ERROR',
            msg_type=params["params_type"],
            log=log
        )

    # =========================================================================
    # Module Primary Code
    # =========================================================================

    # Create output file geodatabase name and path
    fgdb_name = params["output_template_name"]
    if fgdb_name.endswith('.gdb'):
        fgdb_name = fgdb_name[-4]
    output_fgdb = os.path.join(fgdb_name + params["file_type"][-5:-1])
    output_fgdb_path = os.path.join(params["output_folder"], output_fgdb)

    # Check if the File Geodatabase exists. Add Error if Allow Overwrite not enabled
    # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/exists.htm
    if arcpy.Exists(output_fgdb_path):
        if params["allow_overwrite"] == "true":
            messages(
                msgs=[
                    'Deleting {}...'.format(output_fgdb)
                ],
                msg_lvl='WARN',
                msg_type=params["params_type"],
                log=log
            )
            # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/delete.htm
            arcpy.management.Delete(output_fgdb_path)
        else:
            messages(
                msgs=[
                    f'{output_fgdb} already exists.Please select a different location or enable Allow Overwrite in the Options.'
                ],
                msg_lvl='ERROR',
                msg_type=params["params_type"],
                log=log
            )

    messages(
        msgs=[
            '{}'.format("#" * 80),
            'Creating File Geodatabase...',
            '{}'.format("#" * 80)
        ],
        msg_lvl='INFO',
        msg_type=params["params_type"],
        log=log,
        progress=False
    )

    # Create new File Geodatabase
    messages(
        msgs=[
            'Creating...'.format(output_fgdb_path)
        ],
        msg_lvl='INFO',
        msg_type=params["params_type"],
        log=log
    )
    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-file-gdb.htm
    arcpy.management.CreateFileGDB(
        out_folder_path=params["output_folder"],
        out_name=params["output_template_name"],
        out_version=params["gdb_version"]
    )

    # Check if the File Geodatabase was created
    if not arcpy.Exists(output_fgdb_path):
        messages(
            msgs=[
                f'ERROR: {output_fgdb} failed to be created.'
            ],
            msg_lvl='ERROR',
            msg_type=params["params_type"],
            log=log
        )
    else:
        messages(
            msgs=[
                f'{output_fgdb} successfully created.'
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log
        )

    arcpy.env.workspace = output_fgdb_path

    # Create NG9-1-1 FGDB Metadata
    # https://pro.arcgis.com/en/pro-app/latest/arcpy/metadata/metadata-class.htm
    if params['include_metadata'] == 'true':
        md = arcpy.metadata.Metadata(output_fgdb_path)
        md.title = CONSTANTS.MD_TITLE
        md.summary = CONSTANTS.MD_SUMMARY
        md.description = CONSTANTS.MD_DESCRIPTION
        md.tags = CONSTANTS.MD_KEYWORDS
        md.credits = CONSTANTS.MD_CREDIT
        md.save()

    # Create NENA Domains and populate initial data, is provided.
    messages(
        msgs=[
            '{}'.format("#" * 80),
            'Creating Domains...',
            '{}'.format("#" * 80)
        ],
        msg_lvl='INFO',
        msg_type=params["params_type"],
        log=log,
        progress=False
    )
    for domain in DOMAINS:
        messages(
            msgs=[
                f'Creating Domain: {domain["domain_name"]}...'
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log
        )
        # Convert DOMAIN data types to Esri equivalents
        esri_data_type = convert_datatype(domain["field_type"], params, log)

        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-domain.htm
        arcpy.management.CreateDomain(
            in_workspace=output_fgdb_path,
            domain_name=domain["domain_name"],
            domain_description=domain["domain_description"],
            field_type=esri_data_type,
            domain_type=domain["domain_type"]
        )
        if domain["values"] is not None:
            if domain["domain_type"] == 'CODED':
                # The following lines are a workaround for Issue #62 where
                # Python prior to v3.6 where dictionaries are not sorted.
                values = []
                for key, value in iteritems(domain["values"]):
                    values.append([key, value])
                values.sort()
                for value in values:
                    messages(
                        msgs=[
                            '|---Creating {} domain value'.format(value[0])
                        ],
                        msg_lvl='INFO',
                        msg_type=params["params_type"],
                        log=log,
                        progress=False
                    )
                    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-coded-value-to-domain.htm
                    arcpy.management.AddCodedValueToDomain(
                        in_workspace=output_fgdb_path,
                        domain_name=domain["domain_name"],
                        code=value[0],
                        code_description=value[1]
                    )
                messages(
                    msgs=[
                        f'|-  Inserted {len(values)} coded values into {domain["domain_name"]}.'
                    ],
                    msg_lvl='INFO',
                    msg_type=params["params_type"],
                    log=log,
                    progress = False
                )
            elif domain["domain_type"] == 'RANGE':
                min_val = domain["values"]["min"]
                max_val = domain["values"]["max"]
                # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/set-value-for-range-domain.htm
                arcpy.management.SetValueForRangeDomain(
                    in_workspace=output_fgdb_path,
                    domain_name=domain["domain_name"],
                    min_value=min_val,
                    max_value=max_val
                )
                messages(
                    msgs=[
                        f'|-  Set ranged values for {domain["domain_name"]} between {str(min_val)} and {str(max_val)}.'
                    ],
                    msg_lvl='INFO',
                    msg_type=params["params_type"],
                    log=log,
                    progress=False
                )
            else:
                messages(
                    msgs=[
                        'ERROR: Could not determine domain type.'
                    ],
                    msg_lvl='ERROR',
                    msg_type=params["params_type"],
                    log=log
                )

    # Create NENA Feature Classes
    messages(
        msgs=[
            '{}'.format("#" * 80),
            'Creating Feature Classes...',
            '{}'.format("#" * 80)
        ],
        msg_lvl='INFO',
        msg_type=params["params_type"],
        log=log,
        progress=False
    )

    for fc in primary_layers:
        messages(
            msgs=[
                f'Creating Feature Class: {fc["name"]}...'
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log
        )
        # Create Esri spatial reference definition
        # https://pro.arcgis.com/en/pro-app/latest/arcpy/classes/spatialreference.htm
        # TODO: Resolve issue with ArcGIS Pro not recognizing EPSG 4979.
        """
        if fc["has_z"]:
            sr = arcpy.SpatialReference(int(params["spatial_reference_horizontal"]), int(params["spatial_reference_vertical"]))
        else:
            sr = arcpy.SpatialReference(int(params["spatial_reference_horizontal"]))
        """

        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-feature-class.htm
        arcpy.management.CreateFeatureclass(
            out_path=output_fgdb_path,
            out_name=fc["name"],
            geometry_type=fc["geometry_type"],
            has_m="Yes" if fc["has_m"] else "No",
            has_z="Yes" if fc["has_z"] else "No",
            spatial_reference=arcpy.SpatialReference(params["spatial_reference_horizontal"]),
            out_alias=fc["alias"]
        )

        messages(
            msgs=[
                f'|- Creating {fc["fields"]} fields for {fc["name"]}...'
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log,
            progress=False
        )
        for field in fc["fields"]:
            messages(
                msgs=[
                    f'|---Creating {field["field_name"]} field'
                ],
                msg_lvl='INFO',
                msg_type=params["params_type"],
                log=log,
                progress=False
            )
            # Convert FIELD data types to Esri equivalents
            esri_data_type = convert_datatype(field["field_type"], params, log)

            # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-field.htm
            arcpy.management.AddField(
                in_table=fc["name"],
                field_name=field["field_name"],
                field_type=esri_data_type,
                field_precision=field["field_precision"],
                field_scale=field["field_scale"],
                field_length=field["field_length"],
                field_alias=field["field_alias"],
                field_is_nullable=field["field_is_nullable"],
                field_is_required=field["field_is_required"],
                field_domain=field["field_domain"]
            )
            default_value = field["field_default"]
            if len(default_value) > 0:
                messages(
                    msgs=[
                        f'|----Adding default value "{default_value}" to {field["field_name"]} field...'
                    ],
                    msg_lvl='INFO',
                    msg_type=params["params_type"],
                    log=log,
                    progress=False
                )
                # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/assign-default-to-field.htm
                arcpy.management.AssignDefaultToField(
                    in_table=fc["name"],
                    field_name=field["field_name"],
                    default_value=default_value
                )
        messages(
            msgs=[
                '|- Enabling UTC date tracking on DateUpdate field...'
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log,
            progress=False
        )
        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/enable-editor-tracking.htm
        arcpy.management.EnableEditorTracking(
            in_dataset=fc["name"],
            last_edit_date_field="DateUpdate",
            record_dates_in='UTC'
        )

        # Create NG9-1-1 Feature Class Metadata
        # https://pro.arcgis.com/en/pro-app/latest/arcpy/metadata/metadata-class.htm
        if params['include_metadata'] == 'true':
            messages(
                msgs=[
                    '|- Creating Feature Class Metadata...'
                ],
                msg_lvl='INFO',
                msg_type=params["params_type"],
                log=log,
                progress=False
            )
            fc_md = arcpy.metadata.Metadata(fc["name"])
            fc_md.title = fc['alias']
            fc_md.summary = fc["metadata"]["description"]
            fc_md.description = fc["metadata"]["description"]
            fc_md.tags = ", ".join(fc["metadata"]["keywords"])
            fc_md.save()

    # =========================================================================
    # Module Cleanup
    # =========================================================================

if __name__ == '__main__':
    """  Transfers Toolbox Parameters to the script.
          
    :returns  params    Dictionary of script parameters
    """

    # Parameters if you want to run this Python script from the console
    # Be sure to change the main() function kwargs to 'main(**console_params)`
    # and change the variables to your environment

    # desktop_path = "~\\Desktop"
    desktop_path = "~\\OneDrive\\Desktop"
    temp = os.path.expanduser(desktop_path)

    console_params = {
        "params_type": 'CONSOLE',      # Do not change this parameter
        "output_folder": temp,
        "output_template_name": 'NG911_GISDataModelTemplate_v3',
        "file_type": 'File Geodatabase (.gdb)',
        "gdb_version": 'CURRENT',
        "spatial_reference_horizontal": CONSTANTS.SR_WGS84_HORIZONTAL,
        "spatial_reference_vertical": CONSTANTS.SR_WGS84_VERTICAL,
        "allow_overwrite": "true",
        "primary": "false",
        "include_metadata": "true"
    }

    # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/getparameterastext.htm
    # TODO: Not yet implemented.
    toolbox_params = {
        "params_type": 'TOOLBOX',
        "output_folder": arcpy.GetParameterAsText(0),
        "output_template_name": arcpy.GetParameterAsText(1),
        "file_type": 'File Geodatabase (.gdb)',
        "gdb_version": arcpy.GetParameterAsText(2),
        "spatial_reference_horizontal": arcpy.GetParameterAsText(3),
        "spatial_reference_vertical": CONSTANTS.SR_WGS84_VERTICAL,
        "allow_overwrite": arcpy.GetParameterAsText(4),
        "primary": arcpy.GetParameterAsText(5),
        "include_metadata": arcpy.GetParameterAsText(6)
    }
    main(**console_params)
