# -*- coding: utf-8 -*-

# Scrapy settings for milkprice project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'milkbot'

SPIDER_MODULES = ['milkbot.spiders']
NEWSPIDER_MODULE = 'milkbot.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Milk Bot 0.1 (http://food-price.net/pages/bot)'

ITEM_PIPELINES = ['milkbot.pipelines.PriceWatchPipeline']