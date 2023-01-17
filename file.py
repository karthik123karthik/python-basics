'''with open("text.txt","w") as f:
    lines = ["1.line\n","2.line\n","3.line\n"]
    f.writelines(lines)


with open("text.txt","r") as f:
     line = f.readline()
     newline = line.strip("\n")
     #print(newline)
'''

with open("text.txt","w") as f:
    #f.seek(10) #move the pointer position by 10 bytes;
    #print(f.tell())
    #print(f.read())
    f.truncate(5) # reduce my file to first 5 bytes
