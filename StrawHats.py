from battlePy.player import Player
from battlePy.default_config import (BOARD_WIDTH,
                                     BOARD_HEIGHT)
from battlePy.ship import UP, RIGHT
import random


class StrawHats(Player):
    def initPlayer(self, *args, **kwargs):
        self.name = 'Straw Hats'

    def newGame(self):
        self.shots = set()
        self.targetSet = set()
        self.shipBumper = set()

    def placeShip():
        pass
    def placeShips(self):
        for ship in self.ships:
          isValid = False
          while not isValid:
            orientation = random.choice([UP, RIGHT])
            if orientation == UP:
              location = (random.randint(0, BOARD_WIDTH - 1),
              random.randint(0, BOARD_HEIGHT - 1 - ship.size))
              for space in range(1,ship.size):
                spacePlus = space+1
                spaceMinus = space-1
                space1 = (location[0]+spacePlus, location[1])
                self.shipBumper.add(space1)
                space2 = (location[0], location[1]+spacePlus)
                self.shipBumper.add(space2)
                space3 = (location[0]-spaceMinus, location[1])
                self.shipBumper.add(space3)
                space4 = (location[0], location[1]-spaceMinus)
                self.shipBumper.add(space4)
            else:
              location = (random.randint(0, BOARD_WIDTH - 1 - ship.size),
              random.randint(0, BOARD_HEIGHT - 1))
            ship.placeShip(location, orientation)

            if self.isShipPlacedLegally(ship) and not self.shipBumper:
              isValid = True
            else:
              self.shipBumper = set()

    def fireShot(self):
        if not self.targetSet:
          shot = (random.randint(0, BOARD_WIDTH - 1),
                 random.randint(0, BOARD_HEIGHT - 1))

          while shot in self.shots:
            shot = (random.randint(0, BOARD_WIDTH - 1),
                    random.randint(0, BOARD_HEIGHT - 1))
        else:
          shot = self.targetSet.pop()
          while shot in self.shots:
            if not self.targetSet:
              while shot in self.shots:
                shot = (random.randint(0, BOARD_WIDTH - 1),
                random.randint(0, BOARD_HEIGHT - 1))
            else:
              shot = self.targetSet.pop()
        self.shots.add(shot)
        return shot 

    def addTargets(self, shot):
        if (shot[0]+1 >= 0) and (shot[0]+1 <= BOARD_WIDTH-1): 
          shot1 = (shot[0]+1, shot[1])
          self.targetSet.add(shot1)
        if (shot[1]+1 >= 0) and (shot[1]+1 <= BOARD_HEIGHT-1): 
          shot2 = (shot[0], shot[1]+1)
          self.targetSet.add(shot2)
        if (shot[0]-1 >= 0) and (shot[0]-1 <= BOARD_WIDTH-1): 
          shot3 = (shot[0]-1, shot[1])
          self.targetSet.add(shot3)
        if (shot[1]-1 >= 0) and (shot[1]-1 <= BOARD_HEIGHT-1): 
          shot4 = (shot[0], shot[1]-1)
          self.targetSet.add(shot4)

    def shotHit(self, shot, shipName):
        self.addTargets(shot)
    def shotMissed(self, shot):
        pass
    def opponentShot(self, shot):
        pass
    def shipSunk(self, shipName):
        pass
    def gameWon(self):
        pass
    def gameLost(self):
        pass
