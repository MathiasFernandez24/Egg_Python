suma = 0
for num in range(0, 101):
    if num % 2 == 1:
        suma += num
        print(num, suma)
else:
    print(f"Total sumado: {suma}")
