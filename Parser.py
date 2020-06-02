import requests
from bs4 import BeautifulSoup
import re
import sys
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
	print("Downloading testcase for problem "+problem)
	url=URL+"/problem/"+problem
	page=requests.get(url)
	Content=BeautifulSoup(page.content,'html.parser')
	Input=Content.find_all(class_="input")
	Output=Content.find_all(class_="output")
	n=len(Input)
	for i in range(n):
		print(Input[i].find('pre').get_text())
		print(Output[i].find('pre').get_text())

def main():
	if len(sys.argv)==1:
		print("Not Enough arguments")
		return
	global URL
	URL+=str(sys.argv[1])
	print(URL)
	print("Establishing Connection ...")
	page=requests.get(URL)
	print("Connection Established.")
	print("Fetching Problems...")
	Content=BeautifulSoup(page.content,'html.parser')
	problems=parse_contest(Content)
	for i in problems:
		parse_problem(str(i))
if __name__ == '__main__':
    main()