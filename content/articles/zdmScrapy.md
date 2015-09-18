Title: Scrapy抓取SMZDM优惠信息
Date: 2015-09-18 18:32
Category: 爬虫 
Author: Raven 
Summary: Scrapy 抓取试验

SMZDM是一个近几年比较有名的商品推荐类网站。
最近学习了Scrapy爬虫，今天就拿他试试学习成果，抓取下上面的优惠信息。


### 创建project:

    scrapy startproject smzdm

### Items
分析下需要抓取的信息，我们需要商品的名称，价格，具体描述和推送时间。

据此建立我们的items.py

    # -*- coding: utf-8 -*-
    from scrapy.item import Item, Field

    class zdmItem(Item):
        title = Field()
        desc  = Field()
        price = Field()
        time  = Field()


### Pipelines
定义Pipeline处理item，并保存结果到smzdm.json中,pipelines.py

    # -*- coding:utf-8 -*- 
    import json
    import codecs

    class SmzdmPipeline(object):
        def __init__(self):
            self.file = codecs.open('smzdm.json', 'wb', encoding='utf-8')

        def process_item(self, item, spider):
            line = json.dumps(dict(item)) + '\n'
            self.file.write(line.decode("unicode_escape"))
            return item


### settings
settings.py中主要是对爬虫进行配置，这里加上pipeline的配置

    ITEM_PIPELINES = {
        'smzdm.pipelines.SmzdmPipeline':100
    }

### Spider
下面编写我们的Spider

编写Spider需要考虑下网页的遍历方式，通过观察优惠页面，发现了一种很容易的方式，那就是选择第一篇优惠信息作为start_url，分析上一页的链接，爬取下一个优惠信息。

对于我们关心的title,price,description,time和link，直接可以利用xpath分析得到。

spiders/zdmSpider.py

    # -*- coding:utf-8 -*- 

    from smzdm.items import zdmItem
    from scrapy.http import Request
    from scrapy.spiders import Spider

    class zdmSpider(Spider):
        name="zdm"
        
        allowed_domains=["smzdm.com"]
        start_urls=["http://www.smzdm.com/p/702599"]
       
        def parse(self,response):
            item=zdmItem()
            title=response.xpath('//h1/text()')[0].extract().encode('utf-8').lstrip()
            link =response.xpath('//div[@class="pre_next_article"]/span[1]/a/@href')[0].extract()
            if len(response.xpath('//h1/span/text()'))>0:
                price=response.xpath('//h1/span/text()')[0].extract().encode('utf-8')
            else:
                price=""
            desc= response.xpath('//p[@itemprop="description"]/text() | //p[@itemprop="description"]/a/text() | //p[@itemprop="description"]/strong/text()')
            item['desc']=""
            for des in desc:
                item['desc']+=des.extract().encode('utf-8') 

            item['title']=title
            item['price']=price
            item['time']=response.xpath('//span[@class="lrTime"]/text()')[0].extract()
            
            yield item 
            yield Request(link) 


#### 结果
运行爬虫：

	scrapy crawl zdm

查看smzdm.json

    {"price": "2199元包邮，赠摄影包", "time": "2015-09-18 13:10", "desc": "尼康入门级单反近期好价，配备2代尼克尔18-55mm VR镜头，赠摄影包。D3200是于2012年推出入门机型，是D3100的继任者，虽定位低端但参数一点都不逊色，APS-C 2416万像素CMOS传感器首次搭载在尼康机身上，使之不仅超越了一众入门级竞争者，甚至也超过了其他品牌的中端型号。EXPEED 3图像处理器的搭载让人看出了尼康的诚意，这款处理器之前可是用在D4、D800这样的旗舰身上的。对焦方面采用了Multi-CAM 1000自动对焦模块，中央十字+11点对焦在入门机中也算是厚道。ISO 100-6400，4FPS连拍。可拍摄1080p全高清视频。屏幕为3英寸92万像素，虽然不能翻转，但是已经相当细腻。电池为EN-EL14，续航约540张。另外，D3200还有一个特色可以是搭配无线适配器WU-1a（选购），实现与智能设备（Android）相连接，进行无线传送和远程拍摄，这是非常新颖和方便的特性。标配的镜头为18-55VR II，属于防抖镜头，焦段适中，适合初学者入门使用。易迅网目前抢购价2199元，近期好价，额外赠送摄影包，相比8月推荐价格略高但有赠品优势。D3200延续了系列机身无对焦马达的传统，只能搭载AF-S或AF-I系列镜头才可以实现自动对焦功能，如果购买D型镜头将无法自动对焦，建议用户考虑该点，选购对应的新款G镜头，例如35/1.8G等。", "title": "Nikon 尼康 D3200 单反套机（含18-55mm VR II镜头）"}
    {"price": "过期", "time": "2015-09-18 12:11", "desc": "买刷头送牙刷，赠品可能随时售罄，手慢无~值友“净角独眼”的推荐理由：“因为之前买了力博得的声波牙刷看今天有活动在找刷头，发现1号店的“920爱牙日”里买刷头送牙刷的分支活动，虽然自用的力博得声波牙刷使用起来力度偏小，基于价格总体来说还是不错的。这次39元购力博得 ELEC电动专用刷头套装（2支装），赠送价值99元的干电池电动牙刷还附带便携盒。3支刷头，值得推荐。”", "title": ""}
    {"price": "89元包邮，买一赠一", "time": "2015-09-18 11:51", "desc": "适合熟龄肌肤，中样买一赠一。Lancome兰蔻根源补养美容液，为改善肤色的美容液系列，是一款含天然植物提取精华的护肤品。融合红景天、龙胆根、野生山药三种珍贵的植物根部提取物作为配方。通过加强肌肤的新陈代谢而达到改善暗淡发黄气色的功效。为半透明质地，气味芳香不油腻，可快速渗入肌肤、营养肌肤，使肌肤重现光彩，规格50ml。值友“烟柳画桥”反馈：质地偏黏偏厚重，但补水滋润效果好，适合秋冬季节使用。健一网目前此款中样50ml售价89元包邮，参与买一赠一促销，单瓶入手约45元左右，近期好价。中样旅行携带很方便，不过瓶身有“NOTFORSALE”非卖品字样，介意慎拍。", "title": "LANCOME 兰蔻 根源补养美容液 中样 50ml"}

  



