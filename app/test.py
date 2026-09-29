import geopandas as gpd

gdf = gpd.read_file("/Users/tom/Downloads/Watersheds_1M.gdb")
gdf.to_csv("watersheds.csv", index=False)