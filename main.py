a = int(input("Введите первое число:"))
b = input("Введите оператора для математической операции:")
c = int (input("Введите второе число:"))
if b == "+":
 print ("Ответ =",a + c)
elif b == "-":
 print ("Ответ =",a - c)
elif b == "*":
 print ("Ответ =",a * c)
elif b == "/":
 print ("Ответ =",a / c)
elif b == "//":
 print ("Ответ =",a // c)
elif b == "%":
 print ("Ответ =",a % c)
elif b == "**":
 print ("Ответ =",a ** c)
elif b == "=":
 print ("Ответ =",a = c)