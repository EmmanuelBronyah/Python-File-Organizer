# Python File Organizer.
This command-line python file organizer is a program that
scans a directory for files and creates folders for all
the file extensions where each folder bares the name 
of an extension and files in the directory are moved into
these folders according to their extension.

## Features of the file organizer
1. **Takes path**: The program receives as input the path to
the directory whose contents are to be organized. It returns
the path if it is valid or returns None if an error occurs. 
2. **Extracts extension and creates folders**: The program 
extracts the extension of the files in the directory and 
creates a folder for each extension where files of the 
same type are stored.
3. **Organize files**: The extension of each file in the 
directory is checked against the folder names in the directory,
and if the extension matches the name of the folder, the
file is moved into the folder.

## Getting started
1. **Clone the repository to your machine.**
```shell
git clone https://github.com/EmmanuelBronyah/Python-File-Organizer.git
```
2. **Navigate to the project directory.**
```shell
cd file-organizer
```
3. **Run the program.**
```shell
python main.py
```

## Usage
* When you run the program, you will be prompted to provide
the path to the directory you want organized. The program
outputs the message 'Files organized.' when it is done 
executing, or otherwise outputs a different message 
pertaining to an error that might have occurred.

## Example
1. **Providing a valid path which points to a folder.**
```shell
Enter the path to the folder you want to organize: C:\Users\{your-username}\Desktop\{foldername}
Files organized.
```
2. **Providing a valid path which points to a file.**
```shell
Enter the path to the folder you want to organize: C:\Users\{your-username}\Desktop\{filename}
The path "C:\Users\{your-username}\Desktop\{filename}" points to a file, not a folder.
```
3. **Entering an invalid path or an invalid input.**
```shell
Enter the path to the folder you want to organize: \$%67?
The path "\$%67?" is invalid. Enter a valid path.
```

# License
This project is licensed under the MIT license.

# Acknowledgements
* Built by Bronyah Emmanuel.