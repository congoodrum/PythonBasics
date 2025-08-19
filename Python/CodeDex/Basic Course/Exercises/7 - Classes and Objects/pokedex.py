class Pokemon:
    entry: int
    name: str
    types: list[str]
    description: str
    is_caught: bool

    def __init__(self, entry: int, name: str, types: list[str], description: str, is_caught: bool):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    
    def speak(self):
        print(f'{self.name}, {self.name}')
    
    def display_details(self):
        print(f"""Entryt Number: {self.entry}
Name: {self.name}
Type: {self.types}
Description: {self.description}
""")
        if self.is_caught:
            print(f"{self.name} has already been caught")
        else:
            print(f"{self.name} has not yet been caught")

bulbasaur = Pokemon(1, 'Bulbasaur', ['Grass'], 'For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.', False)
charmander = Pokemon(4, 'Charmander', ['Fire'], 'The flame on its tail shows the strength of its life-force. If Charmander is weak, the flame also burns weakly.', False)
squirtle = Pokemon(4, 'Squirtle', ['Water'], 'TAfter birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth.', True)

bulbasaur.display_details()
charmander.display_details()
squirtle.speak()