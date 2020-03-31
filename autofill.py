from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

url = 'https://gartic.io'
path = "C:\\Users\\asus\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
driver = ""

def login():
	global driver

	print("Start login.")
	print("Opening browser...")
	driver = webdriver.Chrome(path)
	
	print()
	print("Opening URL...")
	print("Wait until the browser completely load the homepage.")
	driver.get(url)
	print("Done loading.")

	print("Now please login.")
	_ = input("Press Enter if you're done login >>> ").strip()
	print("Done login.")
	print()

def execute():
	print("Now go to form of theme creating (gartic.io/theme --> create theme)")
	_ = input("Press Enter if you're done preparing form >>> ").strip()
	global driver

	filename = input("Enter file name: ").strip()
	ls = []
	with open(filename, 'r') as f:
		ls = f.readlines()
	ls = [tuple(x.strip().split(',')) for x in ls]

	print()
	print("Please wait while the program filling the form...")
	for phrase, difficulty in ls:
		fill = driver.find_element(By.XPATH, "//*[@id='screens']/div/div[2]/div[1]/div[3]/form/div[1]/label[1]/input")
		fill.send_keys(phrase)

		if difficulty == '0':
			driver.find_element(By.XPATH, "//*[@id='screens']/div/div[2]/div[1]/div[3]/form/div[2]/label[1]/span").click()
		elif difficulty == '1':
			driver.find_element(By.XPATH, "//*[@id='screens']/div/div[2]/div[1]/div[3]/form/div[2]/label[2]/span").click()
		elif difficulty == '2':
			driver.find_element(By.XPATH, "//*[@id='screens']/div/div[2]/div[1]/div[3]/form/div[2]/label[3]/span").click()

		driver.find_element(By.XPATH, "//*[@id='screens']/div/div[2]/div[1]/div[3]/form/div[1]/label[2]/input").click()

	print("Done. Save your theme. Happy playing! :)")

def main():
	login()
	execute()

if __name__ == '__main__':
	main()