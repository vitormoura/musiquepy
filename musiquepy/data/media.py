import os


def get_profile_pictures_dir() -> str:
    root_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(root_path, 'media', 'profile_pictures')
