
# import seaborn as sns
import pandas as pd

import matplotlib
import matplotlib.ticker as ticker

# matplotlib.use('WX')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.dates as mdates
import datetime as dt


filename = "/Users/alessandro/Documents/PhD/trWikipedia/edits_per_week.csv"
datefile = '/Users/alessandro/Documents/PhD/trWikipedia/weekDate.csv'

dfEdits = pd.read_csv(filename)
dateDf = pd.read_csv(datefile)
dfEdits = dfEdits.merge(dateDf, how='inner', on='week_diff')

dfEdits['time_stamp'] = pd.to_datetime(dfEdits['time_stamp'])
dfEdits.sort_values('week_diff', inplace=True)


###depth graph
f3 = plt.figure(figsize=(12,6))
font = {'size': 13}

matplotlib.rc('font', **font)

ax5 = plt.subplot(111)
ax5.plot(dfEdits['time_stamp'],dfEdits['no_edits'], linewidth=1.3,  color='#68BBFF')
# ax5.plot(wdStats_3['timeframe'],dfEdits['avgDepth'],  marker='.', markevery=0.05, linewidth=1.6)
# ax5.plot(wdStats_3['timeframe'],wdStats_3['medianDepth'], marker='x', markevery=0.05, linewidth=1.6, color='#68BBFF')
ax5.grid(color='lightgray', linestyle='--', linewidth=.2)
ax5.legend([r'No. weekly edits'])
ax5.set_ylabel('No. edits')


plt.axvline(dt.datetime(2017, 4, 30), linewidth=0.9, color='red')
# minlocator = matdates.MinuteLocator(byminute=range(60))  # range(60) is the default
tenw_locator = matplotlib.dates.WeekdayLocator(matplotlib.dates.MO, interval=6)
# twow_locator = matplotlib.dates.WeekdayLocator(matplotlib.dates.MO, interval=2)

ax5.xaxis.set_major_locator(tenw_locator)
ax5.xaxis.set_major_formatter(matplotlib.dates.AutoDateFormatter(tenw_locator))
# ax5.xaxis.set_minor_locator(twow_locator)
# ax5.xaxis.set_minor_formatter(matplotlib.dates.AutoDateFormatter(twow_locator))

# seclocator.MAXTICKS  = 40000
# minlocator.MAXTICKS  = 40000
# ax5.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[3,6,9,12]))   #to get a tick every 15 minutes
#
# ax5.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))     #optional formatting

f3.autofmt_xdate()

plt.tight_layout()
plt.show()
plt.savefig('edits_week.eps', format='eps', transparent=True)


##users per week
filename = "/Users/alessandro/Documents/PhD/trWikipedia/users_per_week.csv"

dfEdits = pd.read_csv(filename)
dateDf = pd.read_csv(datefile)
dfEdits = dfEdits.merge(dateDf, how='inner', on='week_diff')

dfEdits['time_stamp'] = pd.to_datetime(dfEdits['time_stamp'])
dfEdits.sort_values('week_diff', inplace=True)


f3 = plt.figure(figsize=(12,6))
font = {'size': 13}

matplotlib.rc('font', **font)

ax5 = plt.subplot(111)
ax5.plot(dfEdits['time_stamp'],dfEdits['no_users'], linewidth=1.3,  color='#DAA520')
# ax5.plot(wdStats_3['timeframe'],dfEdits['avgDepth'],  marker='.', markevery=0.05, linewidth=1.6)
# ax5.plot(wdStats_3['timeframe'],wdStats_3['medianDepth'], marker='x', markevery=0.05, linewidth=1.6, color='#68BBFF')
ax5.grid(color='lightgray', linestyle='--', linewidth=.2)
ax5.legend([r'No. weekly users'])
ax5.set_ylabel('No. users')


plt.axvline(dt.datetime(2017, 4, 30), linewidth=0.9, color='red')
# minlocator = matdates.MinuteLocator(byminute=range(60))  # range(60) is the default
tenw_locator = matplotlib.dates.WeekdayLocator(matplotlib.dates.MO, interval=6)
# twow_locator = matplotlib.dates.WeekdayLocator(matplotlib.dates.MO, interval=2)

ax5.xaxis.set_major_locator(tenw_locator)
ax5.xaxis.set_major_formatter(matplotlib.dates.AutoDateFormatter(tenw_locator))
# ax5.xaxis.set_minor_locator(twow_locator)
# ax5.xaxis.set_minor_formatter(matplotlib.dates.AutoDateFormatter(twow_locator))

# seclocator.MAXTICKS  = 40000
# minlocator.MAXTICKS  = 40000
# ax5.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[3,6,9,12]))   #to get a tick every 15 minutes
#
# ax5.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))     #optional formatting

f3.autofmt_xdate()

plt.tight_layout()
plt.show()
plt.savefig('users_week.eps', format='eps', transparent=True)