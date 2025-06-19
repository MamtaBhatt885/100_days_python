logo = '''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner =""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid =  bid_amount
            winner = bidder

    print(f"The winner is  {winner} with a bid of ${highest_bid}")


bids = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    bid_price = int(input("What is your bid?: $"))
    bids[name] = bid_price

    ask_for_other_bidders = input("Ask if there are other users who want to bid. Press 'y' if there is another user else press 'n':  ").lower()

    if ask_for_other_bidders == 'n':
        continue_bidding = False
        find_highest_bidder(bids)
    elif ask_for_other_bidders == "y":
        print("\n"*20)





