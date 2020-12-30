# Scope

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")  # 2


increase_enemies()
print(f"enemies outside function: {enemies}")  # 1


# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength) <- Error

# Global Scope

player_health = 10


def game():
    def drink_health_potion():
        print(player_health)

    drink_health_potion()


game()
print(player_health)

# There is no Block Scope

game_level = 3


def create_enemy():
    new_enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = new_enemies[0]

    print(new_enemy)


# Modifying Global Scope

monster = "Skeleton"
number_of_monsters = 1

def increase_monsters():
    monster = "Mega Zombie"
    global number_of_monsters
    number_of_monsters += 3
    print(f"Monster inside function: {monster}")


increase_monsters()
print(f"Monster outside function: {monster}")
print(number_of_monsters)
