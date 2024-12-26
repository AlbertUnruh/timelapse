# standard library
from collections.abc import Iterable
from io import BytesIO
from pathlib import Path

# third party
import cv2
import numpy as np
from PIL import Image

# local
from .environment import env


__all__ = ("convert_to_mp4",)


def convert_to_mp4(bytes_files: Iterable[bytes]) -> Path:
    gen = iter(bytes_files)
    path = Path.cwd() / "latest_timelapse.mp4"

    first_frame = Image.open(BytesIO(next(gen)))

    fourcc = cv2.VideoWriter_fourcc(*"avc1")
    video = cv2.VideoWriter(str(path), fourcc, env.FPS, first_frame.size)
    video.write(cv2.cvtColor(np.array(first_frame), cv2.COLOR_BGR2RGB))

    for file in gen:
        frame = Image.open(BytesIO(file))
        video.write(cv2.cvtColor(np.array(frame), cv2.COLOR_BGR2RGB))

    video.release()

    return path
