import cv2
import numpy as np
import extract_four_points.four_points_extractor as four_points_extractor


def create_mask(image_path, print_points):
    extractor = four_points_extractor.FourPointsExtractor(image_path, print_points)
    extracted_points = extractor.extract_four_points_from_image()

    image = cv2.imread(image_path)

    football_field_dimensions = np.array([261, 436, 3], dtype=int)
    football_field_corner_points = np.array([
        [0, 0],
        [435, 0],
        [435, 260],
        [0, 260]
    ], dtype=int
    )
    ones_image = np.ones(football_field_dimensions)
    image_size = (image.shape[1], image.shape[0])

    h, _ = cv2.findHomography(football_field_corner_points, extracted_points)

    transformed_image = cv2.warpPerspective(ones_image, h, image_size)
    cv2.imshow('Transformed Image', transformed_image)
    key = cv2.waitKey(0)

    if key:
        cv2.destroyWindow('Transformed Image')

    return transformed_image
