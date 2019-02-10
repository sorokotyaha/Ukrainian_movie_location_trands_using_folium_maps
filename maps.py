import folium
import pandas as pd
from folium.plugins import HeatMap


def generate_base_map(default_location=[49.09285285, 33.4308188490926], default_zoom_start=5.5):
    """
    This function generates the base map of Ukraine
    :param default_location: lst[float, float]
    :param default_zoom_start: int or float
    :return: folium.Map object
    """
    base_map = folium.Map(location=default_location,
                          control_scale=True,
                          zoom_start=default_zoom_start)
    base_map.save("Base_map.html")
    return base_map


def generate_heat_map(years, base_map):
    """
    This function generates heat map as a second layer of base map
    :return: folium.Map object
    """
    for year in years:
        name = year + '.csv'
        df_coords = pd.read_csv(name)

        hm = folium.FeatureGroup(name="Popularity of locations in " + year)

        df_copy = df_coords.copy()
        df_copy['count'] = 1
        hm.add_child(HeatMap(data=df_copy[['lat', 'lon', 'count']].groupby(
            ['lat', 'lon']).sum().reset_index().values.tolist(), radius=15, max_zoom=13))

        base_map.add_child(hm)
    base_map.add_child(folium.LayerControl())
    base_map.save("Base_map.html")
    return base_map


if __name__ == "__main__":
    b_map = generate_base_map()
    years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']
    generate_heat_map(years, b_map)

