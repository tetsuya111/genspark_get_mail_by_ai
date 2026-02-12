# Backend - 画像変換バッチ

## 概要
Web上からサンプル画像を取得し、128x128のWebP形式に変換するPythonバッチスクリプト。

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
- picsum.photos APIからランダムな画像を取得
- 画像を128x128サイズにリサイズ（アスペクト比を維持してクロップ）
- WebP形式で保存（quality=85）
- 3000枚の画像を生成

## 出力
- 出力先: `backend/images/`
- ファイル名形式: `image_0000.webp` ~ `image_2999.webp`
