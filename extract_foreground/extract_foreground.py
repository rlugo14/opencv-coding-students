import numpy as np
import cv2
import re
from os import path


def extract_foreground(video_file, file_path, alpha=0.0009):
	regex_string = '[^.]+'
	file_name, file_extension = re.findall(regex_string, file_path)

	src = cv2.VideoCapture(video_file)
	has_new_frame, source_frame = src.read()

	avg_values = np.float32(source_frame)
	output_frame = source_frame

	while has_new_frame:
		has_new_frame, source_frame = src.read()
		try:
			cv2.accumulateWeighted(source_frame, avg_values, alpha)
			output_frame = cv2.convertScaleAbs(avg_values)
		except cv2.error:
			print(cv2.error.msg)

			if path.exists(file_path):
				cv2.imwrite(file_name+'%d', output_frame)
			break
	cv2.imwrite(file_path, output_frame)
	src.release()


if __name__ == '__main__':
	extract_foreground('exampleVideo.mp4', './output_images/image-without-foreground.jpeg')
