from random import randint


class Bot:

    def __init__(self, bot_pseudo, bot_health, bot_damage):
        self.bot_pseudo = bot_pseudo
        self.bot_health = bot_health
        self.bot_damage = bot_damage

    def get_bot_pseudo(self):
        return self.bot_pseudo

    def get_bot_health(self):
        return self.bot_health

    def get_bot_damage(self):
        return self.bot_damage

    def bot_damaged(self, damage):
        self.bot_health -= damage


class Player:

    def __init__(self, pseudo, health, damage):
        self.pseudo = pseudo
        self.health = health
        self.damage = damage

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage


turns = 0


def bot_win():
    print(" ")
    print("It seems you have lost all your PVs and died...")
    print("Maybe after all that", bot.get_bot_pseudo(), "was to strong for you...")
    print("It needed", turns, "turns to", bot.get_bot_pseudo(), "to kill you.")
    quit()


def player_win():
    print(" ")
    print("Y O U   W O N !")
    print("GG!")
    print("It needed you", turns, "to kill that", bot.get_bot_pseudo())
    quit()


def player_damaged(damage):
    player.health -= damage


def bot_turn():
    global turns
    turns += 1
    if bot.bot_health <= 0:
        player_win()
    bot_action = randint(1, 2)
    if bot_action == 1:
        player_damaged(bot.get_bot_damage())
        print("Ouch... That was bad.", bot.get_bot_pseudo(), "hurt you and dealt you", bot.get_bot_damage(), "damages.")
        print("You now have", player.get_health(), "PV.")
        player_turn()
    if bot_action == 2:
        bot_restoring_health = randint(5, 7)
        bot.bot_health += bot_restoring_health
        print(bot.get_bot_pseudo(), "healed itself and now has", bot.get_bot_health(), "PV.")
        player_turn()


def player_turn():
    if player.health <= 0:
        bot_win()
    print("Your PV: ", player.get_health(), "     ", bot.get_bot_pseudo(), "PV: ", bot.get_bot_health())
    print(" ")
    print("Your turn! You can:")
    print("1) Attack   2) Heal   3) Skip")
    try:
        enter = int(input("> "))
        if enter == 1:
            bot.bot_damaged(player.get_damage())
            print("Wonderful! You damaged", bot.get_bot_pseudo(), "and dealt it", player.get_damage(), "damages.")
            print(bot.get_bot_pseudo(), "now has", bot.get_bot_health(), "PV.")
        elif enter == 2:
            restoring_health = randint(5, 11)
            player.health += restoring_health
            print("You restored", restoring_health, "PV and you are now", player.get_health(), "PV.")
        elif enter == 3:
            bot_turn()
        bot_turn()
    except ValueError:
        print("Error: Incorrect value!")
        quit()


def game_startup():
    print(player.get_pseudo(), "has joined the game.")
    print(bot.get_bot_pseudo(), "has joined the game.")
    player_turn()


def correct_pseudo(pseudo):
    if pseudo == "Bot":
        print("Your pseudo cannot be Bot! Choose another!")
        quit()


try:
    pseudo = str(input("Choose a pseudo: "))
    correct_pseudo(pseudo)
except ValueError:
    print("Error: Incorrect value!")

player = Player(pseudo, 100, 10)
bot = Bot("Bot", 100, 10)
game_startup()
