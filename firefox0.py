from selenium import webdriver
import selenium
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
from bs4 import BeautifulSoup
import time
import os
import random
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC

def write_file(array):
    filename = "urls_1.txt"
    try: 
        # f = open(filename, "r")
        # items = f.read()
        # itemlll = items.split('\n')
        # print(items.split('\n'))
        # f.close()
    # except:

    # try: 
        f = open(filename, "a")
        for itemurl in array:
            f.write(itemurl+ "\n")
        f.close()
    except:
        print("There was an error writing to the CSV data file.")

def read_products():
    filename = "keyword.txt"
    itemlll = []

    try: 
        print(filename)
        f = open(filename, "r" , encoding="utf8")
        items = f.read()
        itemlll = items.split('\n')
        f.close()
        return itemlll
    except:
        print("There was an error writing to the CSV data file.")
# name = 'printconsumablesupplies'

############################################################################################
binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

caps = DesiredCapabilities.FIREFOX.copy()
caps['marionette'] = True
driver = webdriver.Firefox(firefox_binary=binary,capabilities=caps, executable_path= os.getcwd()+"\geckodriver.exe")
# searchinput = driver.find_element_by_id('newtab-search-text')
num = 0
wait = ui.WebDriverWait(driver, 10)

# driver.delete_all_cookies()
url = "https://signin.ebay.co.uk/signin/"
driver.get(url)
##############################################################################################

def get_email(name):
    while True: 
        print('here is first while')
        try:
            print('here is username')
            username = driver.find_element_by_id('userid')
            loginbut = driver.find_element_by_id('signin-continue-btn')
            time.sleep(4)
            # while True:
            print('here is user click')
            username.send_keys(name)
            # time.sleep(4)
            loginbut.click()
            # soup = BeautifulSoup(driver.page_source, 'html.parser')
            # kk = soup.find('span',{'id':'user-info'}).text
            # print(type(kk), kk)
            #     # if kk and kk == name:
            #     #     break
            break
        except:
        # try:
        #     driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div/button')
        # except:
            time.sleep(3)
    # Need_help = driver.find_element_by_id('need-help-signin-link')
    while True:
        print('here is second while')

        try:
            print('here is nee_help')
            Need_help = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/form[1]/div[3]/div[1]/a')
            Need_help.click()
            # time.sleep(1)
            try:
                print('here is reset_butt')
                reset_butt = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/form[1]/div[3]/div[2]/div[2]/button')
                reset_butt.click()
            except:
                pass
            print('here is email')

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            email = soup.find('p',{'id':'email-desc'}).b.text
            while True:
                print('here is back refresh')
                try:
                    driver.execute_script("window.history.go(-1)")
                    break
                except:
                    time.sleep(1)
                    pass
            return email
            # print(email)
            # break
        except:
            try:
                driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div/button"]').click()
            except:
                time.sleep(3)
            


def read_file():
    import pandas as pd
    df = pd.read_excel('ebay emaila.xlsx', sheet_name='Sheet1')

    print("Column headings:")
    # print(df.columns)
    # print(df['usernames'])
    # usernames = df['usernames']
    # print(df['email we game '])
    return df.values
if __name__ == "__main__":
    records = read_file()
    print(records)
    name = []
    email = [] 
    ebay_emails = []
    for record in records:
        print(record)
        print(record[0])
        ebay_email = get_email(record[0])
        name.append(record[0])
        email.append(record[1])
        ebay_emails.append(ebay_email)    
    
    df = pd.DataFrame({'username':name, 'email':email, 'ebay email':ebay_emails})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as writer:

    # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, sheet_name='Sheet')
    # driver.close()
    # keywords = read_products()
    # print(keywords)
    # for key in keywords:
    #     getelements(key)
    # driver.close()

