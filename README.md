# JDSpider

### 目标：分布式爬取京东商品详情，评论和评论总结

### Power by:
1. Python 3.6
2. Scrapy 1.4
3. pymysql
4. json
5. redis

#### Project blog:  writing...
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

```
Note: Before you run the project, make sure that you have created tables match the requirement
```

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
