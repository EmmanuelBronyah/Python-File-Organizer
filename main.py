import os
import shutil


def main():
    """
    Executes the entire program.

    """
    not_exit = True
    while not_exit:
        path = get_path()
        if path is not None and path != -1:
            extensions = get_extensions(path)
            create_directories(path, extensions)
            organize_files(path)
        else:
            if path == -1:
                not_exit = False
                print('Program ended.')


def get_path():
    """
    Takes as input the path to the folder to be organized.

    If no path is provided, -1 is returned and the program ends.
    Returns None if an error occurs and prints to the screen the error message.
    """
    path = input(r'Enter the path to the folder you want to organize: ') or 'exit'
    if path == 'exit':
        return -1
    try:
        if os.path.isfile(path):
            raise NotADirectoryError(f'The path "{path}" points to a file, not a folder.')
        elif os.path.isdir(path):
            return path
        else:
            print(f'The path {path} is invalid. Enter a valid path.')
            return None
    except NotADirectoryError as inst:
        print(inst)
        return None


def get_extensions(path):
    """
    Generates the extension of files in the current path.

    :param path: This is a string representing the current file path.
    :return: Returns a list of unique extensions from which folders will be created.
    """
    extensions = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            extension = os.path.splitext(file)[1]
            if extension not in extensions:
                extensions.append(extension)
    return extensions


def create_directories(path, extensions):
    """
    Creates folders of the list of extensions.

    :param path: This is a string representing the current file path.
    :param extensions: This is a list of unique extensions from which folders will be created.
    :return: Returns None.
    """
    os.chdir(path)
    for ext in extensions:
        os.makedirs(ext, exist_ok=True)


def organize_files(path):
    """
    Moves files into folders where the file extension is the same as the folder name.

    :param path: This is a string representing the current file path.
    :return: Returns None.
    """
    for item in os.listdir(path):  # item could be a file or folder.
        if os.path.isdir(item):
            for obj in os.listdir(path):  # obj could be a file or folder.
                if os.path.isfile(obj):
                    file_extension = os.path.splitext(obj)[1]
                    if file_extension == item:
                        old_path = os.path.join(path, obj)
                        new_path = os.path.join(os.path.join(path, item), obj)
                        shutil.move(old_path, new_path)
    print('Files organized.')


if __name__ == '__main__':
    main()
