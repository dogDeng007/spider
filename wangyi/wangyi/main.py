from scrapy import cmdline

cmdline.execute('scrapy crawl spider_wy -s LOG_FILE=all.log'.split())