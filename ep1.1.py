
a = float(input("Enter  a: "))
b = float(input("Enter  b: "))
c = float(input("Enter  c: "))
t = float(input("Enter time t : "))
T = a * t**2 + b * t + c
if t >0:
   print(f"At {t} hours, the temperature is {T}°C.")
else:
  print("error")