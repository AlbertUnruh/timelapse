# Troubleshooting
This file contains some exceptions/error you may encounter.

---

## ModuleNotFoundError: No module named 'cv2'
Did you run ``poetry install`` and ``poetry shell`` beforehand?


## ImportError: libGL.so.1: cannot open shared object file: No such file or directory
Try running ``apt-get update && apt-get install libgl1``.
