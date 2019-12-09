# -*- coding: utf-8 -*-
"""Generated by ArcGIS ModelBuilder on: 2019-12-03 15:06:40
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
project_locations = data["wfs_paths"]["WFS_project_locations_path"]
project_listings = data["wfs_paths"]["WFS_project_listings_path"]
field = "CCID"
cursor = arcpy.SearchCursor(project_listings)

# Process: Calculate Field

for row in cursor:
    arcpy.AddMessage(row.getValue(field))
    CCID = row.getValue(field)
    arcpy.CalculateField_management(in_table=project_locations, field="project_locations.CCID", expression=CCID, expression_type="PYTHON3", code_block="")

