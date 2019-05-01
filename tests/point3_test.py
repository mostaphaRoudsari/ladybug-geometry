# coding=utf-8

from ladybug_geometry.point3 import Vector3, Point3, Vector3Immutable, Point3Immutable

import unittest
import pytest
import math


class Point3TestCase(unittest.TestCase):
    """Test for (ladybug_geometry/point3.py)"""

    def test_vector2_init(self):
        """Test the initalization of Vector3 objects and basic properties."""
        vec = Vector3(0, 2, 0)
        str(vec)  # test the string representation of the vector

        assert vec.x == 0
        assert vec.y == 2
        assert vec.z == 0
        assert vec.magnitude == 2
        assert vec.magnitude_squared == 4

        norm_vec = vec.normalized()
        assert norm_vec.x == 0
        assert norm_vec.z == 0
        assert norm_vec.magnitude == 1

        assert vec.magnitude == 2
        vec.normalize()
        assert vec.magnitude == 1

    def test_point3_init(self):
        """Test the initalization of Point3 objects and basic properties."""
        pt_1 = Point3(0, 2, 0)
        str(pt_1)  # test the string representation of the vector
        assert pt_1.x == 0
        assert pt_1.y == 2
        assert pt_1.z == 0

        pt_2 = Point3(2, 2)
        assert pt_1.distance_to_point(pt_2) == 2

    def test_vector3_mutability(self):
        """Test the mutability and immutability of Vector3 objects."""
        vec = Vector3(0, 2, 0)
        assert isinstance(vec, Vector3)
        assert vec.is_mutable is True
        vec.x = 1
        assert vec.x == 1
        vec_copy = vec.duplicate()
        assert vec == vec_copy
        vec_copy.x = 2
        assert vec != vec_copy

        vec_imm = vec.to_immutable()
        assert isinstance(vec_imm, Vector3Immutable)
        assert vec_imm.is_mutable is False
        with pytest.raises(AttributeError):
            vec_imm.x = 2
        with pytest.raises(AttributeError):
            vec_imm.normalize()
        norm_vec = vec_imm.normalized()  # ensure operations tha yield new vectors are ok
        assert norm_vec.magnitude == pytest.approx(1., rel=1e-3)
        assert vec_imm.x == 1

        vec = Vector3Immutable(0, 2, 0)
        assert isinstance(vec, Vector3Immutable)
        assert vec.is_mutable is False
        with pytest.raises(AttributeError):
            vec.x = 1
        assert vec.x == 0
        vec_copy = vec.duplicate()
        assert vec == vec_copy

        vec_mut = vec.to_mutable()
        assert isinstance(vec_mut, Vector3)
        assert vec_mut.is_mutable is True
        vec_mut.x = 1
        assert vec_mut.x == 1

    def test_point3_mutability(self):
        """Test the mutability and immutability of Point3 objects."""
        pt = Point3(0, 2, 0)
        assert isinstance(pt, Point3)
        assert pt.is_mutable is True
        pt.x = 1
        assert pt.x == 1
        pt_copy = pt.duplicate()
        assert pt == pt_copy
        pt_copy.x = 2
        assert pt != pt_copy

        pt_imm = pt.to_immutable()
        assert isinstance(pt_imm, Point3Immutable)
        assert pt_imm.is_mutable is False
        with pytest.raises(AttributeError):
            pt_imm.x = 2
        norm_vec = pt_imm.normalized()  # ensure operations tha yield new vectors are ok
        assert norm_vec.magnitude == pytest.approx(1., rel=1e-3)
        assert pt_imm.x == 1

        pt = Point3Immutable(0, 2, 0)
        assert isinstance(pt, Point3Immutable)
        assert pt.is_mutable is False
        with pytest.raises(AttributeError):
            pt.x = 1
        assert pt.x == 0
        pt_copy = pt.duplicate()
        assert pt == pt_copy

        pt_mut = pt.to_mutable()
        assert isinstance(pt_mut, Point3)
        assert pt_mut.is_mutable is True
        pt_mut.x = 1
        assert pt_mut.x == 1

    def test_vector3_angle(self):
        """Test the methods that get the angle between Vector3 objects."""
        vec_1 = Vector3(0, 2, 0)
        vec_2 = Vector3(2, 0, 0)
        vec_3 = Vector3(0, -2, 0)
        vec_4 = Vector3(-2, 0, 0)
        vec_5 = Vector3(0, 0, 2)
        vec_6 = Vector3(0, 0, -2)
        assert vec_1.angle(vec_2) == pytest.approx(math.pi/2, rel=1e-3)
        assert vec_1.angle(vec_3) == pytest.approx(math.pi, rel=1e-3)
        assert vec_1.angle(vec_4) == pytest.approx(math.pi/2, rel=1e-3)
        assert vec_1.angle(vec_5) == pytest.approx(math.pi/2, rel=1e-3)
        assert vec_5.angle(vec_6) == pytest.approx(math.pi, rel=1e-3)
        assert vec_1.angle(vec_1) == pytest.approx(0, rel=1e-3)

    def test_addition_subtraction(self):
        """Test the addition and subtraction methods."""
        vec_1 = Vector3(0, 2, 0)
        vec_2 = Vector3(2, 0, 0)
        pt_1 = Point3(2, 0, 0)
        pt_2 = Point3(0, 2, 0)
        assert isinstance(vec_1 + vec_2, Vector3)
        assert isinstance(vec_1 + pt_1, Point3)
        assert isinstance(pt_1 + pt_2, Vector3)
        assert isinstance(vec_1 - vec_2, Vector3)
        assert isinstance(vec_1 - pt_1, Point3)
        assert isinstance(pt_1 - pt_2, Vector3)
        assert vec_1 + vec_2 == Vector3(2, 2, 0)
        assert vec_1 + pt_1 == Point3(2, 2, 0)
        assert pt_1 + pt_2 == Vector3(2, 2, 0)
        assert vec_1 - vec_2 == Vector3(-2, 2, 0)
        assert vec_1 - pt_1 == Point3(-2, 2, 0)
        assert pt_1 - pt_2 == Vector3(2, -2, 0)


if __name__ == "__main__":
    unittest.main()