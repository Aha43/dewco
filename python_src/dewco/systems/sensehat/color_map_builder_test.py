import unittest

from .color_map import color_map_builder


class color_map_builder_test(unittest.TestCase):

    def test_raises_if_not_completed(self):
        builder = color_map_builder(2)

        self.assertRaises(ValueError, builder.build)
        builder.add([0, 0, 255])
        self.assertRaises(ValueError, builder.build)
        builder.add([0, 0, 255])
        self.assertRaises(ValueError, builder.build)
        builder.add([0, 0, 255])
        self.assertRaises(ValueError, builder.build)
        builder.add([0, 0, 255])
        mc = builder.build()
        self.assertFalse(mc == None)

    def test_raises_if_receives_not_valid_rgb_for_pixel(self):
        builder = color_map_builder(2)

        with self.assertRaises(ValueError) as cm:
            builder.add([])
        self.assertEqual(str(cm.exception), "rgb list length not 3 but 0")

        with self.assertRaises(ValueError) as cm:
            builder.add([1])
        self.assertEqual(str(cm.exception), "rgb list length not 3 but 1")

        with self.assertRaises(ValueError) as cm:
            builder.add([1, 2])
        self.assertEqual(str(cm.exception), "rgb list length not 3 but 2")

        with self.assertRaises(ValueError) as cm:
            builder.add([1, 2, 3, 4])
        self.assertEqual(str(cm.exception), "rgb list length not 3 but 4")

        with self.assertRaises(ValueError) as cm:
            builder.add([-1, 0, 0])
        self.assertEqual(str(cm.exception), "r < 0 : -1")

        with self.assertRaises(ValueError) as cm:
            builder.add([0, -1, 0])
        self.assertEqual(str(cm.exception), "g < 0 : -1")

        with self.assertRaises(ValueError) as cm:
            builder.add([0, 0, -1])
        self.assertEqual(str(cm.exception), "b < 0 : -1")

        with self.assertRaises(ValueError) as cm:
            builder.add([256, 0, 0])
        self.assertEqual(str(cm.exception), "r > 255 : 256")

        with self.assertRaises(ValueError) as cm:
            builder.add([0, 256, 0])
        self.assertEqual(str(cm.exception), "g > 255 : 256")

        with self.assertRaises(ValueError) as cm:
            builder.add([0, 0, 256])
        self.assertEqual(str(cm.exception), "b > 255 : 256")

    
    def test_map_should_only_have_one_color_and_vertice(self):
        builder = color_map_builder(1)
        builder.add([0, 0, 0])
        map = builder.build()

        self.assertEqual(len(map.indices), 1)
        self.assertEqual(len(map.rgbs), 1)

    def test_map_should_have_one_color_and_four_vertices(self):
        builder = color_map_builder(2)
        builder.add([0, 0, 255])
        builder.add([0, 0, 255])
        builder.add([0, 0, 255])
        builder.add([0, 0, 255])
        map = builder.build()

        self.assertEqual(len(map.indices), 4)
        self.assertEqual(len(map.rgbs), 1)
        self.assertEqual(map.indices[0], 0)
        self.assertEqual(map.indices[1], 0)
        self.assertEqual(map.indices[2], 0)
        self.assertEqual(map.indices[3], 0)

    def test_map_should_have_two_colors_and_four_vertices(self):
        builder = color_map_builder(2)
        builder.add([0, 255, 0])
        builder.add([255, 0, 0])
        builder.add([255, 0, 0])
        builder.add([0, 255, 0])
        map = builder.build()

        self.assertEqual(len(map.indices), 4)
        self.assertEqual(len(map.rgbs), 2)
        self.assertEqual(map.indices[0], 0)
        self.assertEqual(map.indices[1], 1)
        self.assertEqual(map.indices[2], 1)
        self.assertEqual(map.indices[3], 0)  

if __name__ == '__main__':
    unittest.main()
