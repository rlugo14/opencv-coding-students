import numpy as np
import cv2


class BackgroundExtractor:
    # When constructing background subtractor, we
    # take in two arguments:
    # 1) alpha: The background learning factor, its value should
    # be between 0 and 1. The higher the value, the more quickly
    # your program learns the changes in the background. Therefore,
    # for a static background use a lower value, like 0.001. But if
    # your background has moving trees and stuff, use a higher value,
    # maybe start with 0.01.
    # 2) firstFrame: This is the first frame from the video/webcam.
    def __init__(self, alpha, first_frame):
        self.alpha = alpha
        self.backGroundModel = first_frame

    def get_foreground(self, current_frame):
        # apply the background averaging formula:
        # NEW_BACKGROUND = CURRENT_FRAME * ALPHA + OLD_BACKGROUND * (1 - APLHA)

        self.backGroundModel = current_frame * self.alpha + self.backGroundModel * (1 - self.alpha)

        # after the previous operation, the dtype of
        # self.backGroundModel will be changed to a float type
        # therefore we do not pass it to cv2.absdiff directly,
        # instead we acquire a copy of it in the uint8 dtype
        # and pass that to absdiff.

        return cv2.absdiff(self.backGroundModel.astype(np.uint8), current_frame)


source = cv2.VideoCapture(0)
has_new_frame, new_frame = source.read()

while has_new_frame:
    background_extractor = BackgroundExtractor(0.01, new_frame)
    ORIGINAL_FRAME = "Original Frame Window"
    MODIFIED_FRAME = "Modified Frame Window"
    cv2.imshow(ORIGINAL_FRAME, new_frame)
    key = cv2.waitKey(10) & 0xFF

    if key == 27:
        break

source.release()
cv2.destroyAllWindows()
# def denoise(self, current_frame):
#     current_frame = cv2.medianBlur(current_frame, 5)
#     # current_frame = cv2.GaussianBlur(current_frame, (5, 5), 0)
#
#     return current_frame
