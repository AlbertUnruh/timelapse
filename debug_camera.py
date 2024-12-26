# third party
import cv2

# first party
from timelapse.camera import camera


if __name__ == "__main__":
    while True:
        ret, frame = camera.read()
        if not ret:
            break

        cv2.imshow("camera", frame)

        if cv2.waitKey(1) == ord("q"):
            break
