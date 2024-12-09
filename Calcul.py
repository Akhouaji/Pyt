def calculator(num_1, num_2):
    if user_choice == 1:
        result = num_1 + num_2
        return result
    elif user_choice == 2:
        result = num_1 - num_2
        return result
    elif user_choice == 3:
        result = num_1 * num_2
        return result
    elif user_choice == 4:
        if num_2 == 0:
            print("Error, Zou cannot devide by Zero")
        else:
            result = num_1	/ num_2 
            return result
    else:
        print("Your input is invalid")

print("1) + \n2) - \n3) *\n4) /")
user_choice = int(input("What operator do you want to use? "))
x = float(input("Enter The First Number: "))
y = float(input("Enter The Second Number: "))
print("Result:" ,calculator(x, y))