# tabel kebenaran (logika Bolean)
# and or not xor

#NOT
print("*********Logika Not*********")
x = false
y = not x
print("nilai dari x =", x)
print("nilai dari y =", y)

# and (hanya bernilai true, ketika kedua nya true)
# jika ada salah satu saja yang false,maka nilai false
print("\n*********Logika AND*********")
x = False 
y = False
z = x and y
print(x, "and", y, "=", z)

x = False 
y = True
z = x and y
print(x, "and", y, "=", z)

x = True 
y = False
z = x and y
print(x, "and", y, "=", z)

x = True 
y = True
z = x and y
print(x, "and", y, "=", z)


# or (akan bernilai true selama ada satu saja yang true)
# bernilai salah ketika kedua nya salah
print("\n************Logika OR************")
x = False 
y = False
z = x and y
print(x, "or", y, "=", z)

x = True 
y = False
z = x and y
print(x, "or", y, "=", z)

x = False 
y = True
z = x and y
print(x, "or", y, "=", z)

x = True 
y = True
z = x and y
print(x, "or", y, "=", z)









