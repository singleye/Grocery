# 简介
中国行政区信息查询，可以用来开发分级地址管理功能。

# 功能
## 1. 查询API

### API 1: 获取district列表

**URL:** /district

**请求参数:**

N/A

**响应消息:**

格式: JSON

<pre><code>
{
   "data" : [
      {
         "name" : "中国",
         "level" : 1,
         "code" : "100000",
         "parent" : "-1"
      },
      {
         "parent" : "100000",
         "code" : "110000",
         "level" : 2,
         "name" : "北京市"
      },
      ...
      {
         "code" : "820000",
         "parent" : "100000",
         "level" : 2,
         "name" : "澳门特别行政区"
      }
   ],
   "status" : 0
}
</code></pre>


### API 2: 获取具体行政区信息

**URL:** /district/(?P\<code\>[0-9]{6})

**请求参数:**

|参数|类型|描述|
|---|---|---|
|code|str|6位数字组成的行政区号代码|

**响应消息:**

格式: JSON

<pre><code>
{
   "data" : {
      "level" : 1,
      "children" : [
         {
            "name" : "北京市",
            "level" : 2,
            "code" : "110000",
            "parent" : "100000"
         },
         ...
         {
            "parent" : "100000",
            "code" : "820000",
            "level" : 2,
            "name" : "澳门特别行政区"
         }
      ],
      "name" : "中国",
      "code" : "100000",
      "parent" : "-1"
   },
   "status" : 0
}
</code></pre>

## 2. 从原始行政区信息格式创建django fixture

执行district/data/create_fixture.py，输入参数是原始行政区格式"行政区号,级别,名称,父级行政区号"，指定输出文件后会创建fixture文件，fixture文件可以使用django loaddata加载进数据库。

<pre><code>
$ django loaddata data.json
</code></pre>

该功能可以用于后续行政区信息更新。