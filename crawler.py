import scrapy
from scrapy.selector import Selector


class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = []
    urlhead = 'http://www.trackitt.com/usa-immigration-trackers/opt/page/'
    for x in range(50):
        start_urls.append(urlhead + str(x))

    def parse(self, response):
        rows = response.selector.xpath('//tbody/tr[starts-with(@id, "row")]')
        N = len(rows)
        print('total = ' + repr(N))
        approvals = []
        for i in range(N):
            rowex = Selector(text=rows[i].extract()).xpath('//nobr/text()')
            data = rowex.extract()
            if data[8] == 'approved' and data[3].startswith('Potomac'):
                for v in data:
                    if v.endswith('days'):
                        elapsed = v
                approvals.append([data[3], data[4], elapsed])
        if len(approvals) > 0:
            yield {"data": approvals}
