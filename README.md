# ids_spider(python2)
python爬虫 用于抓取身份证前六位的省市区信息

信息来自于：八九网（http://shenfenzheng.bajiu.cn/?daquan）

已知的问题：ip失效 报`urllib2.URLError: <urlopen error [Errno 60] Operation timed out>`
> 可以尝试使用 proxy
> 简单但麻烦的办法是从断的地方继续跑，修改循环`range`即可，因为文件是`append`模式，记得要删除之前跑了一半的该省内容
