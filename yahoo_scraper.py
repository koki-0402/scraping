import requests
import re

# Yahoo! JAPANニューストップページ
url = 'https://news.yahoo.co.jp'
res = requests.get(url)
html = res.text

# ニュースの見出し部分を正規表現で抽出
titles = re.findall(r'<p class="sc-1t7ra5j-7 casbUp">(.*?)</p>', html)

# 抽出結果を出力
print("Yahoo!ニュース 見出し一覧")
print("=" * 30)
for i, title in enumerate(titles, start=1):
    print(f"{i}. {title}")

