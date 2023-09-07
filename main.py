from gps_class import GPSVis

for x in range(1,6):
    vis = GPSVis(
        data_path=x,                                    # <--- data file with GSM positions (change only this row)
        locations="data-locations.csv",                 # restaurants and residences
        map_path="data-map.png",                        # Map downloaded from OSM (https://www.openstreetmap.org/export)
        points=(40.7544, 14.4782, 40.7470, 14.4993)     # Two coordinates of the map (upper left, lower right)
    )

    vis.create_image(color=(0, 0, 255), width=5)  # Set the color and the width of the GNSS tracks.
    vis.plot_map(output='save')

# print()
