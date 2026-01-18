# the seek fun in python is used the move the file pointer or cursor to a specified position 
# with in a file enabling random access to data without loading the entaired file

"""the tell () retuns the current position of the file pointer as an integer"""

with open("file3.txt","r") as file:
    # print(file.seek(5)) #use to move file cursor
    # print(file.tell()) #cursor position as a integer
    print(file.readable())
    print(file.writable())
    print(file.seekable())
