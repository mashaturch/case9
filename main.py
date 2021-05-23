import ru_local
import random
print(ru_local.HI)
ok = input(ru_local.OK).capitalize().strip()
while ok != 'Ok':
    ok = input(ru_local.RESTART).capitalize().strip()
resources = {ru_local.LAND: random.randint(100, 500), ru_local.BUDGET: random.randint(100, 500),
             ru_local.SEED: random.randint(100, 500), ru_local.BREAD: random.randint(100, 500),
             ru_local.PEOPLE: random.randint(100, 500)}
discontent = {ru_local.ANGRY: 10}
print(ru_local.NOW, ru_local.FEERLAND, resources[ru_local.LAND],
      ru_local.MONEY, resources[ru_local.BUDGET], ru_local.LANDSEED, resources[ru_local.SEED],
      ru_local.BREADS, resources[ru_local.BREAD], sep='\n')
print(ru_local.ABILITY)
print('')
ok = input(ru_local.OK).capitalize().strip()
while ok != 'Ok':
    ok = input(ru_local.RESTART).capitalize().strip()
print(ru_local.LASTKING)
print(ru_local.NOWANGRY,
      discontent[ru_local.ANGRY], sep='\n')
ok = input(ru_local.OK).capitalize().strip()
while ok != 'Ok':
    ok = input(ru_local.RESTART).capitalize().strip()
print(ru_local.KING)
data = 2020

def res(data):
    while data != 2040 or discontent[ru_local.ANGRY] < 100:
        if data % 4 == 0:
            RandomEvent()
        print(ru_local.NOW, data, ru_local.YEAR)
        print(ru_local.FEERLAND, resources[ru_local.LAND],
              ru_local.MONEY, resources[ru_local.BUDGET], ru_local.SEEDS, resources[ru_local.SEED],
              ru_local.BREADS, resources[ru_local.BREAD], ru_local.NOWPEOPLE,
              resources[ru_local.PEOPLE], sep='\n')

        print(ru_local.NOWANGRY,
              discontent[ru_local.ANGRY], sep='\n')
        price_bread = random.randint(10, 50)
        price_land = random.randint(10, 50)
        price_corn = random.randint(10, 50)
        corn_plant = int(input(ru_local.HOWSEED))
        print(ru_local.SEEDPRICE, price_corn)
        corn_sell = int(input(ru_local.SEEDSELL))
        while corn_sell + corn_plant > resources[ru_local.SEED]:
            print(ru_local.LOWSEED)
            corn_plant = int(input(ru_local.HOWSEED))
            corn_sell = int(input(ru_local.SEEDSELL))
        resources[ru_local.SEED] -= corn_plant
        resources[ru_local.SEED] -= corn_sell
        print(ru_local.SEEDLEFT, resources[ru_local.SEED])


        bread_people = int(input(ru_local.BREADPEOPLE))

        print(ru_local.BREADPRICE, price_bread)
        bread_sell = int(input(ru_local.HOWBREAD))
        while bread_sell + bread_people > resources[ru_local.BREAD]:
            print(ru_local.LOWBREAD)
            bread_sell = int(input(ru_local.HOWBREAD))
            bread_people = int(input(ru_local.BREADPEOPLE))
        resources[ru_local.BREAD] -= bread_sell
        resources[ru_local.BREAD] -= bread_people
        print(ru_local.BREADLEFT, resources[ru_local.BREAD])
        print(ru_local.LANDPRICE, price_land)
        land_sell = int(input(ru_local.LANDSELL))
        while land_sell > resources[ru_local.LAND]:
            print(ru_local.LOWLAND)
            land_sell = int(input(ru_local.LANDSELL))
        resources[ru_local.LAND] -= land_sell
        print(ru_local.LANDLEFT, resources[ru_local.LAND])

        print(ru_local.MONEY, resources[ru_local.BUDGET])

        print(ru_local.LANDPRICE, price_land)
        buy_land = int(input(ru_local.LANDBUY))
        while buy_land * price_land > resources[ru_local.BUDGET]:
            print(ru_local.LOWMONEY)
            print(ru_local.LANDPRICE, price_land)
            buy_land = int(input(ru_local.LANDBUY))

        resources[ru_local.BUDGET] -= buy_land * price_land

        print(ru_local.MONEY, resources[ru_local.BUDGET])
        print(ru_local.BREADPRICE, price_bread)
        buy_bread = int(input(ru_local.BREADBUY))
        while buy_bread * price_bread > resources[ru_local.BUDGET]:
            print(ru_local.LOWMONEY)
            print(ru_local.BREADPRICE, price_bread)
            buy_bread = int(input(ru_local.BREADBUY))

        resources[ru_local.BUDGET] -= buy_bread * price_bread

        print(ru_local.MONEY, resources[ru_local.BUDGET])
        print(ru_local.SEEDPRICE, price_corn)
        buy_corn = int(input(ru_local.SEEDBUY))
        while buy_corn * price_corn > resources[ru_local.BUDGET]:
            print(ru_local.LOWMONEY)
            print(ru_local.SEEDPRICE, price_corn)
            buy_corn = int(input(ru_local.SEEDBUY))

        resources[ru_local.BUDGET] -= buy_corn * price_corn

        print(ru_local.MONEY, resources[ru_local.BUDGET])
        buy_people = int(input(ru_local.SOCMONEY))
        while buy_people > resources[ru_local.BUDGET]:
            print(ru_local.LOWMONEY)
            buy_people = int(input(ru_local.SOCMONEY))

        resources[ru_local.BUDGET] -= buy_people



        data += 1
        if (resources[ru_local.BREAD] + buy_people) / 2 / resources[ru_local.PEOPLE] < 1:
            discontent[ru_local.ANGRY] += 20
        elif (resources[ru_local.BREAD] + buy_people) / 2 / resources[ru_local.PEOPLE] > 1:
            discontent[ru_local.ANGRY] += 20
        resources[ru_local.BREAD] += round(0.8 * corn_plant * resources[ru_local.LAND])
        resources[ru_local.SEED] += round(buy_corn * price_corn)
        resources[ru_local.LAND] += round(buy_land * price_land)
        resources[ru_local.PEOPLE] += random.randint(-1, 2)
        resources[ru_local.BUDGET] += round(resources[ru_local.PEOPLE] * 10)

print(ru_local.PRESIDENT)


def drought():
    print(ru_local.DROUGHT)
    resources[ru_local.SEED] = resources[ru_local.LAND] / 2

def war():
    print(ru_local.WAR)
    resources[ru_local.BREAD] = 0
    resources[ru_local.SEED] = resources[ru_local.SEED] / 2
    resources[ru_local.PEOPLE] = resources[ru_local.PEOPLE] * 5/6

def inflation():
    print(ru_local.INFLATION)
    resources[ru_local.BUDGET] = resources[ru_local.BUDGET] * 0.8

def victory():
    print(ru_local.VICTORY)
    resources[ru_local.LAND] += 1000
    resources[ru_local.BUDGET] += 200

def riot():
    print(ru_local.RIOT)
    resources[ru_local.PEOPLE] = resources[ru_local.PEOPLE] * 0.95
    resources[ru_local.BREAD] = resources[ru_local.BREAD] * 0.85

def GoodWeather():
    print(ru_local.WEATHER)
    resources[ru_local.SEED] = resources[ru_local.SEED] * 1.1

def RandomEvent():
    event = random.randint(1, 6)
    if event == 1:
        drought()
    elif event == 2:
        war()
    elif event == 3:
        inflation()
    elif event == 4:
        victory()
    elif event == 5:
        riot()
    elif event == 6:
        GoodWeather()





z = res(data)