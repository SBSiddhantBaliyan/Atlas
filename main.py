import random
from locations import locations

class AtlasGame:
    def __init__(self):
        self.locations = locations  # locations is a set
        self.used_names = set()

    def get_last_letter(self, name: str) -> str:
        """Returns the last alphabet letter in a given name."""
        for ch in reversed(name.lower()):
            if ch.isalpha():
                return ch
        return ''

    def valid_next_names(self, last_letter: str) -> list:
        """Returns a list of locations that start with the given last letter and unused."""
        return [name for name in self.locations if name.lower().startswith(last_letter) and name not in self.used_names]

    def user_turn(self, last_letter: str) -> str:
        """Gets the next location from the player."""
        while True:
            name = input(f"Your turn (start with '{last_letter.upper()}'): ").strip()
            if not name:
                print("Please enter a name.")
                continue
            if name in self.used_names:
                print("That name is already used. Try again.")
                continue
            if name not in self.locations:
                print("Name not recognized or not in dataset. Try again.")
                continue
            if name[0].lower() != last_letter:
                print(f"Name must start with '{last_letter.upper()}'. Try again.")
                continue
            self.used_names.add(name)
            return name

    def ai_turn(self, last_letter: str) -> str:
        """Gets the next location from AI."""
        options = self.valid_next_names(last_letter)
        if not options:
            print("I can't think of any more names. You win! 🎉")
            return None
        choice = random.choice(options)
        self.used_names.add(choice)
        print(f"My turn: {choice}")
        return choice

    def play(self):
        """Starts the game."""
        current_name = random.choice(list(self.locations))
        self.used_names.add(current_name)
        print(f"My start: {current_name}")

        while True:
            last_letter = self.get_last_letter(current_name)
            user_word = self.user_turn(last_letter)
            current_name = user_word

            if not user_word:
                break
            last_letter = self.get_last_letter(user_word)
            ai_word = self.ai_turn(last_letter)
            if not ai_word:
                break
            current_name = ai_word

if __name__ == "__main__":
    game = AtlasGame()
    game.play()