def getBingoNumber(matrix, nums):
    bingo = [list() for i in matrix]
    for i in range(len(matrix[0])):
        bingo[i] = [0 for x in matrix[0]] 
    cols = [*zip(*bingo)]
    cols = [list(x) for x in cols]
    for num in nums:
        ans = find(matrix, num)
        bingo[ans[0]][ans[1]] = 1
        print(f"Element found at index: [{ans[0]} {ans[1]}]")
        rowbingo = [all(y) for y in bingo]
        colbingo = [all(x) for x in cols]
        # print(rowbingo)
        # print(colbingo)
        if any(rowbingo):
            return matrix[ans[0]][ans[1]]
        if any(colbingo):
            return matrix[ans[0]][ans[1]]

def find(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (arr[i][j] == target):
                return [i, j]
    return [-1, -1]

mat = [[3,1,8], [4,6,2],[7,5,9]]
arr = [5,4,8,6,1,7,9,2,3]
print(getBingoNumber(mat,arr))