import os
import argparse
import extract_four_points.four_points_extractor as four_points_extractor

if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'image-without-foreground.jpeg')

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image_file", type=str, default=filename,
                        help='name of the image to extract four points from')
    parser.add_argument("-v", "--print_points", type=bool, default=False,
                        help='prints the four extracted points')

    args = vars(parser.parse_args())
    extractor = four_points_extractor.FourPointsExtractor(args.get("print_points"), args.get("image_file"))
    extractor.extract_four_points_from_image()
