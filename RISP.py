import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Load the CSV file
file_path = r'C:\Users\parkj\Desktop\Baseball\Dodgers Lineup - RISP.csv'
data = pd.read_csv(file_path)

# Exclude the "Total" row
data = data[data['Name'] != 'Total']

# Clean the salary column
data['Annual Salary (PV)'] = data['Annual Salary (PV)'].replace('[\$,]', '', regex=True).astype(float)

# Calculate the correlation between Annual Salary and RISP
correlation = data['Annual Salary (PV)'].corr(data['RISP 2024 (9/3/24)'])

# Function to format the x-axis labels with dollar signs
def salary_formatter(x, pos):
    return '${:,.0f}'.format(x)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['Annual Salary (PV)'], data['RISP 2024 (9/3/24)'], color='blue', label='Data Points')

# Add a trend line
z = np.polyfit(data['Annual Salary (PV)'], data['RISP 2024 (9/3/24)'], 1)
p = np.poly1d(z)
plt.plot(data['Annual Salary (PV)'], p(data['Annual Salary (PV)']), color='red', label='Trend Line')

# Label the axes
plt.xlabel('Annual Salary (USD)')
plt.ylabel('RISP 2024 (9/3/24)')
plt.title('Correlation between Annual Salary and RISP')
plt.legend()

# Apply the dollar sign formatting to the x-axis
formatter = FuncFormatter(salary_formatter)
plt.gca().xaxis.set_major_formatter(formatter)

# Annotate the plot with the correlation coefficient
plt.text(0.05, 0.95, f'Correlation: {correlation:.2f}', transform=plt.gca().transAxes,
         fontsize=12, verticalalignment='top')

# Show the plot
plt.grid(True)
plt.show()
