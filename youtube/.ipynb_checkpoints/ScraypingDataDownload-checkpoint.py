
# coding: utf-8

# In[8]:


# !pip install selenium


# In[7]:


# !pip install beautifulsoup4


# In[5]:


from selenium import webdriver
# 処理時間の計測など
import time
# csv操作、グラフ化、データ集計や加工
import pandas as pd


# In[6]:


USER = "test_user"
PASS = "test_pw"


# In[8]:


#Chormeの起動、自動操作
browser = webdriver.Chrome(executable_path = 'C:\\prog\\Python\\Mypandas\\chromedriver.exe')
# 指定したドライバが見つかるまでの待ち時間
browser.implicitly_wait(3)


# In[9]:


# ログインするページへのアクセス
url_login = "https://kino-code.com/membership-login/"
# getで指定のURLへ遷移する
browser.get(url_login)
# URLに遷移した際にすぐに次の処理に行かないようにするため
time.sleep(3)
print("ログインページにアクセスしました")


# In[10]:


# ログインページのテキストボックスに値を入力、HTMLのidやclassはChromeの検証機能で調べる
element = browser.find_element_by_id('swpm_user_name')
# もしテキストボックスに予め値が入力されている場合のClear
element.clear()
element.send_keys(USER)
element = browser.find_element_by_id('swpm_password')
element.clear()
element.send_keys(PASS)
print("フォームを送信")


# In[11]:


# ログインボタンのクリック、HTMLの要素をChromeから調べる、name = swpm-loginであることがわかった
browser_from = browser.find_element_by_name('swpm-login')
time.sleep(3)
browser_from.click()
print("情報を入力してログインボタンを押しました")


# In[12]:


# 会員専用ページのウェブサイトへアクセス
url = "https://kino-code.com/member-only/"
time.sleep(3)
browser.get(url)
print(url, ":アクセス完了")


# In[14]:


# ダウンロードボタンをクリック
frm = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/main/article/div/p[2]/button')
time.sleep(1)
frm.click()
print("ダウンロードボタンをクリック")

