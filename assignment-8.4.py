fname = raw_input("Enter file name: ")
fh = open(fname)

lst = list()
for line in fh:
    words = line.split()

    for word in words:
        if word in lst: continue
        else:
            lst.append(word)
print sorted(lst)