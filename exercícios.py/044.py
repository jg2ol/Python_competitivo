# Distância de Manhattan, fácil
# 335

xm, ym, xr, yr = map(int, input().split())
dx = xm - xr
dy = ym - yr

if dx < 0:
    dx = -dx
if dy < 0:
    dy = -dy

print(dx + dy)