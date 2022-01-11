import sys

print ("Input File =" + sys.argv[1]) 
print ("Output File = " + sys.argv[2])

inputfile = open(sys.argv[1])
outputfile = open (sys.argv[2],"w") 

linenum = int(input("enter line number to be skipped=") )

count =1 

Lines = inputfile.readlines()

NoOfLines = len(Lines) 

print("No of lines in file =" + str(NoOfLines ))
 
if (linenum ==0) :
   print ("Line number cannot be Zero") 
elif (linenum <0) :
   print ("Line Number cannot be negative")
elif (linenum <= NoOfLines ) :
    for  line in Lines : 
       if (count !=linenum) :
           outputfile.write(line.strip()+"\n") 
       count = count +1
else: 
  print ("The entered value is more than the No of lines in the file. Please neter valid valus") 

inputfile.close()
outputfile.close() 

