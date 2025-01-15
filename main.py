while True:
    print("Calculator")
    user_input = (input("Enter the thing here:"))
    
    if "+" in user_input:
        user_input = user_input.split("+")
        
        try:
            num1 = int(user_input[0].strip())
            num2 = int(user_input[1].strip())
            result = num1 + num2
            print(result)
            
        except ValueError:
            print("Invalid")
            
    elif "-" in user_input:
        user_input = user_input.split("-")
        
        try:
            num1 = int(user_input[0].strip())
            num2 = int(user_input[1].strip())
            result = num1 - num2
            print(result)
            
        except ValueError:
            print("Invalid")
            
    elif "x" in user_input:
        user_input = user_input.split("x")
        
        try:
            num1 = int(user_input[0].strip())
            num2 = int(user_input[1].strip())
            result = num1 * num2
            print(result)
            
        except ValueError:
            print("Invalid")
            
    elif "/" in user_input:
        user_input = user_input.split("/")
        
        try:
            num1 = int(user_input[0].strip())
            num2 = int(user_input[1].strip())
            result = num1 / num2
            print(result)
            
        except ValueError:
            print("Invalid") 
    # Hello  