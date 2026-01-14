# Global-Emerald-Spatial-Analysis
Spatial Distribution Analysis of Global Beryl Deposits Using Python and QGIS

Global Emerald Spatial Analysis 🌍💎

Project Overview
This project analyzes the spatial distribution of major global emerald deposits (e.g., Muzo, Panjshir) and their proximity to administrative and tectonic boundaries. 

Using Python (GeoPandas) and QGIS, I calculated the geodesic distance from mining sites to provincial borders to investigate the relationship between mineralization zones and geological/administrative edges.

Visualization
[Emerald Map](Final Map-Emerald.jpg)

Methodologies
1. Data Processing: Used `Pandas` to clean raw coordinate data from geological surveys.
2. Spatial Calculation: 
   - Converted coordinates to EPSG:3857 for accurate metric calculation.
   - Wrote a Python script to calculate the minimum distance from each mine to the nearest `1:10m` provincial boundary.
3. Cartography: Produced a high-resolution hillshade map in QGIS with contour lines to highlight the high-altitude characteristics of emerald deposits.

PS. Files
- `emerald analysis.py`: Python script for distance calculation.
- `final emerald (10m).csv`: The processed dataset with distance results.
- `Final Map-Emerald.jpg`: The final visualization output.
