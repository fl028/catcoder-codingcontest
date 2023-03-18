import unittest
from DeletablePrimes import get_count

class Test(unittest.TestCase):
    def setUp(self):
        print("\nsetUp")

    def tearDown(self):
        print("tearDown\n")

    def test_get_count(self):
        # arrange
        inputs = [4567,4125673, 41256793, 337424981, 537430451, 200899998, 537499093, 2147483059, 410256793, 567629137,46216567629137]
        expected = [3,12,21,14,3,0,8,8,29,84,121]
        outputs = []

        # act
        for index in range(len(inputs)):
            outputs.append(get_count(inputs[index]))
            print(str(inputs[index]) + " -> " + str(outputs[index]))

        # assert
        for index in range(len(outputs)):
            self.assertEqual(outputs[index], expected[index], str(inputs[index]) + " should be " + str(expected[index]) + " actual: " + str(outputs[index]))

if __name__ == '__main__':
    unittest.main()