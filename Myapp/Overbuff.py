
# coding: utf-8

# In[62]:


from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request as req
# 処理時間の計測など
import time
# csv操作、グラフ化、データ集計や加工
import pandas as pd


# In[63]:


# プレイヤー名 テストとしてランキング自分のID
PLAYER = "ISUQQ#1380"


# In[64]:


#Chormeの起動、自動操作
browser = webdriver.Chrome(executable_path = 'C:\\prog\\Python\\WebScraping\\chromedriver.exe')
# 指定したドライバが見つかるまでの待ち時間
browser.implicitly_wait(3)


# In[65]:


# ログインするページへのアクセス
url_login = "https://www.overbuff.com/"
# getで指定のURLへ遷移する
browser.get(url_login)
# URLに遷移した際にすぐに次の処理に行かないようにするため
time.sleep(3)
print("ログインページにアクセスしました")


# In[69]:


# 現在は大画面でのUIにしか対応していない

search_name = browser.find_element_by_name('q')
search_name.clear()
search_name.send_keys(PLAYER)
print("プレイヤー名を入力")


# In[70]:


# 検索ボタンのクリック
search_button = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[1]/form/button')
time.sleep(1)
search_button.click()
print("検索ボタンのクリック")


# In[71]:


# プレイヤーの選択とクリック
#  ※現在の書き方では複数選択肢がある場合は一番最初のものが選択される
player_select = browser.find_element_by_class_name('SearchResult')
player_select.click()


# In[32]:


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


# In[81]:


cur_url = browser.current_url 
# error 429がでる 明日原因を解明しよう
test_url = "https://www.overbuff.com/"
# おそらく以下の書き方だと動的に数値が変わるページには向いていないのかエラーが出る
response = req.urlopen(test_url)
parse_html = BeautifulSoup(response, 'html.parser')

# ブラウザのソースをそのまま取得する方法で解決した
# raw_html = browser.page_source
# print(raw_html)


# In[79]:


parse_html

