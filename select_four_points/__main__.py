import os
import argparse

if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'image-without-foreground.jpeg')

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image_file", type=str, default=filename,
                        help='name of the image to extract four points from')
    parser.add_argument("-v", "--print_points", type=bool, default=False,
                        help='prints the four extracted points')

    args = vars(parser.parse_args())

