
# coding: utf-8

# In[1]:


from selenium import webdriver
# 処理時間の計測など
import time
# csv操作、グラフ化、データ集計や加工
import pandas as pd


# In[2]:


# プレイヤー名 テストとしてランキング1位の人
PLAYER = "PUNK#11600"


# In[3]:


#Chormeの起動、自動操作
browser = webdriver.Chrome(executable_path = 'C:\\prog\\Python\\WebScraping\\chromedriver.exe')
# 指定したドライバが見つかるまでの待ち時間
browser.implicitly_wait(3)


# In[4]:


# ログインするページへのアクセス
url_login = "https://www.overbuff.com/"
# getで指定のURLへ遷移する
browser.get(url_login)
# URLに遷移した際にすぐに次の処理に行かないようにするため
time.sleep(3)
print("ログインページにアクセスしました")


# In[5]:


search_name = browser.find_element_by_name('q')
search_name.clear()
search_name.send_keys(PLAYER)
print("プレイヤー名を入力")


# In[6]:


# 検索ボタンのクリック
search_button = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[1]/form/button')
time.sleep(1)
search_button.click()
print("検索ボタンのクリック")


# In[11]:


# プレイヤーの選択とクリック
#  ※現在の書き方では複数選択肢がある場合は一番最初のものが選択される
player_select = browser.find_element_by_class_name('SearchResult')
player_select.click()

