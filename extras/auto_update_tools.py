import requests
import zipfile
from lxml import etree

def auto_update_tools():
    download_apktools()
    pass

def download_apktools():
    url = 'https://ibotpeaches.github.io/Apktool/'
    response = requests.get(url)
    if response.status_code == 200:
        download_xpath = etree.HTML(response.content).xpath("//ul[@class='nav navbar-nav']/li[@data-toggle='tooltip']/a")
        download_url = download_xpath.xpath('./@href').extract_first()
        download_version = download_xpath.xpath('./strong/text()').extract_first()

        if download_url:
            print("Downloading apktools.Version %s" % download_version)
            download_file = requests.get(download_url)
            with open("apktools/apktools_%s.jar" % download_version,'r') as file:
                file.write(download_file.content)
        else:
            print("Downing Fail")
    else:
        print("Downing Fail")

if __name__ == '__main__':
    auto_update_tools()

