# Jardim de Infância, difícil
# link: https://neps.academy/br/exercise/9

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())
x5, y5 = map(int, input().split())
x6, y6 = map(int, input().split())
x7, y7 = map(int, input().split())

if (x2-x3)**2 + (y2-y3)**2 < (x1-x2)**2 + (y1-y2)**2 + (x1-x3)**2 + (y1-y3)**2:
    if (x1-x2)**2 + (y1-y2)**2 == (x1-x3)**2 + (y1-y3)**2:
        if y2 != y3 != y4 != y5:
            if (x2-x3)/(y2-y3) == (x3-x4)/(y3-y4) == (x4-x5)/(y4-y5):
                if ((x2+x3)/2, (y2+y3)/2) == ((x4+x5)/2, (y4+y5)/2):
                    if (x2-x3)**2 + (y2-y3)**2 > (x4-x5)**2 + (y4-y5)**2:
                        if (x2-x6)**2 + (y2-y6)**2 == (x2-x4)**2 + (y2-y4)**2 + (x4-x6)**2 + (y4-y6)**2 and (x3-x7)**2 + (y3-y7)**2 == (x3-x5)**2 + (y3-y5)**2 + (x5-x7)**2 + (y5-y7)**2:
                            if (x4-x6)**2 + (y4-y6)**2 == (x5-x7)**2 + (y5-y7)**2:
                                if (x1-x4)**2 + (y1-y4)**2 != (x1-x6)**2 + (y1-y6)**2 + (x4-x6)**2 + (y4-y6)**2:
                                    print("S")
                                else:
                                    print("N")
                            else:
                                print("N")
                        else:
                            print("N")
                    else:
                        print("N")
                else:
                    print("N")
            else:
                print("N")
        elif y2 == y3 == y4 == y5 and x2 != x3:
            if ((x2+x3)/2, (y2+y3)/2) == ((x4+x5)/2, (y4+y5)/2):
                if (x2-x3)**2 + (y2-y3)**2 > (x4-x5)**2 + (y4-y5)**2:
                    if (x2-x6)**2 + (y2-y6)**2 == (x2-x4)**2 + (y2-y4)**2 + (x4-x6)**2 + (y4-y6)**2 and (x3-x7)**2 + (y3-y7)**2 == (x3-x5)**2 + (y3-y5)**2 + (x5-x7)**2 + (y5-y7)**2:
                        if (x4-x6)**2 + (y4-y6)**2 == (x5-x7)**2 + (y5-y7)**2:
                            if (x1-x4)**2 + (y1-y4)**2 != (x1-x6)**2 + (y1-y6)**2 + (x4-x6)**2 + (y4-y6)**2:
                                print("S")
                            else:
                                print("N")
                        else:
                            print("N")
                    else:
                        print("N")
                else:
                    print("N")
            else:
                print("N")
        elif x2 == x3 == x4 == x5:
            if ((x2+x3)/2, (y2+y3)/2) == ((x4+x5)/2, (y4+y5)/2):
                if (x2-x3)**2 + (y2-y3)**2 > (x4-x5)**2 + (y4-y5)**2:
                    if (x2-x6)**2 + (y2-y6)**2 == (x2-x4)**2 + (y2-y4)**2 + (x4-x6)**2 + (y4-y6)**2 and (x3-x7)**2 + (y3-y7)**2 == (x3-x5)**2 + (y3-y5)**2 + (x5-x7)**2 + (y5-y7)**2:
                        if (x4-x6)**2 + (y4-y6)**2 == (x5-x7)**2 + (y5-y7)**2:
                            if (x1-x4)**2 + (y1-y4)**2 != (x1-x6)**2 + (y1-y6)**2 + (x4-x6)**2 + (y4-y6)**2:
                                print("S")
                            else:
                                print("N")
                        else:
                            print("N")
                    else:
                        print("N")
                else:
                    print("N")
            else:
                print("N")
        else:
            print("N")
    else:
        print("N")
else:
    print("N")