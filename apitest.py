from mtgsdk import Card
from mtgsdk import Set

x = Set.generate_booster('snc')

for a in x:
    print(a.name, ' ', a.rarity)

testset = Card.where(set='snc')

#https://docs.peewee-orm.com/en/latest/peewee/query_builder.html check this out later for trying to figure out how to actually get something out of the set/card things