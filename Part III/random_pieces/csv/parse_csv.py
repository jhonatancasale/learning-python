#!env python3
# -*- coding: utf-8 -*-

# from https://www.youtube.com/watch?v=Xi52tx6phRU

import csv
from datetime import datetime

def main():
    '''Perform the video example''' 

    path = 'google_stock_data.csv'
    f = open(path, newline='')
    reader = csv.reader(f)

    header = next(reader) # The first line is the header

    data = []
    for row in reader: # Read the remaining data
        # row = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
        date = datetime.strptime(row[0], '%m/%d/%Y')
        open_price = float(row[1])
        high = float(row[2])
        low = float(row[3])
        close = float(row[4])
        volume = int(row[5])
        adj_close = float(row[6])

        data.append([date, open_price, high, low, close, volume, adj_close])
    f.close()

    # Compute and store daily stock returns
    returns_path = 'google_returns.csv'
    f = open(returns_path, 'w')
    writer = csv.writer(f)
    writer.writerow(["Date", "Return"])

    for i in range(len(data) - 1):
        todays_row = data[i]
        todays_date = todays_row[0]
        todays_price = todays_row[-1]
        yesterdays_row = data[i+1]
        yesterdays_price = yesterdays_row[-1]

        daily_return = (todays_price - yesterdays_price) / yesterdays_price
        formatted_date = todays_date.strftime('%m/%d/%Y')
        writer.writerow([formatted_date, daily_return])
    f.close()

if __name__ == '__main__':
    main()
