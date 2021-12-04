import numpy as np

def readInput(filename):
    with open(filename, 'r') as f:
        data = f.readlines()

    return data

class Bingo:

    def __init__(self, inputData):
        self.parseInput(inputData)
    
    def parseInput(self, data):
        self.draws = [int(draw) for draw in data[0].split(',')]

        self.cards = []
        for row in range(2, len(data), 6):
            cardData = data[row:row+5]
            cardNumbers = np.ndarray((5,5))
            for i, row in enumerate(cardData):
                cardNumbers[i] = [int(row[j:j+2]) for j in range(0, len(row), 3)]
            self.cards.append(Card(cardNumbers))

    def part1(self):
        for currentDraw in self.draws:
            for card in self.cards:
                hit = card.checkNumber(currentDraw)
                if hit:
                    isBingo = self.checkBingo(card)
                    if isBingo:
                        return currentDraw * card.sumOfUnmarkedNumers()
        return 0

    def part2(self):
        cards = self.cards
        for currentDraw in self.draws:
            cardsLeft = []
            for card in cards:
                hit = card.checkNumber(currentDraw)
                isBingo = False
                if hit:
                    isBingo = self.checkBingo(card)
                if not isBingo:
                    cardsLeft.append(card)
            cards = cardsLeft
            if len(cardsLeft) == 0:
                return currentDraw * card.sumOfUnmarkedNumers()
            

    def checkBingo(self, card):
        for i in range(5):
            if np.sum(card.checked[i,:]) == 5 or np.sum(card.checked[:,i]) == 5:
                return True
        return False


class Card:
    def __init__(self, inputData):
        self.numbers = inputData
        self.checked = np.zeros((5,5))

    def checkNumber(self, number):
        ind = np.where(self.numbers == number)
        if ind[0].size != 0:
            self.checked[ind[0], ind[1]] = 1
            return True
        return False

    def sumOfUnmarkedNumers(self):
        return np.sum((self.checked - 1) * self.numbers * -1)

if __name__ == "__main__":
    data = readInput("Day4/input.txt")

    bingo = Bingo(data)

    result1 = bingo.part1()
    print(result1)

    result2 = bingo.part2()
    print(result2)