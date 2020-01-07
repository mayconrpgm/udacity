from vector import Vector

def main():
    print("plus")
    print(Vector([8.218, -9.341]).plus(Vector([-1.129, 2.111])))

    print("\nminus")
    print(Vector([7.119, 8.215]).minus(Vector([-8.223, 0.878])))

    print("\ntimes_scalar")
    print(Vector([1.671, -1.012, -0.318]).times_scalar(7.41))

    print("\nmagnitude")
    print(Vector([-0.221, 7.437]).magnitude())
    print(Vector([8.813, -1.331, -6.247]).magnitude())

    print("\nnormalized")
    print(Vector([5.581, -2.136]).normalized())
    print(Vector([1.996, 3.108, -4.554]).normalized())

    print("\ndot")
    print(Vector([7.887, 4.138]).dot(Vector([-8.802, 6.776])))
    print(Vector([-5.955, -4.904, -1.874]).dot(Vector([-4.496, -8.755, 7.103])))

    print("\nangle")
    print(Vector([3.183, -7.627]).angle_with_rad(Vector([-2.668, 5.319])))
    print(Vector([7.35, 0.221, 5.188]).angle_with(Vector([2.751, 8.259, 3.985])))

    print("\nis_parallel_to")
    print(Vector([-7.579, -7.88]).is_parallel_to(Vector([22.737, 23.64])))
    print(Vector([-2.089, 9.97, 4.172]).is_parallel_to(Vector([-9.231, -6.639, -7.245])))
    print(Vector([-2.328, -7.284, -1.214]).is_parallel_to(Vector([-1.821, 1.072, -2.94])))
    print(Vector([2.118, 4.827]).is_parallel_to(Vector([0, 0])))

    print("\nis_orthogonal_to")
    print(Vector([-7.579, -7.88]).is_orthogonal_to(Vector([22.737, 23.64])))
    print(Vector([-2.089, 9.97, 4.172]).is_orthogonal_to(Vector([-9.231, -6.639, -7.245])))
    print(Vector([-2.328, -7.284, -1.214]).is_orthogonal_to(Vector([-1.821, 1.072, -2.94])))
    print(Vector([2.118, 4.827]).is_orthogonal_to(Vector([0, 0])))

    print("\nprojection")
    print(Vector([3.039, 1.879]).component_parallel_to(Vector([0.825, 2.036])))
    print(Vector([3.009, -6.172, 3.692, -2.51]).component_parallel_to(Vector([6.404, -9.144, 2.759, 8.718])))
    
    print("\ncomponent vector")
    print(Vector([-9.88, -3.264, -8.159]).component_orthogonal_to(Vector([-2.155, -9.353, -9.473])))
    print(Vector([3.009, -6.172, 3.692, -2.51]).component_orthogonal_to(Vector([6.404, -9.144, 2.759, 8.718])))

    print("\ncross product")
    print(Vector([8.462, 7.893, -8.187]).cross(Vector([6.984, -5.975, 4.778])).round_coordinates(3))

    print("\narea of the parallelogram")
    print(round(Vector([-8.987, -9.838, 5.031]).area_of_parallelogram(Vector([-4.268, -1.861, -8.866])), 3))

    print("\narea of the triangle")
    print(round(Vector([1.5, 9.547, 3.691]).area_of_triangle(Vector([-6.007, 0.124, 5.772])), 3))

if __name__ == "__main__":
    main()