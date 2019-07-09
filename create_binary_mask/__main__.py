import os
import argparse
import create_binary_mask.mask_creator as mask_creator

if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'image-without-foreground.jpeg')

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image_file", type=str, default=filename,
                        help='name of the image to extract four points from')
    parser.add_argument("-p", "--print_points", type=bool, default=True,
                        help='prints the four extracted points')

    args = vars(parser.parse_args())
    mask_creator.create_mask(args.get('image_file'), args.get('print_points'))
