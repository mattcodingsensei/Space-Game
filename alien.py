import random
import sys
import time
import player
import boss

class Alien:

#alien stats  
  def __init__(self,pl):
    self.syll = ["ba", "be", "bi", "bo", "bu", "boo", "bee",
    "da", "de", "di", "do", "du", "doo", "dee",
    "ca", "ce", "ci", "co", "cu", "coo", "cee", 
    "fa", "fe", "fi", "fo", "fu", "foo", "fee", 
    "ga", "ge", "gi", "go", "gu", "goo", "gee", 
    "ha", "he", "hi", "ho", "hu", "hoo", "hee", 
    "ja", "je", "ji", "jo", "ju", "joo", "jee", 
    "ka", "ke", "ki", "ko", "ku", "koo", "kee",
    "ta", "te", "ti", "to", "tu", "too", "tee", 
    "va", "ve", "vi", "vo", "vu", "voo", "vee", 
    "la", "le", "li", "lo", "lu", "loo", "lee", 
    "ma", "me", "mi", "mo", "mu", "moo", "mee",
    "na", "ne", "ni", "no", "nu", "noo", "nee", 
    "pa", "pe", "pi", "po", "pu", "poo", "pee", 
    "ra", "re", "ri", "ro", "ru", "roo", "ree", 
    "sa", "se", "si", "so", "su", "soo", "see", 
    "wa", "we", "wi", "wo", "wu", "woo", "wee",
    "xa", "xe", "xi", "xo", "xu", "xoo", "xee", 
    "ya", "ye", "yi", "yo", "yu", "yoo", "tee", 
    "za", "ze", "zi", "zo", "zu", "zoo", "zee", 
    "tha", "the", "thi", "tho", "thu", "thoo", "thee" ]
    
    self.hyph_syll = ["ba", "be", "bi", "bo", "bu", "boo", "bee",
    "da", "de", "di", "do", "du", "doo", "dee",
    "ca", "ce", "ci", "co", "cu", "coo", "cee", 
    "fa", "fe", "fi", "fo", "fu", "foo", "fee", 
    "ga", "ge", "gi", "go", "gu", "goo", "gee", 
    "ha", "he", "hi", "ho", "hu", "hoo", "hee", 
    "ja", "je", "ji", "jo", "ju", "joo", "jee", 
    "ka", "ke", "ki", "ko", "ku", "koo", "kee",
    "la", "le", "li", "lo", "lu", "loo", "lee", 
    "ma", "me", "mi", "mo", "mu", "moo", "mee",
    "na", "ne", "ni", "no", "nu", "noo", "nee", 
    "pa", "pe", "pi", "po", "pu", "poo", "pee", 
    "ra", "re", "ri", "ro", "ru", "roo", "ree", 
    "sa", "se", "si", "so", "su", "soo", "see", 
    "ta", "te", "ti", "to", "tu", "too", "tee", 
    "va", "ve", "vi", "vo", "vu", "voo", "vee", 
    "wa", "we", "wi", "wo", "wu", "woo", "wee",
    "xa", "xe", "xi", "xo", "xu", "xoo", "xee", 
    "ya", "ye", "yi", "yo", "yu", "yoo", "tee", 
    "za", "ze", "zi", "zo", "zu", "zoo", "zee", 
    "tha", "the", "thi", "tho", "thu", "thoo", "thee",
    "qua","que", "qui", "quo", "quu","quoo", "quee",
    "tt", "kk",
    "tat", "kak", "kat", "tak",
    "tet", "kek", "ket", "tek",
    "tit", "kik", "kit", "tik",
    "tot", "kok", "kot", "tok",
    "tut", "kuk", "kut", "tuk",]
    
    self.defense = 3
    self.attack = 3
    self.health = 3
    self.alien_name = self.gen()
    self.level = 1
    self.times_defended_a = 1
    self.current_move = ""
    self.player = pl
#delayed print
  def d_print_a (self,word, delay = .04):
    for i in word:
      sys.stdout.write(i)
      time.sleep(delay)
      sys.stdout.flush()
    
#random name generator
  def gen (self):
    hyph = random.randint (1,10)
    w = ""
    if hyph <= 6:
      for i in range(random.randint(2,3)):
        w += self.syll[random.randint(0,len(self.syll) - 1)]
      return w.capitalize()
    elif hyph == 7 or hyph == 8:
      for i in range(random.randint(1,2)):
        w += self.syll[random.randint(0,len(self.syll) - 1)]
        w += "-" + self.hyph_syll [random.randint(0,len(self.hyph_syll) - 1)]
      return w.capitalize()
    else:
      for i in range(random.randint(1,2)):
        w += self.hyph_syll [random.randint(0,len(self.hyph_syll) - 1)] + "-"
        w += self.syll[random.randint(0,len(self.syll) - 1)]
      return w.capitalize()
  
  def name (self):
    print(self.alien_name)
    
#fight   
  def enemy_attack (self, pl):
    if self.attack <= pl.defense:
      pl.health -= 1
      return 1
    else:
      self.attack -= pl.defense
      pl.health -= self.attack
      self.attack += pl.defense
      return self.attack - pl.defense
      
  def enemy_defend (self):
    self.times_defended_a += 1
    self.defense *= ((self.times_defended_a +1)/2)
     
  def enemy_choice (self):
    choice = random.randint(1,2)
    if choice == 1:
      self.current_move = "attack"
    elif choice == 2:
      self.current_move = "defend"
   # self.enemy_action(self.player)
    
  def gen_stats (self, lvl):     
    self.level = lvl
    self.attack = lvl
    self.defense = lvl * 2
    points = (lvl * 2) + 2
    self.health = self.level * 3
    self.attack += random.randint (0,points)
    self.defense += (points - self.attack) + lvl
    
  def enemy_action (self,pl):
    if self.current_move == "attack":
      self.d_print_a ("The alien attacked.\n")
      self.enemy_attack(pl)
      self.d_print_a ("Your health is now " + str(pl.health)+"\n")
      self.current_move = "attack"
    elif self.current_move == "defend":
      self.d_print_a ("The alien defended.\n")
      self.enemy_defend()
      self.d_print_a ("Its defense is now " + str(self.defense)+"\n") 
      self.current_move = "defend"
    elif self.current_move == "parried":
      self.d_print_a ("The alien was going to attack, but you parried.\n")