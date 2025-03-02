import cv2
import numpy as np


def get_perspective(img, masked_num, location, width, height, inv=False):
    pts1 = np.float32(location)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    if inv:
        pts1, pts2 = pts2, pts1
        width, height = img.shape[1], img.shape[0]

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(masked_num, matrix, (width, height))
    return result


def split_boxes(img):
    rows = np.vsplit(img, 9)
    boxes = []
    for row in rows:
        cols = np.hsplit(row, 9)
        for box in cols:
            boxes.append(box)
    return boxes
