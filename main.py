import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime

def fetch_page(url):
    """Webページを取得する"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print(f"✅ ページ取得成功: {url}")
        return response.text
    except Exception as e:
        print(f"❌ 取得エラー: {e}")
        return None

def parse_data(html):
    """HTMLからデータを抽出する"""
    soup = BeautifulSoup(html, 'html.parser')
    results = []

    # サンプル: タイトルとリンクを取得
    for item in soup.find_all('a', href=True):
        title = item.get_text(strip=True)
        link = item['href']
        if title and len(title) > 5:
            results.append({
                'タイトル': title,
                'リンク': link,
                '収集日時': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
    print(f"✅ データ抽出完了: {len(results)}件")
    return results

def save_csv(data, filepath):
    """CSVファイルに保存する"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False, encoding='utf-8-sig')
    print(f"✅ CSVに保存しました: {filepath}")

def save_log(message, filepath):
    """ログを保存する"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def main():
    # サンプルURL（Pythonの公式ドキュメント）
    url = "https://docs.python.org/ja/3/"
    
    print("🔍 Webスクレイピング開始...")
    save_log(f"スクレイピング開始: {url}", 'output/log.txt')

    html = fetch_page(url)
    if html:
        data = parse_data(html)
        if data:
            save_csv(data, 'output/data.csv')
            save_log(f"完了: {len(data)}件取得", 'output/log.txt')
            print(f"\n🎉 完了！{len(data)}件のデータを収集しました。")
        else:
            print("❌ データが取得できませんでした。")
    else:
        print("❌ ページの取得に失敗しました。")

if __name__ == "__main__":
    main()
