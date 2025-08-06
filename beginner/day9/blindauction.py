#function of the program: get input (name and bid), store it to the dictionary.
#loop trough as many times there is something to input.
#compare key values and highest will win the auction.



def get_bids():
    bids = {}
    while True:
        get_choice = input("Do you want to bid? Y or N ").lower().strip()
        if get_choice == "n":
            return bids
        elif get_choice == "y":
            bidder = input("What is your name? ").strip()
            if bidder == "" or not bidder.replace(" ", "").isalpha():
                print("You need a proper name!")
                continue
            bid_amount = input("How much you want to bid? $")
            if not bid_amount.isdigit():
                print("Write only numeric values!")
                continue
            bid_amount = int(bid_amount)
            bids.update({bidder:bid_amount})
            for i in range(15):
                print()
        else:
            print("You need to type Y or N!")
            continue

def highest_bid(bids):
    highest_bidder = ""
    highest_bid = 0
    for key in bids:
        if bids[key] > highest_bid:
            highest_bidder = key
            highest_bid = bids[key]
    
    print(f"Highest bid was {highest_bid}$ by {highest_bidder}.")



bids = get_bids()
highest_bid(bids)
