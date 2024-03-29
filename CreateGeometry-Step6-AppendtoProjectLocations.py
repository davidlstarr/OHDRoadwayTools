# -*- coding: utf-8 -*-
"""Generated by ArcGIS ModelBuilder on: 2019-12-03 14:32:22
All ModelBuilder functionality may not be exported. Edits may be required for equivalency with the original model.
"""

import arcpy
import json

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

# Script parameters
arcpy.env.workspace = arcpy.GetParameterAsText(0)

#Make sure to drop the config file in your ArcPro project
with open(arcpy.env.workspace+'/config.json') as json_data_file:
    data = json.load(json_data_file)

# Local variables:
roads_buffer_clip2 = data["temp_paths"]["roads_buffer_clip2"]
project_locations = data["wfs_paths"]["WFS_project_locations_path"]
project_listings = data["wfs_paths"]["WFS_project_listings_path"]

#arcpy.RemoveJoin_management(project_locations, project_listings)

# Process: Append
arcpy.Append_management(inputs=roads_buffer_clip2, target=project_locations, schema_type="NO_TEST", field_mapping="project_locations.CCID 'CCID' true true false 255 Text 0 0,First,#;project_listings.CCID 'CCID' true true false 255 Text 0 0,First,#;project_listings.UPDATEUSER 'UPDATEUSER' true true false 255 Text 0 0,First,#;project_listings.CONSTR_CONTRACT_NO 'CONSTR_CONTRACT_NO' true true false 255 Text 0 0,First,#;project_listings.PE_FMIS_ID_NO 'PE_FMIS_ID_NO' true true false 255 Text 0 0,First,#;project_listings.PROJECT_TYPE_ID 'PROJECT_TYPE_ID' true true false 255 Text 0 0,First,#;project_listings.PROJECT_TYPE 'PROJECT_TYPE' true true false 255 Text 0 0,First,#;project_listings.DESIGN_BUILD 'DESIGN_BUILD' true true false 255 Text 0 0,First,#;project_listings.FUND_SOURCE 'FUND_SOURCE' true true false 255 Text 0 0,First,#;project_listings.DESCRIPTION 'DESCRIPTION' true true false 255 Text 0 0,First,#;project_listings.ISARCHIVED 'ISARCHIVED' true true false 255 Text 0 0,First,#;project_listings.PROJSTART 'PROJSTART' true true false 8 Date 0 0,First,#;project_listings.ACTUAL_AD 'ACTUAL_AD' true true false 8 Date 0 0,First,#;project_listings.LEAD_DIVISION_ID 'LEAD_DIVISION_ID' true true false 255 Text 0 0,First,#;project_listings.STATUS_ID 'STATUS_ID' true true false 4 Long 0 0,First,#;project_listings.STATUS 'STATUS' true true false 255 Text 0 0,First,#;project_listings.DISPLAYNAME 'DISPLAYNAME' true true false 255 Text 0 0,First,#;project_listings.ENGINEER_ID 'ENGINEER_ID' true true false 255 Text 0 0,First,#;project_listings.COUNTY_ID 'COUNTY_ID' true true false 255 Text 0 0,First,#;project_listings.COUNTY_NAME 'COUNTY_NAME' true true false 255 Text 0 0,First,#;project_listings.PRIMARY_ROUTE 'PRIMARY_ROUTE' true true false 255 Text 0 0,First,#;project_listings.DISTRICT_ID 'DISTRICT_ID' true true false 8 Double 0 0,First,#", subtype="", expression="")

arcpy.SelectLayerByLocation_management(project_locations, "ARE IDENTICAL TO", roads_buffer_clip2)

# aprx = arcpy.mp.ArcGISProject("CURRENT")
# map = aprx.listMaps()[0]  # assumes data to be added to first map listed
# roads_clip_layer = map.listLayers("roads_buffer_clip2")[0]
#
# map.removeLayer(roads_clip_layer)

