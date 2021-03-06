Stock Crawler
=============
Stock Crawler for [台灣證券交易所](http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php) 

## Parameter

| Select Type |Description |
| ----------  | -------- |
|MS           |  大盤統計資訊|
|MS2          |  委託及成交統計資訊|
|ALL          |  貿易百貨|
|ALLBUT0999   |  全部(不含權證、牛熊證、可展延牛熊證)|
|0049         |  封閉式基金|
|0099P        |  ETF|
|019919T      |  受益證券|
|0999         |  認購權證(不含牛證)|
|0999P        |  認售權證(不含熊證)|
|0999C        |  牛證|
|0999B        |  熊證|
|0999X        |  可展延牛證|
|0999Y        |  可展延熊證|
|0999GA       |  附認股權特別股|
|0999GD       |  附認股權公司債|
|0999G9       |  認股權憑證|
|CB           |  可轉換公司債|
|01           |  水泥工業|
|02           |  食品工業|
|03           |  塑膠工業|
|04           |  紡織纖維|
|05           |  電機機械|
|06           |  電器電纜|
|07           |  化學生技醫療|
|21           |  化學工業|
|22           |  生技醫療業|
|08           |  玻璃陶瓷|
|09           |  造紙工業|
|10           |  鋼鐵工業|
|11           |  橡膠工業|
|12           |  汽車工業|
|13           |  電子工業|
|24           |  半導體業|
|25           |  電腦及週邊設備業|
|26           |  光電業|
|27           |  通信網路業|
|28           |  電子零組件業|
|29           |  電子通路業|
|30           |  資訊服務業|
|31           |  其他電子業|
|14           |  建材營造|
|15           |  航運業|
|16           |  觀光事業|
|17           |  金融保險|
|18           |  貿易百貨|
|9299         |  存託憑證|
|23           |  油電燃氣業|
|19           |  綜合     |
|20           |  其他     |

## Requirement

- [Python3](https://www.python.org/)

## Run

```
python StockAll_dbyd.py
```

If you **just** upgraded your python from 2 to 3, the older version (i.e. python 2) might still exist. If this is the case, try

```
python3 StockAll_dbyd.py
```

If it works, the retrived results will be in `stock_all_byday` folder, even if you interrupt the program.

## FAQ
- Why I get the error regarding "urllib.parse"?
Check your Python version by typing

```
python --version
```

Make sure you have updated to Python 3

## Change Log

#### 2015/03/30 v0.0.1
- init
