import matplotlib.pyplot as plt
import numpy as np


def pixels_to_inches(x, y):
    return x/96, y/96


def get_slope(p1, p2):
	if p1[0] == p2[0]:
		return float('inf')
	else:
		return 1.0*(p1[1]-p2[1])/(p1[0]-p2[0])


def get_cross_product(p1, p2, p3):
	return ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))

def convex_hull(arr):
    points = arr.tolist()
    hull = []
    points.sort(key=lambda x: [x[0], x[1]])
    start = points.pop(0)
    hull.append(start)
    points.sort(key=lambda p: (get_slope(p, start), -p[1], p[0]))
    for pt in points:
        hull.append(pt)
        while len(hull) > 2 and get_cross_product(hull[-3], hull[-2], hull[-1]) < 0:
            hull.pop(-2)
    return hull

def get_convex_hull(path):
    points = np.loadtxt(path, dtype=int)
    plt.figure(figsize=(9.6, 5.4))
    plt.plot(points[:, 0], points[:, 1], marker=',', color='k', linestyle='None')
    hull = convex_hull(points)
    hull_x = [row[0] for row in hull]
    hull_y = [row[1] for row in hull]
    plt.plot(hull_x, hull_y)
    plt.savefig('convex_hull_res.jpg')
    plt.show()
    plt.figure(figsize=(9.6, 5.4))
    plt.plot(hull_x, hull_y)
    plt.savefig('just_convex_hull.jpg')
    plt.show()

if __name__=="__main__":
    get_convex_hull("DS5.txt")
