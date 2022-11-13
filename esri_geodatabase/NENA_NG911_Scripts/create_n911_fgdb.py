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
import arcpy
from sys import exit
from schema.schema_fgdb_v2 import DOMAINS, FEATURE_CLASSES, TABLES, RELATES


def main(**params):
    """
    Main module
    :param params    Dictionary of script parameters from the
    """
    # =========================================================================
    # Module Initialization
    # =========================================================================
    # Get version of ArcPy
    # Used for several functional differences in ArcPy between ArcMap and ArcGIS Pro
    # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/getinstallinfo.htm
    version_number = arcpy.GetInstallInfo()['Version']

    # Initialize the Progressor
    # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/setprogressor.htm
    max_steps = 1 + len(DOMAINS) + len(FEATURE_CLASSES) + len(TABLES) + len(RELATES)
    arcpy.SetProgressor(
        type='step',
        min_range=0,
        max_range=max_steps,
        step_value=1
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
            # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/addwarning.htm
            arcpy.AddWarning('Deleting {}...'.format(output_fgdb))
            # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/delete.htm
            arcpy.management.Delete(output_fgdb_path)
        else:
            # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/adderror.htm
            arcpy.AddError('{} already exists.'.format(output_fgdb))
            arcpy.AddError('Please select a different location or '
                           'enable Allow Overwrite in the Options.')
            exit()

    # Add message to ArcGIS Geoprocessing Tool
    # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/addmessage.htm
    arcpy.AddMessage('{}'.format("#" * 80))
    arcpy.AddMessage('Creating File Geodatabase...')
    arcpy.AddMessage('{}'.format("#" * 80))

    # Create new File Geodatabase
    msg = 'Creating {output_fgdb}...'
    arcpy.SetProgressorLabel(msg)
    arcpy.AddMessage(msg)
    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-file-gdb.htm
    arcpy.management.CreateFileGDB(
        out_folder_path=params["output_folder"],
        out_name=params["output_name"],
        out_version=params["gdb_version"]
    )

    # Check if the File Geodatabase was created
    if not arcpy.Exists(output_fgdb_path):
        arcpy.AddError('ERROR: {} failed to be created.'.format(output_fgdb))
        exit()
    else:
        arcpy.AddMessage('{} successfully created.'.format(output_fgdb))
        arcpy.SetProgressorPosition()

    arcpy.env.workspace = output_fgdb_path

    # Create NENA Domains and populate initial data, is provided.
    arcpy.AddMessage('{}'.format("#" * 80))
    arcpy.AddMessage('Creating Domains...')
    arcpy.AddMessage('{}'.format("#" * 80))
    for domain in DOMAINS:
        msg = 'Creating Domain: {}...'.format(domain["domain_name"])
        arcpy.SetProgressorLabel(msg)
        arcpy.AddMessage(msg)
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
                    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-coded-value-to-domain.htm
                    arcpy.management.AddCodedValueToDomain(
                        in_workspace=output_fgdb_path,
                        domain_name=domain["domain_name"],
                        code=k,
                        code_description=values[k]
                    )
                arcpy.AddMessage('-  Inserted {} coded values into {}.'.format(len(values), domain["domain_name"]))
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
                arcpy.AddMessage('-  Set ranged values for {} between {} and {}.'.format(
                    domain["domain_name"], min_val, max_val))
                pass
            else:
                arcpy.AddError('ERROR: Could not determine domain type.')
        arcpy.SetProgressorPosition()

    # Create NENA Feature Classes
    arcpy.AddMessage('{}'.format("#" * 80))
    arcpy.AddMessage('Creating Feature Classes...')
    arcpy.AddMessage('{}'.format("#" * 80))

    for fc in FEATURE_CLASSES:
        msg = 'Creating Feature Class: {}...'.format(fc["out_name"])
        arcpy.SetProgressorLabel(msg)
        arcpy.AddMessage(msg)
        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-feature-class.htm
        if version_number.startswith('10.'):
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
        arcpy.AddMessage('- Creating {} fields for {}...'.format(len(fc["fields"]), fc["out_name"]))
        for field in fc["fields"]:
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
        arcpy.AddMessage('- Enabling UTC date tracking on DateUpdate field...')
        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/enable-editor-tracking.htm
        arcpy.management.EnableEditorTracking(
            in_dataset=fc["out_name"],
            last_edit_date_field="DateUpdate",
            record_dates_in='UTC'
        )
        arcpy.SetProgressorPosition()

    # Create NENA Tables
    arcpy.AddMessage('{}'.format("#" * 80))
    arcpy.AddMessage('Creating Tables...')
    arcpy.AddMessage('{}'.format("#" * 80))

    for table in TABLES:
        msg = 'Creating Table: {}...'.format(table["out_name"])
        arcpy.SetProgressorLabel(msg)
        arcpy.AddMessage(msg)
        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-table.htm
        if version_number.startswith('10.'):
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
        arcpy.AddMessage('- Creating {} fields for {}...'.format(len(table["fields"]), table["out_name"]))
        for field in table["fields"]:
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
        arcpy.AddMessage('- Enabling UTC date tracking on DateUpdate field...')
        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/enable-editor-tracking.htm
        arcpy.management.EnableEditorTracking(
            in_dataset=table["out_name"],
            last_edit_date_field="DateUpdate",
            record_dates_in='UTC'
        )
        arcpy.SetProgressorPosition()

    # Create NENA Relationship Classes
    arcpy.AddMessage('{}'.format("#" * 80))
    arcpy.AddMessage('Creating Relationships...')
    arcpy.AddMessage('{}'.format("#" * 80))

    for relate in RELATES:
        msg = 'Creating Relationship between {} and {}'.format(relate["origin_table"], relate["destination_table"])
        arcpy.SetProgressorLabel(msg)
        arcpy.AddMessage(msg)
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
    Note: To use only as a script, modify the "local_params" values to your 
          environment and change kwargs variable in the main() call.
    """
    sr = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],'\
         'PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;'\
         '-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision'
    local_params = {
        "output_folder": r'C:\Users\<username>\Desktop',
        "output_name": 'ng911',
        "file_type": 'File Geodatabase (.gdb)',
        "gdb_version": 'CURRENT',
        "spatial_reference": sr,
        "allow_overwrite": "true"
    }

    # https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/getparameterastext.htm
    script_params = {
        "output_folder": arcpy.GetParameterAsText(0),
        "output_name": arcpy.GetParameterAsText(1),
        "file_type": 'File Geodatabase (.gdb)',
        "gdb_version": arcpy.GetParameterAsText(2),
        "spatial_reference": arcpy.GetParameterAsText(3),
        "allow_overwrite": arcpy.GetParameterAsText(4)
    }
    main(**script_params)
