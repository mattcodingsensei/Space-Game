import alien
import player
import boss
import planet
import time
import random
import sys

words = ""

player = player.Player()
enemy = alien.Alien(player)
boss = boss.Boss(player)


def dType(words, delay=0.0004):
  for s in words:
    sys.stdout.write(s)
    time.sleep(delay)
    sys.stdout.flush()

dType(words)

#player commands: travel to planet | travel to next galaxy | find a new planet to travel to | start / end game

galaxy = 1
fuel = 0
reso = 0
level = 0
exp = 0

#al = alien.Alien()
pl = planet.Planet(galaxy)
pl.genPlanet()
#print(pl.name)
#pl.describe() = ""

  #print("While you were gathering materials, a strange creature attacked you!")


playing = True

def start():
  # player.name(self)
  dType("Are you ready to start your adventure? [yes|no]")
  start = input()
  if start.upper() == "Y" or start.upper() == "YES":
    dType("Great! Let's start!\n")
    time.sleep(1)
    print(".")
    time.sleep(.5)
    dType("Here are your commands:\n")
    time.sleep(.5)
    dType("Type [travel] to get info and travel to a new planet.\n")
    time.sleep(.5)
    dType("Type [galaxy] to travel to the next galaxy (if you have the requirements to do so)\n")
    time.sleep(.5)
    dType("Type [status] to see your health, fuel and resource levels, etc. \n")
    time.sleep(.5)
    dType("Type [end] to end the game.\n")
    time.sleep(.5)
    dType("And you can type [explain] to see the commands again!")
    print(".")
  elif start.upper() == "N" or start.upper() == "NO":
    exit()
def gameO():
  dType("Game Over...\n")
  time.sleep(2)
  dType("You have failed to reach earth...\nThough you can restart and try again!\n")
  time.sleep(1)
  sys.exit()

def shop():
    dType("Welcome to my shop, traveler.\n")
    time.sleep(0.4)
    dType("1: Health Potion(+1-4 health)\n")
    dType("2: More Durrable Shield(+10 defense)\n")
    dType("3: Sharpened Light Sword(+5 attack)\n")
    answer = int(input("What would you like to buy?\n"))
    if answer == 1 and player.money >= 50:
      dType("You gained health!!\n")
      player.health += random.randint(1,4)
      dType("You now have "+ str(player.health)+ " health!\nYou are satisfied and have left the planet.\n")
      time.sleep(1)
      player.money -= 50
    elif answer == 2 and player.money >= 50:
      dType("You bought the shield!\n")
      dType("You leave the planet with even better defense!\n")
      player.money -= 25
      player.defense += 10
      time.sleep(1)
    elif answer == 3 and player.money >= 50:
      dType("You bought the sharpened sword!\n")
      dType("You leave the planet with better attack!\n")
      time.sleep(1)
      player.money -= 50
      player.attack+=5
    else:
      dType("Sorry, you don't have enough money...\n")
      shop()

def bossBattle():
  battle_end = False
  dType("You ran into the boss The Almighty One\n\n")
  boss.gen_stats(1)
  #boss_stats()
  print("")
  stats
  print("")
  while battle_end == False:
    dType ("What do you want to do?\n")
    dType ("[Attack|Defend|Run|Parry]")
    answer = input ("-")
    print
    if answer.upper() == ("ATTACK"):
      dType ("You did damage.")
      dType ("The alien's health is now\n")
      boss.boss_choice()
      boss.boss_action(player)
    #defend
    elif answer.upper() == ("DEFEND"):
      player.player_defend()
      print
      dType ("Your defense has improved.\n")
      print
      stats()
      print
      boss.boss_choice()
      boss.boss_action(player)
    #parry
    elif answer.upper() == ("PARRY"):
      if player.times_parried == 0:
        boss.boss_choice()
        player.player_parry(boss)
        boss.boss_action(player)
      else:
        dType ("You can't parry twice in a row.\n")
    #run
    elif answer.upper() == ("RUN"):
      dType ("You ran away from the alien.\n")
      print
      escape =  random.randint(1,5)
      if escape == 1 or escape == 2:
        dType ("You escaped.\n")
        print
        battle_end = True
      elif escape == 3 or escape == 4:
        player.health -= 2
        dType ("You escaped, but the alien did damage before you could get away. Your health is now " + str(player.health) + ".\n")
        print
        battle_end = True
      elif escape == 5:
        dType ("You didn't escape. And the alien had an opportunity to attack.\n")
        boss.boss_attack(player)
        dType ("Your health is now " + str(player.health)+"\n")
        print
    else:
      dType ("That's not a command.")
    if player.health < 1 and boss.health < 1:
      battle_end = True
      dType ("You killed the alien, but it wounded you and you died before you could get back to your ship.\n")
      time.sleep(1)
      gameO()
    
    #end of battle you win
    elif boss.health < 1:
      dType ("You vanquished the boss.!\n")
      dType("You can now continue your journey on this planet.\n")
      battle_end = True
      player.xp_gain(boss)
      player.add_money(alien)
      player.xp_check()
      #end of battle you lose   
    elif player.health < 1:
      battle_end = True
      dType ("You died.\n")
      time.sleep(1)
      gameO()


def battle ():
  battle_end = False
  dType ("You ran into a " + str(enemy.alien_name)+"\n")
  print
  enemy.gen_stats(1)
  enemy_stats()
  print
  stats()
  print
  while battle_end == False:
    dType ("What do you want to do?\n")
    dType ("[Attack|Defend|Run|Parry]")
    answer = input ("-")
    print
    if answer.upper() == ("ATTACK"):
      dType ("You did " +str(player.player_attack(enemy)) + " damage.\n")
      dType ("The alien's health is now " + str(enemy.health) + ".\n")
      enemy.enemy_choice()
      enemy.enemy_action(player)
    #defend
    elif answer.upper() == ("DEFEND"):
      player.player_defend()
      print
      dType ("Your defense has improved.\n")
      print
      stats()
      print
      enemy.enemy_choice()
      enemy.enemy_action(player)
    #parry
    elif answer.upper() == ("PARRY"):
      if player.times_parried == 0:
        enemy.enemy_choice()
        player.player_parry(enemy)
        enemy.enemy_action(player)
      else:
        dType ("You can't parry twice in a row.\n")
    #run
    elif answer.upper() == ("RUN"):
      dType ("You ran away from the alien.\n")
      print
      escape =  random.randint(1,5)
      if escape == 1 or escape == 2:
        dType ("You escaped.\n")
        print
        battle_end = True
      elif escape == 3 or escape == 4:
        player.health -= 2
        dType ("You escaped, but the alien did damage before you could get away. Your health is now " + str(player.health) + ".\n")
        print
        battle_end = True
      elif escape == 5:
        dType ("You didn't escape. And the alien had an opportunity to attack.\n")
        enemy.enemy_attack(player)
        dType ("Your health is now " + str(player.health)+"\n")
        print
    else:
      dType ("That's not a command.")
    if player.health < 1 and enemy.health < 1:
      battle_end = True
      dType ("You killed the alien, but it wounded you and you died before you could get back to your ship.\n")
      time.sleep(1)
      gameO()
    
    #end of battle you win
    elif enemy.health < 1:
      dType ("You vanquished the enemy.!\n")
      dType("You can now continue your journey on this planet.\n")
      battle_end = True
      player.xp_gain(enemy)
      # player.add_money()
      player.xp_check()
      #end of battle you lose   
    elif player.health < 1:
      battle_end = True
      dType ("You died.\n")
      time.sleep(1)
      gameO()

def plCmds():
  global reso
  global fuel
  aq = input("What would you like to do at "+pl.name+"? [mine | rest | shop | leave]")
  if aq.upper() == "MINE":
    dType("You went out to mine for resources")
    time.sleep(0.6)
    dType(".")
    time.sleep(0.6)
    dType(".")
    time.sleep(0.6)
    dType(".\n")
    chance = random.randint(1,2)
    if chance == 1:
      dType(" Congrats! You found "+str(pl.reso)+" resources and "+str(pl.fuel)+" fuel!\n")
      reso += pl.reso
      fuel += pl.fuel
      time.sleep(0.7)
      dType("You are satisfied and have left the planet.\n")
      time.sleep(1)
      replit.clear()
    
    else:
      dType("While you were mining for resources, you ran into a strange creature!\n")
      battle()
      if galaxy == 1:
        enemy.gen_stats(random.randint(1,2))
      elif galaxy == 2:
        enemy.gen_stats(random.randint(3,5))
      else:
        enemy.gen_stats(random.randint(6,9))
      enemy.gen()
      plCmds()


  elif aq.upper() == "SHOP":
    shop()
      
  elif aq.upper() == "REST":
    sleepChance = random.randint(1,4)
    if sleepChance == 1:
      dType("You spent the night at "+str(pl.name)+".\n You had a horrible sleep and earned 0 hp.\n")
      time.sleep(0.4)
      dType("You leave the planet very angry.\n")
    elif sleepChance == 2:
      dType("You spent the night at "+str(pl.name)+".\n You had an okay sleep and earned 1 hp!\n")
      player.health += 1
      time.sleep(0.4)
      dType("You leave the planet feeling okay.\n")
    elif sleepChance == 3:
      dType("You spent the night at "+str(pl.name)+".\n You had a good sleep and earned 3 hp!\n")
      player.health += 3
      time.sleep(0.4)
      dType("You leave the planet feeling great!\n")
    else:
      dType("You spent the night at "+str(pl.name)+".\n You had an AMAZING sleep and earned 5 hp!\n")
      player.health += 5
      time.sleep(0.4)
      dType("You leave the planet feeling outstanding!\n")
  elif aq.upper() == "LEAVE":
    dType("Leaving "+pl.name)
    time.sleep(0.8)
    dType(".")
    time.sleep(0.8)
    dType(".")
    time.sleep(0.8)
    dType(".\n")
    time.sleep(1)
    replit.clear()
  else:
    plCmds()

def stats ():
  dType ("Your stats\n")
  dType ("Level " + str(player.level)+"\n")
  dType ("Health " + str(player.health)+"\n")
  dType ("Attack " + str(player.attack)+"\n")
  dType ("Defense " + str(player.defense)+"\n")

def enemy_stats():
  dType ("The alien's stats\n")
  dType ("Level " + str(enemy.level)+"\n")
  dType ("Health " + str(enemy.health)+"\n")
  dType ("Attack " + str(enemy.attack)+"\n")
  dType ("Defense " + str(enemy.defense)+"\n") 

def cmds():
  global fuel
  global reso
  global galaxy
  global exp
  time.sleep(2)
  dType("What would you like to do next?\n")
  ask = input()
  if ask.upper() == "TRAVEL":
    dType("Finding a planet")
    time.sleep(0.8)
    dType(".")
    time.sleep(0.8)
    dType(".")
    time.sleep(0.8)
    dType(". \n")
    time.sleep(random.randint(1, 5))
    dType("Planet located!\n")
    time.sleep(0.5)
    pl.genPlanet()
    pl.describe()
    dType("Do you want to travel to this planet? [y | n]")
    travel = input()
    if travel.upper() == "Y" or travel.upper() == "YES":
      curPlanet = pl
      dType("Traveling to "+pl.name)
      time.sleep(0.8)
      dType(".")
      time.sleep(0.8)
      dType(".")
      time.sleep(0.8)
      dType(".\n")
      time.sleep(1)
      replit.clear()
      plCmds()

      
    
  if ask.upper() == "GALAXY":
    if galaxy == 1:
      if fuel >= 60 and reso >= 60:
        galaxy += 1
        pl.nextGal()
        dType("You have earned enough materials to head to the next galaxy!\n")
        fuel = 0
        reso = 0
        time.sleep(1)
        replit.clear()
      else:
        dType("Oh no! It seems you don't have enough resources and/or fuel!\n")
        time.sleep(0.4)
        dType("Head back to other planets to look for those items!\n")
    elif galaxy == 2:
      if fuel >= 70 and reso >= 70:
        galaxy += 1
        fuel = 0
        reso = 0
        pl.nextGal()
        dType("You have earned enough materials to head to the next galaxy!\n")
        replit.clear()
      else:
        dType("Oh no! It seems you don't have enough resources and/or fuel!\n")
        time.sleep(0.4)
        dType("Head back to other planets to look for those items!\n")
        replit.clear()
    elif galaxy == 3:
      if fuel >= 100 and reso >= 100:
        galaxy += 1
        dType("Congrats! You have gathered enough resources and fuel to head back to your home planet!\n")
        time.sleep(1)
        dType("You have beat the game and get to live a good life away from all danger!")
        exit()
      else:
        dType("Oh no! It seems you don't have enough resources and/or fuel!\n")
        time.sleep(0.4)
        dType("Head back to other planets to look for those items!\n")
  if ask.upper() == "EXPLAIN":
    print(".")
    time.sleep(1.5)
    dType("Here are your commands:\n")
    time.sleep(1.5)
    dType("Type [travel] to get info and travel to a new planet.\n")
    time.sleep(1.5)
    dType("Type [galaxy] to travel to the next galaxy (if you meet the requirements to do so)\n")
    time.sleep(1.5)
    dType("Type [end] to end the game.\n")
    time.sleep(1.5)
    dType("Finally, type [explain] to read the commands again!")
    print(".")
  if ask.upper() == "END":
    exit()
  if ask.upper() == "STATUS":
    dType("Your fuel level is "+str(fuel)+"\n")
    time.sleep(1)
    dType("Your resource level is "+str(reso)+"\n")
    time.sleep(1)
    dType("You are in galaxy "+str(galaxy)+"\n")
    time.sleep(1)
    player.xp_check()
    dType("Your health is  "+ str(player.health)+"\n")
    time.sleep(1)
    dType ("Your attack is " + str(player.attack)+"\n")
    time.sleep(1)
    dType ("Your defense is " + str(player.defense)+"\n")
    time.sleep(1)
    dType("You are level "+str(player.level)+"\n")
    time.sleep(1)
    dType("You have "+str(player.exp)+" exp\n")
    time.sleep(1)
    dType("You have "+str(player.money)+" moneys\n")

  if ask.upper() == "SKIP":
    galaxy += 1
    pl.nextGal()
  if ask.upper() == "NOTHING":
    dType("Well ok then")
    exit()
  if ask.upper() == "EXP":
    player.exp += 100
  if ask.upper() == "LVLUP":
    player.xp_hack(145)
  if ask.upper() == "BATTLE":
    battle()
  if ask.upper() == "GIVEMEACOOKIE":
    player.money += 10000
  if ask.upper() == "PLANET":
    pl.genPlanet()
    plCmds()

    
      
start()
while playing:
  cmds()