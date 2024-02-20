from auction_logo import logo 

print(logo)
print("Welcome to the Secret Auction Program: ")
bid_continue = True
bid_auction = {}


def silent_auction(bid_auctions):
    winner_name = ""
    winner_amount = 0
    for key in bid_auctions:
        if bid_auctions[key] > winner_amount:
            winner_name = key
            winner_amount = bid_auctions[key]
    print(f"The winner is {winner_name} with a bid of ${winner_amount}.")


while bid_continue:
    name = input("What is your name: ")
    bid_amount = int(input("What is your bid: $"))
    bid_auction[name] = bid_amount
    choice = input("Are there any other bidders, Type 'yes' or 'no': ")
    if choice == "no":
        bid_continue = False
        silent_auction(bid_auction)


