#!/usr/bin/env python
#coding:utf-8

import requests
import os

api_host = "http://www.mycolordiary.com/s/api"
picture_host = "http://cdn.mycolordiary.com/s/img/"
out_dir = "."


# 背景: background
# 花边: lace
# 模板: diaryTemplate
def get_content(content_name):
	content_name_path = os.path.join(out_dir,content_name)
	if not os.path.exists(content_name_path):
		print "创建目录: " + content_name
		os.mkdir(content_name_path)

	content_name_payload = { 
		'cmd' : "ColorV120.getMaterialMallList", 
		'name' : content_name
	}

	min_sort = ""

	while True:
		print min_sort
		content_name_payload["idCompare"] = min_sort
		res = requests.post(api_host , data=content_name_payload)
		res_json =  res.json()
		datas =  res_json["res"]["datas"]

		if not datas :
			print "-> " + content_name + " complete"
			break

		min_sort = "<" + datas[len(datas)-1]["sort"]

		for item in datas:
			img_url = picture_host + item["imageSign"]
			img_path = content_name_path + "/" + item["id"] + "_" + item["name"] + ".png"
			if not os.path.exists(img_path):
				print "new " + content_name + " -> " + img_path
				img = requests.get(img_url)
				with open(img_path,'wb') as f:
					f.write(img.content)

# 贴纸: pasterTag
def get_paster():
	content_name = "paster"
	content_name_path = os.path.join(out_dir,content_name)
	if not os.path.exists(content_name_path):
		print "创建目录: " + content_name
		os.mkdir(content_name_path)

	content_name_payload = { 
		'cmd' : "ColorV120.getMaterialMallPasterTagList", 
		"isFree" : "-2",
		"limit" : "20"
	}

	min_sort = ""

	while True:
		print min_sort
		content_name_payload["idCompare"] = min_sort
		res = requests.post(api_host , data=content_name_payload)
		res_json =  res.json()
		datas =  res_json["res"]["datas"]

		if not datas :
			print "-> " + content_name + " complete"
			break

		min_sort = "<" + datas[len(datas)-1]["sort"]

		for data_item in datas:
			data_name = data_item['name']
			data_path = os.path.join(content_name_path,data_name)
			print data_name
			if not os.path.exists(data_path):
				os.mkdir(data_path)

			items = data_item["items"]
			for item in items:
				img_url = picture_host + item["imageSign"]
				img_path = data_path + "/" + item["id"] + "_" + item["name"] + ".png"
				if not os.path.exists(img_path):
					print "new " + data_name + " -> " + img_path
					img = requests.get(img_url)
					with open(img_path,'wb') as f:
						f.write(img.content)



	
if __name__ == '__main__':
	get_paster()
	# get_content("background")
	# get_content("diaryTemplate")
	# get_content("lace")
	











