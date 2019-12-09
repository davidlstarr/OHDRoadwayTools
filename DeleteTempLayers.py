
import arcpy

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

# Script parameters
arcpy.env.workspace = arcpy.GetParameterAsText(0)



# Local variables:
arcpy.Delete_management("roads_buffer")
arcpy.Delete_management("roads_buffer_clip2")
arcpy.TruncateTable_management("roads_buffer_clip")
arcpy.TruncateTable_management("roads_buffer")

