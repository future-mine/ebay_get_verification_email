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
        try:
            username = driver.find_element_by_id('userid')
            loginbut = driver.find_element_by_id('signin-continue-btn')
            time.sleep(2)
            while True:
                try:
                    username.send_keys(name)
                    # time.sleep(4)
                    loginbut.click()

                    try:
                        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/span[2]/p')
                        print('---------------------------------------------------------------')
                        print(name, ' does not exist')
                        print('-------------------------------------------------------------')

                        
                        return None
                    except:
                        pass
                    break
                except:
                    pass
            break
        except:
            try:
                driver.find_element_by_xpath('//*[@id="gdpr-banner-accept"]')
            except:
                time.sleep(1)
    # Need_help = driver.find_element_by_id('need-help-signin-link')
    while True:
        print('here is second while')

        try:
            Need_help = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/form[1]/div[3]/div[1]/a')
            Need_help.click()
            # time.sleep(1)
            try:
                reset_butt = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/form[1]/div[3]/div[2]/div[2]/button')
                reset_butt.click()
            except:
                pass
            print('here is email')
            while True:
                try:
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    email = soup.find('p',{'id':'email-desc'}).b.text
                    break
                except:
                    time.sleep(1)
            while True:
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
                driver.find_element_by_xpath('//*[@id="gdpr-banner-accept"]').click()
            except:
                time.sleep(1)
            


def read_file():
    import pandas as pd
    df = pd.read_excel('ebay emaila.xlsx', sheet_name='Sheet1')

    print("Column headings:")
    # print(df.columns)
    # print(df['usernames'])
    # usernames = df['usernames']
    # print(df['email we game '])
    return df.values
def getelements(keyward):

    if(len(keyward) < 3 ):
        return
    # if(num > 1000):
    #     return False
    url = "https://www.google.com/"
    # keyward = 'inurl:read.php?='
    driver.delete_all_cookies()
    driver.get(url) 

    searchinput = driver.find_element_by_xpath("(//input[@class='gLFyf gsfi'])[position()=1]")
    searchinput.send_keys(keyward)
    searchinput.send_keys(u'\ue007')
    # url = 'https://www.google.com/search?q=inurl:index.php%3Fid%3D&lr=&as_qdr=all&sxsrf=ALeKk01WJyyY8QEZFOIIYr0JaIn5YTN4Pw:1587626556504&ei=PEKhXvOYHtTf-gTBk65Y&start=0&sa=N&ved=2ahUKEwjzpr7ngf7oAhXUr54KHcGJCws4ChDy0wN6BAgMECw&biw=872&bih=946'
    # print(soup)
    array_urls = []

    page_num = 0
    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        items = soup.find_all("div", {'class': 'g'})
        k = len(items)
        # driver.delete_all_cookies()
        delay = random.random()*4
        # time.sleep(3 + delay)
        while k < 1:
            time.sleep(3)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            items = soup.find_all("div", {'class': 'g'})
            k = len(items)

        for it in items:
            site_url = it.find("div", {'class': 'r'}).a['href']
            array_urls.append(site_url)
            print('site number:',num)
            print(site_url)
        # time.sleep(delay)
        write_file(array_urls)
        array_urls = []
        page_num += 1
        print('page_num:',page_num)
        if (page_num == 1):
            Nextbutton = driver.find_element_by_xpath("(//a[@class='G0iuSb'])[position()=1]")
        else:
            try:
                Nextbutton = driver.find_element_by_xpath("(//a[@class='G0iuSb'])[position()=2]")
            except:
                break


        # Nextbutton = driver.find_element_by_class_name('G0iuSb')
        # cardpin = driver.find_element_by_id('card-pin')
        # loginbut = driver.find_element_by_id('submit-library-card')
        # cardnumber.send_keys(CARDNUM)
        # cardpin.send_keys(PINNUM)
        # print(Nextbutton)
        Nextbutton.click()
        # driver.delete_all_cookies()

        # time.sleep(3)
    # print(array_urls)


    itemlll = []

if __name__ == "__main__":
    records = read_file()
    print(records)
    name = []
    email = [] 
    ebay_emails = []

    k = 0

    for record in records:
        print(record)
        print(record[0])
        ebay_email = get_email(record[0])
        if ebay_email is None:
            continue
        name.append(record[0])
        email.append(record[1])
        ebay_emails.append(ebay_email)

        if k > 2:
            k = 0
            t = time.localtime()
            current_time = time.strftime("%H_%M_%S", t)
            file_name = current_time + '.xlsx'    
            print(file_name)
            df = pd.DataFrame({'username':name, 'email':email, 'ebay email':ebay_emails})

            # Create a Pandas Excel writer using XlsxWriter as the engine.
            with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:

            # Convert the dataframe to an XlsxWriter Excel object.
                df.to_excel(writer, sheet_name='Sheet')
            writer.close()
            name = []
            email = [] 
            ebay_emails = []

        k += 1

    else:
        t = time.localtime()
        current_time = time.strftime("%H_%M_S", t)
        file_name = current_time + '.xlsx'    
        df = pd.DataFrame({'username':name, 'email':email, 'ebay email':ebay_emails})

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:

        # Convert the dataframe to an XlsxWriter Excel object.
            df.to_excel(writer, sheet_name='Sheet')
        writer.close()


    driver.close()
    # keywords = read_products()
    # print(keywords)
    # for key in keywords:
    #     getelements(key)
    # driver.close()

