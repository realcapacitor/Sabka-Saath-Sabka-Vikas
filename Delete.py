def func1(var1, var2):
    counter = 0
    if var1 == 1:
        counter+=var2/2
        return 0
    elif(var1%2):
        return counter+func1(var1//2, 2*var2)+var2
    else:
        counter+=2
        return counter+func1(var1//2, 2*var2)-var2
print(func1(20,1))