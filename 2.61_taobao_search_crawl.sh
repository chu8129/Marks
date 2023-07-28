curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker qw
sudo docker pull scrapinghub/splash
# docker run -d -p 8050:8050 scrapinghub/splash

sudo docker run -d -p 8050:8050 --memory=2G --restart=always scrapinghub/splash --maxrss 4000
scrapy startproject taobao
cd taobao
scrapy genspider taobao_goods taobao.com


## 代码不公开了，一堆干无意义事情的
## 极其吐槽那些培训，都是拿爬虫说事，一堆僵尸爬虫
