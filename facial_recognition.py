from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2

currentname = "unknown"
encodingsP = "encodings.pickle"

print("[INFO] loading encodings + face detector...")
with open(encodingsP, "rb") as file:
    data = pickle.load(file)

vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

fps = FPS().start()

try:
    while True:
        frame = vs.read()
        if frame is None:
            print("[ERROR] No frame received from the camera.")
            break

        frame = imutils.resize(frame, width=500)

        boxes = face_recognition.face_locations(frame)
        encodings = face_recognition.face_encodings(frame, boxes)
        names = []

        for encoding in encodings:
            matches = face_recognition.compare_faces(
                data["encodings"], encoding
            )
            name = "Unknown"

            if True in matches:
                matched_idxs = [
                    i for i, matched in enumerate(matches) if matched
                ]
                counts = {}

                for i in matched_idxs:
                    matched_name = data["names"][i]
                    counts[matched_name] = counts.get(matched_name, 0) + 1

                name = max(counts, key=counts.get)

            if currentname != name:
                currentname = name
                print(currentname)

            names.append(name)

        for ((top, right, bottom, left), name) in zip(boxes, names):
            cv2.rectangle(
                frame, (left, top), (right, bottom), (0, 255, 225), 2
            )
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(
                frame,
                name,
                (left, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2,
            )

        cv2.imshow("Facial Recognition is Running", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

        fps.update()

finally:
    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    cv2.destroyAllWindows()
    vs.stop()
