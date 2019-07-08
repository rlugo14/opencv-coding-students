import cv2


class FourPointsExtractor:
    def __init__(self, print_extracted_points_flag, image_path):
        self.print_extracted_points_flag = print_extracted_points_flag
        self.data_object = {
            'corners_positions': dict(),
            'image_with_points': cv2.imread(image_path)
        }

    def extract_four_points_from_image(self):
        cv2.imshow("Points Selection", self.data_object['image_with_points'])
        cv2.setMouseCallback("Points Selection", self.mouse_handler, self.data_object)
        key = cv2.waitKey(0) & 0xFF

        if key == ord('q') | len(self.data_object['corners_positions']) == 3:
            cv2.destroyAllWindows()

        if self.print_extracted_points_flag:
            print(self.data_object['corners_positions'])

        return self.data_object['corners_positions']

    @staticmethod
    def mouse_handler(event, x, y, flags, data_object):
        dict_length = len(data_object['corners_positions'])
        if event == cv2.EVENT_LBUTTONDOWN:
            if dict_length == 0:
                data_object['corners_positions']["top left"] = (x, y)
                cv2.circle(data_object['image_with_points'], (x, y), 2, (0, 0, 255), 5, 16)
                cv2.imshow("Points Selection", data_object['image_with_points'])

            elif dict_length == 1:
                data_object['corners_positions']["top right"] = (x, y)
                cv2.circle(data_object['image_with_points'], (x, y), 2, (0, 0, 255), 5, 16)
                cv2.imshow("Points Selection", data_object['image_with_points'])

            elif dict_length == 2:
                data_object['corners_positions']["bottom right"] = (x, y)
                cv2.circle(data_object['image_with_points'], (x, y), 2, (0, 0, 255), 5, 16)
                cv2.imshow("Points Selection", data_object['image_with_points'])

            elif dict_length == 3:
                data_object['corners_positions']["bottom left"] = (x, y)
                cv2.circle(data_object['image_with_points'], (x, y), 2, (0, 0, 255), 5, 16)
                cv2.imshow("Points Selection", data_object['image_with_points'])
                return
        return
