# standard library
import sys

# first party
from timelapse.environment import env
from timelapse.utils import generate_video_and_save
from timelapse.webdav import find_sessions


if len(sys.argv) == 1:
    print("Session required!", file=sys.stderr)
    print(f"Run something like ``python {sys.argv[0]} YOUR-SESSION``", file=sys.stderr)
    sys.exit(1)


session = " ".join(sys.argv[1:])
if session not in find_sessions():
    url = f"{env.URL.scheme}://{env.URL.host}:{env.URL.port}{env.URL.path}"
    redaction_notice = " (username and password redacted)" if env.URL.username or env.URL.password else ""
    print(f"Unable to find session {session!r} over at {url}{redaction_notice}", file=sys.stderr)
    sys.exit(1)

video_path = generate_video_and_save(" ".join(sys.argv[1:]))
print(f"copy of video saved at {video_path}")
