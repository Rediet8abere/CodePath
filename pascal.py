def pascal_triangle(numRows):
    pascal_list = [[] for _ in range(numRows)]
    print("pascal_list: ", pascal_list)
    for i in range(numRows):
        for j in range(i+1):
            if i == j:
                pascal_list[i].append(1)
            elif j == 0:
                pascal_list[i].append(1)
            else:
                pascal_list[i].append(pascal_list[i-1][j-1] + pascal_list[i-1][j])
    print()
    print("pascal_list: ", pascal_list)

pascal_triangle(5)
