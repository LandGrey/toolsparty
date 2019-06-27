# toolsparty

```
顾名思义, 自己写的、收集的渗透测试中常用的一些小脚本(非工具), 人生苦短, 节省生命.
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

    - [* domain_to_ip](https://github.com/LandGrey/taoman/blob/master/other/domain_to_ip.py)

    ```
    用途: 多线程批量将域名解析成IP地址;
          利用socket.gethostbyname()函数,没有深究其精准程度。
    
    用法: python domain_to_ip.py [domain_lists_path]
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
    - [ip-extender.py](information-gathering/ip-extender.py)

    ```
    用途: 根据收集的同一个目标的多个IP地址, 按照一定策略推测获得更多可能与目标有关联的 IP 地址范围(IP段/C段)。
    
    用法: python ip-extender.py list.txt
    ```

    - [* python_crypto](https://github.com/vergl4s/pentesting-dump/blob/fe0e89cad5da1080bad8efd7979fe38ad2e58e9e/snippets/python_crypto/README.MD)

    ```
    用途: 集成了较多python加解密相关的代码,用到了可以快速借鉴下相关代码。
    ```



    #### 目标收集

    - [crtsh.py](information-gathering/crtsh.py)

    ```
    用途: 使用https://crt.sh/网站, 根据网站域名证书来寻找使用同一证书的域名;
          对快速搜索同属于一个公司/组织的顶级域很有用。
    
    用法: python crtsh.py example.com
    ```
    - [owt.py](information-gathering/owt.py)

    ```
    用途: 正确的批量获取网站Title。
    
    用法: python owt.py -x 10 -t target.txt
    ```

* 杂项

    - [awvs.bat](miscellaneous/awvs.bat)

    ```
    用途: 将Windows平台上安装的AWVS服务设置为手动,需要时用此脚本开启服务;
          将脚本放在"C:\Users\YourName"目录下,按win+r键,用awvs命令使用脚本。
    
    用法: 直接运行
    ```
    - [* dnstricker](https://github.com/LandGrey/dnstricker/blob/master/dnstricker.py)

    ```
    用途: 监听本地端口,响应配置好的DNS记录;
          logeyes平台的一部分,用来模拟dns请求的响应。
    
    用法: python domain_to_ip.py [domain_lists_path]
    ```
    - [getFileType.py](miscellaneous/getFileType.py)

    ```
    用途: 根据文件头前几个字节判断文件类型;
          早期写的代码,有点烂,可以修改源码里的数据字典,识别更多类型文件。
    
    用法: python getFileType.py [file_path]
    ```
    - [nessus.bat](miscellaneous/nessus.bat)

    ```
    用途: 将Windows平台上安装的Nessus服务设置为手动,需要时用此脚本开启服务;
          将脚本放在"C:\Users\YourName"目录下,按win+r键,用nessus命令使用脚本。
    
    用法: 直接运行
    ```
    - [vpnTrafficSwitcher.bat](miscellaneous/vpnTrafficSwitcher.bat)

    ```
    用途: 使用Windows防火墙策略指定出口IP地址,防止使用VPN时真实流量外漏
          适用于Windows7 及以上版本,其它版本按情况修改dos命令
    
    用法: 直接运行,"yes"启用策略,设置VPN的ip地址;"no"恢复原样.
    ```
