import turtle
import time
import random

class RaceSimulator:
    WIDTH, HEIGHT = 500, 500
    COLORS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]

    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(self.WIDTH, self.HEIGHT)
        self.screen.title("Turtle Racing Simulation")
        self.racers = self.number_of_racers()
        random.shuffle(self.COLORS)
        self.colors = self.COLORS[:self.racers]

    def number_of_racers(self):
        """
        Prompts the user to enter the number of racers (2-10).
        """
        while True:
            racers = input("Enter the number of racers! [2-10] ")
            if racers.isdigit():
                racers = int(racers)
            else:
                print("Invalid input! Try again.")
                continue

            if 2 <= racers <= 10:
                return racers
            else:
                print("Number is not in range of 2 to 10. Try again!")

    def create_turtles(self, colors):
        """
        Creates turtle objects for each racer with given colors.
        """
        turtles = []
        spacing_x = self.WIDTH // (len(colors) + 1)
        for i, color in enumerate(colors):
            racer = turtle.Turtle()
            racer.color(color)
            racer.shape("turtle")
            racer.left(90)
            racer.penup()
            racer.setpos(-self.WIDTH//2 + (i+1) * spacing_x, -self.HEIGHT//2 + 20)
            racer.pendown()
            turtles.append(racer)

        return turtles

    def race(self):
        """
        Executes the turtle race simulation.
        """
        turtles = self.create_turtles(self.colors)

        while True:
            for racer in turtles:
                distance = random.randrange(1, 20)
                racer.forward(distance)

                x, y = racer.pos()
                if y >= self.HEIGHT // 2 - 10:
                    return self.colors[turtles.index(racer)]

    def run_simulation(self):
        """
        Runs the entire turtle racing simulation.
        """
        winner = self.race()
        print(f"The winner is the turtle with color {winner}")
        time.sleep(5)
        self.screen.bye()

if __name__ == "__main__":
    simulator = RaceSimulator()
    simulator.run_simulation()
