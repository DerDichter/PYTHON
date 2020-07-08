# Listen kann man auch erstellen.
v = [2,9,80000]
print (v)

# In der Informatik beginnt man immer mit null zu zählen.
# In dieser Liste ist 0 also 2, 1 ist 9 und 2 ist 80000

print (v[0])
print (v[1])
print (v[2])

# Man kann auch rückwärts zählen

print (v[-1])
print (v[-2])

# Listen kann man auch aneinander hängen...
print (v + [5,10000000000,100000000000000000000000000000])

# Man kann auch die Liste ganz schnell ändern.
v[0] = 2020
print (v)

# Oder die eine Zahl mit einer bereits bestehenden Zahl ändern.
v[0] = v[1]
print (v)

# Und sogar rechnen.
v[0] = v[1] + v[2]
print (v)

# Man kann auch Listen aus Listen erstellen
# Liste 1 = v, Liste 2 = x, Liste 3 (aus Listen) = nogger

x = ['x','y','z',]
print (x)
nogger = [v,x]
print (nogger)
