def rotate_key(matrix):
    l = len(matrix)
    temp = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            temp[j][l-i-1] = matrix[i][j]
    return temp


def expand_key(key, l, x, y):
    temp = [[0 for _ in range(l)] for _ in range(l)]

    for i in range(len(key)):
        for j in range(len(key)):
            if 0 <= i+x < l and 0 <= j+y < l:
                temp[i+x][j+y] = key[i][j]

    return temp


def translate(lk, ll):
    temp = []
    for i in range(-(lk-1), lk):
        for j in range(-(lk-1), lk):
            temp.append((i, j))
    return temp


def match_key_lock(key, lock):
    l = len(lock)
    for i in range(l):
        for j in range(l):
            temp = key[i][j] + lock[i][j]
            if temp != 1:
                return False
    return True


def solution(key, lock):
    trans_list = translate(len(key), len(lock))

    for _ in range(4):
        for x, y in trans_list:
            expanded_key = expand_key(key, len(lock), x, y)
            if match_key_lock(expanded_key, lock) is True:
                return True 
        key = rotate_key(key)

    return False


if __name__ == "__main__":
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
                   [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
                   [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 1, 1]]))
