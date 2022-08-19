#simulates the cash value of a pack of magic the gathering cards
#this is an example generates a set that matches a draft pack of Streets of New Capenna in size and currently ignores the chance of foil cards
#ideally you would have a list of everything possible in a given slot in the pack
import random

#generate an example set of cards
#snc 101 commons, 80 uncommons, 60 rare, 20 mythic in new capenna
commons = []
for x in range(1, 102):
  card = {
    'name': 'test_common',
    'rarity': 'commmon',
    'price': round(random.uniform(0.01, 0.05)),
    'setnum': x
  }
  commons.append(card)

uncommons = []
for x in range(1, 81):
  card = {
    'name': 'test_uncommon',
    'rarity': 'uncommmon',
    'price': round(random.uniform(0.10, 2), 2),
    'setnum': x+len(commons)
  }
  uncommons.append(card)    

rares = []
for x in range(1, 61):
  card = {
    'name': 'test_rare',
    'rarity': 'rare',
    'price': round(random.uniform(1, 20), 2),
    'setnum': x+len(commons)+len(uncommons)
  }
  rares.append(card)

mythics = []
for x in range(1, 21):
  card = {
    'name': 'test_mythic',
    'rarity': 'mythic',
    'price': round(random.uniform(1, 50), 2),
    'setnum': x+len(commons)+len(uncommons)+len(rares)
  }
  mythics.append(card)   

#add the commmons and mythics to the pack, without the possibility of duplicates
#a real pack also would account for a spread of different color cards in the pack but the exact collation patterns aren't known so I just take cards at random
#commons and uncommons are a negligible part of the value anyways, usually commmons are essentially worthless and there are a handful of uncommons worth money
packcommmons = random.sample(commons, 10)
packuncommons = random.sample(uncommons, 3)

#mythics replace the rare in the pack in approximately one in six packs
ismythic = random.randint(1,6)
if ismythic == 6:
  packmythics = random.sample(mythics, 1)
  packrares = []
else:
  packrares = random.sample(rares, 1)
  packmythics = []

packvalue = 0
pack = packcommmons + packuncommons + packrares + packmythics

print(pack)

for i in range(len(pack)):
  packvalue += pack[i]['price']

print('final pack value is: ', packvalue)