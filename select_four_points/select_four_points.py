import cv2

class FourPointsExtractor:

    def __init__(self):
        corners_position = dict()

    def mouse_handler(self, event, x, y, corners_positions):
        dict_length = len(corners_positions)
        if event == cv2.EVENT_LBUTTONDOWN:
            if dict_length == 0:
                corners_positions["top left"] = (x, y)
            elif dict_length == 1:
                corners_positions["top right"] = (x, y)
            elif dict_length == 2:
                corners_positions["bottom right"] = (x, y)
            elif dict_length == 3:
                corners_positions["bottom left"] = (x, y)
            else:
                raise Exception('Dictionary exceeds length limit')

    def extract_four_points_in_image(self, image):
        image_copy = image
