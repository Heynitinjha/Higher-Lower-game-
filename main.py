from Data import data
from Logo import logo
from Logo import vs
import random

print(logo)


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]

    return f"{account_name} a {account_desc} from {account_country} "


def check_answer(guess, followers_A, followers_B):
    if followers_A > followers_B:
        return guess == "a"
    else:
        return guess == "b"


score = 0
Should_Continue = True
account_B = random.choice(data)
while Should_Continue:
    account_A = account_B
    account_B = random.choice(data)

    while account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A :{format_data(account_A)} : ")
    print(vs)
    print(f"Compare B :{format_data(account_B)} : ")

    guess = input(" Who has the more followers A or B ?").lower()

    a_followers_count = account_A["follower_count"]
    b_followers_count = account_B["follower_count"]

    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    if is_correct:
        score += 1
        print(f"You won, your score is {score}")
    else:
        Should_Continue = False
        print(f"You loss, your score is {score}")
