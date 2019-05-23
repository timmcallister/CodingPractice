#Solution for problem:
#https://practice.geeksforgeeks.org/problems/count-the-triplets/0

tests_input = int(input())

sum_input, array_input = ([] for i in range(2))

for i in range(tests_input):
    sum_input.append(int(input()))
    array_input.append(list(map(int, input().split())))

for ind in range(tests_input):
    triplets = -1
    size = len(array_input[ind])
    for i in array_input[ind]:
        for j in array_input[ind][array_input[ind].index(i)+1:]:
            for k in array_input[ind]:
                if k == i or k == j:
                    continue
                if i+j==k:
                    if triplets == -1:
                        triplets = 1
                    else:
                        triplets += 1
    print(triplets)
                    
                    
        
