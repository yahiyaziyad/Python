ok='yes'
while ok=='yes':
    
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    print("Pick Operation To Perform :")

    operation = int(input())


    if operation == 1:

        num1 = input("Enter first number : ")
        num2 = input("Enter second number : ")
        print("The Sum is = "+str(int(num1)+int(num2) ))

    elif operation == 2:

        num1 = input("Enter first number : ")
        num2 = input("Enter second number : ")
        print("The Diff is = "+ str(int(num1)-int(num2)))

    elif operation == 3:

        num1 = input("Enter first number : ")
        num2 = input("Enter second number : ")
        print("The Product is = "+ str(int(num1)*int(num2)))

    elif operation == 4:

        num1 = input("Enter first number : ")
        num2 = input("Enter second number : ")
        print("The Quotient is = "+str(int(num1)/int(num2)))

    else:
        print("##invalid##")
    ok=input('do you wnt to continue (yes/no)')