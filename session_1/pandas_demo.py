from matplotlib import pyplot as plt
import pandas as pd

data = {
    'year': [2008, 2012, 2016],
    'attendees': [112, 321, 729],
    'average_age': [24, 43, 31]
}

df = pd.DataFrame(data)

print(df)

print(df['year'])

print(df['year'] < 2013)

earlier_than_2013 = df['year'] < 2013
below_40 = df.average_age < 40

print(df[earlier_than_2013])

plt.plot(df['year'], df['attendees'])
plt.plot(df['year'], df['average_age'])
plt.legend(['attendees', 'average age'])
plt.show()
