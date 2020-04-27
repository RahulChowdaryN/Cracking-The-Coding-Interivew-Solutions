def rotate_matrix(arr):

    # for i in range(len(arr)):
    #     for j in range(i,len(arr)):
    #             arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    #
    #
    # for i in arr:
    #     for j in range(len(i)//2):
    #         i[j] , i[len(i)-j-1] =  i[len(i)-j-1],i[j]
    #
    # return arr

    for i in range(len(arr)):
        for j in range(i):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    for i in arr:
        for j in range(len(i)//2):
            i[j],i[len(i)-j-1] = i[len(i)-j-1],i[j]
    return arr


print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))