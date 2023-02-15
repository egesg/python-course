# file-handling

There are 2 ways to open and close a file
1. open() and close() functions
2. with open() function


# 1st way
## - open()

- It is used for 
    - reading, 
    - writing, and
    - creating files

- It accepts 2 arguments
    1. file name/file location
    2. mode
        - indicates what action is required (reading/writing/creating)
        - specifies file output format (text/binary)

    Mode sets:
    - 'r'   -> open for reading only (text format)
    - 'rb'  -> open for reading only (binary format)
    - 
    - 'w'   -> open for writing only
    - 'wb'  -> open for writing only (binary format)
    - 
    - 'r+'  -> open for reading and writing
    - 'rb+' -> open for reading and writing (binary format)
    - 
    - 'a'   -> open for editing or appending data
    - 'ab'  -> open for editing or appending data (binary format)


## - close()

- It is used for 
    - closing the open file connection

- It does not take any arguments

# 2nd way
## - with open()

It closes the file automatically


# Notes
- reading files with 'r'
    There are 3 methods
    1. read()
    2. readline()
    3. readlines() -> prints the text as a list

- creating files with 'w'
    There are 3 methods
    - write()
    - writeline()
    - writelines()

- paths
    - absolute paths
    1.
    2.
    - relative paths