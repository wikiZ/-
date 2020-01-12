#!/usr/bin/python
#coding:utf-8



import requests
from colorama import init
import threading
import argparse
import sys
import json


init(autoreset=True)
def banner():
	try:
		print("\033[0;32;40m\t\t\t\tDirectory Scanner v2.0\033[0m")
		print("           _     _")	#这段图片我是真的不会搞就网上找了贴上了
		print("          (_)   | |")
		print(" _ __ ___  _ ___| |_____ ____")
		print("| '_ ` _ \| / __| __/ _ \ '__|"+"\033[0;36;40m\t\t大风起兮云飞扬\033[0m")
		print("| | | | | | \__ \ ||  __/ |")
		print("|_| |_| |_|_|___/\__\___|_|")
		print("\033[0;33;40m\t\t\t\tHello World!\033[0m")
		print("\n")

		print("用法:")
		print("	--help:帮助文档")
		print("	-u:网址 (http://www.baidu.com)")
		print("	-d:字典 (-d C:/Users/asus/Desktop/Directory scanning/dict.txt)")
		print("	-s:只显示HTTP状态码为200的页面")
		print("	-o:将扫描结果输出至指定文件 (-o C:/Users/asus/Desktop/a.txt)")
	except:
		pass
    
def doc():
	"""@author 风起 QQ:1402720815"""
	"""要是妹子发现这条注释就加我啊╰(●’◡’●)╮"""
	pass	


def main():
	try:
		banner()
		#print(doc.__doc__)
		parser = argparse.ArgumentParser()
		parser.description="使用教程"
		parser.add_argument("-u","--url", help="输入探测网站的url地址")
		parser.add_argument("-d","--dict", help="指定字典文件",default="dict.txt")
		parser.add_argument("-s","--succeed", help="只显示成功访问的页面",action="store_true")
		parser.add_argument("-o","--output", help="将扫描结果输出至指定文件")
		print("\n")
		args = parser.parse_args()
		HttpError=0
		HttpError=args.url.find("http://")
		if HttpError is -1:
			print("\033[41m默认使用http协议如需指定https协议请在url前手动指定。")
			args.url="http://"+args.url
		d=read(args.url,args.dict,args.succeed)
		if args.output is not None:
			write(args.output,d)
		
	except:
		pass

		
def read(url,dict,succeed):
	try:
		d={}
		for line in open(dict,"r"):
			urls=url+line.strip()		#当指定的字典中目录名前不存在/则替换本行代码进行拼接urls=url+"/"+line.strip()
			r=requests.get(urls,timeout=1)
			if succeed:
				if r.status_code is not 200:
					continue
				else:
					print(urls,"-",r.status_code)
			else:
				print(urls,"-",r.status_code)
			if r.status_code is 200:
				d[urls]=r.status_code	
		return d
	except KeyboardInterrupt:
		pass
		

def write(output,d):
	try:
		with open(output,"w") as file:
			for key,value in d.items():
				file.write(str(key)+" - "+str(value)+"\n")
	except Exception as e:
		print("\033[41m输出格式可能存在错误!")


			
if __name__=="__main__":
	try:	
		t=threading.Thread(target=main)
		t.start()
	except:
		pass
	