# JDSpider

### 目标：分布式爬取京东商品详情和评论

### Power by:
1. Python 3.6
2. Scrapy 1.4
3. pymysql
4. json
5. redis

#### Project blog:  writing...
---
### 进度：目前已可使用
~~1 服务器部署redis数据库  （done)~~<br>
~~2 服务器部署IP池   （done)~~<br>
~~3 获取指定关键词指定页数(max=100)所有商品url  （done）~~<br>
~~4 爬虫间通信  （done）~~<br>
~~5 爬取商品详情及评论总结  （done)~~<br>
~~6 爬取商品指定页数(max=100)评论  （done)~~<br>
7 获取指定关键词下所有商品url  (ing)

---
### How to use ？
```
git clone https://github.com/Dengqlbq/JDSpider.git
```

Override the following content
1. ProjectStart/Test.py  (redis configuration, keywords, page_count)
2. JDUrlsSpider/settings.py  (redis configuration)
3. JDDetailSpider/settings.py  (redis configuration, mysql configuration)
4. JDCommentSpider/settings.py  (redis configuratin, mysql configuration)

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
![1](https://github.com/Dengqlbq/JDSpider/blob/master/Image/detail.png)
![2](https://github.com/Dengqlbq/JDSpider/blob/master/Image/comment.png)
