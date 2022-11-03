n=int(input())
for i in range(1,n+1):
    if n%1==0 and i*(i+1)==n:
        print("YES")
        break
else:
    print("NO")