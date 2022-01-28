def get_values(course_size, sheep_sizes):
    sum = 0
    values = []
    for index in range(len(sheep_sizes)):
        if sum + sheep_sizes[index] <= course_size:
            sum+= sheep_sizes[index]
            values.append(sheep_sizes[index])   
    return values

def recursion_func(course_size, course_limit, sheep_sizes):
    sheep_sizes_copy = sorted(sheep_sizes, reverse = True)
    for i in range(course_limit): 
        sum_values = get_values(course_size, sheep_sizes_copy)
        for value in sum_values:
            sheep_sizes_copy.remove(value)           
    if sheep_sizes_copy:
        recursion_func(course_size + 1, course_limit, sheep_sizes)
    else:
        return print(course_size)
         
    
nk = list(map(int, input().split()))

while(len(nk) != 2 or [i for i in nk if i <= 0]):
    print("Incorrect input:")
    nk = list(map(int, input().split()))

sheep_sizes = list(map(int, input().split()))

while(len(sheep_sizes) != nk[0] or [i for i in nk if i <= 0]):
    print("Incorrect input:")
    sheep_sizes = list(map(int, input().split()))
    
recursion_func(max(sheep_sizes), nk[1], sheep_sizes)
    