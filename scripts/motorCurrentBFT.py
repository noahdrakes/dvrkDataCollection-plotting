import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('../tup_test_w_mio_contact/tup_no_contact.csv')
df2 = pd.read_csv('../tup_test_w_mio_contact/tup_contact.csv')



MIO_VALUES = df2['MIO_PINS']
contact_detected_timestamp = 0

for i in range(len(MIO_VALUES)):
    if (MIO_VALUES[i] != 15):
        contact_detected_timestamp = df2['TIMESTAMP'][i]
        print("found contact!")
        print("contact at ", contact_detected_timestamp)
        break

# Plot the first data set
plt.plot(df1['TIMESTAMP'], df1['MOTOR_CURRENT_3'], label='Motor Current with no obstacle')

# Plot the second data set
plt.plot(df2['TIMESTAMP'], df2['MOTOR_CURRENT_3'], label='Motor Current with obstacle')

plt.axvline(x=contact_detected_timestamp, color='g', linestyle='--', label='Collision point')

# Adding titles and labels
plt.title('Motor Current with obstacle vs no obstacle')
plt.xlabel('Timestamp (s)')
plt.ylabel('Encoder Count')

# Show the legend to differentiate the lines
plt.legend()

# Display the plot
plt.show()
