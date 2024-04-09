import alien
import random
import sys
import boss
import time

class Player:
#player stats
  def __init__ (self):
    self.defense = 5
    self.attack = 5
    self.health = 5
    self.level = 1
    self.name = ""
    self.exp = 0
    self.times_defended = 1
    self.times_parried = 0
    self.money = 100
    self.m = 0

#delayed print
  def d_print_p (self, word, delay = .03):
    for i in word:
      sys.stdout.write(i)
      time.sleep(delay)
      sys.stdout.flush()
    print("")

#player name    
  def player_name(self):
    self.name = input ("What's your name?") 

#level up  
  def level_up(self):
    self.level += 1
    self.defense += 3
    self.attack += 3
    self.health += 5

#attack    
  def player_attack(self,al):
    self.times_parried = 0
    if self.attack <= al.defense:
      al.health -= 1
      return 1
    else:
      self.attack -= al.defense
      al.health -= self.attack
      self.attack += al.defense
      return self.attack - al.defense 

#defend      
  def player_defend(self):
    self.times_defended += 1                                              
    self.defense += (self.times_defended * self.level)
    self.times_parried = 0

#parry                                              
  def player_parry (self, al):             
    if al.current_move == "attack":                                              
      al.defense /= 2
      dmg = self.player_attack(al)                 
      al.defense *=2                                              
      self.times_parried = 1
      self.d_print_p ("You did " + str(dmg) + " damage.")
      al.current_move = "parried"
    elif al.current_move != "attack":   
      self.d_print_p ("You missed your parry.")  
      self.times_parried = 1

      
      
#xp gain                                                    
  def xp_check (self):                                              
    if self.exp >= 100:                          
    
      self.level_up()   
      self.d_print_p ("Congrats! You have leveled up! Your stats have improved!")                              
      self.exp += 100   
      self.level += 1                                           
     # self.xp_check()                                              
 
  def xp_gain(self,al):
    base = random.randint(25,35)
    multiplier = 0
    if al.level == self.level:
      self.exp += base
      self.d_print_p("Nice job! You earned "+str(base)+" exp!\n")
    elif al.level > self.level:
      for i in range (1,al.level - self.level + 1):
        multiplier += i/6
      final = (base * multiplier) + base
      self.exp += round(final)
    else:
      for i in range (1,al.level - self.level + 1):
        multiplier += i/6
      final = base - (base * multiplier)
      self.exp += round(final) 
    self.d_print_p("You have "+str(self.exp)+" exp!\n")
    self.xp_check()

  def xp_hack(self,addedxp):
    self.exp += addedxp
    self.d_print_p ("You added " + str(addedxp) + " xp\n")
#money
  def add_money (self,al):
    self.m = al.level*100 - self.level*100
    if self.m <= 0:
      self.m = 100
    self.money += self.m
    self.d_print_p ("The alien dropped " + str(self.m) + " money.\n")
    self.d_print_p ("You now have" + str(self.m) + " money.\n")


    ''''
    if self.level == alien.level:
      self.money += 100
      self.d_print_p ("The alien dropped " + str(100) + " money\n")
    elif self.level == 1 and alien.level == 2:
      self.money += 200
      self.d_print_p ("The alien dropped " + str(200) + " money\n")
    elif self.level == 1 and alien.level == 3:
      self.money += 300
      self.d_print_p ("The alien dropped " + str(300) + " money\n")
    elif self.level == 2 and alien.level == 1:
      self.money += 50
      self.d_print_p ("The alien dropped " + str(50) + " money\n")
    elif self.level == 2 and alien.level == 3:
      self.money += 200
      self.d_print_p ("The alien dropped " + str(200) + " money\n")
    elif self.level == 3 and alien.level == 1:
      self.money += 25
      self.d_print_p ("The alien dropped " + str(25) + " money\n")
    elif self.level == 3 and alien.level == 2:
      self.money += 50
      self.d_print_p ("The alien dropped " + str(50) + " money\n")
'''
 