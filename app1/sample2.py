
# 【PythonでAI】ディープラーニングで画像認識するプログラム

from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os, time, sys

# 取得したAPI Key
key = "xxxxxxxx"
# 取得したSecrect Key
secret = "xxxxxxxxx"

# 検索キーワード
keyword = "ポケモン"
# 画像を保存するフォルダ
savedir = "./image/pokemon"

# 画像を保存するフォルダを作成
os.makedirs(savedir)

# Flickr APIを使って検索を実行
flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    # 検索キーワード
    text = keyword,
    # 取得する画像数
    per_page = 300,
    # 写真を対象
    media = 'photos',
    # 最新の画像から取得
    sort = 'relevance',
    # 暴力的な画像を排除
    safe_search = 1,
    # オプション（データURL、ライセンスタイプ）
    extras = 'url_q, license'
)


photos = result['photos']

# データURLを元に1枚ずつ画像を取得しフォルダ内に保存
for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(1)