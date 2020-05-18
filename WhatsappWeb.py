from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/Users/alkan/Library/Application Support/Google/Chrome")
options.add_argument("profile-directory=Default")
w = webdriver.Chrome(executable_path="/Users/alkan/PycharmProjects/untitled5/driver/chromedriver", options=options)

w.get("https://web.whatsapp.com/")

name = "Bitanemm❤️"
name = "Efe"
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

# Scan the code before proceeding further
input('Enter anything after scanning QR code')
while 1:
    try:
        user = w.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

        msg_box = w.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

        for i in range(count):
            msg_box.send_keys(msg + Keys.RETURN)
        break
    except:
        pass
