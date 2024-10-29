import math

class Player:
    def __init__(self, name, hp = 10, xp = 0):
        self._name = name
        self._hp = hp
        self._xp = xp
    
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return 1 if self.xp < 300 else int(math.log2(self.xp / 300))
    
    @property
    def xp(self):
        return self._xp
    
    @property
    def hp(self):
        return self._hp
    
    @xp.setter
    def xp(self, value):
        if self._xp < value:
            self._xp = value
    @hp.setter
    def hp(self, value):
        if value <= 10: 
            self._hp = max(0, value)


# Creating a player with default hp and xp values
player1 = Player(name="Hero")

# Checking initial attributes
print(f"Name: {player1.name}")
print(f"HP: {player1.hp}")
print(f"XP: {player1.xp}")
print(f"Level: {player1.level}")

# Increasing XP and checking how the level changes
player1.xp = 100  # Should still be level 1
print(f"XP: {player1.xp}, Level: {player1.level}")

player1.xp = 300  # Should now be level 2
print(f"XP: {player1.xp}, Level: {player1.level}")

player1.xp = 1200  # Should be level 4
print(f"XP: {player1.xp}, Level: {player1.level}")

# Decreasing HP
player1.hp = 5  # Reduces HP to 5
print(f"HP: {player1.hp}")

player1.hp = -10  # Trying to set HP below 0, should remain at 0
print(f"HP: {player1.hp}")

# Attempting to reduce XP
player1.xp = 200  # Should not reduce XP, so it stays at 1200
print(f"XP: {player1.xp}, Level: {player1.level}")
