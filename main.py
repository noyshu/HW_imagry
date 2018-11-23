
import imagry_hw_funcs as hf
if __name__ == '__main__':

    N_points = 300
    N_dim = 3
    min_d = 0.13

    points = hf.gen_random_points_on_sphere_min_d_separated(N_points, N_dim, min_d)
    hf.display_on_sphere(points)

