print("Let's do some division!")

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    result = a / b
    print("Result is:", result)

except ValueError:
    print("❌ Oops! Please enter numbers only. ")

except ZeroDivisionError:
    print("❌ You cannot divide by zero!")

finally:
    print("✅ Program finished. Thank you!")