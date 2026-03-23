# Webスクレイピング・データ収集ツール

Webサイトから自動でデータを収集し、CSV形式で保存するツールです。

## 機能
- Webサイトからの自動データ収集
- 収集データのCSV自動保存
- 収集結果のログ出力

## 使用技術
- Python 3.x
- requests
- BeautifulSoup4
- pandas

## 使い方
1. リポジトリをクローン
2. 必要なライブラリをインストール
```bash
pip install requests beautifulsoup4 pandas
```
3. スクリプトを実行
```bash
python main.py
```

## 出力例
- `output/data.csv` - 収集したデータ
- `output/log.txt` - 収集ログ

## 注意
各Webサイトの利用規約を確認の上、適切にご使用ください。
