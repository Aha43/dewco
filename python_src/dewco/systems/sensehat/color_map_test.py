import unittest
from .color_map import color_map, color_map_builder

class color_map_test(unittest.TestCase):

    def test_color_map_should_have_correct_repr(self):
        builder = color_map_builder(2)
        builder.append_pixel([0, 0, 0])
        builder.append_pixel([0, 1, 0])
        builder.append_pixel([255, 155, 55])
        builder.append_pixel([0, 1, 0])
        cm = builder.build()

        repr = str(cm)

        self.assertEqual(repr, "0,0,0,0,1,0,255,155,55:0,1,2,1")

    def test_color_map_should_create_from_rep(self):
        builder = color_map_builder(2)
        builder.append_pixel([1, 2, 3])
        builder.append_pixel([4, 5, 6])
        builder.append_pixel([7, 8, 9])
        builder.append_pixel([10, 11, 12])
        cm1 = builder.build()

        repr1 = str(cm1)

        cm2 = color_map.from_rep(repr1)
        repr2 = str(cm2)

        self.assertTrue(repr1 == repr2)
