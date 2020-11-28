# 使用方法
- `python main.py`设置执行定时任务,每天中午十二点定时爬取数据，输出文件有两个
    1. `in_port_{dt}.json`  长春龙嘉国际机场航班进港情况
    2. `out_port_{dt}.json` 长春龙嘉国际机场航班出港情况

    其中`{dt}`为`yyyy-mm-dd`格式的日期
- 单独跑今天的数据
    1. `scrapy crawl in_port -o {file_name}` 为输出今天的长春龙嘉国际机场航班进港情况
    2. `scrapy crawl out_port -o {file_name}` 为输出今天的长春龙嘉国际机场航班出港情况
    
    其中`{file_name}`为输出的文件名