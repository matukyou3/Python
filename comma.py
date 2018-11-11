def comma(a):
    for i in range(len(a)-1):
        print(str(a[i])+',',end=' ')
    print('and ' + str(a[-1]))

numbers = [1,5,326,643,15432,6743,1542,634,2,547354,8]
spam = ['apples','bananas','tofu','cats']
comma(spam)
comma(numbers)
