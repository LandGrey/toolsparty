# toolsparty

```
顾名思义, 自己写的渗透测试中常用的一些小脚本, 人生苦短, 节省生命.
上传至此, 防止像以前一样, 写完就丢, 也算个积累吧. 
```


## 详情：

* 信息收集

    - [crtsh.py](information-gathering/crtsh.py)

    ```
    用途: 使用https://crt.sh/网站, 根据网站域名证书来寻找使用同一证书的域名;
          对快速搜索同属于一个公司/组织的顶级域很有用。
    
    用法: python crtsh.py example.com
    ```
    - [filter.py](information-gathering/filter.py)

    ```
    用途: 分类提取某个文件或文件中所有可能的域名、邮件帐户、内部ip、外网ip;
          再也不用傻瓜式的一个个手工复制粘贴了,表示伤不起。
    
    用法: python filter.py file_or_dir [domain_limit(可选)]
    ```
