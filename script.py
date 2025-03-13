import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv(r"C:\Users\Revolt's\Downloads\New folder\results.csv")
data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
data = data.sort_values('timestamp')

plt.figure(figsize=(12, 6))
plt.scatter(data['timestamp'], data['wpm'], color='blue', alpha=0.5, label='WPM')
slope, intercept, r_value, p_value, std_err = stats.linregress(data['timestamp'].astype('int64') / 10**9, data['wpm'])
trend_line = intercept + slope * (data['timestamp'].astype('int64') / 10**9)
plt.plot(data['timestamp'], trend_line, color='red', label=f'Trend (R² = {r_value**2:.2f})')
plt.title('WPM Over Time with Trend Line')
plt.xlabel('Date')
plt.ylabel('Words Per Minute (WPM)')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Typing Statistics:")
print(f"Average WPM: {data['wpm'].mean():.2f}")
print(f"Average Accuracy: {data['acc'].mean():.2f}%")
print(f"Average Consistency: {data['consistency'].mean():.2f}%")
print(f"Best WPM: {data['wpm'].max():.2f} (on {data['timestamp'][data['wpm'].idxmax()]})")
print(f"Lowest WPM: {data['wpm'].min():.2f} (on {data['timestamp'][data['wpm'].idxmin()]})")