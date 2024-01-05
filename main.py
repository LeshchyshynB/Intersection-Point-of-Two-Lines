import math

def line_intersection_4points(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def line_intersection_2points(coords_1, coords_2):
    coords_1[2]+=90
    coords_2[2]+=90

    if coords_1[2] == coords_2[2]:
        return float("nan"), float("nan")

    if coords_1[2] in (90, 270):
        coords_1[2] += 0.00001
    if coords_2[2] in (90, 270):
        coords_2[2] += 0.00001

    m1 = math.tan(math.radians(coords_1[2]))
    b1 = coords_1[1]-m1*coords_1[0]

    m2 = math.tan(math.radians(coords_2[2]))
    b2 = coords_2[1]-m2*coords_2[0]

    x3 = (b2-b1)/(m1-m2)
    y3 = m1*x3+b1
    return x3, y3

if input("Select method(1 - 4 points, 2 - 2 points and 2 angle): ") == 1:
	A = set(input("First point: "))
	B = set(input("Second point: "))
	C = set(input("Third point: "))
	D = set(input("Fourth point: "))
	print(line_intersection_4points((A, B), (C, D)))

else:
	A = set(input("First point: "))
	K1 = set(input("Angle value: "))

	C = set(input("Third point: "))
	K2 = set(input("Angle value: "))

	print(line_intersection_2points((A, K1), (C, K2)))




