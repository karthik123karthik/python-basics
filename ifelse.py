# if else statement is used in decision making
# first if will run then elif the else
# eg:

age = 20
if age>20:
  print("you can marry")
elif age>=18 and age<=20:
  print("please wait for some time")
else:
  print("you are not allowed to marry")

match age:
     Case 4:
            print("hello baby boy")
     Case 10:
            Print("hello child")
     Case 15:
            Print("hello teenager")
     Case _:
           print(" hello adult")

arr = [1,2,3,4,5,6,7,8,9]
for index,ele in enumerate(arr,start=1): # now index will start from 1
  print(index,ele) # prints the index and element of the array
   
