from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
bid_list = []

def bid(name, bid):
  bid_dict = {}
  bid_dict["name"] = name
  bid_dict["bid"] = bid
  bid_list.append(bid_dict)

def highest_bid(bid_list):
  highest_bid = 0
  winner=""
  for bid in bid_list:
    if bid["bid"] > highest_bid:
      highest_bid = bid["bid"]
      winner = bid["name"]
  print(f"The winner is {winner} with a bid of ${highest_bid}")

print(logo)
print("Welcome to the secret auction program.")
while True:
  name = input("What is your name?: ")
  bid_input = int(input("What's your bid?: $"))
  bid(name, bid_input)
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if other_bidders == "yes":
    clear()
  else:
    highest_bid(bid_list)
    break