# opt-tracker-stats: Statistics of monthly and daily OPT processing time
## Prerequisite
* Python 3.x
* Scrapy
* Numpy

## Introduction
First run the following command line to crawl data from the "opt tracker" in `www.trackitt.com`:
```
scrapy runspider crawler.py -o data.json -t json
```

Secondly, run `python explore.py`. Statistic data will be shown in the standard output and a figure of monthly processing time will be shown and saved into a file named `monthly.pdf`. An example of the figure is as below.
