# timelapse
quick and dirty project to generate a timelapse


### Setup
Install the requirements with poetry.
Just run ``poetry install`` :)

### How to run
There are many ways to run the project, but I recommend following steps:
1. set your cwd to the directory of this file (project root)
2. type ``python3.12 -m timelapse``



> [!NOTE]  
> To change settings copy ``.env`` as ``.env.prod``. Values set there will override the default ones and won't be versioned.

> [!NOTE]
> This program is intended to run with a Nextcloud server. It will create a folder called ``sessions`` for frames and ``saves`` for video output. You don't have to create them yourself, the program is intelligent enough to handle missing folders ;)

> [!TIP]
> Run ``debug_camera.py`` to check whether you have the right camera selected and if the field of view is as expected.

> That's some sh*tty code. But it works \o/
> <br>~me
