# toolsparty

```
顾名思义, 自己写的渗透测试中常用的一些小脚本, 人生苦短, 节省生命.
上传至此, 防止像以前一样, 写完就丢, 也算个积累吧. 
```


## 详情：

```
1. 按照工具可能被用的渗透测试阶段分类,并不唯一
2. 名字以"* "开头的工具,表示不在本仓库内,可到链接地址下载
```

* 信息收集

    #### 数据处理

    - [* counter](https://github.com/LandGrey/pydictor)

    ```
    用途: 按照指定分隔符(默认换行符)对文本单词的出现频率进行统计;
          pydictor 的内置功能,避免自己造轮子。
    
    用法: python pydictor.py -tool counter [v,s,vs] [file_path] [view_num]
    ```
    - [filter.py](information-gathering/filter.py)

    ```
    用途: 分类提取某个文件或文件夹中所有可能的域名、邮件帐户、内部ip、外网ip;
          再也不用傻瓜式的一个个手工复制粘贴了,表示伤不起。
    
    用法: python filter.py file_or_dir [domain_limit(可选)]
    ```
    - [* uniqbiner](https://github.com/LandGrey/pydictor)

    ```
    用途: 对指定目录及其子目录下所有文本文件进行合并去重;
          pydictor 的内置功能,避免自己造轮子。
    
    用法: python pydictor.py -tool uniqbiner [dir_path]
    ```
    - [* uniqifer](https://github.com/LandGrey/pydictor)

    ```
    用途: 对爆破字典、域名等文本保持原来顺序的去重;
          pydictor 的内置功能,避免自己造轮子。
    
    用法: python pydictor.py -tool uniqifer [file_path]
    ```

    #### 目标收集

    - [crtsh.py](information-gathering/crtsh.py)

    ```
    用途: 使用https://crt.sh/网站, 根据网站域名证书来寻找使用同一证书的域名;
          对快速搜索同属于一个公司/组织的顶级域很有用。
    
    用法: python crtsh.py example.com
    ```

* 杂项

    - [getFileType.py](miscellaneous/getFileType.py)

    ```
    用途: 根据文件头前几个字节判断文件类型;
          早期写的代码,有点烂,可以修改源码里的数据字典,识别更多类型文件。
    
    用法: python getFileType.py [file_path]
    ```
