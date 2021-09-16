#print("Hello world")

# taking inputs from terminal
#Patient_name = input('What is your name')
#Age= input('what is your age')
#status= input('status')

#print ( "Hello " + Patient_name + " is" +Age + " years old and " + status)

#birth_year = input('what is your birth year')
#Age = 2021 - int(birth_year)
#print(Age)

#calculator program
#first= float(input('enter first number:'))
#second = float(input('Enter second number:'))
#sum = first + second
#print("sum is:" + str(sum))

#for checking

#course = "Python for beginners"
#print(course.upper())
#print(course)
#print(course.find('n'))
#print(course.replace('for', '4'))
#print('Python' in course)

#basicmath operations
#print(10/3) #returnwith decimal
#print(10//3) #returns only number
#print(10%3)  #remiander
#print(10 ** 3) #exponent (10 to the power of 3 here)

#x= 10+3*2
#print (x) #precesion
#y=(10+3)*2
#print(y)

#comparision operators
#x = 3>2
#print(x)

#x = 2<1
#print(x)

#logical operators
#price =25
#print(price > 10 and price <30)
#price = 5
#print(price > 10 or price <30)

#if statements
#temp = 5
#if temp > 30:
 #   print("It's a hot day")
  #  print('Drink pleanty of water')
#elif temp>20:
 #   print("it's a nice day")
#elif temp>10:
 #   print("it's a bit cold")
#else:
 #   print("it's cold")
#print ('done')
#
a= [5,3,2,4,6,13]
b= [2,3,4,5,6,8]
c=[]
for n in range (0, len(a)):
    c.append(a[n] + b[n])
print("the sum list is ", c)
for m in c:
    if m%3== 0 and m%7==0:
        print("Fizzbuzz")
    elif m % 3 == 0:
        print("fizz")
    else:
        print("Buzz")
# weight function
weight = int(input("weight:"))
unit = input("(K)g or (L)bd: ")
if unit.upper() == "K":
    converted = weight/0.45
    print("weight in pounds is : " + str(converted))
else:
    converted = weight *0.45
    print("Weight in kg is " + str(converted))
#while loops - to repeat block of coade multiple time
i=1
while i<=5:
    print(i)
    i=i+1

#functions with while
i=1
while i<=10:
    print(i * '*')
    i=i+1

#Lists
a= 7**2
print(a)