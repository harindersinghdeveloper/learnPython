with open("myfile.txt","w") as f:
    f.write("hello world")
    f.write("\n")
    f.write("i own it")
    f.close()

with open("myfile.txt","r") as f:
   content = f.read()
   f.seek(0) #to set cursor back to first line
   content1 = f.read()
   f.seek(0)
   panelist = f.readlines() # to read each line as a list
   print(content+ "\n" +content1)
   print(panelist)
   f.close()