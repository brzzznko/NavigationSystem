import osmnx

from PathFinder import PathFinder


class AStarForPedestrians(PathFinder):
    def __init__(self):
        self.__road_graph = None

    def find_path(self, start_longitude: float, start_latitude: float,
                  destination_longitude: float, destination_latitude: float):
        pass
