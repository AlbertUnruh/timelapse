# standard library
import sys

# first party
from timelapse.utils import generate_video_and_save


if len(sys.argv) == 1:
    print("Session required!", file=sys.stderr)
    print(f"Run something like ``python {sys.argv[0]} YOUR-SESSION``", file=sys.stderr)
    sys.exit(1)

video_path = generate_video_and_save(" ".join(sys.argv[1:]))
print(f"copy of video saved at {video_path}")
