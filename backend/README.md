# Backend - 画像変換バッチ & スクリーンショット取得

## 概要
Web上からサンプル画像を1枚取得し、128x128のWebP形式に変換するPythonバッチスクリプト。
また、Webページのスクリーンショットを取得する機能も含まれています。

## 要件
- Python 3.8以上
- 必要なライブラリ: Pillow, requests, selenium
- スクリーンショット機能: Firefox ESRまたはGeckodriver（オプション）

## セットアップ

```bash
cd backend
pip install -r requirements.txt
```

## 使用方法

```bash
cd backend
python image_converter.py
```

## 機能
- picsum.photos APIからランダムな画像を1枚取得
- 画像を128x128サイズにリサイズ（アスペクト比を維持してクロップ）
- WebP形式で保存（quality=85）
- エラー時の自動リトライ機能（最大3回）
- 詳細な進捗ログ表示

## 出力
- 出力先: `backend/images/`
- ファイル名: `sample.webp`
- この1枚の画像をフロントエンドで3000枚同時に表示することで負荷テストを実現

---

## スクリーンショット取得機能

### 概要
起動中のWebサーバーのスクリーンショットを取得するスクリプト。

### 使用方法

```bash
# 基本的な使用方法
python screenshot_capture.py http://localhost:3000 screenshot.png

# 待機時間を指定（10秒）
python screenshot_capture.py http://localhost:3000 screenshot.png --wait 10

# 画面サイズを指定
python screenshot_capture.py http://localhost:3000 screenshot.png --width 1280 --height 720

# 表示領域のみキャプチャ（フルページではない）
python screenshot_capture.py http://localhost:3000 screenshot.png --no-full-page
```

### 必要な環境
スクリーンショット機能を使用するには、以下が必要です：

```bash
# Firefox ESRをインストール
sudo apt-get install firefox-esr

# または geckodriver を手動でインストール
# https://github.com/mozilla/geckodriver/releases
```

### 機能
- ヘッドレスブラウザでWebページを開く
- 指定した待機時間後にスクリーンショットを取得
- フルページスクリーンショットに対応
- カスタマイズ可能な画面サイズ
- コマンドライン引数で柔軟な設定

### オプション
- `url`: キャプチャするURL（必須）
- `output`: 出力ファイルパス（必須）
- `--width`: ブラウザ幅（デフォルト: 1920）
- `--height`: ブラウザ高さ（デフォルト: 1080）
- `--wait`: ページ読み込み待機時間（秒）（デフォルト: 5）
- `--no-full-page`: フルページではなく表示領域のみキャプチャ
