# -*- coding: utf-8 -*-
import scrapy
from PIL import Image
import urllib
class DbSpider(scrapy.Spider):
    name = "db"
    # allowed_domains = ["douban.com"]
    start_urls = (
        'https://accounts.douban.com/login',
    )

    def parse(self, response):
        captcha =response.xpath("//img[@id='captcha_image']/@src").extract_first()
        if captcha:
            print (captcha)
            print ('find captcha...')
            urllib.urlretrieve(captcha, 'captcha.jpg')
            Image.open('captcha.jpg')
            cap = raw_input('input captcha manually:')
            captcha_id = response.xpath("//input[@name='captcha-id']/@value").extract_first()
            print (captcha_id)
            yield scrapy.FormRequest(
                url='https://accounts.douban.com/login',
                formdata={
                    'source': 'None',
                    'redir': 'https://www.douban.com /',
                    'form_email': '15995743001',
                    'form_password': '1993827',
                    'login': '登录',
                    'captcha-solution': cap,
                    'captcha-id': captcha_id
                },
                callback=self.parse_after_login,
            )
        else:
            print ('no captcha')
            yield scrapy.FormRequest(
                url='https://accounts.douban.com/login',
                formdata={
                    'source': 'None',
                    'redir': 'https://www.douban.com /',
                    'form_email': '15995743001',
                    'form_password': '1993827',
                    'login': '登录',
                },
                callback=self.parse_after_login,
            )


    def parse_after_login(self, response):
        if response.url == 'https://www.douban.com/':
            print('登录成功')
        else:
            print('登录失败')
        