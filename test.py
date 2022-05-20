# import numpy as np
# import pandas as pd

# # Đọc dữ liệu
# bodyswing_df = pd.read_csv("SWING.txt")

# X = []
# y = []
# no_of_timesteps = 1
# print(bodyswing_df)
# print('----------')
# dataset = bodyswing_df.iloc[:,1:].values
# print(dataset)
# print('----------')

# n_sample = len(dataset)
# for i in range(no_of_timesteps, n_sample):
#     X.append(dataset[i-no_of_timesteps:i,:])
#     print(X)
#     print('----------')
#     y.append(1)

# n = int(input())
# l = []
# for _ in range(n):
#     s = input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "(" + ",".join(args) +")"
#         # eval("l."+cmd)
#         print(cmd)
#     else:
#         print(cmd)
s = 'ABCDCDC'
print(s.count('CDC'))