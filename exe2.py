email = input("Lütfen bir email giriniz")
check = []
for x in email:
    check.append(x)
x = '@'
y = '.'
if check.count(x) == 1 and check.count(y) >= 1 :
    print("Bu, geçerli bir emaildir.")
else:
    print("Bu, geçerli bir email değildir.")