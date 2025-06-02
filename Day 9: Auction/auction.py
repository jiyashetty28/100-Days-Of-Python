logo = '''
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
import os

def clear():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Mac and Linux
    else:
        _ = os.system('clear')
print(logo)

bids={}
bidding_done= False

def find_highest_bidder(bidding_record):
    highest_big = 0
    winner= ""
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highest_big:
            highest_big= bid_amount
            winner= bidder
    print(f"The winner is {winner} with a bid of ${highest_big}")
    
while not bidding_done:
    name= input("What is your name?:")
    price = int(input("What is your bid?: $"))
    bids[name]= price
    should_continue= input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue=="no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
        
        
            
