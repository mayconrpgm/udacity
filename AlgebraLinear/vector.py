from math import sqrt, acos, pi, sin
from decimal import Decimal, getcontext

# Number of decimal places
getcontext().prec = 15

class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector"
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = "No unique parallel component as vector cannot be normalized"
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = "No unique orthogonal component as vector cannot be normalized"
    CANNOT_COMPUTE_ANGLE = "Cannot compute angle with zero vector"
    CANNOT_CALCULATE_CROSS_PRODUCT = "Cannot calculate the cross product of the vectors as one of them have more than 3 dimensions or less than 2 dimensions"
    CANNOT_CALCULATE_AREA_OF_PARALLELOGRAM = "Cannot calculate the area of the parallelogram as the angle between the vectors cannot be calculated as well"
    CANNOT_CALCULATE_AREA_OF_TRIANGLE = "Cannot calculate the area of the triangle as the angle between the vectors cannot be calculated as well"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def round_coordinates(self, dec_places: int):
        return [round(x, dec_places) for x in self.coordinates]

    def magnitude(self):
        return sqrt(sum([a ** 2 for a in self.coordinates]))
    
    def normalized(self):
        try:
            return self.times_scalar(Decimal("1.0") / Decimal(self.magnitude()))
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def plus(self, v):
        r = [a + b for a, b in zip(self.coordinates, v.coordinates)]
        return Vector(r)

    def minus(self, v):
        r = [a - b for a, b in zip(self.coordinates, v.coordinates)]
        return Vector(r)
    
    def times_scalar(self, x):
        r = [a * Decimal(x) for a in self.coordinates]
        return Vector(r)
    
    def dot(self, v):
        return sum([a * b for a, b in zip(self.coordinates, v.coordinates)])
    
    def angle_with_rad(self, v):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            return acos(u1.dot(u2))
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_COMPUTE_ANGLE)
            else:
                raise e

    def angle_with(self, v):
        return self.angle_with_rad(v) * (180.0 / pi)

    def is_parallel_to(self, v):
        return (self.is_zero() 
                or v.is_zero() 
                or self.angle_with_rad(v) == 0 
                or self.angle_with_rad(v) == pi)

    # since values are decimal, due to high precision, we have to specify a tolerance to consider a value to be 0
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    # since values are decimal, due to high precision, we have to specify a tolerance to consider a value to be 0
    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def component_parallel_to(self, v):
        try:
            v_norm = v.normalized()

            return v_norm.times_scalar(self.dot(v_norm))
        
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_orthogonal_to(self, v):
        try:
            v_proj = self.component_parallel_to(v)

            return self.minus(v_proj)
        
        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    def cross(self, v):
        try:
            if self.dimension not in [2, 3] or v.dimension not in [2, 3]:
                raise Exception(self.CANNOT_CALCULATE_CROSS_PRODUCT)
            else:
                if self.dimension == 2 and v.dimension == 2:
                    self_embedded_in_r3 = Vector(self.coordinates + (0, ))
                    v_embedded_in_r3 = Vector(v.coordinates + (0, ))
                
                    return self_embedded_in_r3.cross(v_embedded_in_r3)

            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates

            return Vector(
                [
                    y_1 * z_2 - y_2 * z_1,
                    - (x_1 * z_2 - x_2 * z_1),
                    x_1 * y_2 - x_2 * y_1
                ]
            )
        except Exception as e:
            raise e


    def area_of_parallelogram(self, v):
        try:
            return self.cross(v).magnitude()
        except Exception as e:
            if str(e) == self.CANNOT_COMPUTE_ANGLE:
                raise Exception(self.CANNOT_CALCULATE_AREA_OF_PARALLELOGRAM)
            else:
                raise e

    def area_of_triangle(self, v):
        try:
            return self.area_of_parallelogram(v) / 2.0
        except Exception as e:
            if str(e) == self.CANNOT_CALCULATE_AREA_OF_PARALLELOGRAM:
                raise Exception(self.CANNOT_CALCULATE_AREA_OF_TRIANGLE)
            else:
                raise e

