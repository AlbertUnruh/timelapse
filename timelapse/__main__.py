# standard library
from threading import Thread
from time import sleep

# local
from .camera import capture
from .environment import env
from .utils import capture_and_save, generate_new_session, generate_video_and_save


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
threads: list[Thread] = []

for _ in range(total_frames):
    sleep(seconds_per_frame)
    threads.append(Thread(target=capture_and_save, name=f"capture and save #{_}", args=(current_session,)))
    threads[-1].start()

for thread in threads:  # wait for all threads to finish
    thread.join()

print("last frame has been captured and saved")

video_path = generate_video_and_save(current_session)
print(f"copy of video saved at {video_path}")
