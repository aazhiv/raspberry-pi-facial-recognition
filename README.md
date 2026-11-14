# Raspberry Pi Facial Recognition

A small Python project run on a Raspberry Pi. The program reads frames from a Raspberry Pi camera, detects faces, compares facial encodings against a previously prepared dataset, and displays the matched name.

## Technologies

- Raspberry Pi
- Raspberry Pi camera
- Python
- OpenCV (`cv2`)
- `face_recognition`
- `imutils`
- Pickle

## Project files

- `facial_recognition.py` — main camera and face-recognition program.
- `encodings.pickle` — **not included**. The program expects this file in the same directory. It must be generated separately from images you have permission to use.

## How it works

1. Loads face encodings and corresponding names from `encodings.pickle`.
2. Starts the Raspberry Pi camera video stream.
3. Reads and resizes each frame.
4. Detects face locations and computes face encodings.
5. Compares each encoding with the stored encodings.
6. Displays the recognized name (or `Unknown`) over the face.
7. Press `q` to exit.

## Requirements and setup

This project depends on compatible versions of Python, OpenCV, `face_recognition`, `imutils`, and the Raspberry Pi camera software.

The camera initialization in this code uses the `PiCamera` interface through `imutils` (`usePiCamera=True`). It may not work unchanged with newer Raspberry Pi OS camera configurations.

Install the Python packages in an environment compatible with your Raspberry Pi:
Place a valid `encodings.pickle` file beside `facial_recognition.py`, then run:

```bash
python facial_recognition.py
```


