import unittest
from AuctionBidding import Auction

class Test(unittest.TestCase):
    def setUp(self):
        print("\nsetUp")

    def tearDown(self):
        print("tearDown\n")

    def test_get_bid_history(self):
        # arrange
        inputs = [[1, 15, "A", 5, "B", 10, "A", 8, "A", 17, "B", 17],
                  [100, 0, "C", 100, "C", 115, "C", 119, "C", 121, "C", 144, "C", 154, "C", 157, "G", 158, "C", 171,
                   "C", 179, "C", 194, "C", 206, "C", 214, "C", 227, "C", 229, "C", 231, "C", 298],
                  [100, 325, "C", 100, "C", 115, "C", 119, "C", 121, "C", 144, "C", 154, "C", 157, "G", 158, "C", 171,
                   "C", 179, "C", 194, "C", 206, "C", 214, "C", 227, "C", 229, "C", 231, "C", 298],
                  [100, 160, "C", 100, "C", 115, "C", 119, "C", 121, "C", 144, "C", 154, "C", 157, "G", 158, "C", 171,
                   "C", 179, "C", 194, "C", 206, "C", 214, "C", 227, "C", 229, "C", 231, "C", 298],
                  [1, 0, "nepper", 15, "hamster", 24, "philipp", 30, "mmautne", 31, "hamster", 49, "hamster", 55,
                   "thebenil", 57, "fliegimandi", 59, "ev", 61, "philipp", 64, "philipp", 65, "ev", 74, "philipp", 69,
                   "philipp", 71, "fliegimandi", 78, "hamster", 78, "mio", 95, "hamster", 103, "macquereauxpl", 135],
                  [1, 120, "6a", 17, "kl", 5, "kl", 10, "kl", 15, "cs", 28, "kl", 20, "kl", 25, "hr", 35, "hr", 40,
                   "hr", 41, "hl", 42, "hr", 43, "hr", 44, "hl", 44, "hl", 49, "hr", 47],
                  [1, 47, "6a", 17, "kl", 5, "kl", 10, "kl", 15, "cs", 28, "kl", 20, "kl", 25, "hr", 35, "hr", 40, "hr",
                   41, "hl", 42, "hr", 43, "hr", 44, "hl", 44, "hl", 49, "hr", 47]
                  ]
        expected = ['-,1,A,1,B,6,B,9,A,11,A,15',
                    '-,100,C,100,G,158,C,159',
                    '-,100,C,100,G,158,C,159',
                    '-,100,C,100,G,158,C,159',
                    '-,1,nepper,1,hamster,16,philipp,25,mmautne,31,hamster,32,thebenil,56,fliegimandi,58,ev,60,philipp,62,ev,66,ev,70,ev,72,fliegimandi,75,fliegimandi,78,mio,79,hamster,96,macquereauxpl,104',
                    '-,1,6a,1,6a,6,6a,11,6a,16,cs,18,cs,21,cs,26,hr,29,hl,42,hr,43,hr,44,hl,45,hl,48',
                    '-,1,6a,1,6a,6,6a,11,6a,16,cs,18,cs,21,cs,26,hr,29,hl,42,hr,43,hr,44,hl,45,hl,47'
                    ]
        outputs = []

        # act
        for index in range(len(inputs)):
            auction = Auction(inputs[index])
            outputs.append(auction.get_bid_history())
            print(str(index) + " -> " + str(outputs[index]))

        # assert
        for index in range(len(outputs)):
            self.assertEqual( expected[index],outputs[index], str(inputs[index]) + " should be " + str(expected[index]) + " actual: " + str(outputs[index]))


if __name__ == '__main__':
    unittest.main()