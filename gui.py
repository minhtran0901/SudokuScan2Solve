import cv2
import numpy as np
import torch
from tkinter import Tk, Label, Button, filedialog, Entry, Frame, Toplevel
from PIL import Image, ImageTk
from preprocessing import pre_processing
from contours import get_biggest_contour, reorder
from perspective import get_perspective, split_boxes
from solver import solve
from visualization import display_predict_number
from resnet18 import Resnet18
from model import get_predict

WIDTH, HEIGHT = 450, 450

model = Resnet18(3, 10)
model.load_state_dict(torch.load("resnet18_trained_parameters.pth", map_location=torch.device("cpu")))
model.eval()


def process_image(image):
    img_resized = cv2.resize(image, (WIDTH, HEIGHT))
    thresh = pre_processing(img_resized)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    biggest, _ = get_biggest_contour(contours, img_resized)

    if biggest.size != 0:
        img_warp_colored = cv2.cvtColor(get_perspective(img_resized, img_resized, reorder(biggest), WIDTH, HEIGHT),
                                        cv2.COLOR_BGR2RGB)
        boxes = np.array(split_boxes(img_warp_colored))
        pred = get_predict(boxes, model)
        return pred.tolist(), biggest, img_resized, img_warp_colored

    return None, None, img_resized, None


def edit_predictions(grid, biggest, img_resized, img_warp_colored):
    global img_label

    def confirm_edits():
        for i in range(9):
            for j in range(9):
                try:
                    new_value = int(entries[i][j].get())
                    grid[i][j] = new_value if 0 <= new_value <= 9 else 0
                except ValueError:
                    grid[i][j] = 0
        solve_and_display(grid, reorder(biggest), img_resized, img_warp_colored)

    for widget in frame.winfo_children():
        widget.destroy()

    cv2.drawContours(img_resized, [biggest], -1, (0, 255, 0), 3)
    img_display = cv2.cvtColor(cv2.resize(img_resized, (300, 300)), cv2.COLOR_BGR2RGB)
    img_display = ImageTk.PhotoImage(Image.fromarray(img_display))
    img_label = Label(frame, image=img_display)
    img_label.image = img_display
    img_label.grid(row=0, column=0, rowspan=9, padx=10)

    entries = []
    for i in range(9):
        row_entries = []
        for j in range(9):
            entry = Entry(frame, width=2, font=("Arial", 16), justify="center")
            entry.insert(0, str(grid[i][j]) if grid[i][j] != 0 else "")
            entry.grid(row=i, column=j + 1, padx=2, pady=2)
            row_entries.append(entry)
        entries.append(row_entries)

    Button(frame, text="Confirm", command=confirm_edits).grid(row=10, column=1, columnspan=9, pady=5)


def show_popup(message):
    popup = Toplevel(root)
    popup.title("Notification")
    popup.geometry("300x150")

    Label(popup, text=message, font=("Arial", 14), fg="red").pack(pady=20)
    Button(popup, text="OK", command=popup.destroy, font=("Arial", 12)).pack(pady=10)


def solve_and_display(grid, biggest, img_resized, img_warp_colored):
    original_grid = np.array(grid)

    if solve(grid):
        grid_show = np.where(grid == original_grid, 0, grid)
        solved_image = display_predict_number(img_resized, img_warp_colored, grid_show, biggest, WIDTH, HEIGHT)

        solved_image = cv2.cvtColor(cv2.resize(solved_image, (300, 300)), cv2.COLOR_BGR2RGB)
        solved_image = ImageTk.PhotoImage(Image.fromarray(solved_image))
        img_label.config(image=solved_image)
        img_label.image = solved_image
    else:
        show_popup("No Solution \n Please check for mistakes")


def show_image(image):
    image = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(cv2.resize(image, (WIDTH, HEIGHT)), cv2.COLOR_BGR2RGB)))
    image_label.config(image=image)
    image_label.image = image


def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        image = cv2.imread(file_path)
        grid, biggest, img_contours, img_warp_colored = process_image(image)
        if grid:
            edit_predictions(grid, biggest, img_contours, img_warp_colored)


def open_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        original_frame = frame.copy()
        thresh = pre_processing(frame)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        biggest, _ = get_biggest_contour(contours, frame)

        if biggest.size != 0:
            cv2.drawContours(frame, [biggest], -1, (0, 255, 0), 3)

        cv2.imshow("Scanning... Press 'c' to capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break

    cap.release()
    cv2.destroyAllWindows()

    grid, biggest, img_contours, img_warp_colored = process_image(original_frame)
    if grid:
        edit_predictions(grid, biggest, img_contours, img_warp_colored)


if __name__ == '__main__':
    root = Tk()
    root.title("Sudoku Solver")
    Label(root, text="Sudoku Solver", font=("Arial", 20)).pack(pady=10)

    frame = Frame(root)
    frame.pack()

    image_label = Label(root)
    image_label.pack(pady=10)
    Button(root, text="Open Image", command=open_image, width=20).pack(pady=5)
    Button(root, text="Open Camera", command=open_camera, width=20).pack(pady=5)
    Button(root, text="Exit", command=root.quit, width=20).pack(pady=5)

    root.mainloop()