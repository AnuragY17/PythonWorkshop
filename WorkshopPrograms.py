#1-PYTHON PROGRAM TO PRINT HELLO WORLD!
#print("Hello World!")


#2-PROGRAM FOR ADDITION OF TWO NUMBERS
#num_1=int(input("enter first number:"))
#num_2=int(input("enter second number:"))
#sum1=num_1+num_2
#print("sum of numbers=",sum1) 


#3-PROGRAM TO PRINT QUOTIENT AND REMAINDER OF TWO NUMBERS
#num_1=int(input("enter first number:"))
#num_2=int(input("enter second number:"))
#if(num_1==0 or num_2==0):
#    print("WRONG CHOICE")
#else:
#    print("Quotient on dividing",num_1,"with",num_2,"is",(num_1/num_2))
#    print("Remainder on dividing",num_1,"with",num_2,"is",(num_1%num_2))
#    print("Quotient on dividing",num_2,"with",num_1,"is",(num_2/num_1))
#    print("Remainder on dividing",num_2,"with",num_1,"is",(num_2%num_1))


#4-PROGRAM TO FIND AVERAGE OF THREE NUMBERS
#num_1=int(input("enter first number:"))
#num_2=int(input("enter second number:"))
#num_3=int(input("enter third number:"))
#avg=(num_1+num_2+num_3)/3
#print("average of",num_1,num_2,num_3,"is",avg)


#5-PROGRAM TO FIND SUM OF 5 SUBJECTS AND THEIR PERCENTAGE
#sub_1=int(input("enter marks of first subject:"))
#sub_2=int(input("enter marks of second subject:"))
#sub_3=int(input("enter marks of third subject:"))
#sub_4=int(input("enter marks of fourth subject:"))
#sub_5=int(input("enter marks of fifth subject:"))
#sum_=(sub_1+sub_2+sub_3+sub_4+sub_5)
#percentage=((sub_1+sub_2+sub_3+sub_4+sub_5)*100)/500
#print("sum of five subjects=",sum_)
#print("percentage of five subjects=",percentage,"%")


#6-PROGRAM TO FIND GROSS SALARY
#annual_salary=int(input("enter annual salary:"))
#pay_period=int(input("enter number of pays in an year:"))
#salary=annual_salary/pay_period
#print("Gross salary ineach period=",salary)


#7-PROGRAM TO CALCULATE AREA OF RECTANGLE AND SQUARE
#l=int(input("enter length of rectangle:"))
#b=int(input("enter breadth of rectangle:"))
#a=int(input("enter length of side of square:"))
#a_rect=l*b
#a_sqr=a*a
#print("area of rectangle=",a_rect)
#print("area of square=",a_sqr)


#8-PROGRAM TO CALCULATE AREA OF SCALENE AND RIGHT ANGLED TRIANGLE
#a=int(input("enter length of first side of scalene triangle:"))
#b=int(input("enter length of second side of scalene triangle:"))
#c=int(input("enter length of third side of scalene triangle:"))
#b=int(input("enter base of right angled triangle:"))
#h=int(input("enter height of right angled traingle:"))
#s=(a+b+c)/2
#a_scalene=((s*(s-a)*(s-b)*(s-c))**(1/2)) 
#a_right=(b*h)*(1/2)
#print("area of scalene triangle with side",a,b,c,"is",a_scalene)
#print("area of right angled triangle with base",b,"and",h,"is",a_right)


#9-PROGRAM TO FIND VOLUME AND SURFACE AREA OF CUBE,CUBOID AND CYLINDER
#a=int(input("enter side length of cube:"))
#l=int(input("enter length of cuboid:"))
#b=int(input("enter breadth of cuboid:"))
#h=int(input("enter height of cuboid:'"))
#r=int(input("enter radius of cylinder:"))
#H=int(input("enter height of cylinder:"))
#lsa_cube=(4*a*a)
#tsa_cube=(6*a*a)
#v_cube=a**3
#lsa_cuboid=((2*h)*(l+b))
#tsa_cuboid=2*((l*b)+(b*h)+(l*h))
#v_cuboid=l*b*h
#csa_cylinder=(2*3.14)*(r*H)
#tsa_cylinder=(2*3.14*r)*(H+r)
#v_cylinder=3.14*(r**2)*H
#print()
#print("Lateral surface area of cube=",lsa_cube)
#print("total surface area of cube=",tsa_cube)
#print("volume of cube=",v_cube)
#print("lateral suraface area of cuboid=",lsa_cuboid)
#print("total surface area of cuboid=",tsa_cuboid)
#print("volume of cuboid=",v_cuboid)
#print("curved surface area of cylinder=",v_cylinder)
#print("total surface area of cylinder=",tsa_cylinder)
#print("volume of cylinder=",v_cylinder) 


#10-PROGRAM TO FIND VOLUME AND SURFACE AREA OF CONE,SPHERE AND CYLINDER
#r=int(input("enter radius of cone:"))
#h=int(input("enter height of cone:"))
#R=int(input("enter radius of sphere:"))
#r1=int(input("enter radius of cylinder:"))
#H=int(input("enter height of cylinder:"))
#l=((h**2)+(r**2))**(1/2)
#csa_cone=(3.14*r*l)
#tsa_cone=((3.14*r)*(r+l))
#v_cone=(3.14*(r**2)*h)/3
#tsa_sphere=4*3.14*(R**2)
#v_sphere=(4*3.14*(R**3))/3
#csa_cylinder=(2*3.14)*(r1*H)
#tsa_cylinder=(2*3.14*r1)*(H+r1)
#v_cylinder=3.14*(r1**2)*H
#print("curved surface area of cone=",csa_cone)
#print("total surface of cone=",tsa_cone)
#print("volume of cone=",v_cone)
#print("total surface area of sphere=",tsa_sphere)
#print("volume of sphere=",v_sphere)
#print("curved surface area of cylinder=",csa_cylinder)
#print("total surface area of cylinder=",tsa_cylinder)
#print("volume of cylinder=",v_cylinder)


#11-PROGRAM TO FIND AREA OF TRAPEZIUM,RHOMBUS AND PARALLELOGRAM
#a=int(input("enter length of first parallel side of trapezium:"))
#b=int(input("enter length of second parallel side of trapezium:"))
#h=int(input("enter height betweeen parallel side of trapezium:"))
#B=int(input("enter breadth of parallelogram:"))
#H=int(input("enter height of parallelogram:"))
#d1=int(input("enter length of diagonal one of rhombus:"))
#d2=int(input("enter length of diagonal second of rhombus:"))
#a_trap=((a+b)*h)/2
#a_pllgm=B*H
#a_rhombus=(d1*d2)/2
#print("area of trapezium=",a_trap)
#print("area of rhombus:",a_rhombus)
#print("area of parallelogram=",a_pllgm)


#12-PROGRAM TO FIND PERIMETER OF CIRCLE,RECTANGLE AND TRIANGLE
#r=int(input("enter radius of circle:"))
#l=int(input("enter length of rectangle:"))
#b=int(input("enter breadth of triangle:"))
#s1=int(input("enter length of first side of triangle:"))
#s2=int(input("enter length of second side of triangle:"))
#s3=int(input("enter length of third side of triangle:"))
#p_circle=2*3.14*r
#p_rectangle=2*(l+b)
#p_triangle=s1+s2+s3
#print("perimeter of circle=",p_circle)
#print("perimeter of rectangle=",p_rectangle)
#print("perimeter of triangle=",p_triangle)


#13-PROGRAM TO CALCULATE COMPOUND INTEREST
#p=int(input("enter principal amount:"))
#r=float(input("enter interest rate:"))
#t=float(input("enter time in yrs:"))
#si=(p*r*t)/100
#print("Simple Interest when principal amount,rate and time respectively is",p,r,t,"is",si)


#14-PROGRAM TO CONVERT FAHRENHEIT TEMPERATURE TO CELCIUS
#f=float(input("enter temperature in fahrenheit:"))
#c=(f-32)/(9/5)
#print("temperature in celcius=",c)


#15-PROGRAM TO FIND GRAVITATIONAL FORCE ACTING BETWEEN TWO OBJECTS
#m1=float(input("enter mass of first body in kg:"))
#m2=float(input("enter mass of second body in kg:"))
#r=float(input("enter separation between the two objects:"))
#f=(((6.67*(10**(-11)))*(m1*m2))/(r**2))
#print("Gravitational force between the two bodies of masses",m1,m2,"respectively and separation",r,"is:",f)


#16-PROGRAM TO SWAP VALUES OF TWO VARIABLES WITH AND WITHOUT THIRD VARIABLE
#print("SWAPPING WITHOUT USING THIRD VARIABLE")
#a=int(input("enter first number:"))
#b=int(input("enter second number:"))
#a=a+b
#b=a-b
#a=a-b
#print("First Number=",a)
#print("Second Number=",b)
#print("SWAPPING WITH USING THIRD VARIABLE")
#a=int(input("enter first number:"))
#b=int(input("enter second number:"))
#c=a
#a=b
#b=c
#print("First Number=",a)
#print("Second Number=",b)


#17-PROGRAM TO PERFORM ARITHMETIC OPERATIONS ON a=8,b=3
#a=8
#b=3
#print("USING ADDITION OPERATOR","+")
#print("Addition of",a,b,"is",(a+b))
#print("USING SUBTRACTION OPERATOR")
#print("Subtraction of",a,b,"is",(a-b))
#print("USING MULTIPLICATION OPERATOR")
#print("Multiplication of",a,b,"is",(a*b))
#print("USING DIVISION OPERATOR")
#print("Division of",a,b,"is",(a/b))
#print("USING MODULUS OPERATOR")
#print("Modulus of",a,b,"is",(a%b))
#print("USING EXPONENTIATION OPERATOR")
#print("Exponentiation of",a,b,"is",(a**b))
#print("USING FLOOR DIVISION OPERATOR")
#print("Floor Division of",a,b,"is",(a//b))


#18-PROGRAM TO PERFORM RELATIONAL OPERATIONS ON a=8,b=3
#a=8
#b=3
#print("USING GREATER THAN OPERATOR BETWEEN a=8 AND b=3")
#print(a>b)
#print("USING LESS THAN OPERATOR BETWEEN a=8 AND b=3")
#print(a<b)
#print("USING DOUBLE EQUAL TO OPERATOR BETWEEN a=8 AND b=3")
#print(a==b)
#print("USING NOT EQUAL TO OPERATOR BETWEEN a=8 AND b=3")
#print(a!=b)
#print("USING GREATER THAN OR EQUAL TO OPERATOR BETWEEN a=8 AND b=3")
#print(a>=b)
#print("USING LESS THAN OR EQUAL TO OPERATOR BETWEEN a=8 AND b=3")
#print(a<=b)


#19-PROGRAM TO ASSIGNMENT OPERATOR ON a=8 AND b=3
#a=8
#b=3
#print("USING EQUAL TO OPERATOR ON a=8 AND b=3")
#c=a+b
#print(c)
#print("USING ADD AND ASSIGN OPERATOR ON a=8 AND b=3")
#a=8
#b=3
#a+=b
#print(a)
#print("USING SUBTRACT AND ASSIGN OPERATOR ON a=8 AND b=3")
#a=8
#b=3
#a-=b
#print(a)
#print("USING MULTIPLY AND ASSIGN OPERATOR ON a=8 AND b=3")
#a=8
#b=3
#a*=b
#print(a)
#print("USING DIVIDE AND ASSIGN OPERATOR ON a=8 AND b=3")
#a=8
#b=3
#a/=b
#print(a)
#print("USING MODULUS AND ASSIGN OPERATOR ON a=8 AND b=3")
#a=8
#b=3
#a%=b
#print(a)
#print("USING FLOOR AND ASSIGN OPERATOR ON a=8 AND b=3")
#a=8
#b=3
#a//=b
#print(a)
#print("USING EXPONENT AND ASSIGN OPERATOR ON a=8 AND b=3")
#a=8
#b=3
#a**=b
#print(a)
#print("USING BITWISE AND ASSIGN OPERATOR ON a=8 AND b=3")
#a=8
#b=3
#a&=b
#print(a)
#print("USING BITWISE OR ASSIGN OPERATOR ON a=8 AND b=3")
#a=8
#b=3
#a|=b
#print(a)
#print("USING BITWISE XOR ASSIGN OPERATOR ON a=8 AND b=3")
#a=8
#b=3
#a^=b
#print(a)
#print("USING BITWISE RIGHT SHIFT ASSIGN OPERATOR ON a=8 AND b=3")
#a=8
#b=3
#a>>=b
#print(a)
#print("USING BITWISE LEFT SHIFT OPERATOR ON a=8 AND b=3")
#a=8
#b=3
#a<<=b
#print(a)


#20-PROGRAM TO APPLY LOGICAL OPERATIONS ON a=8 AND b=3
#a=8
#b=3
#print("USING LOGICAL AND OPERATOR ON a=8 AND b=3")
#if(a>0 and b>0):
#    print("BOTH NUMBERS ARE GREATER THAN ZERO")
#else:
#    print("ATLEAST ONE NUMBER IS NOT GREATER THAN ZERO")
#print("USING LOGICAL OR OPERATOR ON a=8 AND b=3")
#if(a>0 or b>0):
#    print("EITHER OF THE NUMBER IS GREATER THAN ZERO")
#else:
#    print("NO NUMBER IS GREATER THAN ZERO")
#print("USING LOGICAL AND OPERATOR ON a=8 AND b=3")
#if not a:
#    print("Boolean value of a is True")
#  
#if not (a%4==0 or a%5==0):
#    print("10 is not divisible by either 3 or 5")
#else:
#    print("10 is divisible by either 3 or 5")


#21-PROGRAM TO APPLY BITWISE OPERATION ON a=8 AND b=3
#a=8
#b=3
#print("USING BITWISE AND OPERATOR")
#print("a&b=",a&b)
#print("USING BITWISE OR OPERATOR")
#print("a|b=",a|b)
#print("USING BITWISE NOT OPERATOR")
#print("~a=",~a)
#print("USING BITWISE XOR OPERATOR")
#print("a^b=",a^b)
#print("USING BITWISE RIGHT SHIFT OPERATOR")
#print("a>>2",a>>2)
#print("USING BITWISE LEFT SHIFT OPERATOR")
#print("a<<2",a<<2)


#22-PROGRAM TO APPLY IDENTITY OPERATOR ON a=8 AND b=3
#a=8
#b=3
#print("USING IS IDENTITY OPERATOR ON a=8 AND b=3")
#print(a is b)
#print("USING IS NOT IDENTITY OPERATOR ON a=8 AND b=3")
#print(a is not b)


#23-PROGRAM TO SWAP CONTENT OF TWO VARIABLES USING XOR OPERATOR a=8 AND b=3
#a=8
#b=3
#print("SWAPPING USING XOR OPERATOR OF a=8 AND b=3")
#a=a^b
#b=a^b
#a=a^b
#print("a=",a)
#print("b=",b)


#24-PROGRAM TO MULTIPLY GIVEN NUMBER BY 4 USING BITWISE OPERATORS
#n=int(input("enter a number:"))
#print("MULTIPLYING GIVEN NUMBER",n,"BY 4 USING BITWISE OPERATORS")


#25-PROGRAM TO FIND SQUARE ROOT OF A NUMBER
#n=int(input("enter a number:"))
#print("SQUARE ROOT OF",n,"is",(n**(0.5)))


#26-PROGRAM TO CONVERT ALL UNITS OF TIME INTO SECONDS
#d=int(input("enter number of days:"))
#h=int(input("enter number of hours:"))
#m=int(input("enter number of minutes:"))
#s=int(input("enter number of seconds:"))
#t=(d*24*3600)+(h*3600)+(m*60)+s
#print("time in seconds=",t)


#27-Python program to calculate midpoints of a line-segment
#x1=float(input("enter first x-coordinate:"))
#x2=float(input("enter second x-coordinate:"))
#y1=float(input("enter first y-coordinate:"))
#y2=float(input("enter second y-coordinate:"))
#x=(x1+x2)/2
#y=(y1+y2)/2
#print("coordinates of mid-points of line segments are",x,",",y)


#28-Python program to display your details like name, age, address in three different lines
#name=input("enter your name:")
#age=int(input("enter your age in years:"))
#address=input("enter your address:")
#print("Name=",name)
#print("Age=",age)
#print("Address=",address)


#29-Python program to compute the distance between the points (x1, y1) and (x2, y2)
#x1=float(input("enter first x-coordinate:"))
#x2=float(input("enter second x-coordinate:"))
#y1=float(input("enter first y-coordinate:"))
#y2=float(input("enter second y-coordinate:"))
#d=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
#print("distance between two points is:",d)


#31-WAP to demonstrate implicit and explicit type conversion.
#print("DISPLAYING IMPLICIT TYPE CONVERSION")
#a=3
#print("type of a=3 is",type(a))
#print("DISPLAYING EXPLICIT TYPE CONVERSION")
#A=3
#B=float(a)
#print("type of A=3 after conversion and saving in B is",type(B))


#33-WAP to reverse a string.
#str1=input("enter a string:")
#print("reverse of string",str1,"is",str1[::-1])


#34-WAP to develop a new string has even position characters of given string. Ex: input: “GOKUGOHAN”,
#Output: “GKGHN""
#str1=input("enter a string:")
#print("even position of string",str1,"is",str1[0:len(str1):2])


#35-Write a program to Accept two Integers and Check if they are Equal
#num_1=int(input("enter first number:"))
#num_2=int(input("enter second number:"))
#if(num_1==num_2):
#    print("GIVEN NUMBERS ARE EQUAL")
#else:
#    print("GIVEN NUMBERS ARE NOT EQUAL")


#36-Write a program to Check if a given Integer is Positive or Negative and Odd or Even. 
#n=int(input("enter a integer number:"))
#print("CHECKING IF NUMBER IS POSITIVE OR NEGATIVE")
#if(n>0):
#    print("number",n,"is positive")
#if(n<0):
#    print("number",n,"is negative")
#print("CHECKING NUMBER IS EVEN OR ODD")
#if(n%2==0):
#    print("number",n,"is even number")
#if(n%2!=0):
#    print("number",n,"is odd number")


#37-Write a program to Check if a given Integer is Divisible by 7 or not.
#n=int(input("enter a number:"))
#if(n%7==0):
#    print("number",n,"is divisible by 7")
#else:
#    print("number",n,"is not divisible by 7")


#38-Write a program to find the greatest of three numbers using else if.
#a=int(input("enter first number:"))
#b=int(input("enter second number:"))
#c=int(input("enter third number:"))
#if(a>b and a>c):
#    print("largest number is:",a)
#elif(b>c):
#   print("largest number is:",b)
#else:
#    print("largest number is:",c)


#39-Write a program to find the greatest of three numbers using Nested if.
#a=int(input("enter first number:"))
#b=int(input("enter second number:"))
#c=int(input("enter third number:"))
#if(a>b):
#    if(a>c):
#        print("largest number is:",a)
#if(b>a):
#    if(b>c):
#       print("largest number is:",b)
#if(c>a):
#    if(c>b):
#        print("largest number is:",c)


#40-Write a program to convert an Upper-case character into lower case and vice-versa
#str1=input("enter a character:")
#if(str1>='A' and str1<='Z'):
#    print(str1,"is upper case character")
#    str2=ord(str1)
#    print(str1,"in lower case is",chr(str2+32))
#elif(str1>='a' and str1<="z"):
#    print(str1,"is lowercase character")
#    str2=ord(str1)
#    print(str1,"in upper case is",chr(str2-32))
 

#41-Write a program to check weather an entered year is leap year or not.
#n=int(input("enter a year:"))
#if((n%100==0 and n%400==0) or (n%100!=0 and n%4==0)):
#    print(n,"is leap year")
#else:
#    print(n,"is not a leap year")


#42-Write a Program to check whether an alphabet entered by the user is a vowel or a constant
#str1=input("enter a character:")
#if(str1 in ('a','e','i','o','u')):
#    print(str1,"is vowel")
#elif(str1 in ('1','2','3','4','5','6','7','8','9','0')):
#    print(str1,"is constant")
#else:
#    print("other character")


#43-Write a program to Read a Coordinate Point and Determine its Quadrant.
#x=float(input("enter x-coordinate:"))
#y=float(input("enter y-coordinate:"))
#if(x>0 and y>0):
#    print("coordinates is of first quadrant")
#elif(x<0 and y>0):
#    print("coordinates is of second quadrant")
#elif(x<0 and y<0):
#    print("coordinates is of third quadrant")
#else:
#    print("coordinates is of fourth quadrant")
    
    
#44-Write a program to Add two Complex Numbers.
#x1=float(input("enter real part of first complex number:"))
#x2=float(input("enter real part of second complex number:"))
#j1=float(input("enter imaginary part of first complex number:"))
#j2=float(input("enter imaginary part of second complex number:"))
#print("sum of two complex number is:",(x1+x2),"+",(j1+j2),"i")


#45-Write a Program to find roots of a quadratic expression.
#a=float(input("enter coefficient of x^2:"))
#b=float(input("enter coefficient of x:"))
#c=float(input("enter constant term:"))
#D=(b**2)-(4*a*c)
#if(D>0):
#    x1=(-b+(D**(1/2)))/(2*a)
#    x2=(-b-(D**(1/2)))/(2*a)
#    print("real and different roots are",x1,"and",x2)
#elif(D==0):
#    x=-b/(2*a)
#    print("equal roots are:",x,"and",x)
#else:
#    print("imaginary roots")
 

#46-Write a program to print day according to the day number entered by the user



#47-Write a program to print color name, if user enters the first letter of the color name
#print("for blue and brown write U and Z respectively")
#str1=input("enter first character of color name in upper case:")
#if(str1=="B"):
#    print("color name is BLACK")
#elif(str1=="W"):
#    print("color name is WHITE")
#elif(str1=="R"):
#    print("color name is RED")
#elif(str1=="Y"):
#    print("color name is YELLOW")
#elif(str1=="U"):
#    print("color name is BLUE")
#elif(str1=="G"):
#    print("color name is GREEN")
#elif(str1=="P"):
#    print("color name id PINK")
#elif(str1=="V"):
#    print("color name is VOILET")
#elif(str1=="Z"):
#    print("color name is BROWN")
#elif(str1=="O"):
#    print("color name is ORANGE")


#48-Write a program to Simulate Arithmetic Calculator.
#print("ARITHMETIC CALCULATOR")
#num_1=float(input("enter first number:"))
#num_2=float(input("enter second number:"))
#op=input("enter operation you want to perform in symbol of operation:")
#if(op=="+"):
#    print("SUM OF",num_1,"AND",num_2,"IS",(num_1+num_2))
#elif(op=="-"):
#    print("SUBTRACTION OF",num_1,"AND",num_2,"IS",(num_1-num_2))
#elif(op=="*"):
#    print("MULTIPLICATION OF",num_1,"AND",num_2,"IS",(num_1*num_2))
#elif(op=="/"):
#    print("DIVISION OF",num_1,"AND",num_2,"IS",(num_1/num_2))
#elif(op=="%"):
#    print("MODULUS OF",num_1,"AND",num_2,"IS",(num_1%num_2))
#elif(op=="**"):
#    print("EXPONENTIATION OF",num_1,"AND",num_2,"IS",(num_1**num_2))
#elif(op=="//"):
#    print("FLOOR DIVISION OF",num_1,"AND",num_2,"IS",(num_1//num_2))
 

#49-Write a menu driven program for calculating area of different geometrical figures such as circle,
#square, rectangle, and triangle.
#print("MENU DRIVEN PROGRAM FOR AREA OF FOLLOWING FIGURES:")
#print("1.CIRCLE")
#print("2.SQUARE")
#print("3.RECTANGLE")
#print("4.TRIANGLE")
#ch=int(input("enter serial number of geometrical figure you want to calculate:"))
#if(ch==1):
#    r=float(input("enter radius of circle:"))
#    a=3.14*(r**2)
#    print("area of circle=",a,"sq. units")
#elif(ch==2):
#    a=int(input("enter side length of square:"))
#    A=a*a
#    print("area of square=",A,"sq. units")
#elif(ch==3):
#    l=float(input("enter length of rectangle:"))
#    b=float(input("enter breadth of rectangel:"))
#    a=l*b
#    print("area of rectangel=",a,"sq.units")
#elif(ch==4):
#    a=int(input("enter length of first side of scalene triangle:"))
#    b=int(input("enter length of second side of scalene triangle:"))
#    c=int(input("enter length of third side of scalene triangle:"))
#    s=(a+b+c)/2
#    a_scalene=((s*(s-a)*(s-b)*(s-c))**(1/2)) 
#    print("area of scalene triangle with side",a,b,c,"is",a_scalene,"sq. units")
#else:
#    print("WRONG CHOICE")
 

#50-WAP that accepts the marks of 5 subjects and finds the percentage marks obtained by the student. It
#also prints grades according to the following criteria: Between 90-100% Print 'A', 80-90% Print 'B', 60-
#80% Print 'C', 50-60% Print 'D', 40-50% Print 'E', Below 40% Print 'F’.   
#sub_1=int(input("enter marks of first subject:"))
#sub_2=int(input("enter marks of second subject:"))
#sub_3=int(input("enter marks of third subject:"))
#sub_4=int(input("enter marks of fourth subject:"))
#sub_5=int(input("enter marks of fifth subject:"))
#percentage=((sub_1+sub_2+sub_3+sub_4+sub_5)*100)/500
#print("percentage of five subjects=",percentage,"%")
#if(percentage>90 and percentage<=100):
#    print("GRADE=A")
#elif(percentage>80 and percentage<=90):
#    print("GRADE=B")
#elif(percentage>60 and percentage<=80):
#    print("GRADE=C")
#elif(percentage>50 and percentage<=60):
#    print("GRADE=D")
#elif(percentage>40 and percentage<=50):
#   print("GRADE=E")
#else:
#    print("GRADE=F")
    
 
#51-WAP to enter a character and then determine whether it is a vowel, consonants, or a digit.
#str1=input("enter a character in lower case if alpha:")
#if(str1 in ('a','e','i','o','u')):
#    print(str1,"is vowel")
#elif(str1 in ('1','2','3','4','5','6','7','8','9','0')):
#    print(str1,"is digit")
#else:
#    print(str1,"is consonant")


#52-Write a program to display all even numbers from 1 to 20
#i=1
#print("EVEN NUMBERS BETWEEN 1 TO 20 ARE:")
#while(i<=20):
#    if(i%2==0):
#        print(i)
#    i+=1
        
    
#53-Write a program to print all the Numbers Divisible by 7 from 1 to 100.
#i=1
#print("NUMBERS DIVISIBLE BY 7 BETWEEN 1 TO 100 ARE:")
#while(i<=100):
#    if(i%7==0):
#        print(i)
#    i+=1


#54-Write a program to print table of any number.
#n=int(input("\nenter a number:"))
#i=1
#while(i<=10):
#    print(n,"*",i,"=",(n*i))
#   i+=1


#55-Write a program to print 1,2,3,5,6,7,8,9 use continue statement
#for i in range(1,10):
#    if(i==4):
#        continue
#    print(i)

 
#56-Write a program to print table of 5 in following format  
#n=5
#i=1
#while(i<=10):
#    print(n,"*",i,"=",(n*i))
#    i+=1
 

#57-Write a program to Find the Sum of first 50 Natural Numbers using for Loop
#s=0
#for i in range(1,51):
#    s+=i
#print("sum of first 50 natural numbers=",s)
 

#58-Write a program to calculate factorial of a given number using for loop and also using while loop
#print("FACTORIAL OF A NUMBER USING WHILE LOOP")
#n=int(input("\nenter a number:"))
#f=1
#i=1
#while(i<=n):
#    f=f*i
#    i+=1
#print("factorial of",n,"is",f)
#print("FACTORIAL USING FOR LOOP")
#F=1
#for i in range(1,n+1):
#   F=F*i
#print("factorial of",n,"is",F)


#59-Write a program to count the sum of digits in the entered number.
#n=int(input("\nenter a number:"))
#s=0
#while(n>0):
#    d=n%10
#    s=s+d
#    n=n//10
#print("sum of digits=",s)


#60-Write a program to find the reverse of a given number.
#n=int(input("\nenter a number:"))
#s=0
#a=n
#while(n>0):
#    d=n%10
#    s=(s*10)+d
#    n=n//10
#print("reverse of number",a,"is",s)


#61-Write a program to Check whether a given Number is Perfect Number.
#n=int(input("enter a number:"))
#s=0
#for i in range(1,n):
#    if(n%i==0):
#       s+=i
#if(s==n):
#    print(n,"is perfect number")
#else:
#    print(n,"is not a perfect number")
    

#62-Write a program to check if the given number is a Disarium Number (1
#1+ 72 + 53 = 1+ 49 + 125 = 175).
#n=int(input("enter a number:"))
#s=0
#n=str(n)
#for i in range(len(str(n))):
#    
#    d=str(n[i])
#    s=s+(int(d)**(i+1))
#s=str(s)
#if(s==n):
#    print(s,"is disarian number")
#else:
#    print(s,"is not a disarium number")    


#62-METHOD-2
#n=int(input("enter a number:"))
#s=0
#a=n
#c=0
#while(n>0):
#    n=n//10
#    s+=1
#while (n>0):
#       d=n%10
#       c=c+(d**s)
#       n=n//10
#       s-=1
#if(c==a):
#    print(a,"is disarium number")
#else:
#    print(a,"is not a disarium number")
 

#63-Write a program to determine whether the given number is a Harshad Number (If a number is divisible
#by the sum of its digits, then it will be known as a Harshad Number).
#n=int(input("enter a number:"))
#s=0
#a=n
#while(n>0):
#    d=n%10
#    s+=d
#    n=n//10
#if(a==s):
#    print(a,"is harshad number")
#else:
#    print(a,"is harshad number")


#64-Write a program to Print Armstrong Number from 1 to 1000.
#i=1
#while(i<=1000):
#    a=i
#    s=0
#    while(a>0):
#        d=a%10
#        s=s+(d**3)
#        a=a//10
#    if(i==s):
#        print(i,"is armstrong number")
#    i+=1
 

#65-Write a program to Compute the Value of X^n
#x=int(input("enter a number:"))
#n=int(input("enter powers of x you want to go:"))
#i=1
#while(i<=n):
#    print(x,"to the power",i,"is",(x**i))
#    i+=1


#66-Write a program to Calculate the value of C(n,r)
#n=int(input("enter total number of objects in the set:"))
#r=int(input("enter number of choosing objects in the set:"))
#N=1
#R=1
#D=1
#for i in range(1,n+1):
#    N=N*i
#for i in range(1,r+1):
#    R=R*i
#for i in range(1,(n-r+1)):
#    D=D*i
#ans=N/(R*D)
#print(" value of C",n,r,"is",ans)


#67-Write a program to generate the Fibonacci Series.
#n=int(input("\nenter a limit:"))
#f=0
#s=1
#print(f,s,end=' ')
#i=3
#while(i<=n):
#    t=f+s
#    print(t,end=' ')
#    f=s
#    s=t
#    i+=1


#68-Write a program to check whether a given Number is Palindrome or Not.
#n=int(input("\nenter a number:"))
#s=0
#a=n
#while(n>0):
#    d=n%10
#    s=(s*10)+d
#    n=n//10
#if(s==a):
#    print(a,"is palindrome")
#else:
#    print(a,"is not a palindrome")


#69-Write a program to Check whether a given Number is an Armstrong Number.
#n=int(input("\nenter a number:"))
#s=0
#a=n
#while(n>0):
#    d=n%10
#    s=s+(d**3)
#    n=n//10
#if(s==a):
#    print(a,"is armstrong number")
#else:
#    print(a,"is not a armsrtong number") 


#70-Write a program to check weather a given number is prime number or not.
#n=int(input("\nenter a number:"))
#c=0
#i=1
#while(i<=n):
#    if(n%i==0):
#        c+=1
#   i+=1
#if(c==2):
#    print(n,"is prime number")
#else:
#    print(n,"is not a prime number")


#71-Write a program to print all prime numbers from 1-500
#i=1
#while(i<=500):
#    j=1
#    c=0
#    while(j<=i):
#        if(i%j==0):
#            c+=1
#        j+=1
#    if(c==2):
#        print(i,"is prime number")
#    i+=1


#72-Write a program to find the Sum of all prime numbers from 1-1000.
#i=1
#s=0
#while(i<=1000):
#    j=1
#    c=0
#    while(j<=i):
#        if(i%j==0):
#            c+=1
#        j+=1
#    if(c==2):
#        print(i,"is prime number")
#        s+=i
#     i+=1
#print("sum of prime numbers between 1 to 1000 =",s)


#73-Write a program to display the following pattern:
#* * * * *
#* * * * *
#* * * * *
#* * * * *
#* * * * *
#i=1
#while(i<=5):
#    print("* "*5)
#    i+=1
 

#73-METHOD-2
#for i in range(5):
#    for j in range(5):
#        print("*",end=' ')
#    print()


#74- Write a program to display the following pattern:
#*
#* *
#* * *
#* * * *
#* * * * *
#for i in range(5):
#    for j in range(i+1):
#        print("*",end=' ')
#    print()


#75-Write a program to display the following pattern:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
#for i in range(1,6):
#    for j in range(1,i+1):
#        print(j,end=' ')
#    print()


#76-Write a program to display the following pattern:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
#for i in range(1,6):
#    for j in range(1,i+1):
#        print(i,end=' ')
#    print()


#77-Write a program to display the following pattern:
#A
#B B
#C C C
#D D D D
#E E E E E
#ch=65
#for i in range(1,6):
#    for j in range(1,i+1):
#        print(chr(ch),end=' ')
#    ch+=1
#    print()


#78-Write a program to display the following pattern:
#* * * * *
#* * * *
#* * *
#* *
#*
#for i in range(5):
#    for j in range(5):
#        if((i+j)<5):
#            print("*",end=' ')
#    print()
 

#79- Write a program to display the following pattern:
#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1
#for i in range(1,6):
#    for j in range(1,6):
#        if((i+j)<7):
#            print(j,end=' ')
#    print()


#80-Write a program to display the following pattern:
#        *
#      * * *
#    * * * * *
#  * * * * * * *
#* * * * * * * * *

#for i in range(5):
#    k=1
#    for j in range(9):
#        if((i+j)<4):
#            print(" ",end=' ')
#        else:
#            while(k<=(2*(i+1)-1)):
#                print("*",end=' ')
#                k+=1
#            break
#    k+=1
#    print()

#81-Write a program to display the following pattern:
#         1
#       2 3 2
#     3 4 5 4 3
#   4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5
#for i in range(5):
#    m=i+1
#    for j in range(5):
#       if((i+j)<4):
#            print(" ",end=' ')
#    for k in range(i+1):
#        print(m,end=' ')
#        m+=1
#    for l in range(i):
#        m-=2
#        print(m,end=' ')
#    print()
    
    
#82-Write a program to display the following pattern:
#* * * * * * * * *
#  * * * * * * *
#    * * * * *
#      * * *
#        *    
#for i in range(5):
#    for j in range(1,i+1):
#        print(" ",end=' ')
#    for k in range(5,i,-1):
#        print("*",end=' ')
#    for l in range(4,i,-1):
#        print("*",end=' ')
#    print()

#83-Write a program to display the following pattern (Pascal Triangle):
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
#1 5 10 10 5 1
#for i in range(1,6):
#    for j in range(0,6-i+1):
#        print(" ",end=' ')
#    c=1
#    for j in range(1,i+1):
#        print(" ",c,sep=" ",end=' ')
#        c=c*(i-j)//j
#    print()
    
    

#97. Write a program to Find the Sum of A.P Series.
#n=int(input("enter number of terms of A.P.:"))
#a=int(input("enter first term of A.P:"))
#d=int(input("enter common difference of A.P.:"))
#A_n=a+((n-1)*d)
#sum_ap=(n*(a+A_n))/2
#print("sum of A.P.=",sum_ap)
 

#98.Write a program to Find the Sum of G.P Series.
#n=int(input("enter number of terms of G.P.:"))
#r=int(input("enter common ratio of G.P.:"))
#a=int(input("enter first term of G.P.:"))
#sum_gp=(a*((r**n)-1))/(r-1)
#print("sum of G.P.=",sum_gp)

#100.Write a program to print the following sequence of integers.
#1, 2, 4, 8, 16, 32
#n=2
#i=0
#while(i<=5):
#    print(2**i,sep=' ',end=' ')
#    i+=1
 

#101.Write a program to find the Sum of following Series:
#(1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n)
#n=int(input("enter number of terms:"))
#i=1
#s=0
#while(i<=n):
#    s=s+(i*i)
#    i+=1
#print("sum=",s)
    

#102.Write a program to find the Sum of following Series:
#(1) + (1+2) + (1+2+3) + (1+2+3+4) + ... + (1+2+3+4+...+n)
#n=int(input("enter limit:"))
#i=1
#s=0
#while(i<=n):
#    j=1
#    while(j<=i):
#        s+=j
#        j+=1
#    i+=1
#print("sum=",s)
    

#103.Write a program to find the Sum of following Series:
#1! + 2! + 3! + 4! + 5! + ... + n!
#n=int(input("enter limit:"))
#i=1
#s=0
#while(i<=n):
#   j=1
#    f=1
#    while(j<=i):
#        f=f*j
#        j+=1
#    s+=f
#    i+=1
#print("sum=",s)
 
#104.Write a program to find the Sum of following Series:
#(1^1) + (2^2) + (3^3) + (4^4) + (5^5) + ... + (n^n)
#n=int(input("enter limit:"))
#i=1
#s=0
#while(i<=n):
#    s=s+(i**i)
#    i+=1
#print("sum=",s)


#105. Write a program to find the Sum of following Series:
#(1!/1) + (2!/2) + (3!/3) + (4!/4) + (5!/5) + ... + (n!/n)
#n=int(input("enter limit:"))
#s=0
#i=1
#while(i<=n):
#    j=1
#    f=1
#    while(j<=i):
#        f=f*j
#        j+=1
#    s=s+(f/i)
#    i+=1
#print("sum=",s)


#106.Write a program to find the Sum of following Series:
#[(1^1)/1] + [(2^2)/2] + [(3^3)/3] + [(4^4)/4] + [(5^5)/5] + ... + [(n^n)/n]
#n=int(input("enter limit:"))
#s=0
#i=1
#while(i<=n):
#    s=s+((i**i)/i)
#    i+=1
#print("sum=",s)


#107. Write a program to find the Sum of following Series:
#[(1^1)/1!] + [(2^2)/2!] + [(3^3)/3!] + [(4^4)/4!] + [(5^5)/5!] + ... + [(n^n)/n!]
#n=int(input("enter limit:"))
#s=0
#i=1
#while(i<=n):
#    j=1
#    f=1
#    while(j<=i):
#        f=f*j
#        j+=1
#    s=s+((i**i)/f)
#    i+=1
#print("sum=",s)


#108.Write a program to find the Sum of following Series:
#1/2 - 2/3 + 3/4 - 4/5 + 5/6 - ...... upto n terms
#n=int(input("enter limit:"))
#s=0
#i=1
#while(i<=n):
#    if(i%2!=0):
#        s=s+(i/(i+1))
#    else:
#        s=s-(i/(i+1))
#    i+=1
#print("sum=",s)
 

#109. Write a program to print the following Series:
#1, 2, 3, 6, 9, 18, 27, 54, ... upto n terms   
#n=int(input("enter limit:"))
#a=0
#b=1
#c=2
#print(b,c,end=',')
#for i in range(3,n+1):
#    if(i%2==0):
#        d=a+b+c
#    else:
#        d=b+c
#    print(d,end=',')
#    a=b
#    b=c
#    c=d


#110.Write a program to print the following Series:
#2, 15, 41, 80, 132, 197, 275, 366, 470, 587    
#n=int(input("enter limit:"))
#s=2
#j=1
#c=1
#print(s,end=',')
#while(j<=n):
#    s=s+(13*c)
#    print(s,end=',')
#    j+=1
#    c+=1


#111.Write a program to print the following Series:
#1, 3, 4, 8, 15, 27, 50, 92, 169, 311    
#a=1
#b=3
#c=4
#n=int(input("enter limit:"))
#print(a,b,end=',')
#i=4
#s=0
#while(i<=n):
#    s=a+b+c
#    print(s,end=',')
#    a=b
#    b=c
#    c=s
#    i+=1
    
    
#112.Write a program to Convert the given Binary Number into Decimal
#b=int(input("enter a binary number:"))
#s=0
#i=0
#a=b
#while(b>0):
#    d=b%10
#    s=s+(d*(2**i))
#    b=b//10
#    i+=1
#print("decimal number of binary number",a,"is",s)


#113.Write a program to Convert Binary to Hexadecimal.
#b=int(input("enter a binary number:"))
#s=0
#i=0
#a=b
#while(b>0):
#    d=b%10
#    s=s+(d*(16**i))
#    b=b//10
#    i+=1
#print("hexa-decimal number of binary number",a,"is",s)
 

#114.Write a program to Convert Decimal to Hexadecimal
#d=int(input("enter a decimal number:"))
#lst=[]
#while(d>0):
#    n=d%16
#    lst.append(n)
#    d=d//16
#l=len(lst)
#for i in range(-1,-l-1,-1):
#    if(lst[i]=='10'):
#        print('A',end='')
#    elif(lst[i]==11):
#        print('B',end='')
#    elif(lst[i]==12):
#        print('C',end='')
#    elif(lst[i]==13):
#        print('D',end='')
#    elif(lst[i]==14):
#        print('E',end='')
#    elif(lst[i]==15):
#        print('F',end='')
#    else:
#        print(lst[i],end='')

#116.Write a program to Convert Hexadecimal to Binary.
#n=int(input("enter a hexadecimal number:"))
#s=[]

#while(n>0):
#    d=n%10
#    while(d>0):
#        a=d%2
#        s.append(a)
#        d=d//2
#    n=n//10
#    l=len(s)
#    lst=[]
#    for i in range(-1,-l-1,-1):
#        lst.append(s[i])
#    j=len(lst)
#    if(j==3):
#        lst=[0]+lst
#        print("if",lst)
#    elif(j==2):
#        lst=[0,0]+lst
#        print("elif1",lst)
#    elif(j==1):
#        lst=[0,0,0]+lst
#        print("elif2",lst)
#print(lst)
        
    
    
#117.Write a program to Find the Sum of two Binary Numbers.       
        
        
        





#127. Write a Python function to find the Max of three numbers
#def max_three(a,b,c):
#    if(a>b and a>c):
#        print(a,"is largest number")
#    elif(b>a and b>c):
#        print(b,"is largest number")
#    else:
#        print(c,"is largest number")
#a=int(input("enter first number:"))
#b=int(input("enter second number:"))
#c=int(input("enter third number:"))
#max_three(a,b,c)


#128.Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20
#def sum_list(lst):
#    s=0
#    l=len(lst)
#    for i in range(l):
#        s+=lst[i]
#    print("sum of elements of list",lst,"is:",s)
#lst=eval(input("enter a list:"))
#sum_list(lst)


#129.Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336
#def multiply_list(lst):
#    p=1
#    l=len(lst)
#    for i in range(l):
#        p*=lst[i]
#    print("multiplication of elements of list",lst,"is:",p)
#lst=eval(input("enter a list:"))
#multiply_list(lst)



#130.Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"
#def reverse_string(str1):
#    print("reverse of string is",str1)
#    print(str1[::-1])
#str1=input("enter a string:")
#reverse_string(str1)


#131.Write a Python program calculate the factorial of a number using lambda and reduce functions. The
#function accepts the number as an argument.


#132.Write a Python function to check whether a number falls in a given range
#def range_check(n,l,u):
#    for i in range(l,u+1):
#        if(i==n):
#            print(n,"is at position",i,"between the numbers",l,"and",u)
#            break
#n=int(input("enter a number:"))
#l=int(input("enter lower limit:"))
#u=int(input("enter upper limit:"))
#range_check(n,l,u)        


#133.Write a Python function that accepts a string and calculate the number of upper-case letters and
#lower-case letters.
#Sample String: 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12
#def num_upperlower(str1):
#    u=0
#    l=0
#    l1=len(str1)
#    for i in range(l1):
#        if(str1[i]>='A' and str1[i]<='Z'):
#            u+=1
#        elif(str1[i]>='a' and str1[i]<='z'):
#            l+=1
#    print("Number of uppercase alphabets in",str1,"is:",u)
#    print("Number of lowercase alphabets in",str1,"is:",l)
#str1=input("enter a string:")
#num_upperlower(str1)


#134.Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
#def unique_elements(lst):
#    l=len(lst)
#    lst1=[]
#    for i in lst:
#        if(i not in lst1):
#            lst1.append(i)
#    print("list with only unique elements:",lst1)
#lst=eval(input("enter a list of numbers:"))
#unique_elements(lst)


#135.Write a Python function that takes a number as a parameter and check the number is prime or not.
#def prime_check(n):
#    c=0
#    for i in range(1,n+1):
#        if(n%i==0):
#            c+=1
#    if(c==2):
#        print(n,"is a prime number")
#    else:
#        print(n,"is not a prime number")
#n=int(input("enter a number:"))
#prime_check(n)


#136.Write a Python function that checks whether a passed string is palindrome or not
#def reverse_check(str1):
#    str2=""
#    str2=str1[::-1]
#    if(str1==str2):
#        print(str1,"is a palindrome")
#    else:
#        print(str1,"is not a palindrome")
#str1=input("enter a string:")
#reverse_check(str1)


#137.Write a Python function that prints out the first n rows of Pascal's triangle.
#def pascal(n):
#    for i in range(1,n+1):
#        c=1
#        for j in range(1,i+1):
#            print(" ",c,sep=" ",end=' ')
#            c=c*(i-j)//j
#        print()
#n=int(input("enter number of rows of pascal's triangle:"))
#pascal(n)


#138.Write a Python function to check whether a string is a pangram or not.
#Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example: "The quick brown fox jumps over the lazy dog"
#def pangram_check(str1):
#    c=0
#    for i in range(1,27):
#        ch=97
#        str1=str1.lower()
#        if(chr(ch) in str1):
#            c+=1
#        ch+=1
#    print(c)
#    if(c==26):
#        print(str1,"is pangram")
#    else:
#        print(str1,"is not a pangram")
#str1=input("enter a string:")
#pangram_check(str1)
        

#139.Write a Python function that accepts a hyphen-separated sequence of words as input and prints the
#words in a hyphen-separated sequence after sorting them alphabetically.
#Sample Items: green-red-yellow-black-white
#Expected Result: black-green-red-white-yellow
#def hypen(str1):
#    str1=str1.split("-")
#    str1.sort()
#    str1="-".join(str1)
#    print(str1)
#str1="green-red-yellow-black-white"
#hypen(str1)
        
        
#140.Python function to convert height (in feet and inches) to centimeters.    
#def height_converter(f,i):
#    cm=(f*30.48)+(i*2.54)
#    print("Height in centimeters:",cm)
#print("Enter your height:")
#f=int(input("enter feet:"))
#i=int(input("enter inch:"))
#height_converter(f,i)


#141.Python function to Convert Celsius to Fahrenheit.
#def fahrenheit_celcius(c):
#    f=(1.8*c)+32
#    print("Temperature in celcius:",f)
#c=float(input("enter temperature in celcius:"))
#fahrenheit_celcius(c)


#142.Python function to display all the Armstrong number from 1 to n.
#def armstrong_limit(n):
#    for i in range(1,n+1):
#        c=0
#        a=i
#        while(i>0):
#            d=i%10
#            c=c+(d**3)
#            i=i//10
#        if(c==a):
#            print(a,"is armstrong number")
#n=int(input("enter limit:"))
#armstrong_limit(n)


#161.Python program to check whether the string is Symmetrical or Palindrome
#str1=input("enter a string:")
#str2=str1[::-1]
#print("Reverse of string",str1,"is:",str2)



#162.Ways to remove i’th character from string in Python
#str1=input("Enter a string:")
#p=int(input("enter position of character:"))
#print("1.Removing i'th character via slicing from string")
#str2=str1[:i]+str1[i+1:]
#print("string after removing",p,"position element from",str1,"is:",str2)

#print("2.Removing i'th character via looping from string")
#l=len(str1)
#str3=""
#for i in range(l):
#    if(str1[i]==str1[p]):
#        continue
#   else:
#        str3=str3+str1[i]
#print("string after removing",p,"position element from",str1,"is:",str3")


#163.Python program to Check if a Substring is Present in a Given String
#str1=input("Enter a string:")
#str2=input("Enter a substring:")
#if str2 in str1:
#    print("True")
#else:
#    print("False")



#164.Find length of a string in python (4 ways)
#str1=input("Enter a string:")
#print("1.LENGTH OF STRING VIA LEN FUNCTION")
#l=len(str1)
#print("Length of string:",str1,"is:",l)

#print("2.LENGTH OF STRING VIA FOR LOOP")
#c=0
#for i in str1:
#    c+=1
#print("Length of string:",str1,"is:",c)

#print("3.LENGTH OF STRING VIA SLICING")
#d=0
#l1=1
#str2=""
#while str1[l::-1]:
#    if(l!=0):
#        d+=1
#    else:
#        break
#    l-=1
#print(d)

#print("5.LENGTH OF STRING VIA REDUCE LAMBDA FUNCTION")
#import functools
 
#def findLen(string):
#    return functools.reduce(lambda x,y: x+1, string, 0)
 
 
# Driver Code
#string = 'hello'
#print(findLen(string))

#print("6.LENGTH OF STRING VIA SUM FUNCTION")
#def findLen(string):
#    return sum( 1 for i in string);
 
 
# Driver Code
#string = 'geeks'
#print(findLen(string))


print("All this code is written by Anurag\nThank u")
    