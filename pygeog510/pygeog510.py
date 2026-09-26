import ipyleaflet


class Map(ipyleaflet.Map):

    def __init__(self, center=[20, 0], zoom=2, height="600px", **kwargs):
        """Initialize Map class

        Args:
            center (list, optional): _description_. Defaults to [20, 0].
            zoom (int, optional): _description_. Defaults to 2.
            height (str, optional): _description_. Defaults to "600px".
        """
        super().__init__(center=center, zoom=zoom, **kwargs)
        self.layout.height = height

    def add_basemap(self, basemap="OpenTopoMap"):
        """Adds a basemap to the map based on user input (or defaults to OpenTopoMap)

        Args:
            basemap (str, optional): _description_. Defaults to "OpenTopoMap".
        """
        url = eval(f"ipyleaflet.basemaps.{basemap}").build_url()
        layer = ipyleaflet.TileLayer(url=url, name=basemap)
        self.add(layer)

    def add_geojson(
        self,
        data,
        zoom_to_layer=True,
        hover_style=None,
        **kwargs,
    ):
        """Adds a GeoJSON layer to the map.

        Args:
            data (str or dict): The GeoJSON data. Can be a file path (str) or a dictionary.
            zoom_to_layer (bool, optional): Whether to zoom to the layer's bounds. Defaults to True.
            hover_style (dict, optional): Style to apply when hovering over features. Defaults to {"color": "yellow", "fillOpacity": 0.2}.
            **kwargs: Additional keyword arguments for the ipyleaflet.GeoJSON layer.

        Raises:
            ValueError: If the data type is invalid.
        """

        import geopandas as gpd

        if hover_style == None:
            hover_style = {"color": "yellow", "fillOpacity": 0.2}

        gdf = gpd.read_file(data)
        geojson = gdf.__geo_interface__

        layer = ipyleaflet.GeoJSON(data=geojson, hover_style=hover_style)
        self.add_layer(layer)

        if zoom_to_layer:
            bounds = gdf.total_bounds
            self.fit_bounds([[bounds[1], bounds[0]], [bounds[3], bounds[2]]])

    def add_layer_control(self):
        """Adds a layer control widget to the map."""
        control = ipyleaflet.LayersControl(position="topright")
        self.add_control(control)
