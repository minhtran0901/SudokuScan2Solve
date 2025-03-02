import cv2
import numpy as np


def get_biggest_contour(contours, image):
    biggest = np.array([[]])
    max_area = 0

    for i in contours:
        area = cv2.contourArea(i)
        if area > 100:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)

            if len(approx) == 4:
                if area > max_area:
                    max_area = area
                    biggest = approx

    return biggest, max_area


def reorder(my_points):
    my_points = my_points.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), dtype=np.int32)
    add = my_points.sum(1)
    myPointsNew[0] = my_points[np.argmin(add)]
    myPointsNew[3] = my_points[np.argmax(add)]
    diff = np.diff(my_points, axis=1)
    myPointsNew[1] = my_points[np.argmin(diff)]
    myPointsNew[2] = my_points[np.argmax(diff)]
    return myPointsNew
