# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}

# num1 = int(input("Enter number1 "))
# num2 = int(input("Enter number2 "))
#
#
# maximum = max(num1,num2)
# print("maximum is" , maximum)
# power = pow(num1 , num2)
# print("power is" ,power)
# print("sum is :", num1+num2)
# print("sub is :",  num1-num2)
# print("mul is :",num1*num2)
# print("div is:" , num1/num2)

num1 = int(input("Enter number1 "))
num2 = int(input("Enter number2 "))

maximum = max(num1, num2)
print(f"{"maximum is"} = {maximum}")
power = pow(num1, num2)
print(f"{"power is"}= {power}")
print(f"{"sum is"}= {num1 + num2}")
print(f"{"sub is :"} ={num1 - num2}")
print(f"{"mul is :"}, {num1 * num2}")
print(f"{"div is:"}, {num1 / num2}")
