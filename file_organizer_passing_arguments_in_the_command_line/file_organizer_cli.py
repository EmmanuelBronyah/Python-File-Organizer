import os
import shutil
import argparse
import mimetypes


def main():
    args = arg_parser()
    path = path_validation(args)
    if path is not None and path != -1:
        error = False
        try:
            file_formats = get_file_formats(args)
            create_directories(args, file_formats)
        except (AttributeError, UnboundLocalError):
            print(
                "Could not parse file. A file in the folder may be an executable or may have an unsupported type."
            )
            error = True
        error = organize_files(path, error)
        if error:
            return
        print('Files organized.')
    else:
        if path == -1:
            print("Program ended.")


def arg_parser():
    parser = argparse.ArgumentParser(
        prog="File organizer",
        description="Takes a valid path and groups files based on their file format.",
        epilog="The program scans a directory for files and creates folders for all \
                the file formats where each folder bares the name \
                of a format and files in the directory are moved into \
                these folders according to their file format.",
    )
    parser.add_argument(
        "path", metavar="P", type=str, nargs="?", help="Path to the folder."
    )
    args = parser.parse_args()
    args = args.path
    return args


def path_validation(path):
    """
    Takes as input the path to the folder to be organized.

    If no path is provided, -1 is returned and the program ends.
    Returns None if an error occurs and prints to the screen the error message.
    """
    path = path or "exit"
    if path == "exit":
        return -1
    try:
        if os.path.isfile(path):
            raise NotADirectoryError(
                f'The path "{path}" points to a file, not a folder.'
            )
        elif os.path.isdir(path):
            return path
        else:
            print(f"The path {path} is invalid. Enter a valid path.")
            return None
    except NotADirectoryError as inst:
        print(inst)
        return None


def get_file_formats(path):
    """
    Generates the extension of files in the current path.

    :param path: This is a string representing the current file path.
    :return: Returns a list of unique extensions from which folders will be created.
    """
    try:
        file_formats = []
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                mime_type, _ = mimetypes.guess_type(file_path)
                file_format, extension = mime_type.split("/")
                if all(
                    [
                        file_format == "text",
                        extension == "plain",
                        file_format not in file_formats,
                    ]
                ):
                    file_formats.append(file_format)
                if all(
                    [
                        file_format == "text",
                        extension != "plain",
                        extension not in file_formats,
                    ]
                ):
                    file_formats.append(extension)
                if all(
                    [
                        file_format != "text",
                        file_format != "application",
                        file_format not in file_formats,
                    ]
                ):
                    file_formats.append(file_format)
                if all([file_format == "application", extension not in file_formats]):
                    file_formats.append(extension)
    except AttributeError:
        raise AttributeError
    return file_formats


def create_directories(path, file_formats):
    """
    Creates folders of the list of extensions.

    :param path: This is a string representing the current file path.
    :param file_formats: This is a list of file formats from which folders will be created.
    :return: Returns None.
    """
    try:
        os.chdir(path)
        for file_format in file_formats:
            os.makedirs(file_format, exist_ok=True)
    except UnboundLocalError:
        raise UnboundLocalError



def organize_files(path, error):
    """
    Moves files into folders where the file format is the same as the folder name.

    :param path: This is a string representing the current file path.
    :return: Returns None.
    """
    for folder in os.listdir(path):
        if not os.path.isdir(folder):
            continue
        for file in os.listdir(path):
            if not os.path.isfile(file):
                continue
            mime_type, _ = mimetypes.guess_type(file)
            file_format, extension = mime_type.split("/")
            if any([file_format == folder, extension == folder]):
                old_path = os.path.join(path, file)
                new_path = os.path.join(os.path.join(path, folder), file)
                shutil.move(old_path, new_path)
    return error


if __name__ == "__main__":
    main()
