import matplotlib.pyplot as plt
import transformations
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math


def gen_points_on_sphere_min_d_separated(N_points, N_dim, min_d):
    """
    This function randomly samples points from a uniform distribution on a n_dim sphere
    so that no two points are less then min_d closer to each other
    :param N_points: the number of points to return
    :param N_dim: the dimension of the sphere ans points
    :param min_d: min distance between the points
    :return: N_points, if the function times out and can't generate it will return
    the points it succeeded generating
    """
    timeout_thershold = N_points
    points = []
    timeout = 0
    while len(points) < N_points and timeout < timeout_thershold:
        point = gen_random_point_on_sphere(N_dim)
        if is_min_d_far_from_points(point, points, min_d):
            points.append(point)
            timeout = 0
        else:
            timeout += 1
    # if we try to generate a point timeout_threshold times and don't succeed, we time out
    if timeout == timeout_thershold:
        print("Timed out! Couldn't find enough points to satisfy the condition.")
        print("Found ", len(points), "points")
    return points


def gen_random_point_on_sphere(N_dim):
    """
    Generate a uniformly distributed point on a unit sphere of N_dim dimensions
    :param N_dim: Dimension of the sphere
    :return: A N_dim dimension point
    """
    # Generate a random gaussian vector
    gaussian_vector = np.random.normal(0, 1, N_dim)
    # Normalize the vector
    return transformations.unit_vector(gaussian_vector, None)


def dist_on_hypersphere(point_a, point_b):
    """
    Return the distance between two points as measured on a unit sphere centered at the origin
    :return: distance between the two points
    """
    return math.acos(np.dot(point_a, point_b))


def is_min_d_far_from_points(point, other_points, min_d):
    """
    Check if point is at least min_d distance from all the points at other_points
    :param point: the point being checked
    :param other_points: a list of points to check the distance from
    :param min_d: the minimum distance between two points
    :return: true if the point is farther then min_d from all other points.
    false otherwise
    """
    for other_point in other_points:
        if dist_on_hypersphere(point, other_point) < min_d:
            return False
    return True


def display_on_sphere(points):
    """
    display points on a 3 dimensional unit sphere
    :param points:list of 3 dimensional points
    :return: None
    """
    points_array = np.asarray(points)
    xx, yy, zz = np.hsplit(points_array,3)

    ax, x, y, z = create_sphere()
    ax.plot_surface(
        x, y, z, rstride=1, cstride=1, color='b', alpha=0.3, linewidth=0)
    ax.scatter(xx, yy, zz, color="k", s=20)

    plt.tight_layout()
    plt.show()


def create_sphere():
    """"
    create a 3 dimensional sphere and return it as a figure
    """
    # create sphere
    radius = 1
    pi = np.pi
    phi, theta = np.mgrid[0.0:pi:100j, 0.0:2.0 * pi:100j]
    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    # Set colours and render
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_aspect("equal")
    return ax, x, y, z
