class Auction:
    def __init__(self, auction_history):
        self.auction_history_raw = auction_history
        self.auction_bids_raw = auction_history[1:]
        self.bids = []
        self.highest_bid = None
        self._parse_auction_history()

    def __str__(self):
        return str(self.auction_history_raw)

    def _parse_auction_history(self):
        initial_bid = Bid("start bid", self.auction_history_raw[0],None)
        self.bids.append(initial_bid)
        self.highest_bid = initial_bid

        for index in range(0, len(self.auction_bids_raw), 2):
            self.bids.append(Bid(self.auction_bids_raw[index], self.auction_bids_raw[index + 1], self.highest_bid))

            if self.bids[-1].bid > self.highest_bid.bid or len(self.bids) == 2:
                self.highest_bid = self.bids[-1]

    def get_highest_bid(self):
        return str(self.highest_bid.bidders_name) + "," + str(self.bids[-1].current_price)


class Bid:
    def __init__(self, bidders_name, bid, highest_bid):
        self.bidders_name = bidders_name
        self.bid = bid

        if highest_bid != None and highest_bid.bidders_name == "start bid":
            self.current_price = highest_bid.bid
        elif highest_bid != None and self.bid > highest_bid.bid and highest_bid.bidders_name == self.bidders_name:
            self.current_price = highest_bid.current_price
        elif highest_bid != None and self.bid > highest_bid.bid:
            self.current_price = highest_bid.bid + 1
        elif highest_bid != None and self.bid < highest_bid.bid:
            self.current_price = self.bid + 1
        elif highest_bid != None and self.bid == highest_bid.bid:
            self.current_price = self.bid

    def __str__(self):
        return f"{self.bidders_name}, {self.current_price}"

def get_highest_bid_in_auction(auction_history):
    auction = Auction(auction_history)
    return auction.get_highest_bid()


# main
if __name__ == '__main__':
    inputs = [[1,"A",5,"B",10,"A",8,"A",14,"A",17,"B",17],
              [1,"nepper",15,"hamster",24,"philipp",30,"mmautne",31,"hamster",49,"hamster",55,"thebenil",57,"fliegimandi",59,"ev",61,"philipp",64,"philipp",65,"ev",74,"philipp",69,"philipp",71,"fliegimandi",78,"hamster",78,"mio",95,"hamster",103,"macquereauxpl",135],
              [15,"urtyp",17,"neuli",16,"schlurchi",25,"tokay",75,"horni",35,"sue",60,"sue",65,"gap",70],
              [100,"A",100,"A",115,"A",119,"A",144,"A",145,"A",157,"A",158,"A",171,"A",179,"A",194,"A",206,"A",207,"A",227,"A",229,"A",231,"A",234],
              [100,"C",100,"C",115,"C",119,"C",121,"C",144,"C",154,"C",157,"G",158,"C",171,"C",179,"C",194,"C",206,"C",214,"C",227,"C",229,"C",231,"C",298]
              ]

    for item in inputs:
        auction = Auction(item)
        print(str(item) + " -> " + str(auction.get_highest_bid()))
