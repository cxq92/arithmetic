
# 归并
def merge(A, p, r, q):
    '''
    #该段代码主要是为了对列表A的部分元素进行分两组来归并，每次取两组最小的元素进行归并
    #param A: 表示list
    #param p: 列表需要归并的数据中最小的标注
    #param r: 列表需要归并的数据中最大的标注
    #param q: 列表需要归并的数据中进行切分的标注
    #return: 返回归并的listA
    '''
    n1 = q - p + 1  # 序列 1 的个数
    n2 = r - q  # 序列 2 的个数
    # print(n1)
    L = []
    R = []
    for i in range(0, n1):
        L.append(A[i + p])

    for j in range(0, n2):
        R.append(A[j + q + 1])
    L.append(float("inf"))  # float("inf")表示正无穷, float("-inf")表示负无穷
    R.append(float("inf"))  # 这两行是给出结束条件
    #print(L)
    #print(R)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            #print(A[k])
            i += 1
        else:
            A[k] = R[j]
            #print(A[k])
            j += 1
    return (A)

# 归并排序
def mergesort(A, p, r):
    '''
    对列表A的部分元素进行归并排序。
    归并排序是将列表需要排序的数据首先全部拆成一个个单独的数，在一层层归并回去
    :return: 返回需要部分排序好的A
    '''
    if p < r:
        q = int((p + r) / 2)
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, r,q )
        print(merge(A, p, r,q ))
    return(A)

A = [3,1,5,2,1,6,4,6]
print(mergesort(A,0,3))

# #过程展示
# mergesort(A,0,3),[3,1,5,2],p=0,r=3
#     mergesort(A, 0, 1) [3,1]
#         mergesort(A, 0, 0) [3] #递归到这一步，无法继续递归，就接着下面第49行代码执行
#         mergesort(A, 1, 1) [1] #递归到这一步，无法继续递归，就接着下面第50行代码执行
#         merge(A, 0, 1,0 )
#         return A  [1,3,5,2,1,6,4,6]
#     mergesort(A, 2, 3) [5,2]
#         mergesort(A, 2, 2) [5] #递归到这一步，无法继续递归，就接着下面第49行代码执行
#         mergesort(A, 3, 3) [2] #递归到这一步，无法继续递归，就接着下面第50行代码执行
#         merge(A, 2, 3,2 )
#         return A  [1,3,2,5,1,6,4,6]
#     merge(A, 0, 3,2 )
#     return(A) [1,2,3,5,1,6,4,6]



#上面对A列表进行部分的数据进行一个排序，下面写的是一个对整个list的归并排序。
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist   #注意不是continue ,在递归嵌套执行的时候，走到list切分为一个个值的时候，此时要返回元素
    mid = n // 2
    #left 采用归并排序后形成的有序的新的列表
    left = merge_sort(alist[:mid])  # 不包含alist[mid]元素
    # right 采用归并排序后形成的有序的新的列表
    right = merge_sort(alist[mid:])
    # 将两个有序的子序列合并为一个新的整体
    left_pointer ,right_pointer = 0,0
    result = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result += left[left_pointer:]
    result += right[right_pointer:]
    return result

if __name__ == '__main__':
    li = [3,1,5,2,1,6,4,6]
    print(li)
    sorted_list = merge_sort(li) #由于该程序返回的是result，重新定义的，故而要有变量接收该结果 ，会有空间上的额外开销
    print(sorted_list)

# #过程展示
# merge_sort(li)  li = [3,1,5,2,1,6,4,6] ,n = 4,
# left = merge_sort([3,1,5,2])  n =2,
#     left = merge_sort([3,1]) #拿到left的结果resul
#         left = merge_sort([3])  #第64行运行结束，返回3，接下来运行第66行
#             return [3]
#         right = merge_sort([1]) #返回1，继续下面的程序
#             return [1]
#         result = [1,3]
#         return result
#     right = merge_sort([5,2])
#         left = merge_sort([5])#第64行运行结束，返回5，接下来运行第66行
#             return [5]
#         right = merge_sort[2] #返回2，继续下面的程序
#             return [2]
#         result = [2,5]
#         return result
#     result = [1,2,3,5]
#     return result
# right = merge_sort([1,6,4,6])
#     left = merge_sort([1,6])
#         left = merge_sort([1])
#             return [1]
#         right = merge_sort([6])
#             return [6]
#         result = [1,6]
#         return result
#     right = merge_sort([4,6])
#         left = merge_sort([4])
#             return [4]
#         right = merge_sort([6])
#             return [6]
#         result = [4,6]
#         return result
#     result = [1,4,6,6]
#     return result
# result = [1, 1, 2, 3, 4, 5, 6, 6]
# return result

#最优时间复杂度O(nlogn)
#最坏时间复杂度O(nlogn)
#稳定性：稳定
