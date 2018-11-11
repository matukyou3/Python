import random
secret_number = random.randint(1,20)

for i in range(1,7):
    num = int(input())
    if num < secret_number:
        print("Small Number!")
    elif num > secret_number:
        print("Big Number!")
    else:
        break
    
if num == secret_number:
    print("Success!!! times " + str(i))
else:
    print("Faild Answer is"+ str(secret_number))


