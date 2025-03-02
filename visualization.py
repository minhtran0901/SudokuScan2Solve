import cv2
import numpy as np
from perspective import get_perspective


def display_predict_number(img, img_, num_pred, biggest, width, height):
    img_empty = np.zeros_like(img_)
    for i in range(9):
        for j in range(9):
            if num_pred[i, j] != 0:
                cv2.putText(img_empty, str(num_pred[i, j]), (j * 50 + 10, i * 50 + 35),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    inv = get_perspective(img, img_empty, biggest, width, height, inv=True)
    combined = cv2.addWeighted(inv, 1, img, 0.5, 1)
    return np.clip(combined, 0, 255)


def draw_grid(image, grid_size=9, color=(255, 255, 255), thickness=3):
    height, width, _ = image.shape

    cell_width = width // grid_size
    cell_height = height // grid_size

    for i in range(1, grid_size):
        x = i * cell_width
        cv2.line(image, (x, 0), (x, height), color, thickness)

    for i in range(1, grid_size):
        y = i * cell_height
        cv2.line(image, (0, y), (width, y), color, thickness)

    return image
