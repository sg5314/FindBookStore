# FindBookStore
 
It is an introduction to the links to the screens to check the inventory of books (online Bookstores and real Bookstores).

本の在庫（オンライン書店・リアル書店）を確認画面へのリンクを紹介するシステム

# DEMO
  
 
# Requirement
 
- Required Python packages are listed in requirements.txt
- 必要なPythonパッケージはrequirements.txtに記載

*Python 3.8.9*
* Django==3.2
* requests==2.24.0
 
# Installation
 
Requirementで列挙したライブラリなどのインストール方法を説明

docker build -t findbookstore:latest .

コンテナを切ったらすぐにコンテナも削除
docker run --rm -it -v ./FindBookStore:/FindBookStore {IMAGE ID} bash
 
```bash
pip install huga_package
```
 
# Usage
 
DEMOの実行方法など、"hoge"の基本的な使い方を説明
 
```bash
git clone https://github.com/hoge/~
cd examples
python demo.py
```
 
# Note
 
このシステムは，Djangoで構築しています．
 
# Author
 
作成情報を列挙する
 
* sg5314
* [Intelligent Systems Design Laboratory](https://sites.google.com/view/doshisha-isdl)