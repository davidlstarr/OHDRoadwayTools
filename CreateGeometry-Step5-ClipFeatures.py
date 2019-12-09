# -*- coding: utf-8 -*-
"""Generated by ArcGIS ModelBuilder on: 2019-12-03 12:09:37
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
roads_buffer = data["temp_paths"]["roads_buffer"]
roads_buffer_clip = data["temp_paths"]["roads_buffer_clip"]
roads_buffer_clip2 = data["temp_paths"]["roads_buffer_clip2"]
roads_clip_path = r"" + arcpy.env.workspace + "\\roads_buffer_clip2"

# Process: Clip

arcpy.Delete_management(roads_buffer_clip2)
arcpy.Clip_analysis(in_features=roads_buffer, clip_features=roads_buffer_clip, out_feature_class=roads_buffer_clip2, cluster_tolerance="")


aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]  # assumes data to be added to first map listed
map.addDataFromPath(roads_clip_path)


