#INTRODUCTION TO COMPUTING ASSIGNMENT 2

#Ques1
string='Python is a case sensitive language'

#a
print(len(string))      #finding legnth of string by using len function

#b
print(string[::-1])       #printing string in reverse order using slicing

#c
new_string=string[10:26]        #slicing the string and storing the value in a new variable
print(new_string)

#d
string_new=string.replace('a case sensitive','object oriented')       #Using replace function to alter string
print(string_new)

#e
print(string.index('a'))        #finding position of substring using index function

#f
print(string.replace(' ',''))       #using replace function to replace white spaces with no spaces


print(100*'*')


#Ques2
name=str(input('Enter your name:'))
sid=int(input('Enter your sid:'))
dept=str(input('Enter your department:'))
cgpa=float(input('Enter your cgpa:'))

output=f"Hey,{name} here!\nMy SID is {sid}\nI am from {dept} and my cgpa is {cgpa}"
print(output)


print(100*'*')


#Ques3
a=56
b=10              #use bitwise operators


#a
print(a&b)      #using bitwise operator 'and'

#b
print(a|b)      #using bitwise operator 'or'

#c
print(a^b)      #using bitwise operator 'XOR'

#d
print(a<<2,b<<2)    #performing left shift

#e
print(a>>2,b>>4)    #performing right shift


print(100*'*')


#Ques4
x=float(input('Enter a number:'))
y=float(input('Enter a number:'))
z=float(input('Enter a number:'))

if x>y and x>z:
    largest_number=x

elif y>x and y>z:
    largest_number=y        

else:
    largest_number=z    #all cases where z>x and z>y

print('The largest number is',largest_number)


print(100*'*')


#Ques5
string_by_user=str(input('Enter a string:'))
sub_string='name'

if (string_by_user.find('name')==-1):
    print('No')

else:
    print('Yes')



print(100*'*')


#Ques6
side1=int(input('enter length of first side:'))
side2=int(input('enter length of second side:'))
side3=int(input('enter length of third side:'))

if (side1+side2>side3) and (side2+side3>side1) and (side1+side3>side2):
          print('Yes')

else:
    print('No')



        

