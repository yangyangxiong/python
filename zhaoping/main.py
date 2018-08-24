from scrapy.cmdline import execute
import os,sys

sys.path.append(os.path.dirname(os.path.basename(__file__)))
execute(['scrapy','crawl','lieping'])
        
