import pathlib
from stat import S_IXUSR

def find_the_first_file_owner_admin_executable_lower_than_14_MB(user_path):
    """
    The function will find the first file matching these requirements:
       * size < 14MB
       * owner can execute it
       * owner name is "admin"
    :param user_path:path of the directory to scan
    :return: absolute path string of the file or error message string
    """
    path = pathlib.Path(user_path)
    max_size = 14*2**20 #14MB

    if path.exists() == False:
        return "Path not valid"
    for file in path.iterdir():
        # Don't check for directory
        if file.is_dir():
            continue
        # S_IXUSR is a the mask to apply of mode result to know if Owner has execute permission.
        if file.owner() == "admin" and file.stat().st_size <= max_size and file.stat().st_mode & S_IXUSR != 0:
                return file.name
    return "No file matching found"
