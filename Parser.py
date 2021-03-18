import requests
from bs4 import BeautifulSoup
import re
import sys
import time
from selenium import webdriver
yellow="\033[1;33;40m"
red="\033[1;31;40m"
blue="\033[1;36;40m"
purple="\033[1;35;40m"
URL="https://codeforces.com/contest/"
def parse_contest(Content):
	print(Content)
	possible=Content.find_all('option')
	problems={}
	pattern=re.compile("[A-Z][0-9]?")
	for i in possible:
		x=str(i['value'])
		if pattern.match(x):
			problems[x]=1
	print(problems)
	return problems

def parse_problem(problem):
	global URL
	print(yellow+"Downloading testcase for problem "+problem+" ...")
	url=URL+"/problem/"+problem
	#page=requests.get(url)
	browser=webdriver.Safari()
	browser.get(url)
	time.sleep(3)
	page=browser.page_source
	browser.close()
	Content=BeautifulSoup(page,'lxml')
	Input=Content.find_all(class_="input")
	Output=Content.find_all(class_="output")
	n=len(Input)
	for i in range(n):
		inp=open(problem+str(i+1)+".in","w")
		out=open(problem+str(i+1)+".out",'w')
		inp.write(Input[i].find('pre').get_text()[1:])
		out.write(Output[i].find('pre').get_text()[1:])
		print(blue+"Fetched testcase "+str(i))
		inp.close()
		out.close()

def isContest(cnumber):
	return cnumber.isdigit()
def parse_practice():
	global URL
	print(URL)
	print(yellow+"Establishing Connection ...")
	page=requests.get(URL)
	print(blue+"Connection Established.")
	print(yellow+"Fetching testcases ...")
	Content=BeautifulSoup(page.content,'html.parser')
	Input=Content.find_all(class_="input")
	Output=Content.find_all(class_="output")
	n=len(Input)
	for i in range(n):
		inp=open(str(sys.argv[1])+str(i+1)+".in","w")
		out=open(str(sys.argv[1])+str(i+1)+".out",'w')
		inp.write(Input[i].find('pre').get_text()[1:])
		out.write(Output[i].find('pre').get_text()[1:])
		print(blue+"Fetched testcase "+str(i))
		inp.close()
		out.close()
def main():
	if len(sys.argv)==1:
		print(red+"Not Enough arguments")
		return
	global URL
	if(not isContest(str(sys.argv[1]))):
		c=""
		pos=0
		s=str(sys.argv[1])
		for i in str(sys.argv[1]):
			if(not(i>='A' and i<='Z')):
				c+=i
			else:
				print(pos)
				#print(c)
				URL+=c
				URL+="/problem/"+s[pos:]
			pos+=1
		parse_practice()
		return
	URL+=str(sys.argv[1])
	print(URL)
	print(yellow+"Establishing Connection ...")
	#page=requests.get(URL)
	browser=webdriver.Safari()
	browser.get(URL)
	time.sleep(3)
	page=browser.page_source
	print(page)
	#print(page)
	browser.close()
	#exit()
	print(blue+"Connection Established.")
	print(yellow+"Fetching Problems...")
	Content=BeautifulSoup(page,'lxml')
	problems=parse_contest(Content)
	for i in problems:
		parse_problem(str(i))

if __name__ == '__main__':
    main()
