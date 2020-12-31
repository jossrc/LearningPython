import random
from game_data import data


def show_profile_info(profile: dict[str, any]):
    return f"{profile['name']}, a {profile['description']}, from {profile['country']}"


def get_number_of_followers(profile: dict[str, any]):
    return profile["follower_count"]


a = random.choice(data)
score = 0
should_continue = True

while should_continue:
    b = random.choice(data)

    while a == b:
        b = random.choice(data)

    print(f"\nCompare A: {show_profile_info(a)}")
    print(f"Against B: {show_profile_info(b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower().strip()

    count_a = get_number_of_followers(a)
    count_b = get_number_of_followers(b)

    answer_a = guess == 'a' and count_a > count_b
    answer_b = guess == 'b' and count_a < count_b

    if answer_a or answer_b:
        score += 1
        a = b
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False
