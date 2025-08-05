class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

london = City('London', 'England', 8900000, ['Big Ben', 'The Shard', 'London Bridge'])
tokyo = City('Tokyo', 'Japan', 9700000, ['Tokyo Tower', 'Meiji Jingu'])