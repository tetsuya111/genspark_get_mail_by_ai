# Backend - 画像変換バッチ

## 概要
Web上からサンプル画像を1枚取得し、128x128のWebP形式に変換するPythonバッチスクリプト。

## 要件
- Python 3.8以上
- 必要なライブラリ: Pillow, requests

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
- この1枚の画像をフロントエンドで3000回表示することで負荷テストを実現
