# FindBookStore
 
It is an introduction to the links to the screens to check the inventory of bookstore </br>
(online Bookstores and real Bookstores).

本の在庫（オンライン書店・リアル書店）を確認するために，「サイト先リンク」を紹介するシステム

# DEMO

- 以下のサイトにアクセス</br>
[在庫店舗検索システム](https://findbookstore.herokuapp.com/)
 
# Requirement

- Python 3.8.9
- 必要なPythonパッケージ：requirements.txt
  
 
# Installation
 
Requirementで列挙したライブラリなどのインストール方法を説明

docker build -t findbookstore:latest .

コンテナを切ったらすぐにコンテナも削除
docker run --rm -it -v ./FindBookStore:/FindBookStore {IMAGE ID} bash
 
```bash

```
 
# Usage

 
* インストールが完了後に，以下のコマンドを実行

```bash
python manage.py runserver
```
* <http://127.0.0.1:8000/> にアクセス
 
# Author

* sg5314
