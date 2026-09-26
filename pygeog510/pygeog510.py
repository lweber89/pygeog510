import ipyleaflet


class Map(ipyleaflet.Map):
    """_summary_"""

    def __init__(self, center=[20, 0], zoom=2, height="600px", **kwargs):
        """_summary_

        Args:
            center (list, optional): _description_. Defaults to [20, 0].
            zoom (int, optional): _description_. Defaults to 2.
            height (str, optional): _description_. Defaults to "600px".
        """
        super().__init__(center=center, zoom=zoom, **kwargs)
        self.layout.height = height

    def add_basemap(self, basemap="OpenTopoMap"):
        """_summary_

        Args:
            basemap (str, optional): _description_. Defaults to "OpenTopoMap".
        """
        url = eval(f"ipyleaflet.basemaps.{basemap}").build_url()
        layer = ipyleaflet.TileLayer(url=url, name=basemap)
        self.add(layer)
