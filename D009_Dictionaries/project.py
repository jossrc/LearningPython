list_of_bidders = []


def add_new_bidder(bidder_name, bidder_bid):
    bidder = {
        "name": bidder_name,
        "bid": bidder_bid
    }
    list_of_bidders.append(bidder)


def get_winner():
    highest_bid = list_of_bidders[0]["bid"]
    winner_index = 0
    for idx in range(1, len(list_of_bidders)):
        auxiliary_bid = list_of_bidders[idx]["bid"]

        if auxiliary_bid > highest_bid:
            highest_bid = auxiliary_bid
            winner_index = idx

    return list_of_bidders[winner_index]


there_are_bidders = True


while there_are_bidders:
    name = input("\nWhat is your name?: ").strip()
    bid = int(input("What's your bid?: $").strip())
    add_new_bidder(name, bid)
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        there_are_bidders = False

winner = get_winner()

print(f"\nThe winner is {winner['name']} with a bid of ${winner['bid']}.")
