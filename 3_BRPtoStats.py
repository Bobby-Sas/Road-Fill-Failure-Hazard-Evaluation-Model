# ---------------------------------------------------------------------------
# 3_BRPtoStats.py
# Created on: Mon Mar 17 2008 04:21:34 PM
#   (generated by ArcGIS/ModelBuilder)
# Product: Bobby Sas, Student, MS Applied Geosciences, San Francisco State University
# Code: Jerry Davis and Barry Nickel, Institute for Geographic Information Science, San Francisco State University
#
# General Description: 3_BRPtoStats.py is step 3 of 4. Analyze DEM for Slope Values. 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Check out any necessary licenses
gp.CheckOutExtension("spatial")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Spatial Analyst Tools.tbx")
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Conversion Tools.tbx")
gp.AddToolbox("C:/docs/py/geomorph/BRPtools.tbx")
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Analysis Tools.tbx")


# Local variables...
SelectedRoadSeg_shp = "C:\\docs\\py\\geomorph\\SelectedRoadSeg.shp"
buffered_points = "C:\\docs\\py\\geomorph\\densifiedRdPts_Buffer.shp"
rdbed_shp = "C:\\docs\\py\\geomorph\\rdbed.shp"
slopecells = "C:\\docs\\py\\geomorph\\slopecells"
v0 = "0"
slopepoly_shp = "C:\\docs\\py\\geomorph\\slopepoly.shp"
slopepoly_Union_shp = "C:\\docs\\py\\geomorph\\slopepoly_Union.shp"
notRoad_mask_shp = "C:\\docs\\py\\geomorph\\notRoad_mask.shp"
undensifiedPoints_shp = "C:\\docs\\py\\geomorph\\undensifiedPoints.shp"
SelectedRoadSeg_shp__2_ = "C:\\docs\\py\\geomorph\\SelectedRoadSeg.shp"
Circle_Statistics = "C:\\docs\\py\\geomorph\\zonalStats.dbf"
densifiedPts_shp = "C:\\docs\\py\\geomorph\\densifiedPts.shp"
v90m_slp_int__2_ = "C:\\docs\\py\\geomorph\\90m_slp_int"
MotorROAD_Project1_shp__2_ = "C:\\docs\\py\\geomorph\\MotorROAD_Project1.shp"
notRdMask = "C:\\docs\\py\\geomorph\\notRdMask"

# Process: Select...
gp.Select_analysis(MotorROAD_Project1_shp__2_, SelectedRoadSeg_shp, "\"FID\" = 15")

# Process: Convert Line Vertices to Points...
gp.toolbox = "C:/docs/py/geomorph/BRPtools.tbx"
gp.lines2pts(SelectedRoadSeg_shp, undensifiedPoints_shp)

# Process: DensifyArcs...
gp.toolbox = "C:/docs/py/geomorph/BRPtools.tbx"
gp.DensifyArcs(SelectedRoadSeg_shp, "100", "0")

# Process: Convert Line Vertices to Points (2)...
gp.toolbox = "C:/docs/py/geomorph/BRPtools.tbx"
gp.lines2pts(SelectedRoadSeg_shp__2_, densifiedPts_shp)

# Process: Buffer...
gp.Buffer_analysis(densifiedPts_shp, buffered_points, "100 Feet", "FULL", "ROUND", "NONE", "")

# Process: Greater Than Equal...
gp.GreaterThanEqual_sa(v90m_slp_int__2_, v0, slopecells)

# Process: Raster to Polygon...
gp.RasterToPolygon_conversion(slopecells, slopepoly_shp, "NO_SIMPLIFY", "VALUE")

# Process: Buffer (2)...
gp.Buffer_analysis(SelectedRoadSeg_shp, rdbed_shp, "10 Feet", "FULL", "ROUND", "ALL", "")

# Process: Union...
gp.Union_analysis("C:\\docs\\py\\geomorph\\slopepoly.shp #;C:\\docs\\py\\geomorph\\rdbed.shp #", slopepoly_Union_shp, "ALL", "", "GAPS")

# Process: Select (2)...
gp.Select_analysis(slopepoly_Union_shp, notRoad_mask_shp, "\"FID_rdbed\" = -1")

# Process: Feature to Raster...
tempEnvironment0 = gp.XYResolution
gp.XYResolution = ""
tempEnvironment1 = gp.scratchWorkspace
gp.scratchWorkspace = ""
tempEnvironment2 = gp.MTolerance
gp.MTolerance = ""
tempEnvironment3 = gp.randomGenerator
gp.randomGenerator = "0 ACM599"
tempEnvironment4 = gp.outputCoordinateSystem
gp.outputCoordinateSystem = ""
tempEnvironment5 = gp.outputZFlag
gp.outputZFlag = "Same As Input"
tempEnvironment6 = gp.qualifiedFieldNames
gp.qualifiedFieldNames = "true"
tempEnvironment7 = gp.extent
gp.extent = "C:\\docs\\py\\geomorph\\90m_slp_int"
tempEnvironment8 = gp.XYTolerance
gp.XYTolerance = ""
tempEnvironment9 = gp.cellSize
gp.cellSize = "20"
tempEnvironment10 = gp.outputZValue
gp.outputZValue = ""
tempEnvironment11 = gp.outputMFlag
gp.outputMFlag = "Same As Input"
tempEnvironment12 = gp.geographicTransformations
gp.geographicTransformations = ""
tempEnvironment13 = gp.ZResolution
gp.ZResolution = ""
tempEnvironment14 = gp.workspace
gp.workspace = ""
tempEnvironment15 = gp.MResolution
gp.MResolution = ""
tempEnvironment16 = gp.ZTolerance
gp.ZTolerance = ""
gp.FeatureToRaster_conversion(notRoad_mask_shp, "FID_slopep", notRdMask, v90m_slp_int__2_)
gp.XYResolution = tempEnvironment0
gp.scratchWorkspace = tempEnvironment1
gp.MTolerance = tempEnvironment2
gp.randomGenerator = tempEnvironment3
gp.outputCoordinateSystem = tempEnvironment4
gp.outputZFlag = tempEnvironment5
gp.qualifiedFieldNames = tempEnvironment6
gp.extent = tempEnvironment7
gp.XYTolerance = tempEnvironment8
gp.cellSize = tempEnvironment9
gp.outputZValue = tempEnvironment10
gp.outputMFlag = tempEnvironment11
gp.geographicTransformations = tempEnvironment12
gp.ZResolution = tempEnvironment13
gp.workspace = tempEnvironment14
gp.MResolution = tempEnvironment15
gp.ZTolerance = tempEnvironment16

# Process: Circle Stats...
tempEnvironment0 = gp.cellSize
gp.cellSize = "MAXOF"
tempEnvironment1 = gp.mask
gp.mask = "C:\\docs\\py\\geomorph\\notRdMask"
gp.toolbox = "C:/docs/py/geomorph/BRPtools.tbx"
gp.circlestats(buffered_points, v90m_slp_int__2_, Circle_Statistics)
gp.cellSize = tempEnvironment0
gp.mask = tempEnvironment1
