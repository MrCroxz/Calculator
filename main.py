def Calculator():
    print("")
    total = 0
    Continue = True

    while Continue:
        if total == 0:
            number1 = float(input("Enter the first number: "))
            total = number1
        else:
            print(f"Current total: {total}")     
            
        operation = input("Choose an operation (+, -, *, /): ")
        
        if operation == 'q':
            Continue = False
            break

        number2 = float(input("Enter the next number: "))
        
        if operation == '+':
            total += number2
        elif operation == '-':
            total -= number2
        elif operation == '*':
            total *= number2
        elif operation == '/':
            if number2 != 0:
                total /= number2
                
            else:
                print("Cannot divide by zero!")
        else:
            print("Invalid!")

        more = input("Want to add more numbers? (yes/no): ")
        if more.lower() != 'yes':
            Continue = False
            
    print(f"Total is: {total}")
    
Calculator()
