file_name = raw_input("Enter file name: ")
fh = open(file_name)

allTheFloats = []

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    else:
        string_as_float = float(line.split(':')[1].strip())
        allTheFloats.append(string_as_float)


print "Average spam confidence: " + str(sum(allTheFloats)/len(allTheFloats))