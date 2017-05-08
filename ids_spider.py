#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# author: cheny1ran <chenyr626@gmail.com>

import urllib2
from lxml import etree
from io import StringIO, BytesIO

rootPage = "http://shenfenzheng.bajiu.cn"
pvs = ['北京市','天津市','河北省','内蒙古自治区','山西省','福建省','江西省','山东省','浙江省','江苏省','安徽省',
'上海市','海南省','广西壮族自治区','广东省','湖南省','湖北省','河南省','辽宁省','吉林省','黑龙江省','新疆维吾尔自治区',
'青海省','宁夏回族自治区','甘肃省','陕西省','西藏自治区','贵州省','云南省','四川省','重庆市']
rvs = ['北京市','天津市','上海市','重庆市']

csv = '/Users/it/Documents/idsPython1.csv'
file = open(csv,'a')

for i in range(1,32):
	url = rootPage + "/?id=" + str(i)
	province = urllib2.urlopen(url)
	htt = etree.HTML(province.read())
	provinceName = unicode(pvs[i-1],'utf-8')
	for i in htt.xpath('/html/body/main/article/p[2]/a'):
		cityName = i.text
		cityUrl = rootPage + i.get('href')
		city = urllib2.urlopen(cityUrl)
		cityHtt = etree.HTML(city.read())

		idNum = unicode(cityHtt.xpath('/html/body/main/article/p[1]/span[1]/text()[1]')[0],'utf-8')
		# print idNum
		try:
			flag = cityHtt.xpath('/html/body/main/article/p[2]/a')[0]

			for i in cityHtt.xpath('/html/body/main/article/p[2]/a'):
				countyName = i.text
				countyUrl = rootPage + i.get('href')
				county = urllib2.urlopen(countyUrl)
				countyHtt = etree.HTML(county.read())
				idNum = countyHtt.xpath('/html/body/main/article/p[1]/span[1]/text()[1]')[0]
				ans = '"' + idNum + '","' + provinceName + '","' + cityName + '","' + countyName + '"'
				print ans
				file.write(ans.encode('utf-8'))
				file.write('\n')
		except IndexError, e:
			ans = ''
			if provinceName == u'北京市' or provinceName == u'天津市' or provinceName == u'上海市' or provinceName == u'重庆市':
				ans = '"' + idNum + '","' + provinceName + '","' + provinceName + '","' + cityName + '"'
			else:
				ans = '"' + idNum + '","' + provinceName + '","' + cityName + '","' + 'none' + '"'
			print ans
			file.write(ans.encode('utf-8'))
			file.write('\n')
		

		
		
		
	
