# standard library
from io import BytesIO

# third party
import cv2
from PIL import Image

# local
from .environment import env


__all__ = ("capture",)


camera: cv2.VideoCapture = cv2.VideoCapture(env.CAMERA)
if not camera.isOpened():
    raise RuntimeError(f"Unable to capture from camera #{env.CAMERA}")  # noqa: TRY003, EM102


def capture() -> bytes:
    ret, frame = camera.read()
    if ret is False:
        return b""

    png_file = BytesIO()

    Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).save(png_file, format="png")

    return png_file.getvalue()
