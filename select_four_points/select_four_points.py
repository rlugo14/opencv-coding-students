

class FourPointsExtractor:

    def __init__(self):
        corners_position = {
            "top left": (0, 0),
            "top right": (0, 0),
            "bottom right": (0, 0),
            "bottom left": (0, 0)
        }

    def mouse_handler(self, event, x, y, corners_positions):

