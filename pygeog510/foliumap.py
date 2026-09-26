import folium


class Map(folium.Map):
    def __init__(self, center=(0, 0), zoom=2, **kwargs):
        """_summary_

        Args:
            center (tuple, optional): _description_. Defaults to (0, 0).
            zoom (int, optional): _description_. Defaults to 2.
        """
        super().__init__(location=center, zoom_start=zoom, **kwargs)

    def add_basemap(self, *args, **kwargs):
        print("Made it to add_basemap")

    def add_layer_control(self, *args, **kwargs):
        print("Made it to add_layer_control")

    def add_vector(self, *args, **kwargs):
        print("Made it to add_vector")
