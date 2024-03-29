import numpy as np
import cv2
from os import path
from os import remove


def extract(video_file, output_file_path, show_process, alpha=0.0009):
    src = cv2.VideoCapture(video_file)
    has_new_frame, source_frame = src.read()

    avg_values = np.float32(source_frame)
    output_frame = source_frame

    if path.exists(output_file_path):
        remove(output_file_path)

    while has_new_frame:
        try:
            cv2.accumulateWeighted(source_frame, avg_values, alpha)
            output_frame = cv2.convertScaleAbs(avg_values)
        except cv2.error:
            print(cv2.error.msg)
            cv2.imwrite(output_file_path, output_frame)
            break

        if show_process:
            cv2.imshow('Source Frame', source_frame)
            cv2.imshow('Output Frame', output_frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                cv2.destroyAllWindows()
                break

        has_new_frame, source_frame = src.read()

    cv2.imwrite(output_file_path, output_frame)
    cv2.destroyAllWindows()
    src.release()
