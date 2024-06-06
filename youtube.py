# print("q1) Find the common letters of the given two strings...")
# def common():
#     str1=input("enter the string1:")
#     str2=input("enter the string2:")
#     obj1=set(str1)
#     obj2=set(str2)
#     print(obj1)
#     print(obj2)
#     res=obj1 & obj2
#     print("the common letters are:",res)
# if(__name__=="__main__"):
#     common()    



# print("q2) find the freqeuncy of strins(count the number of strins which is how many)")
# def frequency():
#     str1=input("enter the string object:")
#     li=str1.split()
#     d1={}
#     for x1 in li:
#         if x1 not in d1.keys():
#             d1[x1]=0
#         d1[x1]=d1[x1]+1
#     print(d1)
# frequency()   


# print("--------------or---------------------")
 
# from collections import Counter
# str1=input("enter the string object:")
# str2=str1.split()
# obj1=Counter(str2)
# print("the number of elemets in the list are:",obj1)   



# print("combine two lists into a Dictionary...")
# def dict1():
#     str1=['naina','keemi','reena','pushpa']
#     str2=[1000,2000,3000,4000]
#     res=dict(zip(str1,str2))
#     print(res)
# dict1() 



# print("find the sum of two numbers to add we get the 17 as a value.")
# def case1(array,target):
#     array.sort()
#     left=0
#     right=len(array)-1
#     while(left<right):
#         if (array[left]+array[right]>target):
#             right=right-1
#         if(array[left]+array[right]<target):
#             left=left+1
#         if(array[left]+array[right]==target):
#             print("the numbers are:",array[left],array[right])
#             right=right-1
#             left=left+1
# array=[1,8,9,3,4,22,18,17,16,24] 
# sum=17          
# case1(array,sum)
                    
                    
# print("print swap tow numbers for ex:x=10,y=20 to x=20,y=10 by using two ways") 
# print("by using temparory variable ....")
# def case1():
#     x=10
#     y=20
#     temp=x
#     x=y
#     y=temp
#     print()
#     print("the value of x after swapping:",x)
#     print("the value of y after swapping:",y)
# if(__name__=="__main__"): 
#     case1()
    
           
# print("without using temparory variable")
# def case2():
#     x=10
#     y=20
#     x,y=y,x
#     print()
#     print("the value of x after swapping is:",x)
#     print("the value of y after swapping is:",y)
# if (__name__=="__main__"):
#     case2()    
            

# print("Q)write a pyhton program to swap  first and last elements in the list  numbers in the list")
# print("by using temp variable")
# def test_case1():
#     l1=[10,20,30,40,50,60,70,80]
#     temp=l1[0]
#     l1[0]=l1[-1]
#     l1[-1]=temp
#     print("the list after swapping is:",l1)
# if (__name__=="__main__"):    
#     test_case1()    
      
# print("without using temp variable")
# def case1():
#     l1=[10,20,30,40,50,60,70,80]
#     l1[0],l1[-1]=l1[-1],l1[0]   
#     return "the numbers after swapping is:",l1
# if(__name__=="__main__"):
#     print(case1())    


# def case1():
#     l1=[12,13,14,15,16,17,18,19]
#     tuple=(l1[-1],l1[0])
#     l1[0],l1[-1]=tuple 
#     print("the list after swapping is:",l1)
# case1()      


# print("Q) Swap any two numbwrs from the list by using two methods")
# def test_Case1():
#     list=[12,14,19,2,9]
#     print("list before swapping:",list)
#     temp=list[1]
#     list[1]=list[-1]
#     list[-1]=temp
#     print("the list after swapping is",list)
# if(__name__=="__main__"):
#     test_Case1()
         
         
# print("by using method 2 is")
# def case1():
#     list=[12,191,11,9,23]
#     print("list before swapping:",list)
#     list[1],list[-1]=list[-1],list[1]  
#     print("the list is after swapping is:",list)
# if(__name__=="__main__"):
#     case1()           



# print("find out wether the given number is a prime or not and count the factors also")
# def test_Case1():
#     number=eval(input("input enter the number:"))#5
#     count=0
#     if number > 1:
#         for x1 in range(1,number+1):
#             if (number%x1==0):
#                 count=count+1
#         if (count==2):
#             print(number,"it is a prime number")
#         else:
#             print(number,"it is not a prime number")
#     print("the numer of factors are:",count)            
# test_Case1()            


            
            
# print("Q)write the facorial of a number using two methods.")
# def case1():
#     factorial=1
#     num=int(input("enter the number what you want:"))
#     if num<0:
#         print("the factorial is does not exist")
#     elif(num==0) or (num==1):
#         print("the factorial is 1")
#     else:
#         for x1 in range(1,num+1):
#             factorial=factorial*x1 
#         print("the facotial of",num,"is",factorial)
# if (__name__=="__main__"):
#     case1() 



# print("factorial of a funtion by writing recursive funtion")
# def factorial(num):
#     if(num==0 or num==1):
#         return 1
#     else:
#         return num*factorial(num-1)
# num=10    
# print("the factorial of",num,"is",factorial(num))
    
    
# def factorial(num):
#     if (num<0):
#         return "factorial is not applicable"
#     elif(num==0 or num==1):
#         return 1
#     else:
#         return num * factorial(num-1)
# if (__name__=="__main__"):
#     num=6
#     print("the facotial of",num,"is",factorial(num))   


# print("Q) find the fibonacci series of a number:")
# def fibnacci(num):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for x1 in range(2,num+1):
#         c=a+b
#         print(c)
#         a=b
#         b=c
#     print() 
# num=11    
# fibnacci(num)     

# print("Q) find the sum of elements in a array")
# def test_case1():
#     l1=[1,2,3,4,5,6,7]
#     sum=0
#     for x1 in l1:
#         sum=sum+x1
#     print("the sum of elements in a list is:",sum)    
# test_case1()    
  
  
# print("Q) find the maximum and minimum number of an array")
# def case1(array):
#     array.sort()
#     print("the maximum number of an array is:",array[-1])
#     print()
#     print("the minimum number of an array is:",array[0])
#     print()
# if (__name__=="__main__"):
#     array=[12,14,1,2,19,29,3,98,23,11,14,8,21]
#     case1(array)  




# print("write a python script to sort the list of elements in a list with out using sort keyword")
# l1=[100,29,49,13,144,19,36,19,27]
# for x1 in range(0,len(l1)):
#     for y1 in range(x1+1,len(l1)):
#         if l1[x1]>=l1[y1]:
#             l1[x1],l1[y1]=l1[y1],l1[x1]
# print()
# print(l1)            


# print("descending order ")
# l1=[100,29,49,13,144,19,36,19,27]
# for x1 in range(0,len(l1)):
#     for y1 in range(x1+1,len(l1)):
#         if l1[x1]<=l1[y1]:
#             l1[x1],l1[y1]=l1[y1],l1[x1]
# print()
# print(l1)            


# print("find the wether the string is polyndrom or not")
# def test_case1():
    
#     str=input("enter the string from the keyboard:")
#     if (str[::]==str[::-1]):
#         print(str,"the  given string is a polyndrom")
#     else:
#         print(str,"the given string is a not a polyndrom.... ")    
# if (__name__=="__main__"):
#     test_case1()     



# def test_case1():
#     number=int(input("enter a number:"))
#     str1=str(number)
#     if (str1[::]==str1[::-1]):
#         print(str1,"the  given string is a polyndrom")
#     else:
#         print(str1,"the given string is a not a polyndrom.... ")    
# if (__name__=="__main__"):
#     test_case1()   


# print("find the number of vowels in the given string")
# print("find the vowels and consonents in the given program ")
# def case1():
#     str1=input("enter the string:") 
#     vowels=0
#     consonents=0
#     for x1 in str1:
#         if x1 in "AEIOUaeiou":
#             vowels+=1
#     print("the number of vowels in a given string is:",vowels)
#     for x2 in str1:
#         if x2 not in "AEIOUaeiou":
#             consonents=consonents+1
#     print("the number of consonents are:",consonents)
# if(__name__=="__main__"):
#     case1()                

for x1 in range(5):
    for x2 in range(5-x1):
        print("*",end=" ")
    print()    
print( )
        
  
# print("Q)find the length of the list")                
# l1=[10,20,30,40,50,12,13,14,15]
# l2=len(l1)
# print("the length of the using len()method  is:",l2)


# print("length of the list without using len () method:")
# l1=[1,2,3,4,5,6,7,8,9,10]
# count=0
# for x1 in l1:
#     count=count+1
# print("the length of the list is:",count)
# print()    



# print("Q)) write a program to remove the repeted words from the list")
# l1=["Greeks","for","Greeks"]
# print(l1)
# set1=set(l1)
# l2=list(set1)
# print("the list is after operations",l2)

# l1=["anil","likes","apples","and","prashanth","also","likes","apples"]
# l2=[]
# for x1 in l1:
#     if x1 not in l2:
#         l2.append(x1)
# print("the list after operations are:",l2)
# print()        



# print("Q) fing the element in the gien list")
# def case1():
#     list=[12,13,14,151,5,15,19,22,39,90,25]
#     element=13
#     for x1 in list:
#         if(x1==element):
#             print(element,"the elemet is found.....")
#             break
#     else:
#         print(element,"the element is not found")    
# if (__name__=="__main__"):
#     case1()


# print("by using in operator")
# def case1():
#     l1=[12,123,1414,133,151,90]
#     element=901
#     if (element in l1):
#         print(element,"the elemet is in  the list")
#     else:
#         print(element,"the elemet is not in the list")   
        
# if(__name__=="__main__"):
#     case1()         
            
            
# print("Q)))write a  python  program to clear the list by using four approches..")
# def case2():
#     l1=[1,2,3,5,6,7,8,9,10]
#     print("my list before operations",l1)
#     l1.clear()
#     print("my list after the operations is:",l1)
# if(__name__=="__main__"):
#     case2()    
             
             
# def case1():
#     l2=[23,24,25,26,29]
#     print("the list before operations:", l2)
#     l2=[]
#     print("my list after the operations",l2)
# if(__name__=="__main__"):
#     case1()
    
# def case3():
#     l3=[12,13,14,151,51,24,44,32,2]
#     print("my list before operations is:",l3)
#     l3 *=0
#     print("my list after the operations is:",l3)
# if(__name__=="__main__"):
#     case3()
    
    
# def case4():
#     l4=[12,121,122,123,124,144,155,15]
#     print("my list before operations",l4)
#     del l4[:]
#     print("my list after the operations is:",l4)
# if(__name__=="__main__"):
#     case4()        
                   
# print("Q))) write a pyhton progrm to reverse a string by using two methods")                   
# def case1():
#     l1=[1,2,3,4,5,6,7,8,9,10] 
#     print(l1)
#     print(l1[::-1])
# if(__name__=="__main__"):
#     case1()                                                     

# print("Q)))==========write the reverse of the list=====================")
# def case1():
#     l1=[10,20,30,40,50,60,70]
#     print("the list before operations is:",l1)
#     l1.reverse()
#     print("the list after operations is:",l1)
# if(__name__=="__main__"):
#     case1()



# print("by using slice operator")
# def case1():
#     l1=[10,20,30,50,40,80]
#     print("the list before operations",l1)
#     print("the list after operations is",l1[::-1])
# print()
# if(__name__=="__main__"):
#     case1()    


# print("Q))) ===============Copy the list using five methods==========================")
# l1=[1,2,3,4,5,6,7,8,9]
# obj1=l1.copy()
# print("the list is:",obj1)     


print("by using the slice method")
# l1=[1,2,3,4,5,6,7,8,9]
# obj1=l1[:]
# print(obj1)

# print("using extend method")
# l1=[]
# l2=[1,2,3,4,5,6,7,8,9]
# l1.extend(l2)
# print(l1)


# l1=[1,2,3,4,5,6,7,8,9]
# obj1=list(l1)
# print(obj1)


# print("given a list count the number of times of the given number")
# l1=[1,2,3,3,3,33,14,15,15,13,23,3,233,19,20,22,223,4,3,29,10]
# number=3
# count=0
# for x1 in l1:
#     if(x1==number):
#         count=count+1
# print("the number 3 is repeted in the list is :",count)
# print()        


# from collections import *
# l1=[10,20,30,40,50,60,70,10,10,20,30,40]
# obj1=Counter(l1)
# print("the number of element in the list with count is:",obj1)



# print("Q)))================the sum of elemet in the list=========================")
# def case1():
#     l1=[1,2,3,4,5,6,7,8,9,10]
#     sum=0
#     for x1 in l1:
#         sum=sum+x1
#     print("the sum of values are:",sum)
# if(__name__=="__main__"):
#     case1()
    
    
# print("======or=======")
# l1=[1,2,3,4,5,6,7,8,9,10]
# l2=sum(l1)
# print("the sum of number in the list is:",l2)
# print()


# print("or")
# import numpy 
# list=[1,2,3,4,5]
# res=numpy.sum(list)
# print("the product of the elements are:",res)
# print()


# print("how to multiply all  the numbers in a list")
# l1=[1,2,3,4,5]
# sum=1
# for x1 in l1:
#     sum=sum*x1 
# print("the product of all the numbers in  list is:",sum)
# print()              




    # import numpy 
    # list=[1,2,3,4,5]
    # res=numpy.prod(list)
    # print("the product of the elements are:",res)
    # print()
    
    
# print("Q)))  The largest and smallest elemet in the list in the list")
# def case1():
#     l1=[1011,201,310,140,150,620,100]
#     l1.sort()
#     print("the smallest elemet in  the list is:",l1[0])
#     print("the lergest elemt of the list is:",l1[-1])
# if(__name__=="__main__"):
#     case1()     
       
# print("another method")
# def case1():
#     l1=[1,19,22,0,29,38,498,21,1]
#     print("the smallest elemetnt in the list is:",min(l1))
#     print("the maximum element in the list is:",max(l1))
# if(__name__=="__main__"):
#     case1()           



print("Q)))==============Find the second largest number in the given list================")
# def k1():
#     l1=[10,29,39,49,59,60]
#     print(l1)
#     l1.remove(max(l1))
#     print("the second maximum number in the list is",max(l1))
#     print()
# if(__name__=="__main__"):
#     k1()    


# print("or")
# def case1():
#     l1=[1,2,3,4,12,11,20,33,12,11,223,4,223344,2334]
#     l1.sort()
#     print(l1)
#     print("the second largest maximum number is:",l1[-2])
# if(__name__=="__main__"):
#     case1()   



# print("Q)) find the given string is polyndrom or not") 


# print("Q)) find the given string is polyndrom or not ")
# def case1():
#     str1=input("enter a string object:")
#     print(str1)
#     if(str1==str1[::-1]):
#         print(str1,"it is a polyndrom")
#     else:
#         print(str1,"it is not a polyndrom....")
# if(__name__=="__main__"):
#     case1()             



# def case1():
#     number=142142
#     str1=str(number)
#     print(str1)
#     if(str1==str1[::-1]):
#         print(str1,"it is a polyndrom")
#     else:
#         print(str1,"it is not a polyndrom....")
# if(__name__=="__main__"):
#     case1()             


# print("check wether the given string is a polyndrom or not without using sliceing")
# str1="anilrasa"
# str2=""
# for x1 in str1:
#     if x1  not in str2:
#         str2=x1+str2
#     print()    
# print("str 2 is:",str2)    



# print("Q))) reverse of a sting objects from the given strings") 
# str1="welcome to python programming language"
# str2=str1.split()
# temp=str2[0]
# str2[0]=str2[-1]
# str2[-1]=temp 
# print(str2)
# str3=" ".join(str2)
# print(str3)
        


# str1="welcome to python  programming language"
# str2="python"
# str3=str1.split()
# for x1 in str3:
#     if (x1==str2):
#         print(str2," is presented in the given string")
#         break
#     print()
# else:
        
#     print(str2,"it is not presented in the given string....")
# print()         


print("Q))) find length of the string by using five methods...")

# str1="welcome"
# print("the length of the string is:",len(str1))

# str1="welcome"
# count=0
# for x1 in str1:
#     count=count+1
# print("the length of the string is:",count)
# print()



# str1="welcome"
# count=0
# a=0
# while(a<len(str1)):
#     count=count+1
#     a+=1
# print("the length of the string is:",count)
# print()  


import re
str1="welcome@#!$%^&*()"
obj1=re.compile("@#$%^&")
if(obj1.search(str1)==None):
    print("there is a special characters in the code ")
else:
    print("no special characters in the code...")
print()          