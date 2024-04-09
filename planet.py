import random
import time
import sys
class Planet:
  def __init__(self, t):
    self.fuel = ""
    self.reso = ""
    self.tier = t
    self.name = ""
    self.temp = ""
    
  def dType(self, words, delay=0.05):
    for s in words:
        sys.stdout.write(s)
        time.sleep(delay)
        sys.stdout.flush()
        
  def genPlanet(self):
    tp = ["Freezing", "Cold", "Temperate", "Hot", "Burning"]
    g1 = ["Pohz", "Epes", "Xes", "Eno", "Nya"]
    g2 = ["Vie", "Dypxo", "Yro", "Linif", "Luag", "Oux", "Nuca",]
    g3 = ["Pluto", "Neptune", "Uranus", "Titan", "Saturn", "Io", "Jupiter", "Mars", "The Moon",]
    g1_f = random.randint(5, 35)
    g1_r = random.randint(5, 35)
    self.fuel = g1_f
    self.reso = g1_r
    self.temp = random.choice(tp)
    if self.tier == 1:
      self.name = random.choice(g1)
      
    elif self.tier == 2:
      self.name = random.choice(g2)

    else:
      self.name = random.choice(g3)
  
  def describe(self):
    self.dType("This planet's name is "+self.name+"\n")
    time.sleep(0.99)
    self.dType("This region's climate is "+self.temp+"\n")
    time.sleep(0.99)
    self.dType("You can find "+str(self.fuel)+" hectoliters of fuel on this planet\n")
    time.sleep(0.99)
    self.dType("You can find "+str(self.reso)+" megagrams of resources on the planet\n")
    time.sleep(0.99)
    self.dType("This planet's tier level is "+str(self.tier)+"\n")
    
  def nextGal(self):
    if self.tier == 1:
      self.tier = 2
    elif self.tier == 2:
      self.tier = 3
    