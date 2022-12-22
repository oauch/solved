a, b = input().split()

result = 0
int_a = int(a, 2)
int_b = int(b, 2)

result = int_a + int_b

print(bin(result)[2:])