import time

cnt = 1000

new_list = []
for _ in range(cnt):
    start = time.time()  # 시작 시간 저장
    temp = [0 for _ in range(100000)]
    new_list.append(time.time() - start)

print('new_list', sum(new_list)/cnt)

new_list2 = []
for _ in range(cnt):
    start = time.time()  # 시작 시간 저장
    temp = [0] * (100000)
    new_list2.append(time.time() - start)

print('new_list2', sum(new_list2)/cnt)

# init_list = []
# temp = [0 for _ in range(100000)]
# for _ in range(cnt):
#     start = time.time()  # 시작 시간 저장
#     for i in range(100000):
#         temp[i] = 0
#     init_list.append(time.time() - start)

# print('init_list', sum(init_list)/cnt)

