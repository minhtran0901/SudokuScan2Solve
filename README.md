# Sudoku Solver

A Python-based Sudoku solver that processes images of Sudoku grids, predicts numbers using a ResNet-18 model, and provides a solution. Users can upload an image or use a webcam to scan a Sudoku puzzle.

## Features

- **Image Input**: Upload an image or scan using a webcam.
- **Preprocessing**: Detects the largest quadrilateral contour in the image and applies a linear mapping to correct the perspective, extracting the Sudoku grid.
- **Digit Recognition**: Uses ResNet-18 for digit classification.
- **Manual Editing**: Allows users to correct predictions before solving.
- **Puzzle Solving**: Implements a backtracking algorithm to solve Sudoku.
- **Graphical Interface**: Built with Tkinter for easy interaction.

## Installation

Ensure you have Python 3.7+ installed. Then, install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage

### Run the application

```sh
python gui.py
```

### Upload an image or scan using the camera

- Click **"Exit"** to exit the program.


![Interface](https://github.com/minhtran0901/SudokuScan2Solve/blob/main/Interface.png)


- Click **"Open Image"** to upload a Sudoku puzzle image.


![Open Image](https://github.com/minhtran0901/SudokuScan2Solve/blob/main/Selecting%20image.png)


- Click **"Open Camera"** to open your laptop webcam. Press **"c"** to capture an image from the webcam.


![Scanning](https://github.com/minhtran0901/SudokuScan2Solve/blob/main/Scanning.png)

### Edit & Solve

- The program detects and predicts the Sudoku grid.
- You can manually edit incorrect predictions.


![Editing](https://github.com/minhtran0901/SudokuScan2Solve/blob/main/Verify%20Prediction.png)


- Click **"Confirm"** to solve.


![Final result](https://github.com/minhtran0901/SudokuScan2Solve/blob/main/Solved%20puzzle.png)

## Model Weights

The pre-trained ResNet-18 model for digit recognition is too large for GitHub. Download it from Google Drive:

[resnet18_trained_parameters.pth](https://drive.google.com/file/d/1j4m1gAvC4tERiuZ_5yCDj-2yTddPiEp-/view?usp=sharing)

Place the file in the project directory before running the program.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Note

If you want to dive deep into the math you can read my project report (in Vietnamese).

---
