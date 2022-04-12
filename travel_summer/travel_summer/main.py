from scrapy import cmdline

cmdline.execute('scrapy crawl spider_travel -s LOG_FILE=all.log'.split())