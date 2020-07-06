
def ssprint(Msg):
    print(f'    {Msg}\n')


class Subordinates:
    def __init__(self):
        self.starting_state = []
        self.subordinates = {'Special S': [], 'S': [], 'Special A': [], 'A+': [], 'A': [],
                             'A-': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'Other': [],
                             }

    def generator(self, character=None):
        """
        Yields the subordinates under specified character.
        """

        for level, sub_list in self.subordinates.items():
            for subordinate in sub_list:
                yield subordinate

    def add(self, name, character):
        """
        Naming subordinates and give blessing.

        Args:
            name: Set name to new subordinates.
            character: Character name or object to be named.

        Usage:
            .add('Tempest Wolf', 'Ranga')
        """

        char = self.get_object(character, sub=True)
        char.name = name
        char.blessing = self.shared_blessing
        if char.species in self.subs:
            self.subs[char.species].append(char)
        else:
            self.subs[char.species] = list([char])
