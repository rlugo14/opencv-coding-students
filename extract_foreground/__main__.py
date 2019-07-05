import os
import argparse
import extract_foreground.foreground as foreground

if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'exampleVideo.mp4')
    output_filename = os.path.join(dirname, 'output_images/image-without-foreground.jpeg')

    print(dirname)
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source_file", type=str, default=filename,
                        help='name of the video to extract foreground from')
    parser.add_argument("-v", "--show_process", type=bool, default=False,
                        help='shows the transformation of the image in run time')
    parser.add_argument("-o", "--output_filename", type=str, default=output_filename,
                        help='path of the output image')

    args = vars(parser.parse_args())

    foreground.extract(args.get("source_file"), args.get("output_filename"), args.get("show_process"))
