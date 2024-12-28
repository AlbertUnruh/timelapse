# timelapse
quick and dirty project to generate a timelapse


### Setup
Install the requirements with poetry.
Just run ``poetry install`` :)

### How to run
There are many ways to run the project, but I recommend following steps:
1. set your cwd to the directory of this file (project root)
2. open a shell with ``poetry shell``
3. type ``python -m timelapse`` to run the project

#### Troubleshooting
Please refer to [TROUBLESHOOTING.md](./TROUBLESHOOTING.md).


---

> [!NOTE]  
> To change settings copy ``.env`` as ``.env.prod``. Values set there will override the default ones and won't be versioned.

> [!NOTE]
> This program is intended to run with a Nextcloud server. It will create a folder called ``sessions`` for frames and ``saves`` for video output. You don't have to create them yourself, the program is intelligent enough to handle missing folders ;)

> [!TIP]
> Run ``debug_camera.py`` to check whether you have the right camera selected and if the field of view is as expected.

> [!TIP]
> If you already have frames but no video (due to crash or termination) you can generate the video with following command(s):
> ```python
> from timelapse.utils import generate_video_and_save
> generate_video_and_save("YOUR SESSION")  # returns the path to the local copy
> ```
> Alternatively you can run ``python generate_and_save_video.py YOUR-SESSION``

> That's some sh*tty code. But it works \o/
> <br>~me
