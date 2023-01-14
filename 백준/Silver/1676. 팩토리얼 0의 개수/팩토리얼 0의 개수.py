import math

N = int(input())
count = 0

fn = math.factorial(N)
fn = str(fn)
reverse_fn = fn[::-1]

for i in reverse_fn:
    if i == '0':
        count += 1
    else:
        break
print(count)