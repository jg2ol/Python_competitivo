np = []

# for k in range(1, 3):
#     print(30*k+21, 70*k+21, 110*k+11, 130*k+91)
#     print(30*k+3, 70*k+63, 110*k+33, 130*k+13)
#     print(30*k+27, 70*k+7, 110*k+77, 130*k+117)
#     print(30*k+9, 70*k+49, 110*k+99, 130*k+39)
# print()

for k in range(1, 10):
    # print(30*k+21, 30*k+3, 30*k+27, 30*k+9)
    np.append(30*k+21)
    np.append(30*k+3)
    np.append(30*k+27)
    np.append(30*k+9)

print()
for k in range(0, 7):
    # print(70*k+21, 70*k+63, 70*k+7, 70*k+49)
    np.append(70*k+21)
    np.append(70*k+63)
    np.append(70*k+7)
    np.append(70*k+49)

print()
for k in range(1, 4):
    # print(110*k+11, 110*k+33, 110*k+77, 110*k+99)
    np.append(110*k+11)
    np.append(110*k+33)
    np.append(110*k+77)
    np.append(110*k+99)

print()
for k in range(1, 2):
    # print(130*k+91, 130*k+13, 130*k+117, 130*k+39)
    np.append(130*k+91)
    np.append(130*k+13)
    np.append(130*k+117)
    np.append(130*k+39)

for k in range(3, 29):
    if 10*k+1 not in np:
        print(10*k+1, end = " ")
    if 10*k+3 not in np:
        print(10*k+3, end = " ")
    if 10*k+7 not in np:
        print(10*k+7, end = " ")
    if 10*k+9 not in np:
        print(10*k+9, end = " ")
