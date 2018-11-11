import sys
def collatz(number):
    while number>1:
        if number % 2 ==1:
            number = 3 * number +1
        else:
            number =  number /2
        print(int(number))

try:
    number= int(input())
    collatz(number)
except:
    print("Error faild Input your number!!!")



