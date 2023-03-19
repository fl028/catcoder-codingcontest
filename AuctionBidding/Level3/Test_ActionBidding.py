import unittest
from AuctionBidding import Auction

class Test(unittest.TestCase):
    def setUp(self):
        print("\nsetUp")

    def tearDown(self):
        print("tearDown\n")

    def test_get_bid_history(self):
        # arrange
        inputs = [[1, "A", 5, "B", 10, "A", 8, "A", 14, "A", 17, "B", 17],
                  [100, "A", 100, "A", 115, "A", 119, "A", 144, "A", 145, "A", 157, "A", 158, "A", 171, "A", 179, "A",
                   194, "A", 206, "A", 207, "A", 227, "A", 229, "A", 231, "A", 234],
                  [100, "C", 100, "C", 115, "C", 119, "C", 121, "C", 144, "C", 154, "C", 157, "G", 158, "C", 171, "C",
                   179, "C", 194, "C", 206, "C", 214, "C", 227, "C", 229, "C", 231, "C", 298],
                  [1, "nepper", 15, "hamster", 24, "philipp", 30, "mmautne", 31, "hamster", 49, "hamster", 55,
                   "thebenil", 57, "fliegimandi", 59, "ev", 61, "philipp", 64, "philipp", 65, "ev", 74, "philipp", 69,
                   "philipp", 71, "fliegimandi", 78, "hamster", 78, "mio", 95, "hamster", 103, "macquereauxpl", 135],
                  [15, "urtyp", 15],
                  [1, "rx", 50, "aa", 2000, "de", 3558, "einseins", 3999, "ek", 4999, "yd", 8332, "lb", 5000, "lb",
                   6000, "lb", 7000, "lb", 8000, "lb", 8999, "yd", 9999, "zn", 11000, "ir", 11110, "nr", 12999, "kt",
                   12567, "kt", 12667, "kt", 13000, "go", 14000, "ym", 14999, "hm", 15400, "nr", 15690, "nr", 17000,
                   "td", 18500, "kt", 18750, "uy", 18850, "hr", 18999, "td", 19049, "st", 19200]
                  ]
        expected = ['-,1,A,1,B,6,B,9,A,11,A,17',
                    '-,100,A,100',
                    '-,100,C,100,G,158,C,159',
                    '-,1,nepper,1,hamster,16,philipp,25,mmautne,31,hamster,32,thebenil,56,fliegimandi,58,ev,60,philipp,62,ev,66,ev,70,ev,72,fliegimandi,75,fliegimandi,78,mio,79,hamster,96,macquereauxpl,104',
                    '-,15,urtyp,15',
                    '-,1,rx,1,aa,51,de,2001,einseins,3559,ek,4000,yd,5000,yd,5001,yd,6001,yd,7001,yd,8001,lb,8333,yd,9000,zn,10000,ir,11001,nr,11111,nr,12568,nr,12668,kt,13000,go,13001,ym,14001,hm,15000,nr,15401,td,17001,kt,18501,uy,18751,hr,18851,td,19000,st,19050'
                    ]
        outputs = []

        # act
        for index in range(len(inputs)):
            auction = Auction(inputs[index])
            outputs.append(auction.get_bid_history())
            print(str(index) + " -> " + str(outputs[index]))

        # assert
        for index in range(len(outputs)):
            self.assertEqual(expected[index],outputs[index], str(inputs[index]) + " should be " + str(expected[index]) + " actual: " + str(outputs[index]))


if __name__ == '__main__':
    unittest.main()