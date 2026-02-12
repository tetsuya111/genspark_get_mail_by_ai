#!/usr/bin/env python3
"""
Webページスクリーンショット取得スクリプト

目的:
- ローカルで起動中のWebサーバーのスクリーンショットを取得
- Selenium + Firefoxを使用してページをキャプチャ
- フルページスクリーンショットに対応
"""

import sys
import time
import argparse
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ScreenshotCapture:
    """スクリーンショット取得クラス"""
    
    def __init__(self, url, output_path, width=1920, height=1080, wait_time=5, full_page=True):
        """
        初期化
        
        Args:
            url: キャプチャするURL
            output_path: 出力ファイルパス
            width: ブラウザ幅
            height: ブラウザ高さ
            wait_time: ページ読み込み待機時間（秒）
            full_page: フルページスクリーンショットを取得するか
        """
        self.url = url
        self.output_path = Path(output_path)
        self.width = width
        self.height = height
        self.wait_time = wait_time
        self.full_page = full_page
        
        # 出力ディレクトリを作成
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        
    def setup_driver(self):
        """
        Firefoxドライバーをセットアップ
        
        Returns:
            WebDriver: 設定済みのWebDriverインスタンス
        """
        options = Options()
        options.add_argument('--headless')  # ヘッドレスモード
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument(f'--window-size={self.width},{self.height}')
        
        print(f"Firefoxドライバーを起動中...")
        
        try:
            driver = webdriver.Firefox(options=options)
            driver.set_window_size(self.width, self.height)
            return driver
        except Exception as e:
            print(f"エラー: Firefoxドライバーの起動に失敗しました: {e}", file=sys.stderr)
            print("ヒント: 以下のコマンドでFirefoxとgeckodriverをインストールしてください:", file=sys.stderr)
            print("  sudo apt-get install firefox-esr", file=sys.stderr)
            print("  または geckodriver をダウンロードしてPATHに追加", file=sys.stderr)
            raise
    
    def capture_screenshot(self):
        """
        スクリーンショットを取得
        
        Returns:
            bool: 成功した場合True、失敗した場合False
        """
        driver = None
        
        try:
            print("=" * 60)
            print("スクリーンショット取得開始")
            print("=" * 60)
            print(f"URL: {self.url}")
            print(f"出力先: {self.output_path}")
            print(f"画面サイズ: {self.width}x{self.height}")
            print(f"待機時間: {self.wait_time}秒")
            print(f"フルページ: {'はい' if self.full_page else 'いいえ'}")
            print("=" * 60)
            print()
            
            # ドライバーをセットアップ
            driver = self.setup_driver()
            
            # ページにアクセス
            print(f"ページにアクセス中: {self.url}")
            driver.get(self.url)
            
            # ページが読み込まれるまで待機
            print(f"{self.wait_time}秒待機中...")
            time.sleep(self.wait_time)
            
            # スクリーンショットを取得
            print("スクリーンショットを取得中...")
            
            if self.full_page:
                # フルページスクリーンショット
                # ページの全体の高さを取得
                total_height = driver.execute_script("return document.body.scrollHeight")
                print(f"ページの高さ: {total_height}px")
                
                # 一時的にウィンドウサイズを変更
                driver.set_window_size(self.width, total_height)
                time.sleep(1)
            
            # スクリーンショット保存
            driver.save_screenshot(str(self.output_path))
            
            print(f"✅ 成功: スクリーンショットを保存しました")
            print(f"   ファイル: {self.output_path}")
            print(f"   サイズ: {self.output_path.stat().st_size / 1024:.2f} KB")
            
            return True
            
        except Exception as e:
            print(f"❌ エラー: スクリーンショットの取得に失敗しました: {e}", file=sys.stderr)
            return False
            
        finally:
            if driver:
                driver.quit()
                print("ブラウザを閉じました")


def main():
    """メイン処理"""
    parser = argparse.ArgumentParser(
        description='Webページのスクリーンショットを取得',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # ローカルホストのスクリーンショットを取得
  python screenshot_capture.py http://localhost:3000 screenshot.png
  
  # 公開URLのスクリーンショットを取得
  python screenshot_capture.py https://example.com output.png
  
  # 待機時間を指定
  python screenshot_capture.py http://localhost:3000 screenshot.png --wait 10
  
  # 画面サイズを指定
  python screenshot_capture.py http://localhost:3000 screenshot.png --width 1280 --height 720
  
  # 表示領域のみキャプチャ（フルページではない）
  python screenshot_capture.py http://localhost:3000 screenshot.png --no-full-page
        """
    )
    
    parser.add_argument('url', help='キャプチャするURL')
    parser.add_argument('output', help='出力ファイルパス (.png)')
    parser.add_argument('--width', type=int, default=1920, help='ブラウザ幅 (デフォルト: 1920)')
    parser.add_argument('--height', type=int, default=1080, help='ブラウザ高さ (デフォルト: 1080)')
    parser.add_argument('--wait', type=int, default=5, help='ページ読み込み待機時間（秒）(デフォルト: 5)')
    parser.add_argument('--no-full-page', action='store_true', help='フルページではなく表示領域のみキャプチャ')
    
    args = parser.parse_args()
    
    # スクリーンショット取得を実行
    capture = ScreenshotCapture(
        url=args.url,
        output_path=args.output,
        width=args.width,
        height=args.height,
        wait_time=args.wait,
        full_page=not args.no_full_page
    )
    
    start_time = time.time()
    success = capture.capture_screenshot()
    elapsed_time = time.time() - start_time
    
    print()
    print("=" * 60)
    if success:
        print("✅ 処理完了")
        print(f"処理時間: {elapsed_time:.2f}秒")
    else:
        print("❌ 処理失敗")
        print(f"処理時間: {elapsed_time:.2f}秒")
        sys.exit(1)
    print("=" * 60)


if __name__ == "__main__":
    main()
