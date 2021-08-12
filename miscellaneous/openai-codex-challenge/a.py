from datetime import date
from datetime import datetime

import pandas


def diff_days(csv_contents: str) -> int:
    csv_contents = csv_contents.strip()
    rows = csv_contents.split('\n')
    d = rows[0].split(',').index('Date')
    dates = []
    for row in rows[1:]:
        row = row.split(',')
        dates.append(datetime.strptime(row[d] , '%Y-%m-%d'))
    return (max(dates) - min(dates)).days


# Examples
print(diff_days("Date,Price,Volume\n2014-01-27,550.50,1387\n2014-06-23,910.83,4361\n2014-05-20,604.51,5870"))
print(diff_days('Date\n2000-01-01\n2000-01-01\n'))

# The last expression evaluated is always shown when
# you run your code, just like a Jupyter notebook cell.
"Good luck!"