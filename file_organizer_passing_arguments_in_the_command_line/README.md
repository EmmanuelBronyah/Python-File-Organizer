# Python File Organizer.
This command-line python file organizer is a program that
scans a directory for files and creates folders for all
the file formats where each folder bares the name 
of the file format and files in the directory are moved into
these folders according to their formats.


## Features of the file organizer
1. **Takes path as a command-line argument**: The program takes the path(which must be embedded in quotes("")) to
the directory whose contents are to be organized through the command-line. It organizes
the files in the directory if the path is valid or returns an error message if an error occurs. 
2. **Extracts file format and creates folders**: The program 
extracts the formats of the files in the directory and 
creates a folder for each file format where files of the 
same type are stored.
3. **Organize files**: The file format of each file in the 
directory is checked against the folder names in the directory,
and if the format matches the name of the folder, the
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
python file_organizer_cli.py
```

## Usage
* You would need to add the path as argument in the 
command-line when you run the script. The program
outputs the message 'Files organized.' when it is done 
executing, or otherwise outputs a different message 
pertaining to an error that might have occurred.
Please note that the path to the folder must be placed in quotes("").
And also folder names with spaces would require the path
to be embedded in quotes("").

## Example
1. Adding a path argument.
```shell
(venv) PS C:\Users\{User}\PycharmProjects\file-organizer> python file_organizer_cli "C:\Users\ManuelB\Desktop\File-arranger-folder"
Files organized.
```
2. Adding a path argument not embedded in quotes("") where the folder name has spaces.
```shell
(venv) PS C:\Users\{User}\PycharmProjects\file-organizer> python file_organizer_cli C:\Users\ManuelB\Desktop\File arranger folder
usage: File organizer [-h] [P]
File organizer: error: unrecognized arguments: arranger folder
```

# License
This project is licensed under the MIT license.

# Acknowledgements
* Built by Bronyah Emmanuel.