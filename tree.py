""" def trees(num, heights):
    inc_list = []
    dec_list = []
    increasing = 1
    decreasing = 1
    for i in range(num - 1):
        if heights[i+1] > heights[i]:
            increasing += 1
            inc_list.append(increasing)
            decreasing = 1
        if heights[i+1] < heights[i]:
            decreasing += 1
            dec_list.append(decreasing)
            increasing = 1
    print(max(inc_list))
    print(max(dec_list)) """

def trees(num, heights):
    inc_list = []
    dec_list = []
    increasing = 1
    decreasing = 1
    for i in range(num - 1):
        if heights[i+1] > heights[i]:
            increasing += 1
            inc_list.append(increasing)
            decreasing = 1
        if heights[i+1] < heights[i]:
            decreasing += 1
            dec_list.append(decreasing)
            increasing = 1
    print(max(inc_list))
    print(max(dec_list))



trees(10, [2, 1, 4 ,6 ,8, 2, 9, 5, 2, 3])
""" trees(4, [1, 3, 4, 2]) """