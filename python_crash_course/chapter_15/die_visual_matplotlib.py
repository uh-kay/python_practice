import matplotlib.pyplot as plt

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = [die.roll() for roll_num in range(1000)]

# Analyze the results.
poss_results = range(1, die.num_sides+1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
fig, ax = plt.subplots()
ax.bar(poss_results, frequencies)
title = "Results of Rolling One D6 1,000 Times"
ax.set_title(title, fontsize=18)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)

plt.show()
