from models import MealModel

class MealService:
    def __init__(self):
        self.model = MealModel()

    def create(self, params):
        return self.model.create(params)

    def update(self, day, params):
        return self.model.update(day, params)

    def delete(self, day):
        return self.model.delete(day)

    def list(self):
        return self.model.list_items()

    def get_by_day(self, day):
        return self.model.get_by_day(day)