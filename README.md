# opt-tracker-stats
Statistics of monthly and daily OPT processing time
## Introduction
Firstly, run the following command line to crawl data from the "opt tracker" in `www.trackitt.com`:
```
scrapy runspider crawler.py -o data.json -t json
```

Secondly, run the following command
```
python explore.py
```
Statistic data will be shown in the standard output and a figure of monthly processing time will be shown and saved into a file named `monthly.pdf`. An example of the figure is as below.

## Prerequisite
* Python 3.x
* Scrapy
* Numpy

