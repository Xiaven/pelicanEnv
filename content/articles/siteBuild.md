Title:基于Pelican的Blog搭建 
Date: 2015-09-17 21:06
Category: Web 
Author: Raven 
Summary: 搭建全记录


记录下小站的搭建过程：

###1. 简介

**Pelican**

Pelican是一个用Python语言编写的静态网站生成器，支持使用restructuredText和Markdown写文章，配置灵活，扩展性强，有许多优秀的主题和插件可供使用。

Pelican 的Github地址是：<https://github.com/getpelican/pelican>

**Github Pages**

GitHub Pages本用于介绍托管在GitHub的项目， 由于空间免费稳定，用来做搭建一个博客再好不过。

Github Pages提供了两种Pages模式：

1.** User/Organization Pages** 个人或公司站点

- 使用自己的用户名，每个用户名下面只能建立一个；

- 资源命名必须符合这样的规则username/username.github.com；

- 主干上内容被用来构建和发布页面

2.** Project Pages**项目站点

-  gh-pages分支用于构建和发布；

- 如果user/org pages使用了独立域名，那么托管在账户下的所有project pages将使用相同的域名进行重定向，除非project pages使用了自己的独立域名；

- 如果没有使用独立域名，project pages将通过子路径的形式提供服务username.github.com/projectname；

- 自定义404页面只能在独立域名下使用，否则会使用User Pages 404；

这里选用了项目站点, gh-pages这种方式

###2. Git的安装与配置
安装

	apt-get install git

配置

	git config --global user.name "xxx"
	git config --global user.emailxxx@gmail.com 

配置Git验证   
Git的验证方式有Https和SSH两种，这里选用Https, 配置Git的credential helper

	git config --global credential.helper cache
	git config --global credential.helper 'cache --timeout=3600'

查看配置信息

	git config --list 

###3. Pelican的安装与快速向导
安装

	pip install pelican 
	pip install markdown

创建项目目录

	mkdir myblog
	cd myblog

运行pelican快速向导

	pelican-quickstart

	Welcome to pelican-quickstart v3.6.3.

	This script will help you create a new Pelican-based website.

	Please answer the following questions so this script can generate the files
	needed by Pelican.

	    
	> Where do you want to create your new web site? [.] 
	> What will be the title of this web site? Raven Site
	> Who will be the author of this web site? Raven
	> What will be the default language of this web site? [en] zh
	> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) y
	> What is your URL prefix? (see above example; no trailing slash) http://raven47git.github.io    
	> Do you want to enable article pagination? (Y/n) 
	> How many articles per page do you want? [10] 
	> What is your time zone? [Europe/Paris] 
	> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) 
	> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) 
	> Do you want to upload your website using FTP? (y/N) 
	> Do you want to upload your website using SSH? (y/N) 
	> Do you want to upload your website using Dropbox? (y/N) 
	> Do you want to upload your website using S3? (y/N) 
	> Do you want to upload your website using Rackspace Cloud Files? (y/N) 
	> Do you want to upload your website using GitHub Pages? (y/N) y
	Done. Your new project is available at /home/raven/python/pelican_env/src/blog

配置pelicanconf.py,加入如下内容

	# Content path
	PATH = 'content'
	PAGE_PATHS = ['pages']
	ARTICLE_PATHS = ['articles']
	STATIC_PATHS = ['images', 'files']

	# URL
	SITEURL = 'http://raven47git.github.io/blog'
	ARTICLE_URL = ('articles/{slug}.html')
	ARTICLE_SAVE_AS = ('articles/{slug}.html')


进入content目录,创建一些相关的内容目录

	mkdir articles files images pages


###4. 使用Markdown撰写第一篇Blog

	cd articles
	vi hello.md
内容为

	Title: Hello
	Date: 2015-09-17 20:32
	Category: Other 
	Author: Raven 
	Summary: hello 

	Hello,everyone!

编译页面

	make html

**预览结果**
直接调用脚本develop_server.sh即可

	./develop_server.sh start

	./develop_server.sh stop


打开<http://localhost:8000/>即可看到生成的页面


###5. 上传到github pages

首先需要在github主页里创建一个新的repo: myblog, 接下来就生成的页面push到这个repo

	cd output
	git init
	git checkout --orphan gh-pages
	git remote add origin https://github.com/raven47git/myblog.git
	git add -A
	git commit -m "Update Blog"
	git push -u origin gh-pages

现在去 <http://raven47git.github.io/myblog>即可看到劳动成果啦～～

###6. 其他：

**主题设置**

下载风格包pelican-themes与插件包pelican-plugins

	git clone https://github.com/getpelican/pelican-themes.git
	git clone https://github.com/getpelican/pelican-plugins.git

在pelican-thems中选择一个喜欢的主题， 放入 blog所在文件夹，在配置文件中指定主题名称

	THEME = 'zurb-F5-basic'

###7. 总结

一步一步摸索着建起这个Blog，还是蛮有意思的，希望对也想搭一个类似Blog的各位有些帮助。

Pelican doc:    
 <http://pelican.readthedocs.org/en/3.6.3/quickstart.html>

Python Markdown:   
<http://pythonhosted.org/Markdown/index.html>

