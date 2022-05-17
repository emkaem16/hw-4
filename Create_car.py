class Car:
    def __init__(self, title, model):
        self.title = title
        self.model = model


class Carrss(Car):
    def __init__(self, title, model, color):
        super().__init__(title, model)
        self.color = color

    def start_engine(self):
        print(f"Engine {self.title} {self.model} {self.color} started!")

    def stop_engine(self):
        print(f"Engine {self.title} {self.model} {self.color} stoped!\n")

    def get_car_info(self):
        print(f'\n{self.title} {self.model} {self.color}')