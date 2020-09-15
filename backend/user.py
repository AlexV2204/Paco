class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.nb_player = "1"

    def create_user(self):
        self.user_name = input("Quel est votre nom ? ")
        print("Bonjour", self.user_name, "!")

    def generate_players(self):
        while self.nb_player.isnumeric():
            self.nb_npc = input("Combien d'adversaire souhaitez-vous avoir ? ")
        self.nb_player = int(self.nb_player) + int(self.nb_npc)


if __name__ == "__main__":
    user = User("")
    user.create_user()