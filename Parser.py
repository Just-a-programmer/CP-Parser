import requests
from bs4 import BeautifulSoup
import re
import sys
yellow="\033[1;33;40m"
red="\033[1;31;40m"
blue="\033[1;36;40m"
purple="\033[1;35;40m"
URL="https://codeforces.com/contest/"
def parse_contest(Content):
	possible=Content.find_all('option')
	problems={}
	pattern=re.compile("[A-Z][0-9]?")
	for i in possible:
		x=str(i['value'])
		if pattern.match(x):
			problems[x]=1
	return problems

def parse_problem(problem):
	global URL
	print(yellow+"Downloading testcase for problem "+problem+" ...")
	url=URL+"/problem/"+problem
	page=requests.get(url)
	Content=BeautifulSoup(page.content,'html.parser')
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

def main():
	if len(sys.argv)==1:
		print(red+"Not Enough arguments")
		return
	global URL
	URL+=str(sys.argv[1])
	print(URL)
	print(yellow+"Establishing Connection ...")
	page=requests.get(URL)
	print(blue+"Connection Established.")
	print(yellow+"Fetching Problems...")
	Content=BeautifulSoup(page.content,'html.parser')
	problems=parse_contest(Content)
	for i in problems:
		parse_problem(str(i))

if __name__ == '__main__':
    main()