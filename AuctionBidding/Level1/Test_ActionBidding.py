import unittest
from AuctionBidding import Auction

class Test(unittest.TestCase):
    def setUp(self):
        print("\nsetUp")

    def tearDown(self):
        print("tearDown\n")

    def test_get_highest_bid(self):
        # arrange
        inputs = [[1, "A", 5, "B", 10, "A", 8, "A", 17, "B", 17],
                  [1, "nepper", 15, "hamster", 24, "philipp", 30, "mmautne", 31, "hamster", 49, "thebenil", 57,"fliegimandi", 59, "ev", 61, "philipp", 64, "ev", 74, "philipp", 69, "philipp", 71, "fliegimandi",78, "hamster", 78, "mio", 95, "hamster", 103, "macquereauxpl", 135],
                  [1, "cable", 5, "ente", 10, "karl", 19, "moehe", 14, "moehe", 23, "michbex", 24, "melloy", 25, "achi",26],
                  [1, "cable", 5, "ente", 10, "karl", 19, "moehe", 23, "michbex", 24, "melloy", 29, "achi", 26],
                  [15, "urtyp", 17, "neuli", 16, "schlurchi", 25, "tokay", 75, "horni", 35, "sue", 60, "sue", 70],
                  [15, "urtyp", 15]]
        expected = ['A,17','macquereauxpl,104','achi,26','melloy,27','tokay,71','urtyp,15']
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