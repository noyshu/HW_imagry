import matplotlib.pyplot as plt
import transformations
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math


def gen_random_points_on_sphere_min_d_separated(N_points, N_dim, min_d):
    points = []
    timeout = 0
    while len(points) < N_points and timeout < 50:
        point = gen_random_point_on_sphere(N_dim)
        if not is_min_d_far_from_points(point, points, min_d):
            timeout += 1
            continue
        points.append(point)
        timeout = 0
    if timeout == 50:
        print("timed out! couldn't find enough points to satisfy the condition\nfound ", len(points), "points")
    return points


def gen_random_point_on_sphere(N_dim):
    x = np.random.normal(0, 1, N_dim)
    return transformations.unit_vector(x, None)


def dist_on_hypersphere(a, b):
    return math.acos(np.dot(a, b))


def is_min_d_far_from_points(point, other_points, min_d):
    for otherPoint in other_points:
        if dist_on_hypersphere(point,otherPoint) < min_d:
            return False
    return True


def display_on_sphere(points):
    points_array = np.asarray(points)
    xx, yy, zz = np.hsplit(points_array,3)

    ax, x, y, z = create_sphere()
    ax.plot_surface(
        x, y, z, rstride=1, cstride=1, color='b', alpha=0.3, linewidth=0)
    ax.scatter(xx, yy, zz, color="k", s=20)

    plt.tight_layout()
    plt.show()


def create_sphere():
    # create sphere
    r = 1
    pi = np.pi
    cos = np.cos
    sin = np.sin
    phi, theta = np.mgrid[0.0:pi:100j, 0.0:2.0 * pi:100j]
    x = r * sin(phi) * cos(theta)
    y = r * sin(phi) * sin(theta)
    z = r * cos(phi)

    # Set colours and render
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_aspect("equal")
    return ax, x, y, z
