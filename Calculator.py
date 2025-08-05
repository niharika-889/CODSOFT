
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

print("\nChoose an operation")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice=input("Enter your choice (1/2/3/4): ")
if choice=='1':
    result=num1+num2
    operation="+"
elif choice=='2':
    result=num1-num2
    operation="-"
elif choice=='3':
    result=num1*num2
    operation="*"
elif choice=='4':
    if num2!=0:
        result=num1/num2
        operation="/"
    else:
        result="Undefined (cannot divide by zero)"
        operation="/"
else:
    result="Invalid choice"
    operation="?"
print(f"\nResult: {num1} {operation} {num2} = {result}")



