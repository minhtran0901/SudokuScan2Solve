# SudokuScan2Solve
SudokuScan2Solve is an Sudoku solver that scans puzzles from images or live camera feeds, recognizes digits using ResNet-18, and solves them instantly. Built with OpenCV, PyTorch, and Tkinter for an interactive user experience.

## Features
- **Image Input**: Upload an image or scan using a webcam.
- **Processing**: Detects the largest quadrilateral contour in the image and applies a linear mapping to correct the perspective, extracting the Sudoku grid.-
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
- Click **"Open Image"** to upload a Sudoku puzzle image.
- Click **"Open Camera"** to turn on webcam. Press key 'c' to capture an image from the webcam.
- Click **"Exit"** to exit the program.

### Edit & Solve
- The program detects and predicts the Sudoku grid.
- You can manually edit incorrect predictions.
- Click **"Confirm"** to solve.
- If unsolvable, a message will be displayed.

## Model Weights
The pre-trained ResNet-18 model for digit recognition is too large for GitHub. Download it from Google Drive:

[resnte18_trained_parameters.pth](https://drive.google.com/file/d/1j4m1gAvC4tERiuZ_5yCDj-2yTddPiEp-/view?usp=sharing)

Place the file in the project directory before running the program.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
If you want to dive deeper into the details or the math you can read my project report (althought it was writen in Vietnames) 
If you have any questions or suggestions regarding this application, please feel free to contact me at [anhminhtran.09.01.2003@gmail.com]
---
