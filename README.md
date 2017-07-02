# Arrogant（傲慢）

![剛之煉金術師的怠惰](http://att.bbs.duowan.com/forum/201311/04/194746kxk1y8j331lqji8i.jpg)

求職資訊的api
_`arrogant`_ 是天主教中七原罪的傲慢之罪<br>
因為系統會幫學生累計他們的實習紀錄等等，當成`胸前的勳章`<br>
期望大家在累積的過程中要小心不要傲慢(好像有點牽強XD)


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

- `school`：餐廳的id
- `dept`：系所。
- `degree`：年級。
- `location`：所在的縣市名稱。
- `start`：如果回傳型態是陣列的話，需要指定回傳陣列的哪個部份（python的slice）。例如回傳使用者的評論時，若指定start=1，則會回傳array[0:15]共15個。
- `id`：該職缺物件的ID

### usage and Results

API使用方式（下面所寫的是api的URL pattern）<br>
Usage of API (pattern written below is URL pattern)：


1. _`get/jvalue`_：  

  - 職缺id
  - example： [http://127.0.0.1:8000/arrogant/get/jvalue?id=38](http://127.0.0.1:8000/arrogant/get/jvalue?id=38)

    ```
    {
      "JobTag": [
        {
          "name": "數位內容",
          "id": 23
        }
      ],
      "name": "網頁後端工程師 實習生",
      "salary": "未公開",
      "feedback_FU": 3.0,
      "feedback_easy": 3.0,
      "id": 38,
      "feedback_salary": 3.0,
      "feedback_amount": 0,
      "Category": "全端/後端工程",
      "avatar": "https://s3-ap-northeast-1.amazonaws.com/yourator/banners/banners/000/000/387/original/6a641d3c178813441e8fb277182c3be6098478a6.jpg?1480993690",
      "has_salary_info": false,
      "feedback_freedom": 3.0,
      "category": 3,
      "intern_tf": true,
      "company": {
        "brand": "2erguy",
        "description": "你有機會加入一個偉大的團隊",
        "path": "/companies/2erguy",
        "banner": "https://s3-ap-northeast-1.amazonaws.com/yourator/banners/banners/000/000/387/original/6a641d3c178813441e8fb277182c3be6098478a6.jpg?1480993690",
        "公司規模": "4人",
        "資本額": "未公開",
        "area": "台北",
        "地址": "台北市中正區館前路65號11樓"
      },
      "path": "/companies/2erguy/jobs/597",
      "feedback_knowledgeable": 3.0,
      "skilltag": [
        {
          "skill_field": "後端",
          "name": "Rails",
          "id": 11
        },
        {
          "skill_field": "後端",
          "name": "Ruby",
          "id": 12
        }
      ]
    }
    ```

2. _`get/recommendJvalue`_：取得推荐的實習或求職執缺

  - dept
  - expample： [http://127.0.0.1:8000/arrogant/get/recommendJvalue?dept=資訊工程](http://127.0.0.1:8000/arrogant/get/recommendJvalue?dept=資訊工程)

    ```
    {
      "JobTag": [
        {
          "name": "APP",
          "id": 19
        }
      ],
      "name": "IOS / ReactNative 工程獅",
      "salary": "未公開",
      "feedback_FU": 3.0,
      "feedback_easy": 3.0,
      "id": 56,
      "feedback_salary": 3.0,
      "feedback_amount": 0,
      "Category": "iOS工程師",
      "avatar": "https://s3-ap-northeast-1.amazonaws.com/yourator/banners/banners/000/000/289/original/efe46eb2c4ebfdc9dc7bbcf99e38546a53931eaa.png?1476452562",
      "has_salary_info": false,
      "feedback_freedom": 3.0,
      "category": 11,
      "intern_tf": true,
      "company": {
        "brand": "tico 及時通訊",
        "description": "通訊軟體是最難作的世界級題目，\r\n沒有想清楚前不要來，\r\n來了就當你想清楚了。",
        "path": "/companies/tico",
        "banner": "https://s3-ap-northeast-1.amazonaws.com/yourator/banners/banners/000/000/289/original/efe46eb2c4ebfdc9dc7bbcf99e38546a53931eaa.png?1476452562",
        "公司規模": "3人",
        "資本額": "未公開",
        "area": "台北",
        "地址": "台北市大安區復興南路二段337巷六弄2號"
      },
      "path": "/companies/tico/jobs/1166",
      "feedback_knowledgeable": 3.0,
      "skilltag": [
        {
          "skill_field": "前端",
          "name": "Redux",
          "id": 16
        },
        {
          "skill_field": "後端",
          "name": "Node.js",
          "id": 8
        },
        {
          "skill_field": "行動",
          "name": "Objective-C",
          "id": 14
        },
        {
          "skill_field": "行動",
          "name": "Swift",
          "id": 17
        },
        {
          "skill_field": "行動",
          "name": "ReactNative",
          "id": 15
        }
      ]
    }
    ```

3. _`get/jlist`_：取得實習列表

  - start
  - 範例： [http://127.0.0.1:8000/arrogant/get/jlist?start=1](http://127.0.0.1:8000/arrogant/get/jlist?start=1)

    ```
    [
      {
        "TotalPage": 3,
        "category": "行銷/社群經營"
      },
      {
        "name": "電子商務 / 商品銷售企劃實習生",
        "salary": "未公開",
        "jobtag": [
          "電商"
        ],
    	...    
      },
      {
        "name": "行銷/社群人員 Marketing/Social Media",
        "salary": "NT$135 - NT$150(時薪)",
        "jobtag": [
          "O2O",
          "市場調查"
        ],
        ...
      }
    ]
    ```
4. _`get/comment`_：取得該實習的使用者留言

  - id
  - start  
  - expample： [http://127.0.0.1:8000/arrogant/get/comment?id=754&start=1](http://127.0.0.1:8000/arrogant/get/comment?id=754&start=1)

    ```
    [
      {
        "fields": {
          "Job": 754,
          "create": "2017-04-24T11:54:42Z",
          "raw": "測試測試"
        },
        "model": "arrogant.comment",
        "pk": 1
      },
      {
        "fields": {
          "Job": 754,
          "create": "2017-04-24T14:13:08.788Z",
          "raw": "這是測試"
        },
        "model": "arrogant.comment",
        "pk": 2
      },
      {
        "fields": {
          "Job": 754,
          "create": "2017-04-24T14:19:11.154Z",
          "raw": "測試第三次XD"
        },
        "model": "arrogant.comment",
        "pk": 3
      }
    ]
    ```
5. _`get/jcategory`_：取得所有實習的類型  
  - example：[http://127.0.0.1:8000/arrogant/get/jcategory](http://127.0.0.1:8000/arrogant/get/jcategory)
    ```
    [
      {
        "fields": {
          "name": "Data Science/ML"
        },
        "model": "arrogant.category",
        "pk": 1
      },
      {
        "fields": {
          "name": "編輯/內容經營"
        },
        "model": "arrogant.category",
        "pk": 2
      }
      ...
]
    ```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisities

1. OS：Ubuntu / OSX would be nice
2. environment：need `python3`

  - Linux：`sudo apt-get update; sudo apt-get install; python3 python3-dev`
  - OSX：`brew install python3`

## Installing

1. `pip install arrogant`

## Running & Testing

## Run

1. `settings.py`裏面需要新增`arrogant`這個app：

  - add this:

    ```
    INSTALLED_APPS=[
    ...
    ...
    ...
    'arrogant',
    ]
    ```

2. `urls.py`需要新增下列代碼 把所有search開頭的request都導向到`arrogant`這個app：

  - add this:

    ```
    import arrogant.urls
    urlpatterns += [
        url(r'^arrogant/',include(arrogant.urls, namespace="arrogant") ),
    ]
    ```

3. `python manage.py updateIntern yourator職缺.json`：把準備好的json插入資料庫中。

### Break down into end to end tests

目前還沒寫測試...

### And coding style tests

目前沒有coding style tests...

## Deployment

`arrogant` is a django-app, so depends on django project.

## Built With

- djangoApiDec,

## Contributors

- **張泰瑋** [david](https://github.com/david30907d)

## License

This package use `GPL3.0` License.

## Acknowledgments

感謝 `剛之煉金術師`給予命名靈感
