import unittest
from AuctionBidding import Auction

class Test(unittest.TestCase):
    def setUp(self):
        print("\nsetUp")

    def tearDown(self):
        print("tearDown\n")

    def test_get_highest_bid(self):
        # arrange
        inputs = [[1, "A", 5, "B", 10, "A", 8, "A", 14, "A", 17, "B", 17],
                  [1, "nepper", 15, "hamster", 24, "philipp", 30, "mmautne", 31, "hamster", 49, "hamster", 55,
                   "thebenil", 57, "fliegimandi", 59, "ev", 61, "philipp", 64, "philipp", 65, "ev", 74, "philipp", 69,
                   "philipp", 71, "fliegimandi", 78, "hamster", 78, "mio", 95, "hamster", 103, "macquereauxpl", 135],
                  [15, "urtyp", 17, "neuli", 16, "schlurchi", 25, "tokay", 75, "horni", 35, "sue", 60, "sue", 65, "gap",
                   70],
                  [100, "A", 100, "A", 115, "A", 119, "A", 144, "A", 145, "A", 157, "A", 158, "A", 171, "A", 179, "A",
                   194, "A", 206, "A", 207, "A", 227, "A", 229, "A", 231, "A", 234],
                  [100, "C", 100, "C", 115, "C", 119, "C", 121, "C", 144, "C", 154, "C", 157, "G", 158, "C", 171, "C",
                   179, "C", 194, "C", 206, "C", 214, "C", 227, "C", 229, "C", 231, "C", 298]
                  ]
        expected = ['A,17','macquereauxpl,104','tokay,71','A,100','C,159']
        outputs = []

        # act
        for index in range(len(inputs)):
            auction = Auction(inputs[index])
            outputs.append(auction.get_highest_bid())
            print(str(index) + " -> " + str(outputs[index]))

        # assert
        for index in range(len(outputs)):
            self.assertEqual(expected[index],outputs[index], str(inputs[index]) + " should be " + str(expected[index]) + " actual: " + str(outputs[index]))


if __name__ == '__main__':
    unittest.main()