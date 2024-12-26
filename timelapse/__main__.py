# local
from .camera import capture
from .utils import generate_new_session
from .webdav import find_sessions, save_image


# take one initial capture
capture()


current_session = generate_new_session()

save_image(current_session, capture())
print(find_sessions())  # noqa: T201
