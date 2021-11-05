N = int(input("Bir sayı giriniz"))
even = [x for x in range(2, N + 1, 2)]
odd = [x for x in range(1, N + 1, 2)]
print(sum(odd))
print(sum(even) / len(even))