
# coding: utf-8

# In[10]:


# !pip install bs4


# In[42]:


from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd


# In[17]:


html="""
<html>
    <head>
        <meta charset="utf-8">
        <title>テストタイトル
        </title>
    </head>
    <body>
        <h1>こんにちは</h1>
    </body>
</html>
"""


# In[18]:


html


# In[19]:


# htmlを解析する
parse_html = BeautifulSoup(html, 'html.parser')


# In[20]:


print(parse_html)


# In[21]:


# 更に見やすくする
print(parse_html)


# In[22]:


url = "https://kino-code.com/python-scraping/"
# urlopen 指定したWebサイトのHTMLを取得する
response = req.urlopen(url)


# In[23]:


parse_html = BeautifulSoup(response, 'html.parser')


# In[24]:


parse_html


# In[27]:


# タイトルタグの表示
print(parse_html.title)
# タイトルタグ内のテキストのみ表示
print(parse_html.title.string)


# In[28]:


# urlを取得するためにaタグを取得する
print(parse_html.find_all('a'))


# In[29]:


title_lists = parse_html.find_all('a')
title_lists[1:10]


# In[36]:


title_lists[10].string


# In[35]:


# hrefのみ取得
title_lists[10].attrs['href']


# In[38]:


title_list=[]
url_list=[]

for i in title_lists:
    title_list.append(i.string)
    url_list.append(i.attrs['href'])


# In[39]:


title_list


# In[40]:


url_list


# In[44]:


# pandasを用いて見やすく表示
df_title_url = pd.DataFrame({'Title':title_list, 'URL':url_list})


# In[45]:


df_title_url


# In[48]:


# 欠損値 none を除く
# how='any'で行に一つでも欠損値があれば除く allですべて
df_notnull = df_title_url.dropna(how='any')


# In[47]:


df_notnull


# In[51]:


# 特定の文字列が入っているものを表示
df_notnull['Title'].str.contains('Python超入門コース')


# In[52]:


df_notnull[df_notnull['Title'].str.contains('Python超入門コース')]


# In[53]:


df_contain_python = df_notnull[df_notnull['Title'].str.contains('Python超入門コース')]


# In[55]:


# CSVファイルにする
df_contain_python.to_csv('output.csv')

