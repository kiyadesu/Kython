import requests
import hashlib
import time

PAGENUMBER = 1 			# 第几页

host = "http://api.91dict.com"
SRTString = "qthYkmVEEJsui2pymyfiOAgCb4VLb55J"	# bytes2string，固定值
USERAGENT = "RRDict/1.3 10/4.4.4 1/1.0.23"		# 词典版本+系统版本
DID = "358239054072808"							# Android:IMEI	 IOS:uuid

headers = {
	"did": DID,
	"User-Agent": USERAGENT,
	"Accept-Encoding": "gzip, deflate",
	"Connection": "keep-alive"
}


millis = int(round(time.time()))
ak1_md5 = hashlib.md5(SRTString + USERAGENT + DID + str(millis))
ak1_res = ak1_md5.hexdigest()

init_payload = { 
	'ak':ak1_res, 
	't':millis
}

# 请求一个ck值
res = requests.get(host + "/init", headers=headers , params=init_payload)
print res.url
print res.text
res_json =  res.json()

CK =  res_json[u"ck"]
context = 'pageNo=' + str(PAGENUMBER) + '&pageSize=20'
ak2 = SRTString + CK + USERAGENT + DID + str(millis) + context
ak2_md5 = hashlib.md5(ak2)
ak2_res = ak2_md5.hexdigest()

req_payload = {
	'ak' : ak2_res,
	'pageNo' : str(PAGENUMBER),
	'pageSize' : '20',
	't' : millis
}

# 带着上次的ck值请求内容
res = requests.get(host + "/index", headers=headers , params=req_payload)
print res.url
print res.text







