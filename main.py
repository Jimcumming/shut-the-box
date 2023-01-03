# Simulates a game of Shut the Box to determine the odds of various strategies

import random

class ShutTheBoxGame:
    def __init__(self, strategy):
        self.boxes = list(range(1, 10))  # list of boxes, starting at 1 and ending at 9
        self.score = 0  # current score
        self.strategy = strategy  # selection strategy

    def roll_dice(self):
        """Roll the appropriate number of dice and return the sum."""
        if sum(self.boxes) > 6:
            num_dice = 2
        else:
            num_dice = 1

        roll = 0
        for i in range(num_dice):
            roll += random.randint(1, 6)

        return roll

    def find_combinations(self, roll):
        """Find all valid combinations of boxes that sum to the roll."""
        combinations = []
        for i in range(len(self.boxes)):
            for j in range(i+1, len(self.boxes)):
                if self.boxes[i] + self.boxgitges[j] == roll:
                    combinations.append((self.boxes[i], self.boxes[j]))
            if self.boxes[i] == roll:
                combinations.append((self.boxes[i],))

        return combinations

    def choose_combination(self, combinations):
        """Choose a combination of boxes based on the selection strategy."""
        if self.strategy == "random":
            # Choose a random combination
            combination = random.choice(combinations)
        elif self.strategy == "highest":
            # Choose the highest available numbers
            highest_numbers = []
            for combination in combinations:
                for box in combination:
                    if box in self.boxes:
                        highest_numbers.append(box)
            highest_numbers = sorted(highest_numbers, reverse=True)
            if len(highest_numbers) >= 2:
                combination = tuple(highest_numbers[:2])
            else:
                combination = tuple(highest_numbers)
        elif self.strategy == "lowest":
            # Choose the lowest available numbers
            lowest_numbers = []
            for combination in combinations:
                for box in combination:
                    if box in self.boxes:
                        lowest_numbers.append(box)
            lowest_numbers = sorted(lowest_numbers)
            if len(lowest_numbers) >= 2:
                combination = tuple(lowest_numbers[:2])
            else:
                combination = tuple(lowest_numbers)
        elif self.strategy == "middle":
            # Choose the middle available numbers
            middle_numbers = []
            for combination in combinations:
                for box in combination:
                    if box in self.boxes:
                        middle_numbers.append(box)
            middle_numbers = sorted(middle_numbers)
            if len(middle_numbers) >= 2:
                combination = tuple(middle_numbers[1:3])
            elif len(middle_numbers) == 1:
                combination = tuple(middle_numbers)
            else:
                combination = tuple()
        elif self.strategy == "odd":
            # Choose the highest odd number available, if any
            odd_numbers = []
            for combination in combinations:
                for box in combination:
                    if box in self.boxes and box % 2 == 1:
                        odd_numbers.append(box)
            if odd_numbers:
                combination = (max(odd_numbers),)
            else:
                # Choose the highest even number available, if any
                even_numbers = []
                for combination in combinations:
                    for box in combination:
                        if box in self.boxes and box % 2 == 0:
                            even_numbers.append(box)
                if even_numbers:
                    combination = (max(even_numbers),)
                else:
                    combination = tuple()

        elif self.strategy == "even":
            # Choose the highest even number available, if any
            even_numbers = []
            for combination in combinations:
                for box in combination:
                    if box in self.boxes and box % 2 == 0:
                        even_numbers.append(box)
            if even_numbers:
                combination = (max(even_numbers),)
            else:
                # Choose the highest odd number available, if any
                odd_numbers = []
                for combination in combinations:
                    for box in combination:
                        if box in self.boxes and box % 2 == 1:
                            odd_numbers.append(box)
                if odd_numbers:
                    combination = (max(odd_numbers),)
                else:
                    combination = tuple()

        return combination        


    def shut_boxes(self, combination):
        """Remove the boxes from the list and add their values to the score."""
        for box in combination:
            self.boxes.remove(box)
            self.score += box

    def play(self):
        """Play a single game of Shut the Box."""
        while self.boxes:  # while there are still boxes left
            roll = self.roll_dice()
            combinations = self.find_combinations(roll)

            # If there are no valid combinations, end the game
            if not combinations:
                break

            combination = self.choose_combination(combinations)
            self.shut_boxes(combination)

def simulate_games(num_games, strategy):
    """Simulate a number of games and return the odds of winning."""
    total_wins = 0  # number of times the player was able to shut all the boxes

    for i in range(num_games):
        game = ShutTheBoxGame(strategy)
        game.play()
        if not game.boxes:
            total_wins += 1

    # Calculate the odds of winning
    print(f'Total wins {total_wins} / Num games {num_games}')
    odds = total_wins / num_games
    return odds

# Simulate 10000 games for each strategy
random_odds = simulate_games(1000000, "random")
highest_odds = simulate_games(1000000, "highest")
lowest_odds = simulate_games(1000000, "lowest")
middle_odds = simulate_games(1000000, "middle")
even_odds = simulate_games(1000000, "even")
odd_odds = simulate_games(1000000, "odd")

# Print the odds of winning for each strategy
print(f"Odds of winning (random): {random_odds:.2f}")
print(f"Odds of winning (highest): {highest_odds:.2f}")
print(f"Odds of winning (lowest): {lowest_odds:.2f}")
print(f"Odds of winning (middle): {middle_odds:.2f}")
print(f"Odds of winning (even): {even_odds:.2f}")
print(f"Odds of winning (odd): {odd_odds:.2f}")

