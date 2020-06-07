import unittest
from .sense_hat_front import SenseFront

class sense_hat_dummy_front_led_test(unittest.TestCase):

    def test_led_matrix_should_initial_be_black(self):
        front = SenseFront.create_dummy_front()

        for i in range(8):
            for j in range(8):
                pixel = front.get_pixel(i, j)
                self.assertEqual(pixel[0], 0)
                self.assertEqual(pixel[1], 0)
                self.assertEqual(pixel[2], 0)


    def test_clear(self):
        front = SenseFront.create_dummy_front()

        front.clear([1, 2, 3])
        for i in range(8):
            for j in range(8):
                pixel = front.get_pixel(i, j)
                self.assertEqual(pixel[0], 1)
                self.assertEqual(pixel[1], 2)
                self.assertEqual(pixel[2], 3)

    def test_set_single_pixel_1(self):
        front = SenseFront.create_dummy_front()

        front.set_pixel(5 , 2, 255, 255, 255)

        for i in range(8):
            for j in range(8):
                if i != 5 and j != 2:
                    pixel = front.get_pixel(i, j)
                    self.assertEqual(0, pixel[0])
                    self.assertEqual(0, pixel[1])
                    self.assertEqual(0, pixel[2])

        pixel = front.get_pixel(5, 2)
        self.assertEqual(255, pixel[0])
        self.assertEqual(255, pixel[1])
        self.assertEqual(255, pixel[2])


    def test_set_single_pixel_2(self):
        front = SenseFront.create_dummy_front()

        front.set_pixel(5 , 2, [255, 255, 255])

        for i in range(8):
            for j in range(8):
                if i != 5 and j != 2:
                    pixel = front.get_pixel(i, j)
                    self.assertEqual(0, pixel[0])
                    self.assertEqual(0, pixel[1])
                    self.assertEqual(0, pixel[2])

        pixel = front.get_pixel(5, 2)
        self.assertEqual(255, pixel[0])
        self.assertEqual(255, pixel[1])
        self.assertEqual(255, pixel[2])


    def test_set_all_pixel_1(self):
        front = SenseFront.create_dummy_front()

        k = 0
        for i in range(8):
            for j in range(8):
                front.set_pixel(i, j, [i, j, k])
                k = k + 1

        k = 0
        for i in range(8):
            for j in range(8):
                pixel = front.get_pixel(i, j)
                self.assertEqual(i, pixel[0])
                self.assertEqual(j, pixel[1])
                self.assertEqual(k, pixel[2])
                k = k + 1


    def test_set_all_pixel_2(self):
        front = SenseFront.create_dummy_front()

        k = 0
        for i in range(8):
            for j in range(8):
                front.set_pixel(i, j, i, j, k)
                k = k + 1

        k = 0
        for i in range(8):
            for j in range(8):
                pixel = front.get_pixel(i, j)
                self.assertEqual(i, pixel[0])
                self.assertEqual(j, pixel[1])
                self.assertEqual(k, pixel[2])
                k = k + 1

        