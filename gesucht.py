# https://www.wg-gesucht.de/
def get_persons(s,select):
  if 'title' in s:
    data=s.split('span')[1].replace(">",'').replace('"','').replace('title=','').split('\n')[0]
    print(data)
    person=data.split()[-1]
    count=[]
    print(person)
    person=(person.replace('(','').replace(')','').replace('w','').replace('m','').replace('d','').split(','))
    if select=='Gender':
      if person[0]!='0' and person[1]!='0':

        return 'any'
      elif person[0]!='0':
        return 'Women'
      elif person[1]!='0':
        return 'men'
      else:
        return 'NA'
    if select=='person':
      return data.split()[0].replace('er','')
    return data
import pickle
import html2text
import time
from auth import *
import pandas as pd
from datetime import date
import json

urls=['https://www.wg-gesucht.de/wg-zimmer-und-1-zimmer-wohnungen-und-wohnungen-und-haeuser-in-Dusseldorf.30.0+1+2+3.0.0.html','https://www.wg-gesucht.de/wg-zimmer-und-1-zimmer-wohnungen-und-wohnungen-und-haeuser-in-Frankfurt-am-Main.41.0+1+2+3.0.0.html','https://www.wg-gesucht.de/wg-zimmer-und-1-zimmer-wohnungen-und-wohnungen-und-haeuser-in-Frankfurt-Oder.40.0+1+2+3.0.0.html','https://www.wg-gesucht.de/wg-zimmer-und-1-zimmer-wohnungen-und-wohnungen-und-haeuser-in-Hamburg.55.0+1+2+3.0.0.html','https://www.wg-gesucht.de/wg-zimmer-und-1-zimmer-wohnungen-und-wohnungen-und-haeuser-in-Munchen.90.0+1+2+3.0.0.html','https://www.wg-gesucht.de/wg-zimmer-und-1-zimmer-wohnungen-und-wohnungen-und-haeuser-in-Berlin.8.0+1+2+3.0.0.html','https://www.wg-gesucht.de/wg-zimmer-und-1-zimmer-wohnungen-und-wohnungen-und-haeuser-in-Berlingen.5038.0+1+2+3.0.0.html','https://www.wg-gesucht.de/wg-zimmer-und-1-zimmer-wohnungen-und-wohnungen-und-haeuser-in-Berlingerode.10902.0+1+2+3.0.0.html']


driver= get_driver()
# df = pd.DataFrame({'Link':[''],'Posting Date':[''],'vacant_form':[''],'vacant_till':['']})
# today = date.today()
# day = str(today).split('-')[-1]
# day='18'
# urls=['https://www.wg-gesucht.de/wg-zimmer-und-1-zimmer-wohnungen-und-wohnungen-und-haeuser-in-Munchen.90.0+1+2+3.0.0.html']

# action = ActionChains(driver)

# for url in urls:
#     driver.get(url)
#     with open('cookies.json','rb') as f:

#         cookies = json.load(f)

#         for cookie  in cookies:

#             driver.add_cookie(cookie)

#     driver.refresh()
#     element= driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/form/div/div[3]/button[2]')
#     action.move_to_element_with_offset(to_element=element, xoffset=100,yoffset= 200)
#     try:
#         last_page= driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div/ul/li[8]/a').text
#     except:
#         last_page=1
#     print(last_page)
#     flag=0
#     share_person=driver.find_elements(By.XPATH,'/html/body/div/div/div/div/table/tbody/tr/td[2]')
    

    # pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    
#     for i in range(int(last_page)):
#         element= driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/form/div/div[3]/button[2]')
#         action.move_to_element_with_offset(to_element=element, xoffset=100,yoffset= 200)
#         if flag==1:
#             break
#         link_url =url.split('0.html')[0]+str(i)+'.html'
#         driver.get(link_url)
#         time.sleep(2)
#         data=[]
#         posting_date = driver.find_elements(By.XPATH,'/html/body/div/div/div/div/table/tbody/tr/td[3]/a/span')
#         page_link= driver.find_elements(By.XPATH,'/html/body/div[3]/div[2]/div[5]/div[1]/table/tbody/tr/td[3]/a')
#         if len(page_link)==0:
#             page_link = driver.find_elements(By.XPATH,' /html/body/div[1]/div[2]/div/div/table/tbody/tr/td[6]/a')                                 
#         print(len(page_link))
#         vacant_form = driver.find_elements(By.XPATH,'/html/body/div/div/div/div/table/tbody/tr/td[7]/a/span')
#         vacant_till = driver.find_elements(By.XPATH,'/html/body/div/div/div/div/table/tbody/tr/td[8]/a')
#         for i in range(len(posting_date)):
#             scrape_date =posting_date[i].text
#             # if scrape_date.split('.')[0]!=day:
#             if scrape_date.split('.')[0] not in ['19','18','17','16']:
#                 flag=1
#                 break
#             print(scrape_date)
#             value= page_link[i].get_attribute('href')
#             vacant_till_data=html2text.html2text(vacant_till[i].get_attribute('innerHTML'))
#             vacant_form_data =vacant_form[i].text
#             if value not in data:
#                 print(value)
#                 df=df.append({'Link':value,'Posting Date':scrape_date,'vacant_form':vacant_form_data,'vacant_till':vacant_till_data},ignore_index=True)
# df.to_csv('links1.csv')

    

# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))



# cookies = pickle.load(open("cookies.pkl", "rb"))

# for cookie in cookies:

#     driver.add_cookie(cookie)
# input=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[4]/div/div/div/div/form/div[1]/div/div/input[1]')

# input.send_keys('Berlin')
# input.click()
# driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[4]/div/div/div/div/form/div[2]/div[2]/button').click()
# select=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div[4]/div/div/div/div/form/div[2]/div[2]/div/div/ul/li/a')
# for j in range(len(select)):
#     if j==1:
#         continue
#     select[j].click()
# button = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[4]/div/div/div/div/form/div[4]/div/input').click()

# time.sleep(11)
# try:
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[5]/div[1]/div[1]/div[2]/div/label[1]').click()
# except:
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[5]/div[1]/div[1]/div[2]/div/label[1]"))).click()
# time.sleep(1)
###############################################################
df_main = pd.DataFrame({'Posting date':[''],'Caption':[''],'Address':[''],'Vacant Form':[''],'Vacant Till':[''],'Duration':[''],'Cold Rent':[''],'Warm Rent':[''],'Deposit':[''],'Area Flat':[''],'Area of room':[''],'No. of room':[''],'No. of people':[''],'Gender':[''],'Rooms':[''],'Bedrooms':[''],'Kitchen':[''],'Bathrooms':[''],'Floor':[''],'Description':[''],'Type':[''],'Furnished':[''],'Poster Name':[''],'Agent Name':[''],'Company':[''],'Number':[''],'Pic URL':['']})
        
df = pd.read_csv('links1.csv')
asset_url = df['Link'][2:] 
posting_date = df['Posting Date'][2:]
vacant_form = df['vacant_form'][2:]
vacant_till = df['vacant_till'][2:]

# f_index=int(input('starting index'))
# l_index = int(input('last index'))
f_index=2
l_index=10
for link in range(f_index,l_index+1):
    print(asset_url[link])
    if asset_url[link]:
        driver.get(asset_url[link])
        with open('cookies.json','rb') as f:
            cookies = json.load(f)
            for cookie  in cookies:
                driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(2)
        try:
            image_urls = driver.find_elements(By.CSS_SELECTOR,'img.sp-thumbnail')
            all_img_urls=[]
            for img in range(0,len(image_urls)):
                img_url = image_urls[img].get_attribute('src')
                all_img_urls.append(img_url)
                print(img_url)
                print()
        except:
            pass
        
        # client_name = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div/div[2]/b').text
        # print(client_name)
        # try:
        #     image_url = driver.find_element(By.XPATH,'//*[@id="bildContainer"]/div[1]/div/img').get_attribute('src')
        #     print(image_url)
        # except:
        #     pass
        try:
            area_of_room = driver.find_element(By.XPATH,'//*[@id="rent_wrapper"]/div[2]/label[1]/font/font').text
        except:
            area_of_room=""
        print(area_of_room)
        try:
            area_of_flat= driver.find_element(By.XPATH,'//*[@id="rent_wrapper"]/div[1]/label[1]').text
        except:
            area_of_flat=''
        print(area_of_flat)
        try:
            description = driver.find_element(By.XPATH,'//*[@id="freitext_0"]')
            description=html2text.html2text(description.get_attribute('innerHTML'))
        except:
            description=""
        try:
            s=driver.find_element(By.XPATH,'//*[@id="WG-Pictures"]/h1/span').get_attribute('innerHTML')
            print(get_persons(s,'person'))
        except:
            pass
        print(description)
        try:
            deposite= driver.find_element(By.XPATH ,'//*[@id="kaution"]').get_attribute('value')
        except:
            deposite=""
        print(deposite)
        try:
            warm_rent= driver.find_element(By.XPATH,'//*[@id="main_column"]/div/div/div/div/table/tbody/tr[1]/td[2]/b').text
        except:
            rent=''
        print(rent)
        try: 
            cold_rent= driver.find_element(By.XPATH,'//*[@id="main_column"]/div[1]/div/div/div/table/tbody/tr[1]/td[2]/b').text
        except:
            cold_rent=''
        try:
            Address = driver.find_element(By.XPATH,'//*[@id="main_column"]/div/div/div[6]/div[2]')
            address=html2text.html2text(Address.get_attribute('innerHTML'))
        except:
            address=''
        try:
            furniture = driver.find_element(By.CLASS_NAME ,'mdi mdi-bed-double-outline mdi-36px noprint')
            furniture ='Y'
        except:
            furniture ='N'
        print(furniture)
        try:
            bathroom = driver.find_element(By.CLASS_NAME,'mdi mdi-shower mdi-36px noprint')
            bathroom= 'Y'
        except:
            bathroom='N'
        try:
            kitchen = driver.find_element(By.CLASS_NAME,'mdi mdi-silverware-fork-knife mdi-36px noprint')
            kitchen ='Y'
        except:
            kitchen='N'
        print(kitchen,bathroom)
        # try:
        #     floor = driver.find_element(By.CLASS_NAME,'mdi mdi-office-building mdi-36px noprint')
        #     floor='Y'
        # except:
        #     floor=''
        df_main=df_main.append({'Posting date':posting_date[link],'Caption':'','Address':address,'Vacant Form':vacant_form[link],'Vacant Till':vacant_till[link],'Duration':'','Cold Rent':"",'Warm Rent':rent,'Deposit':deposite,'Area Flat':area_of_flat,'Area of room':area_of_room,'No. of room':'','No. of people':'','Gender':'','Rooms':'','Bedrooms':'','Kitchen':kitchen,'Bathrooms':bathroom,'Floor':'','Description':description,'Type':'','Furnished':'','Poster Name':'','Agent Name':'','Company':'','Number':'','Pic URL':",".join(all_img_urls)},ignore_index=True)
        
df_main.to_csv('data.csv')

















'''

1 
'''
df = pd.read_csv('links1.csv')

for i in df['Link'][4:]:
    
    if len(str(i))>4:
        print(i)
        driver.get(i)
# client_name = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div/div[2]/b').text
# print(client_name)
# try:
#     image_url = driver.find_element(By.XPATH,'//*[@id="bildContainer"]/div[1]/div/img').get_attribute('src')
#     print(image_url)
# except:
#     pass
# try:
#     area_of_room = driver.find_element(By.XPATH,'//*[@id="rent_wrapper"]/div[2]/label[1]/font/font').text
# except:
#     area_of_room=""
# print(area_of_room)
# area_of_flat= driver.find_element(By.XPATH,'//*[@id="rent_wrapper"]/div[1]/label[1]').text
# print(area_of_flat)
# description = driver.find_element(By.XPATH,'//*[@id="freitext_0"]')

# description=html2text.html2text(description.get_attribute('innerHTML'))
# print(description)
# deposite= driver.find_element(By.XPATH ,'//*[@id="kaution"]').get_attribute('value')
# print(deposite)
# rent= driver.find_element(By.XPATH,'//*[@id="main_column"]/div/div/div/div/table/tbody/tr[1]/td[2]/b').text
# print(rent)


# Address = driver.find_element(By.XPATH,'//*[@id="main_column"]/div/div/div[6]/div[2]')
# address=html2text.html2text(Address.get_attribute('innerHTML'))
# print(address)
# # 
# # Caption= driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/h1')
# # print(Caption)

# duration = driver.find_element(By.XPATH,'//*[@id="main_column"]/div/div/div[6]/div[3]/h3').text
        
        # print(kitchen,bathroom,floor)