# Raspberry Pi Facial Recognition

A small Python computer-vision project developed for a Raspberry Pi. The program reads frames from a Raspberry Pi camera, detects faces, compares facial encodings against a previously prepared dataset, and displays the matched name.

## Technologies

- Raspberry Pi
- Raspberry Pi camera (the code uses `imutils.video.VideoStream` with `usePiCamera=True`)
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

The camera initialization in this code uses the `PiCamera` interface through `imutils` (`usePiCamera=True`). This is associated with the legacy Raspberry Pi camera stack. It may not work unchanged with newer Raspberry Pi OS camera configurations. Confirm that your OS, camera stack, and installed libraries support this interface before running the program.

Install the Python packages in an environment compatible with your Raspberry Pi:

```bash
python -m pip install imutils opencv-python face_recognition
```

You may need additional system packages or a compatible installation method for `dlib` / `face_recognition` on your Raspberry Pi. The command above is not a guarantee that every dependency will install successfully on every Pi OS version.

Place a valid `encodings.pickle` file beside `facial_recognition.py`, then run:

```bash
python facial_recognition.py
```

## Important notes

- This repository does not include the trained face dataset or `encodings.pickle`.
- The code has been formatted and lightly cleaned up, but it has **not been verified on the author's current camera setup**.
- Only use face images with the subjects' informed permission. Do not publish face images, face encodings, or other identifying biometric data in this repository.
- Facial recognition can make mistakes. Do not use this demo to make consequential decisions about people.

## Project status

Personal learning project / prototype. Camera compatibility and runtime behavior depend on the Raspberry Pi hardware, operating system, camera stack, and Python dependencies.
