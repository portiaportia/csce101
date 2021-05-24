#learn various for loops
# loop from 1 to 10, then 
# from 2 to 20
# from 10 down to 1

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
for i in range(1,11):
    if i == 10:
        print(i)  # print on 1 line
    else:
        print(f"{i}, ", end = "")  # print on 1 line
