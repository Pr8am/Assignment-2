import matplotlib.pyplot as plt

# Function to compute the sum of the series up to n terms
def series_sum(n):
    a = 9  # first term
    d = 8  # common difference
    return (n / 2) * (2 * a + (n - 1) * d)

# Number of terms in the series
num_terms = 20

# Compute the sum for each term
sums = [series_sum(n) for n in range(1, num_terms + 1)]

# Generate stem values (term numbers)
stems = list(range(1, num_terms + 1))

# Plot the stem graph
plt.stem(stems, sums, linefmt='b-', markerfmt='bo', basefmt=' ')

# Mark the first 12 terms in a different color
plt.stem(stems[:12], sums[:12], linefmt='r-', markerfmt='ro', basefmt=' ')

# Add labels and title
plt.xlabel('Term Number')
plt.ylabel('Sum')
plt.title('Stem Graph of the Series Sum')

# Show the plot
plt.show()

