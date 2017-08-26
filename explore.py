import re
import json
import numpy as np

json_data = open('data.json').read()
data = json.loads(json_data)

combined_data = []
for x in data:
    combined_data.extend(x['data'])
data = combined_data

meandays = {}
counts = {}
meandays_mo = {}
counts_mo = {}

for x in data:
    ndays = re.sub(' days$', '', x[2])
    ndays = int(ndays)
    if not x[1] in counts:
        meandays[x[1]] = 0
        counts[x[1]] = 0
    mo = x[1].split('/')[0] + '/' + x[1].split('/')[2]
    if not mo in counts_mo:
        counts_mo[mo] = 0
        meandays_mo[mo] = 0
    meandays[x[1]] += ndays
    meandays_mo[mo] += ndays
    counts_mo[mo] += 1
    counts[x[1]] += 1

for x in meandays_mo:
    meandays_mo[x] /= counts_mo[x]
for x in meandays:
    meandays[x] /= counts[x]

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
xlabels = []
y = []
for mo in sorted(meandays_mo.keys()):
    xlabels.append(mo)
    y.append(meandays_mo[mo])
    print("%s: %.2f %d" % (mo, meandays_mo[mo], counts_mo[mo]))
ind = np.arange(len(xlabels))
width = 0.7
rect = ax.bar(ind, y, width)
ax.set_xticks(ind)
ax.set_xticklabels(xlabels)
ax.set_title('OPT total processing days')
ax.set_ylabel('Days')


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2.,
            height - 5,
            '%d' % int(height),
            ha='center',
            va='bottom',
            color='w')


autolabel(rect)

plt.savefig('monthly.pdf', format='pdf')
plt.show()

for key in sorted(meandays.keys()):
    print("%s: %.2f %d" % (key, meandays[key], counts[key]))
