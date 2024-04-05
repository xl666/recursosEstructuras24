planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

for lunas in planet_moons.values():
    moons1 =lunas + planet_moons.values()

total_planets1 = len(planet_moons)

moons = planet_moons.values()
total_planets = len(planet_moons.keys())

print(moons , total_planets, ' ', moons1, '' , total_planets1)