# aliens3.py, Chapter 6, Python Crash Course
# program generates yellow and green aliens

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens
for alien in aliens[0:5]:
    print(alien)
print("...")



