a=input("a:")
b=input("b:")
print("Değiştirilmeden önceki değer\na: {} b: {}\n".format(a,b))

a,b=b,a
print("Değiştirildikten sonraki değer\na: {} b: {}\n".format(a,b))