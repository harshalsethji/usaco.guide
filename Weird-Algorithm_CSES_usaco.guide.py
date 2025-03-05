n = int(input())
answer = ""
while n != 1:
    answer = answer + (str(int(n)))+" "
    if n%2 == 1:
        n = (3*n)+1
    else:
        n = n/2
answer = answer + (str(int(n)))+" "
if n%2 == 1:
    n = (3*n)+1
else:
    n = n/2
print(answer)