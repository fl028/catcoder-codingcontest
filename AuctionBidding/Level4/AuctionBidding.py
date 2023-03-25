class Auction:
    def __init__(self, auction_history):
        self.auction_history_raw = auction_history
        self.auction_bids_raw = auction_history[2:]
        self.bids = []
        self.highest_bid = None
        self.bid_history = []
        self.buy_now_price = None
        if auction_history[1] > 0:
            self.buy_now_price = auction_history[1]
        self._parse_auction_history()

    def __str__(self):
        return str(self.auction_history_raw)

    def _parse_auction_history(self):
        initial_bid = Bid("-", self.auction_history_raw[0],None,self.buy_now_price)
        self.bids.append(initial_bid)
        self.highest_bid = initial_bid
        self.bid_history.append("-")
        self.bid_history.append(str(self.highest_bid.bid))

        for index in range(0, len(self.auction_bids_raw), 2):
            self.bids.append(Bid(self.auction_bids_raw[index], self.auction_bids_raw[index + 1], self.highest_bid,self.buy_now_price))

            if self.bids[-1].bid > self.highest_bid.bid or len(self.bids) == 2:
                self.highest_bid = self.bids[-1]

            if self.bid_history[-2] != self.bids[-1].bidders_name:
                self.bid_history.append(self.highest_bid.bidders_name)
                self.bid_history.append(str(self.bids[-1].current_price))

                if self.buy_now_price != None and self.buy_now_price <= self.bids[-1].current_price:
                    break



    def get_highest_bid(self):
        return str(self.highest_bid.bidders_name) + "," + str(self.bids[-1].current_price)


    def get_bid_history(self):
        return ','.join(self.bid_history)

class Bid:
    def __init__(self, bidders_name, bid, highest_bid,buy_now_price):
        self.bidders_name = bidders_name
        self.bid = bid

        if bidders_name == "-":
            self.current_price = self.bid
        elif highest_bid != None and highest_bid.bidders_name == "-":
            self.current_price = highest_bid.bid
        elif highest_bid != None and self.bid > highest_bid.bid and highest_bid.bidders_name == self.bidders_name:
            self.current_price = highest_bid.current_price
        elif highest_bid != None and self.bid > highest_bid.bid:
            self.current_price = highest_bid.bid + 1
        elif highest_bid != None and self.bid < highest_bid.bid:
            self.current_price = self.bid + 1
        elif highest_bid != None and self.bid == highest_bid.bid:
            self.current_price = self.bid

        if buy_now_price != None and buy_now_price <= self.current_price:
            self.current_price = buy_now_price

    def __str__(self):
        return f"{self.bidders_name}, {self.current_price}"

# main
if __name__ == '__main__':
    inputs = [[1,15,"A",5,"B",10,"A",8,"A",17,"B",17],
              [100,0,"C",100,"C",115,"C",119,"C",121,"C",144,"C",154,"C",157,"G",158,"C",171,"C",179,"C",194,"C",206,"C",214,"C",227,"C",229,"C",231,"C",298],
              [100,325,"C",100,"C",115,"C",119,"C",121,"C",144,"C",154,"C",157,"G",158,"C",171,"C",179,"C",194,"C",206,"C",214,"C",227,"C",229,"C",231,"C",298],
              [100,160,"C",100,"C",115,"C",119,"C",121,"C",144,"C",154,"C",157,"G",158,"C",171,"C",179,"C",194,"C",206,"C",214,"C",227,"C",229,"C",231,"C",298],
              [1,0,"nepper",15,"hamster",24,"philipp",30,"mmautne",31,"hamster",49,"hamster",55,"thebenil",57,"fliegimandi",59,"ev",61,"philipp",64,"philipp",65,"ev",74,"philipp",69,"philipp",71,"fliegimandi",78,"hamster",78,"mio",95,"hamster",103,"macquereauxpl",135],
              [1,120,"6a",17,"kl",5,"kl",10,"kl",15,"cs",28,"kl",20,"kl",25,"hr",35,"hr",40,"hr",41,"hl",42,"hr",43,"hr",44,"hl",44,"hl",49,"hr",47],
              [1,47,"6a",17,"kl",5,"kl",10,"kl",15,"cs",28,"kl",20,"kl",25,"hr",35,"hr",40,"hr",41,"hl",42,"hr",43,"hr",44,"hl",44,"hl",49,"hr",47]
              ]

    for index in range(len(inputs)):
        auction = Auction(inputs[index])
        print(str(index) + " -> " + str(auction.get_bid_history()))
