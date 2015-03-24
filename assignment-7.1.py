# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
file_contents = fh.read()
print(file_contents.upper().strip())
