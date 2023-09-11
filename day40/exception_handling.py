try:
    # Code that may raise an exception
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))
    result = num1 / num2

except ZeroDivisionError:
    # Handle division by zero exception
    print("Error: Division by zero!")

except ValueError:
    # Handle invalid input (non-integer) exception
    print("Error: Invalid input. Please enter valid integers.")

else:
    # Code in this block is executed if no exception is raised
    print(f"Result of division: {result}")

finally:
    # Code in this block is always executed, whether an exception occurred or not
    print("Execution completed.")

# Rest of the program
print("Program continues after exception handling.")
