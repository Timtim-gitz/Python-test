import matplotlib.pyplot as plt

# 1. Set up the data labels and the exact scores we found for 2023
countries = ['South Sudan', 'Global Average', 'Iceland']
hdi_scores = [0.388, 0.740, 0.959]

# 2. Pick clean colors for our bars (Red for low, Gray for average, Green for high)
bar_colors = ['#e74c3c', '#bdc3c7', '#2ecc71']

# 3. Create a window canvas for our bar graph
plt.figure(figsize=(8, 5))
plt.bar(countries, hdi_scores, color=bar_colors, width=0.5)

# 4. Add a descriptive title and labels
plt.title('Global Human Development Index Disparity Analysis (2023)', fontweight='bold')
plt.ylabel('HDI Score Value')

# 5. Show the graphic chart window on your desktop screen
plt.show()