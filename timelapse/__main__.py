# standard library
from threading import Thread
from time import sleep

# local
from .camera import capture
from .environment import env
from .utils import capture_and_save, generate_new_session
from .video import convert_to_mp4
from .webdav import download_session, save_video


# take initial capture(s)
print(f"taking {env.PRE_CAPTURES} pre-captures...")
for _ in range(env.PRE_CAPTURES):
    capture()


current_session = generate_new_session()
total_frames: int = env.FPS * env.DURATION
seconds_per_frame = 60 * 60 * 24 * env.SPAN / total_frames

print(f"span to cover:         {env.SPAN} days")
print(f"frames per second:     {env.FPS}")
print(f"duration of timelapse: {env.DURATION} seconds")
print(f"total frames:          {total_frames + 1}")
print(f"seconds per frame:     {seconds_per_frame}")


capture_and_save(current_session)  # one initial frame
latest_thread = None

for _ in range(total_frames):
    sleep(seconds_per_frame)
    latest_thread = Thread(target=capture_and_save, name=f"capture and save #{_}", args=(current_session,))
    latest_thread.start()

if latest_thread is not None:
    latest_thread.join()  # wait for latest thread to finish

print("last frame has been captured and saved")

video_path = convert_to_mp4(download_session(current_session))
print(f"copy of video saved at {video_path}")

save_video(current_session, video_path.read_bytes())
