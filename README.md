# JDSpider

### 目标：分布式爬取京东商品详情，评论和评论总结

### Feature
1. 总体框架划分四部分（一总控，三爬虫）灵活分配
2. 爬虫皆为分布式部署，解决带宽和性能瓶颈
3. proxy_pool防止ip封禁
4. mysql底层数据存储

### Power by:
1. Python 3.6
2. Scrapy 1.4
3. pymysql
4. json
5. redis

#### Project blog:  http://blog.csdn.net/sinat_34200786/article/details/78770356
---
### How to use ？
```
git clone https://github.com/Dengqlbq/JDSpider.git
```

Override the following content
1. ProjectStart/Test.py  (redis configuration, keywords, page_count)
2. JDUrlsSpider/settings.py  (redis configuration)
3. JDDetailSpider/settings.py  (redis configuration, mysql configuration， DOWNLOAD_DELAY)
4. JDCommentSpider/settings.py  (redis configuratin, mysql configuration， DOWNLOAD_DELAY)

```
cd ProjectStart
python Test.py
```

```
cd JDUrlsSpider
scrapy crawl JDUrlsSpider
```

```
cd JDDetailSpider
scrapy crawl JDDetailSpider
(This is distributed crawler, you can run more than one JDDetailSpider)
```

```
cd JDCommentSpider
scrapy crawl JDCommentSpider
(This is distributed crawler, you can run more than one JDCommentSpider)
```


Note: 
1. Before you run the project, make sure that you have created tables match the requirement.<br>
2. If you did not build a [proxy_pool](https://github.com/jhao104/proxy_pool), disable the
   "ProxyMiddleware" in JDCommetSpider/settings.py


---
### Achievement
Product detail and comment summary
![商品详情和评论总结](https://github.com/Dengqlbq/JDSpider/blob/master/Image/detail.png)
<br>
Some comments<br>
![部分评论数据](https://github.com/Dengqlbq/JDSpider/blob/master/Image/partial.png)
<br>
Full comment 
![评论都是完整评论](https://github.com/Dengqlbq/JDSpider/blob/master/Image/comment.png)
