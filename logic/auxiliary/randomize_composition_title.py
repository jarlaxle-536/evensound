import faker

class CompositionTitleRandomizer:
    def __init__(self):
        self.faker = faker.Faker()
    def action(self):
        self.title = faker.sentence()
