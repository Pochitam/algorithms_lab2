import bisect
from persistenTree import PersistentTree, Node
import sys

sys.setrecursionlimit(300000)


def pereborchik(arr, x, y):
    count = 0
    for reqtan in arr:
        if reqtan[0][0] <= x < reqtan[1][0] and reqtan[0][1] <= y < reqtan[1][1]: count += 1 
    return count

def karta_prepare(arr):
    arr_x = []
    arr_y = []
    for req in arr:
        arr_x.extend([req[0][0], req[1][0]])
        arr_y.extend([req[0][1], req[1][1]])
    arr_x, arr_y = sorted(set(arr_x)), sorted(set(arr_y))

    if len(arr_x) < 2 or len(arr_y) < 2:
        return [[0]], arr_x, arr_y
    
    xn, yn = len(arr_x), len(arr_y)
    dct_x, dct_y = {arr_x[i]:i for i in range(xn)}, {arr_y[i]:i for i in range(yn)}
    matrix = [[0 for _ in range(xn)] for _ in range(yn)]
    for req in arr:
        for y in range(dct_y[req[0][1]], dct_y[req[1][1]]):
            for x in range(dct_x[req[0][0]], dct_x[req[1][0]]):
                matrix[y][x] += 1
    return (matrix, arr_x, arr_y)
    
def karta(matrix, arr_x, arr_y, x, y):
    if not arr_x or not arr_y or not matrix: return 0
    x_place, y_place = bisect.bisect_right(arr_x, x)-1, bisect.bisect_right(arr_y, y)-1
    if x_place < 0 or y_place < 0: return 0
    if x_place >= len(arr_x) - 1 or y_place >= len(arr_y) - 1: return 0
    return matrix[y_place][x_place]

def pst_prepare(arr):
    if not arr:
        return PersistentTree(0), [], []
    events, lst_y = [], []
    for (x1, y1), (x2, y2) in arr:
        events.append((x1, 1, y1, y2))
        events.append((x2, -1, y1, y2))
        lst_y.extend([y1, y2])
    lst_y = sorted(set(lst_y))

    if len(lst_y) < 2:
        return PersistentTree(0), [], lst_y
    
    dct_y = {lst_y[i]:i for i in range(len(lst_y))}
    events.sort()

    tree_size = len(lst_y)-1
    pst = PersistentTree(tree_size)
    lst_x = []
    i=0
    while i<len(events):
        x = events[i][0]
        cur_root = pst.roots[-1]

        while i<len(events) and x==events[i][0]:
            _, mark, y1, y2 = events[i]
            y1_idx, y2_idx = dct_y[y1], dct_y[y2]
            if y1_idx < y2_idx:
                cur_root = pst.update(0, tree_size - 1, y1_idx, y2_idx - 1, cur_root, mark)
            i += 1
        pst.roots.append(cur_root)
        lst_x.append(x)
    return pst, lst_x, lst_y

def pst(pst, lst_x, lst_y, x, y):
    if not lst_x or not lst_y or pst.size <= 0:
        return 0
    
    version = bisect.bisect_right(lst_x, x)
    ind = bisect.bisect_right(lst_y, y)-1
    if ind<0 or ind>=len(lst_y) - 1: return 0
    return pst.get_ans(ind, version)
