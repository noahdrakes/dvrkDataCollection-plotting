import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
df1 = pd.read_csv('../tup_test_w_mio_contact/tup_no_contact.csv')
df2 = pd.read_csv('../tup_test_w_mio_contact/tup_contact.csv')

# Plot the first data set
plt.plot(df1['TIMESTAMP'], df1['ENCODER_VEL_3'], label='Encoder Velocity with no obstacle')

# Plot the second data set
plt.plot(df2['TIMESTAMP'], df2['ENCODER_VEL_3'], label='Encoder Velocity with obstacle')

# Adding titles and labels
plt.title('Encoder Velocity with obstacle vs no obstacle')
plt.xlabel('Timestamp (s)')
plt.ylabel('Encoder Count')

# Show the legend to differentiate the lines
plt.legend()

# Display the plot
plt.show()
