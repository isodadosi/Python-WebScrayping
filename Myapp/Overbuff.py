
# coding: utf-8

# In[61]:


from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request as req
import datetime
# 処理時間の計測など
import time
# csv操作、グラフ化、データ集計や加工
import pandas as pd


# In[62]:


# プレイヤー名 テストとして自分のID
PLAYER_PC = "ISUQQ#1380"
PLAYER_PS4 = "isopon_24"


# In[63]:


#Chormeの起動、自動操作
browser = webdriver.Chrome(executable_path = 'C:\\prog\\Python\\WebScraping\\chromedriver.exe')
# 指定したドライバが見つかるまでの待ち時間
browser.maximize_window()
browser.implicitly_wait(3)


# In[64]:


# ログインするページへのアクセス
url_login = "https://www.overbuff.com/"
# getで指定のURLへ遷移する
browser.get(url_login)
# URLに遷移した際にすぐに次の処理に行かないようにするため
time.sleep(3)
print("ログインページにアクセスしました")


# In[65]:


# 現在は大画面でのUIにしか対応していない

search_name = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div[1]/section[1]/article/form/input')
search_name.clear()
search_name.send_keys(PLAYER_PS4)
print("プレイヤー名を入力")


# In[66]:


# 検索ボタンのクリック
# 画面上の検索ボタン
# search_button = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[1]/form/button')

# 画面中央の検索ボタン
search_button = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div[1]/section[1]/article/form/button')

time.sleep(1)
search_button.click()
print("検索ボタンのクリック")


# In[67]:


# プレイヤーの選択とクリック
#  ※現在の書き方では複数選択肢がある場合は一番最初のものが選択される

player_select = browser.find_element_by_class_name('SearchResult')

player_select.click()


# In[68]:


# いろいろ試してみたがセッションで値が変わる様なページでは直接値を取得するのは向いていないっぽい
# HTMLを取得してから値を取得する方法を次に試してみる

# now_tank_rate = raw_html.findElement(By.xpath('/html/body/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/section/article/table')).fidElements(By.tagName("tr").size()
# now_tank_rate = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/section/article/table/tbody/tr/td[3]')

# element = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/section/article/table/tbody/tr/td[2]')
# print(element)
# valString = element.get_attribute("value")
# print(valString)

# tableElem = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/section/article/table")
# trs = tableElem.find_elements(By.TAG_NAME, "tr")

# print(tableElem)


# In[69]:


# 1. urllibを使用してソースを取得する方法は失敗、overbuffのサイトで429エラーがでる
# test1->pass test2->error cur->error
# cur_url = browser.current_url 
# # error 429がでる 明日原因を解明しよう
# test1_url = "https://ja.wikipedia.org/wiki/%E3%82%A6%E3%82%A3%E3%82%AD"
# test2_url = "https://www.overbuff.com/"
# response = req.urlopen(test_url)


# 2. ブラウザのソースをそのまま取得する方法で解決した(seleniumで取得->Beautifulsoupへ変換)
raw_html = browser.page_source
parse_html = BeautifulSoup(raw_html, 'html5lib')
# print(parse_html.prettify())


# In[70]:


# 各ロールのrateを出力

table = parse_html.findAll("table", {"class":"table-data"})[0]
rows = table.findAll("tr")

rate_list = []
rate_damage_list = []
rate_support_list = []
rate_tank_list = []

def record_list():

    for row in rows[1:] :
    #     print(row)
        for sell in row.findAll('td'):
            rate_list.append(sell.get_text())


    rate_damage_list.append(rate_list[2])
    rate_support_list.append(rate_list[5])
    rate_tank_list.append(rate_list[8])
    rate_list.clear()

def remove_list():
    rate_damage_list.clear()
    rate_suppport_list.clear()
    rate_tank_list.clear()


# In[71]:


# record_list()


# In[72]:


# 更新ボタン押したあとにデータを追加
update_button = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/i')
time.sleep(1)
update_button.click()
print("更新ボタンをクリック")

time.sleep(10)

record_list()
print("データを追加")


# In[73]:


# Pandasを用いて見やすい表へ
time = datetime.datetime.now()
df_rate_list = pd.DataFrame({'time': '{0:%Y/%m/%d %H:%M}'.format(time), 'Damege':rate_damage_list,'Suport':rate_support_list, 'Tank':rate_tank_list})
print("pandasのdataframeへ")


# In[74]:


df_rate_list


# In[2]:


# CSVファイルへ
df_rate_list.to_csv('overbuff.csv', mode='a', header=False)
print('csvファイルへ出力')

