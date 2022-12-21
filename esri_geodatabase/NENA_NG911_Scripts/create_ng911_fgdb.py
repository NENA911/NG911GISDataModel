# create_ng11_fgdb.py
"""
| Name:      Create NG9-1-1 File Geodatabase
| Purpose:
|
| Notes:     This code is written so it will support both Python 2.7.x
|            and Python 3.x.
|
| Author:    NENA Data Structures Committee, DS-GIS Template Working Group
|
| Created:   2022-11-05
| Modified:  2022-11-13
"""
import os
from sys import exit
import arcpy

from util import CreateLogger
from schema.schema_fgdb_v2 import DOMAINS, FEATURE_CLASSES, TABLES, RELATES

# ==============================================================================
# Constants
# ==============================================================================
SR_WGS84 = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",' \
           'SPHEROID["WGS_1984",6378137.0,298.257223563]],' \
           'PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];' \
           '-400 -400 1000000000;-100000 10000;' \
           '-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision'


def messages(msgs, msg_lvl, msg_type, log, progress=True):
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
    log.info('{}'.format(__file__))
    log.info(' ')

    # Get version of ArcPy
    #   Required to several functional differences in ArcPy between ArcMap and ArcGIS Pro
    #   https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/getinstallinfo.htm
    install_info = arcpy.GetInstallInfo()

    # Initialize the Progressor, if ArcGIS Toolbox
    if params["params_type"] == 'TOOLBOX':
        # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/setprogressor.htm
        max_steps = 1 + len(DOMAINS) + len(FEATURE_CLASSES) + len(TABLES) + len(RELATES)
        arcpy.SetProgressor(
            type='step',
            min_range=0,
            max_range=max_steps,
            step_value=1
        )

    # Check the license level is not "Basic" as the CreateRelationshipClass
    # function requires a "Standard or "Advanced" license
    if install_info['Version'].startswith('10.'):
        if arcpy.ProductInfo() == 'ArcView':
            messages(
                msgs=[
                    'This script requires an ArcGIS Desktop licensing level '
                    'of "Standard" or "Advanced".'
                ],
                msg_lvl='ERROR',
                msg_type=params["params_type"],
                log=log
            )
    else:
        if install_info['LicenseLevel'] == "Basic":
            messages(
                msgs=[
                    'This script requires an ArcGIS Desktop licensing level '
                    'of "Standard" or "Advanced".'
                ],
                msg_lvl='ERROR',
                msg_type=params["params_type"],
                log=log
            )

    # =========================================================================
    # Module Primary Code
    # =========================================================================

    # Create output file geodatabase name and path
    fgdb_name = params["output_name"]
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
                    '{} already exists.'.format(output_fgdb),
                    'Please select a different location or '
                    'enable Allow Overwrite in the Options.'
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
        out_name=params["output_name"],
        out_version=params["gdb_version"]
    )

    # Check if the File Geodatabase was created
    if not arcpy.Exists(output_fgdb_path):
        messages(
            msgs=[
                'ERROR: {} failed to be created.'.format(output_fgdb)
            ],
            msg_lvl='ERROR',
            msg_type=params["params_type"],
            log=log
        )
    else:
        messages(
            msgs=[
                '{} successfully created.'.format(output_fgdb)
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log
        )

    arcpy.env.workspace = output_fgdb_path

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
                'Creating Domain: {}...'.format(domain["domain_name"])
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log
        )
        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-domain.htm
        arcpy.management.CreateDomain(
            in_workspace=output_fgdb_path,
            domain_name=domain["domain_name"],
            domain_description=domain["domain_description"],
            field_type=domain["field_type"],
            domain_type=domain["domain_type"]
        )
        if domain["values"] is not None:
            if domain["domain_type"] == 'CODED':
                values = domain["values"]
                for k in values:
                    messages(
                        msgs=[
                            '|---Creating {} domain value'.format(k)
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
                        code=k,
                        code_description=values[k]
                    )
                messages(
                    msgs=[
                        '-  Inserted {} coded values into {}.'.format(
                            len(values), domain["domain_name"])
                    ],
                    msg_lvl='INFO',
                    msg_type=params["params_type"],
                    log=log,
                    progress = False
                )
            elif domain["domain_type"]:
                min_val = domain["values"][0]
                max_val = domain["values"][1]
                # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/set-value-for-range-domain.htm
                arcpy.arcpy.management.SetValueForRangeDomain(
                    in_workspace=output_fgdb_path,
                    domain_name=domain["domain_name"],
                    min_value=min_val,
                    max_value=max_val
                )
                messages(
                    msgs=[
                        '-  Set ranged values for {} between {} and {}.'.format(
                            domain["domain_name"], min_val, max_val)
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

    for fc in FEATURE_CLASSES:
        messages(
            msgs=[
                'Creating Feature Class: {}...'.format(fc["out_name"])
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log
        )
        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-feature-class.htm
        if install_info['Version'].startswith('10.'):
            arcpy.management.CreateFeatureclass(
                out_path=output_fgdb_path,
                out_name=fc["out_name"],
                geometry_type=fc["geometry_type"],
                has_m=fc["has_m"],
                has_z=fc["has_z"],
                spatial_reference=params["spatial_reference"],
            )
            arcpy.AlterAliasName(
                table=fc["out_name"],
                alias=fc["out_alias"]
            )
        else:
            arcpy.management.CreateFeatureclass(
                out_path=output_fgdb_path,
                out_name=fc["out_name"],
                geometry_type=fc["geometry_type"],
                has_m=fc["has_m"],
                has_z=fc["has_z"],
                spatial_reference=params["spatial_reference"],
                out_alias=fc["out_alias"]
            )
        messages(
            msgs=[
                '- Creating {} fields for {}...'.format(len(fc["fields"]), fc["out_name"])
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log,
            progress=False
        )
        for field in fc["fields"]:
            messages(
                msgs=[
                    '|---Creating {} field'.format(field[0])
                ],
                msg_lvl='INFO',
                msg_type=params["params_type"],
                log=log,
                progress=False
            )
            # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-field.htm
            arcpy.management.AddField(
                in_table=fc["out_name"],
                field_name=field[0],
                field_type=field[1],
                field_precision=field[2],
                field_scale=field[3],
                field_length=field[4],
                field_alias=field[5],
                field_is_nullable=field[6],
                field_is_required=field[7],
                field_domain=field[8]
            )
        messages(
            msgs=[
                '- Enabling UTC date tracking on DateUpdate field...'
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log,
            progress=False
        )
        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/enable-editor-tracking.htm
        arcpy.management.EnableEditorTracking(
            in_dataset=fc["out_name"],
            last_edit_date_field="DateUpdate",
            record_dates_in='UTC'
        )

    # Create NENA Tables
    messages(
        msgs=[
            '{}'.format("#" * 80),
            'Creating Tables...',
            '{}'.format("#" * 80)
        ],
        msg_lvl='INFO',
        msg_type=params["params_type"],
        log=log,
        progress=False
    )

    for table in TABLES:
        messages(
            msgs=[
                'Creating Table: {}...'.format(table["out_name"])
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log
        )
        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-table.htm
        if install_info['Version'].startswith('10.'):
            arcpy.management.CreateTable(
                out_path=output_fgdb_path,
                out_name=table["out_name"]
            )
            arcpy.AlterAliasName(
                table=table["out_name"],
                alias=table["out_alias"]
            )
        else:
            arcpy.management.CreateTable(
                out_path=output_fgdb_path,
                out_name=table["out_name"],
                out_alias=table["out_alias"],
            )
        messages(
            msgs=[
                '- Creating {} fields for {}...'.format(len(table["fields"]), table["out_name"])
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log,
            progress=False
        )
        for field in table["fields"]:
            messages(
                msgs=[
                    '|---Creating {} field'.format(field[0])
                ],
                msg_lvl='INFO',
                msg_type=params["params_type"],
                log=log,
                progress=False
            )
            # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-field.htm
            arcpy.management.AddField(
                in_table=table["out_name"],
                field_name=field[0],
                field_type=field[1],
                field_precision=field[2],
                field_scale=field[3],
                field_length=field[4],
                field_alias=field[5],
                field_is_nullable=field[6],
                field_is_required=field[7],
                field_domain=field[8]
            )
        messages(
            msgs=[
                '- Enabling UTC date tracking on DateUpdate field...'
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log,
            progress=False
        )
        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/enable-editor-tracking.htm
        arcpy.management.EnableEditorTracking(
            in_dataset=table["out_name"],
            last_edit_date_field="DateUpdate",
            record_dates_in='UTC'
        )

    # Create NENA Relationship Classes
    messages(
        msgs=[
            '{}'.format("#" * 80),
            'Creating Relationships...',
            '{}'.format("#" * 80)
        ],
        msg_lvl='INFO',
        msg_type=params["params_type"],
        log=log,
        progress=False
    )

    for relate in RELATES:
        messages(
            msgs=[
                'Creating Relationship between {} and {}'.format(
                    relate["origin_table"], relate["destination_table"])
            ],
            msg_lvl='INFO',
            msg_type=params["params_type"],
            log=log
        )
        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-relationship-class.htm
        arcpy.management.CreateRelationshipClass(
            origin_table=relate["origin_table"],
            destination_table=relate["destination_table"],
            out_relationship_class=relate["out_relationship_class"],
            relationship_type=relate["relationship_type"],
            forward_label=relate["forward_label"],
            backward_label=relate["backward_label"],
            message_direction=relate["message_direction"],
            cardinality=relate["cardinality"],
            attributed=relate["attributed"],
            origin_primary_key=relate["origin_primary_key"],
            origin_foreign_key=relate["origin_foreign_key"]
        )

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
    temp = r'C:\Users\tomne\OneDrive\Desktop'
    # r'C:\Users\<username>\Desktop'
    console_params = {
        "params_type": 'CONSOLE',      # Do not change this parameter
        "output_folder": temp,
        "output_name": 'ng911',
        "file_type": 'File Geodatabase (.gdb)',
        "gdb_version": 'CURRENT',
        "spatial_reference": SR_WGS84,
        "allow_overwrite": "true"
    }

    # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/getparameterastext.htm
    toolbox_params = {
        "params_type": 'TOOLBOX',
        "output_folder": arcpy.GetParameterAsText(0),
        "output_name": arcpy.GetParameterAsText(1),
        "file_type": 'File Geodatabase (.gdb)',
        "gdb_version": arcpy.GetParameterAsText(2),
        "spatial_reference": arcpy.GetParameterAsText(3),
        "allow_overwrite": arcpy.GetParameterAsText(4)
    }
    main(**toolbox_params)
