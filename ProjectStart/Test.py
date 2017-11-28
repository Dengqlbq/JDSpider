import redis
from urllib import parse

r = redis.Redis(host='YOUR_HOST', port=6379, password='YOUT_PASS_IF_HAVE')

# 测试关键词
keywords = '电脑'
keywords = parse.quote(keywords)

# 测试页数
page_count = 10
current_page = 1
start_index = 1

url = 'https://search.jd.com/Search?keyword={0}&enc=utf-8&qrst=1&rt' \
      '=1&stop=1&vt=2&wq={1}&page={2}&s={3}&click=0'

# 这里只能获取每一页的一半商品url，另一半是异步加载出来的
# 在测试中先忽略这部分商品url
for i in range(page_count):
    r.lpush('JDUrlsSpider', url.format(keywords, keywords, current_page, start_index))
    current_page += 2
    start_index += 55
