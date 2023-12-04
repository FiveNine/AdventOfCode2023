import re
from typing import List

from datetime import datetime

startTime = datetime.now()

lines = []
with open('./input.txt') as f:
    lines = f.readlines()

class ScratchCard:
    def __init__(self, id, numberOfWinningCards):
        self.id = id
        self.numberOfWinningCards = numberOfWinningCards
        self.winningCards = []
    
    def updateWinningCards(self, listOfCards: List):
        nextId = self.id
        self.winningCards = listOfCards[nextId : nextId + self.numberOfWinningCards]
        return self

result = 0
cardInfo = []
for line in lines:
    l, r = line.split(' | ')
    game, winningNumbers = l.split(': ')
    game = game[-1]

    winningNumbers = re.findall(r'\d+', winningNumbers)
    
    rolledNumbers = re.finditer(r'\d+', r)
    
    matches = 0
    for num in rolledNumbers:
        if num.group() in winningNumbers:
            matches += 1
    
    cardInfo.append(matches)

# create ScratchCard objects
scratchCards : List[ScratchCard] = []
for i, card in enumerate(cardInfo):
    scratchCard = ScratchCard(i+1, card)
    scratchCards.append(scratchCard)

# go through again after list of ScratchCard objects is complete
# and set which cards this won
for scratchCard in scratchCards:
    scratchCard.updateWinningCards(scratchCards)

def getCardsWonForId(cardId):
    cardsWon = scratchCards[cardId-1].numberOfWinningCards
    for card in scratchCards[cardId-1].winningCards:
        cardsWon += getCardsWonForId(card.id)
    return cardsWon

cardsWon = 0
for card in scratchCards:
    cardsWon += getCardsWonForId(card.id) + 1
print(cardsWon)
