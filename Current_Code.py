# IMPORTS
import random
import time
import os
import math
from pprint import pprint


# HERO Class

class hero:
    def __init__(self, Hmaxhealth, Hhealth, Hattack, Hluck, Hranged, Hdefence, Hmagic, Hname, Hlevel, Hexp):
    
        self.maxhealth = Hmaxhealth
        self.health = Hhealth
        self.attack = Hattack
        self.luck = Hluck
        self.ranged = Hranged
        self.defence = Hdefence
        self.magic = Hmagic
        self.name = Hname
        self.level = Hlevel
        self.exp = Hexp

    heroinv1 = {'name': '',
                'value': '',
                'stat': '', }
    heroinv2 = {'name': '',
                'value': '',
                'stat': '', }
    heroinv3 = {'name': '',
                'value': '',
                'stat': '', }

    # HERO Getters
    def getHealth(self):
        return self.health
    
    def getMaxHealth(self):
        return self.maxhealth
    
    def getAttack(self):
        return self.attack

    def getLuck(self):
        return self.luck

    def getRanged(self):
        return self.ranged

    def getDefence(self):
        return self.defence

    def getMagic(self):
        return self.magic

    def getLevel(self):
        return self.level

    def getExp(self):
        return self.exp

        # HERO Setters

    def setHealth(self, newHealth):
        self.health = newHealth

    def setAttack(self, newAttack):
        self.attack = newAttack

    def setLuck(self, newLuck):
        self.luck = newLuck

    def setRanged(self, newRanged):
        self.ranged = newRanged

    def setDefence(self, newDefence):
        self.defence = newDefence

    def setMagic(self, newMagic):
        self.magic = newMagic

    def setName(self, newName):
        self.name = newName

    def setLevel(self, newLevel):
        self.level = newLevel

    def setExp(self, newExp):
        self.exp = newExp

    def setMaxHealth(self,newMaxHealth):
        self.maxhealth = newMaxHealth
    
        # ENEMY CLASS


class enemy:
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename, Eexp, Egold, ):  # what can be passed into a class
        self.health = Ehealth  # Assigning these to a class
        self.attack = Eattack
        self.special = Especial
        self.chance = Echance
        self.name = Ename
        self.exp = Eexp
        self.gold = Egold

        # ENEMY Getters

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getSpecial(self):
        return self.special

    def getChance(self):
        return self.chance

    def getName(self):
        return self.name

    def getExp(self):
        return self.exp

    def getGold(self):
        return self.gold
        # ENEMY Setters

    def setHealth(self, newHealth):
        self.health = newHealth

    def setAttack(self, newAttack):
        self.health = newAttack

    def setSpecial(self, newSpecial):
        self.health = newSpecial

    def setChance(self, newChance):
        self.health = newChance

    def setName(self, newName):
        self.health = newName

    def setExp(self, newExp):
        self.exp = newExp

    def setGold(self, newGold):
        self.gold = newGold

    # inherit enemy class so boss will be a kind of child class of it


class boss(enemy):
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename, Eexp, Egold,
                 EsuperMove):  # Inherit the prevoius intakes same order + NEW at the end
        super().__init__(Ehealth, Eattack, Especial, Echance, Ename, Eexp,
                         Egold, )  # Shows what to inherit from parent class including defs
        # assigning and creting defs for NEW Attributes to the class
        self.superMove = EsuperMove

    def getSuper(self):
        return self.superMove

    def setSuper(self, newSuperMove):
        self.superMove = newSuperMove
    # now you can either create an enemy either by pluggin in these functions into an object or use some randomuizations with lists etc


def createClass():
    a = input("Please choose your starting character:\n(1) Warrior\n(2) Archer\n(3) Mage\n(4) Test Class\n")
    while a != '1' and a != '2' and a != '3' and a != '4':
        print("Plese Try again !")
        input(a)

    if a == '1':
        heroAttack = 10
        heroRanged = 0
        heroMagic = 0
        heroDefence = 11
        

    elif a == '2':
        heroAttack = 0
        heroRanged = 15
        heroMagic = 0
        heroDefence = 6
        
    elif a == '3':
        heroAttack = 0
        heroRanged = 0
        heroMagic = 17
        heroDefence = 4
        

    elif a == '4':
        heroAttack = 100
        heroRanged = 50
        heroMagic = 25
        heroDefence = 0
        
    heroLevel = 1
    heroExp = 0
    heroHealth = 100
    heroMaxHealth = 100
    
    

    b = input("Press enter to roll a dice...\n")
    time.sleep(0.2)
    print("Rolling dice...")
    heroLuck = random.randint(9, 15)
    print("Your hero has", heroLuck, "amount of luck out of 15")

    heroName = input("What is you name hero?\n")
    print("Welcome", heroName, "!!!")
    # passing attributes from a function into a list below                                    #Class Variables in a list
    return (heroMaxHealth, heroHealth, heroAttack, heroLuck, heroRanged, heroDefence, heroMagic, heroName, heroLevel, heroExp,)


def enemyGen(levelBoss):  # Takes in a boolean to see if it should spawn boss
    temp = []
    file = open('Adjectives.txt', 'r')
    lines = file.readlines()
    adjective = lines[random.randint(0, len(lines) - 1)][
                :-1]  # Choose a random line between first and laast position between 0 and amount of lines in the files -1 letter from the adjective
    file.close
    file = open('Animals.txt', 'r')  # Opend both to generate character name
    lines = file.readlines()
    animal = lines[random.randint(0, len(lines) - 1)][:-1]
    file.close

    if levelBoss == False:  # Spawning normal if boolean is False
        health = random.randint(50, 100)
        attack = random.randint(1, 15)
        special = random.randint(10, 20)
        chance = random.randint(1, 15)
        exp = random.randint(5, 20)
        gold = random.randint(1, 20)

        return enemy(health, attack, special, chance, adjective + ' ' + animal, exp,
                     gold)  # call the class enemy with these stuff pluged in and return

    else:  # If boolean is true GENERATE BOSS
        health = random.randint(100, 200)
        attack = random.randint(10, 30)
        special = random.randint(30, 50)
        chance = random.randint(6, 15)
        superMove = random.randint(50, 100)
        exp = random.randint(20, 50)
        gold = random.randint(20, 50)

        return boss(health, attack, special, chance, adjective + ' ' + animal,
                    superMove, exp, gold)  # call the class enemy with these stuff pluged in and return


def enemyAttack(hitChance, attackValue, name, defence):
    print(name, "is preparing to make an attack")
    hit = random.randint(1, 15)
    if hitChance > hit:
        print(name, "hits the hero!")
        loss = attackValue - defence
        if loss < 0:
            print("The attack didn't pierce your armor, you're lucky !")
            return 0

        else:
            pass
        print("You have just lost", loss, "health!")
        return math.ceil(loss)
    else:
        print(name, "missed the attack !")
        return 0


def hitChance(luck):
    hit = random.randint(0, 13)  #####MODIFY HIT CHANCE TO HERO/ENEMY LUCK RATIO####
    if luck < hit:
        print('Unlucky, You have missed the attack !')
        return False  # ??? EXPLAIN
    else:
        print("You have succesfully attacked the enemy.")
        return True  # ???  EXPLAINe


def isDead(health):
    if health < 1:
        return True
    else:
        return False
    
def checkXp(genEnemy, genCharacter):
        genCharacter.setExp(genCharacter.getExp() + genEnemy.getExp())
        print ("You have just gained", genEnemy.getExp(), "exp. You currently have", genCharacter.getExp(), 'exp.')

def levelUp(genCharacter):
    if genCharacter.getExp() >= 100:
            Levelup = 1
            genCharacter.setLevel(genCharacter.getLevel() + Levelup)
            genCharacter.setExp(0)
            genCharacter.setMaxHealth(genCharacter.getMaxHealth() + 10)
            print("You have just leveled up ! You are currently level", genCharacter.getLevel())
    else:
        pass

def loot(luck, genCharacter):
    lootChance = random.randint(0, 15)
    if luck < lootChance:
        print("You have examined the enemy, there is nothing worth taking.")
    else:
        tableNum = 0 #random.randint(0, 4)
        lootTableList = ["items", "ranged", "defence", "magic", "attack"]
        itemType = lootTableList[tableNum]
        file = open(itemType + '.txt', 'r')
        lines = file.readlines()

        print("You have examined the enemy and you have found a...")

        item = random.randint(0, len(lines) - 1)

        itemLine = lines[item]

        splitItemLine = itemLine.split(",")

        name = splitItemLine[0]
        value = int(splitItemLine[1])

        print(name)

        if itemType == "attack":
            genCharacter.setAttack(genCharacter.getAttack() + value)
            print("Your new malee attack is...")
            print(genCharacter.getAttack())

        elif itemType == "ranged":
            genCharacter.setRanged(genCharacter.getRanged() + value)
            print("Your new ranged attack is...")
            print(genCharacter.getRanged())

        elif itemType == "defence":
            genCharacter.setDefence(genCharacter.getDefence() + value)
            print("Your new defence is...")
            print(genCharacter.getDefence())

        elif itemType == "magic":
            genCharacter.setMagic(genCharacter.getMagic() + value)
            print("Your new magic attack is...")
            print(genCharacter.getMagic())

        else:

            if splitItemLine[2] == 'luck':
                genCharacter.setLuck(genCharacter.getLuck() + value)
                print("Your new Luck is...")
                print(genCharacter.getLuck())

            elif splitItemLine[2] == 'health':
                if genCharacter.getHealth() >= genCharacter.getMaxHealth():
                    print("Your health is at the maximum")
                    print(genCharacter.getHealth())
                elif genCharacter.getHealth() + value >= genCharacter.getMaxHealth():
                    genCharacter.setHealth(genCharacter.getMaxHealth())
                    print("Your new health is...")
                    print(genCharacter.getHealth())
                else:
                    genCharacter.setHealth(genCharacter.getHealth() + value)
                    print("Your new health is...")
                    print(genCharacter.getHealth())

def gameOver(enemyDead):
    if enemyDead == True:
        print("Time for another battle!!")

    else:
        print("You have died..")
        print("Better luck next time!!")
        exit()




def battle(genEnemy, genCharacter):
    print("whats that coming over the hill??")
    print("It's a ...'", genEnemy.getName(), "'looking for a fight!")
    print("Check out its stats...")
    pprint(vars(genEnemy))

    battle = True

    while battle == True:

        print('1. Sword Attack\n2. Ranged Attack\n3. Magic Attack')
        choice = input()

        while choice != '1' and choice != '2' and choice != '3':
            print('OOPS..Try again...')
            print('1. Sword Attack\n2. Ranged Attack\n3. Magic Attack\n')
            choice = input()

        if choice == '1':
            damage = genCharacter.getAttack()

        elif choice == '2':
            damage = genCharacter.getRanged()

        elif choice == '3':
            damage = genCharacter.getMagic()

        print('You wind up for the attack !!!')
        hit = hitChance(genCharacter.getLuck())

        if hit == True:
            genEnemy.setHealth(genEnemy.getHealth() - damage)
            print(' You have hit the enemy !!')
            print("The Enemies health is now...", genEnemy.getHealth())

        else:
            print("Your attack missed!")

        enemyDead = isDead(genEnemy.getHealth())

        if enemyDead == False:
            genCharacter.setHealth(
                genCharacter.getHealth() - enemyAttack(genEnemy.getChance(), genEnemy.getAttack(), genEnemy.getName(),
                                                       genCharacter.getDefence()))

            characterDead = isDead(genCharacter.getHealth())

            if characterDead == True:
                battle = False
                return False

            else:
                print("Your characters remaining health is...", genCharacter.getHealth())

        else:
            battle = False
            print("You have defeated the enemy!")
            print("did it drop any loot?...")

            loot(genCharacter.getLuck(), genCharacter)

            checkXp(genEnemy, genCharacter)
            levelUp(genCharacter)

            return True


def levelGenerator(character, level):
    maxNumberOfEnemies = math.ceil(level * 5)
    print('The amount of enemies on the current level is', maxNumberOfEnemies)

    for x in range(0, maxNumberOfEnemies):
        bossChance = random.randint(1, 10)

        if bossChance > 8:
            levelBoss = True
        else:
            levelBoss = False

        characterDead = battle(enemyGen(levelBoss), character)  # fight will generate result true or false
        gameOver(characterDead)  # will check generated result so see if game continues


def main():
    print("Welcome to Desktop Adventures\nVersion 0.1")
    classData = createClass()
    character = hero(classData[0], classData[1], classData[2], classData[3], classData[4], classData[5], classData[6], classData[7],
                     classData[8], classData[9])
    pprint(vars(character))
    print("Level 1 out of 5...")
    levelGenerator(character, 1)
    print("Level 2 out of 5...")
    levelGenerator(character, 2)
    print("Level 3 out of 5...")
    levelGenerator(character, 3)
    print("Level 4 out of 5...")
    levelGenerator(character, 4)
    print("Level 5 out of 5...")
    levelGenerator(character, 5)
    print("You Won!!!")
    pprint(vars(character))

main()