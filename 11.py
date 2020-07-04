"""Create a variable, filename. Assuming that it has a three-letter
extension, and using slice operations, find the extension. For
README.txt, the extension should be txt. Write code using slice
operations that will give the name without the extension. Does your
code work on filenames of arbitrary length?"""

def filename(name):
    extension = name[-3:]
    filename = name[:-3]

    print(filename, extension, sep=" is filename and extension is ")


name = input("Enter a  filename with extension: ")
filename(name)