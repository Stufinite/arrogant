# GluttonyTw（暴食）

今天吃什麼的api

_`gluttony`_ 是天主教中七原罪的暴食之罪<br>
因為貼切反應學生使用此功能的動機<br>
所以以此命名。無奈gluttony在pypi上已經被註冊過了，所以後面加上Tw

_`gluttonyTw`_ 提供兩類api

1. 顧客類：可以用來定餐、查詢過往定餐紀錄等等。
2. 餐廳類：可以查店家資訊、菜色以及收到的訂單。

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [API](#api)
  - [parameter](#parameter)
  - [usage and Results](#usage-and-results)
- [Getting Started](#getting-started)
- [Prerequisities](#prerequisities)
- [Installing](#installing)
- [Running & Testing](#running--testing)
- [Run](#run)
  - [Break down into end to end tests](#break-down-into-end-to-end-tests)
  - [And coding style tests](#and-coding-style-tests)
- [Deployment](#deployment)
- [Built With](#built-with)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## API

api domain：目前還沒架起來，所以暫定`127.0.0.1`<br>
請在api domain後面接上正確的url pattern以及query string<br>
詳細的參數以及結果請參閱下面介紹

### parameter

- `res_id`：餐廳的id
- `order_id`：訂單的id，用在揪團訂購的時候，需要指定你要參加的是哪一筆揪團訂單
- `date`：時間參數

### usage and Results

API使用方式（下面所寫的是api的URL pattern）<br>
Usage of API (pattern written below is URL pattern)：

- 餐廳類別：<br>
  可以查店家資訊、菜色以及收到的訂單。

  1. _`api/restaurant/`_：取得餐廳的訂單資料，需要指定餐廳id

    - 加上`date`參數可以指定某日期的訂單： `http://127.0.0.1:8000/t2e/api/restaurant/?res_id=1&date=2017-2-1`

      ```
      {
      "Score": 3,
      "Type": [
      "中式"
      ],
      "ResName": "鼎日",
      "OrderList": [
      {
      "total": 300,
      "OrderId": 1,
      "ResOrder": {
      "今日特餐": 6
      },
      "Create": "2017-02-01T13:26:57.447Z"
      }
      ],
      "Date": "2017-02-01",
      "ResAddress": "台中市南區興大路"
      }
      ```

    - 不加date預設是顯示當天的訂單： `http://127.0.0.1:8000/t2e/api/restaurant/?res_id=1`

      ```
      {
      "Score": 3,
      "Type": [
      "中式"
      ],
      "ResName": "鼎日",
      "OrderList": [],
      "Date": "2017-02-02",
      "ResAddress": "台中市南區興大路"
      }
      ```

  2. _`api/restaurant/prof/`_：取得餐廳的介紹，並且回傳照片的網址

    - 需要指定res_id（餐廳在資料庫的id）： `http://127.0.0.1:8000/t2e/api/restaurant/prof/?res_id=1`

      ```
      {
      "last_reserv": "20:00",
      "feature": "http://127.0.0.1:8000/media/%E6%96%99%E7%90%86%E7%89%B9%E8%89%B2.jpg",
      "environment": "http://127.0.0.1:8000/media/%E7%94%A8%E9%A4%90%E7%92%B0%E5%A2%83.jpg",
      "ResName": "鼎日",
      "envText": "以新鮮食材佐特製湯頭，搭配風格設計空間，讓聚餐除了享受美食，也能提升時尚品味！",
      "ResFavorDish": [],
      "ResLike": 50,
      "phone": [
      "0972800000"
      ],
      "featureText": "均勻分布的油花與鮮紅肉質，讓口感更加紮實不凡，肉獨有的香氣與油花潤飾，放進精心熬煮清甜的湯汁中輕涮，令人流連忘返的香滑柔嫩口感，讓你感動不已！",
      "date": [],
      "country": "台中市",
      "address": "台中市南區興大路",
      "avatar": "http://127.0.0.1:8000/media/%E9%8D%8B%E8%A3%A1%E9%8D%8B%E7%89%A9.jpg",
      "score": 3
      }
      ```

  3. _`api/restaurant/list/`_：取得包含所有餐廳的陣列

    - `start`：從第幾筆餐廳資料開始
    - `gap`(optional)：一次取幾筆，預設值是15筆
    - 範例： `http://127.0.0.1:8000/t2e/api/restaurant/list?start=1`

      ```
      [
      {
      "avatar": "http://127.0.0.1:8000/media/%E9%8D%8B%E8%A3%A1%E9%8D%8B%E7%89%A9.jpg",
      "score": 3,
      "ResName": "鼎日",
      "ResLike": 50
      }
      ]
      ```

  4. _`api/restaurant/menu/`_：取得餐廳的菜單與照片

    - 需要指定res_id（餐廳在資料庫的id）： `http://127.0.0.1:8000/t2e/api/restaurant/menu/?res_id=1`

      ```
      {
      "dish": [
      {
      "price": 50,
      "image": "http://127.0.0.1:8000/media/%E6%8E%92%E9%AA%A8%E9%A3%AF.jpg",
      "isSpicy": true,
      "name": "今日特餐"
      }
      ],
      "menu": [
      "http://127.0.0.1:8000/media/%E8%8F%9C%E5%96%AE_FtgeMqS.jpg"
      ]
      }
      ```

  4. _`api/restaurant/boss/`_：讓老闆可以看到他們該月份的營業額

    - 需要指定res_id（餐廳在資料庫的id）： `http://127.0.0.1:8000/t2e/api/restaurant/boss/?res_id=1`

      ```
      {
        "chart": {
          "2017-04-01": 50,
          "2017-04-02": 80,
          ...
          "2017-04-30": 120
        },
        "sells": {
          "今日特餐": {
            "price": 50000,
            "amout": 1000
          }
        },
        "revenue": 70000
      }
      ```

- 顧客類別：<br>
  可以用來定餐、查詢過往定餐紀錄等等。

  1. _`api/order/user/`_：取得顧客的訂單資料

    - 加上`date`參數可以指定某日期的訂單： `http://127.0.0.1:8000/t2e/api/order/user/?date=2017-02-01`

      ```
      {
      "Order": [
      {
        "create": "2017-02-01T14:36:13.239Z",
        "total": 100,
        "meal": [
          {
            "name": "今日特餐",
            "amount": "2"
          }
        ]
      }
      ],
      "User": "root",
      "FDish": null,
      "Date": "2017-02-01",
      "Ftype": null
      }
      ```

    - 不加date預設是顯示當天的訂單： `http://127.0.0.1:8000/t2e/api/order/user/`

      ```
      {
      "Order": [],
      "User": "root",
      "FDish": null,
      "Date": "2017-02-02",
      "Ftype": null
      }
      ```

  2. _`api/order/join`_：發起揪團訂單或是參加揪團訂購
    - 程式實作：呼叫此api要用post  
    以下用python示範：
    ```
    >>> import requests  
    >>> payload={'今日特餐':2, 'period':'午餐'}
    >>> # 建立訂單 requests.post('http://127.0.0.1:8000/t2e/api/order/join?res_id=1', data=payload)
    >>> # 參與揪團 requests.post('http://127.0.0.1:8000/t2e/api/order/join?order_id=10', data=payload)
    ```

    - 發起人需要指定res_id（餐廳在資料庫的id）： `http://127.0.0.1:8000/t2e/api/order/join/?res_id=1`

      ```
      {"purchase": "success"}
      ```

    - 參與揪團的人要指定orderID （訂單在資料庫的id）： `http://127.0.0.1:8000/t2e/api/order/join/?order_id=6`

      ```
      {"purchase": "success"}
      ```

  3. *`api/order/join_order_list/`*：取得包含所有揪團訂單的陣列  

    - 需要指定res_id（餐廳在資料庫的id）： `http://127.0.0.1:8000/t2e/api/order/join_order_list/?res_id=1`

      ```
      [
  {
    "createUser": "root",
    "period": "午餐",
    "restaurant": "鼎日",
    "order_id": 1
  },
  {
    "createUser": "root",
    "period": "午餐",
    "restaurant": "鼎日",
    "order_id": 2
  },
]
      ```
- 留言版：<br>
  回傳該間餐廳的留言評價  
  1. *`/api/restaurant/comment/`*：顯示該間餐廳的留言 or 留言給餐廳
    * `res_id`：餐廳ID
      * 顯示該間餐廳的留言：
        * （optional）`start`：從第幾筆餐廳留言開始取，留言有按讚數量（like），Descending排列，每次提供 start ~ start + 15 的範圍
      * 留言給餐廳：
        * （optional）post所接受的欄位如下：
          ```
          class Comment(models.Model):
              restaurant = models.ForeignKey(ResProf)
              author = models.ForeignKey(EatUser)
              feeling = models.CharField(max_length=200, null=True)
              like = models.PositiveSmallIntegerField(default=1)
          ```
    * Get範例：`http://127.0.0.1:8000/t2e/api/restaurant/comment/?res_id=1&start=1`  
    ```
    [
  {
    "fields": {
      "author": 1,
      "feeling": "還行拉 蠻有特色的店",
      "like": 20
    },
    "model": "gluttonyTw.comment",
    "pk": 3
  },
  {
    "fields": {
      "author": 1,
      "feeling": "氣氛佳 不過稍貴就是了",
      "like": 10
    },
    "model": "gluttonyTw.comment",
    "pk": 2
  },
]
    ```
    * Post範例：
      ```
      等松鬆綁上去測測看 因為使用者帳號的Request一定要從網頁發出去我才知道他的帳號
      我現在覽的綁到網頁上所以你幫我測一下XD
      ```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisities

1. OS：Ubuntu / OSX would be nice
2. environment：need `python3`

  - Linux：`sudo apt-get update; sudo apt-get install; python3 python3-dev`
  - OSX：`brew install python3`

## Installing

1. `pip install gluttonyTw`

## Running & Testing

## Run

1. `settings.py`裏面需要新增`gluttonyTw`這個app：

  - add this:

    ```
    INSTALLED_APPS=[
    ...
    ...
    ...
    'gluttonyTw',
    ]
    ```

2. `urls.py`需要新增下列代碼 把所有search開頭的request都導向到`gluttonyTw`這個app：

  - add this:

    ```
    import gluttonyTw.urls
    urlpatterns += [
        url(r'^t2e/',include(gluttonyTw.urls,namespace="gluttonyTw") ),
    ]
    ```

3. `python manage.py runserver`：即可進入頁面測試 `gluttonyTw` 是否安裝成功。

### Break down into end to end tests

目前還沒寫測試...

### And coding style tests

目前沒有coding style tests...

## Deployment

`curso` is a django-app, so depends on django project.

`暴食` 是一般的django插件，所以必須依存於django專案

## Built With

- djangoApiDec==1.2,

## Contributors

- **張泰瑋** [david](https://github.com/david30907d)

## License

This package use `GPL3.0` License.

## Acknowledgments

感謝 `剛之煉金術師`給予命名靈感
