def count_even_numbers(A, B):
    result = []
    
    for i in B:
        start_index, end_index = i[0], i[1]
        count = 0
        
        for j in range(start_index, end_index + 1):
            if A[j] % 2 == 0:
                count += 1
        
        result.append(count)
    
    return result

A = list(map(int,input().split()))
B = eval(input())
output = count_even_numbers(A, B)
print(output) 

