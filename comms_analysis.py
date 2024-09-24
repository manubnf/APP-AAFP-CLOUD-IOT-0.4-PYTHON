import pandas as pd
import matplotlib.pyplot as plt

def analyze_support_data(filename):
    data = pd.read_csv(filename, names=['Date', 'Requests', 'Assistance_Provided'])
    data['Date'] = pd.to_datetime(data['Date'])
    
    print(data.describe())
    
    data.plot(x='Date', y=['Requests', 'Assistance_Provided'], kind='line', figsize=(10, 5))
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('Support Requests vs Assistance Provided Over Time')
    plt.show()

if __name__ == "__main__":
    analyze_support_data('support_data.csv')
