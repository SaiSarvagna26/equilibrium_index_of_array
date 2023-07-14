list_a=list(map(int,input().split()))
total=sum(list_a)
counter=0
for i in range(len(list_a)):
    total-=list_a[i]
    if counter==total:
        print(i)
        break
    counter+=list_a[i]
else:
    print(-1)
