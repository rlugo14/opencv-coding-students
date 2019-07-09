import cv2
import numpy as np


class FourPointsExtractor:
    def __init__(self, image_path, print_points):
        image = cv2.imread(image_path)
        self.print_extracted_points_flag = print_points
        self.data_object = {
            'corners_positions': dict(),
            'image_with_points': image.copy(),
            'image_to_show': image.copy(),
        }

    def extract_four_points_from_image(self):
        cv2.putText(
            self.data_object['image_to_show'],
            "Select TOP LEFT Corner",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2
        )
        cv2.imshow("Points Selection", self.data_object['image_to_show'])
        cv2.setMouseCallback("Points Selection", self.mouse_handler, self.data_object)
        key = cv2.waitKey(0)

        corners_positions_array = np.array(list(self.data_object['corners_positions'].values()))

        if self.print_extracted_points_flag:
            print(self.data_object['corners_positions'])

        if key:
            cv2.destroyWindow("Points Selection")

        return corners_positions_array

    @staticmethod
    def mouse_handler(event, x, y, flags, data_object):
        dict_length = len(data_object['corners_positions'])
        if event == cv2.EVENT_LBUTTONDOWN:
            if dict_length == 0:
                data_object['corners_positions']["top left"] = (x, y)
                cv2.circle(data_object['image_with_points'], (x, y), 2, (0, 255, 255), 5, 16)
                data_object['image_to_show'] = data_object['image_with_points'].copy()
                cv2.putText(
                    data_object['image_to_show'],
                    "Select TOP RIGHT Corner",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 255),
                    2
                )
                cv2.imshow("Points Selection", data_object['image_to_show'])

            elif dict_length == 1:
                data_object['corners_positions']["top right"] = (x, y)
                cv2.circle(data_object['image_with_points'], (x, y), 2, (0, 255, 255), 5, 16)
                data_object['image_to_show'] = data_object['image_with_points'].copy()
                cv2.putText(
                    data_object['image_to_show'],
                    "Select BOTTOM RIGHT Corner",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 255),
                    2
                )
                cv2.imshow("Points Selection", data_object['image_to_show'])

            elif dict_length == 2:
                data_object['corners_positions']["bottom right"] = (x, y)
                cv2.circle(data_object['image_with_points'], (x, y), 2, (0, 255, 255), 5, 16)
                data_object['image_to_show'] = data_object['image_with_points'].copy()
                cv2.putText(
                    data_object['image_to_show'],
                    "Select BOTTOM LEFT Corner",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 255),
                    2
                )
                cv2.imshow("Points Selection", data_object['image_to_show'])

            elif dict_length == 3:
                data_object['corners_positions']["bottom left"] = (x, y)
                cv2.circle(data_object['image_with_points'], (x, y), 2, (0, 255, 255), 5, 16)
                data_object['image_to_show'] = data_object['image_with_points'].copy()
                cv2.putText(
                    data_object['image_to_show'],
                    "Press any key to finish",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 255),
                    2
                )
                cv2.imshow("Points Selection", data_object['image_to_show'])
