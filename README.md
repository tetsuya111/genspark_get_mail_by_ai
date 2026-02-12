# 画像表示負荷テストシステム

## 🎯 目的
画像表示によりWebページの負荷テストを行うシステム

## 📋 システム構成

### Backend（Python）
- **役割**: Web上からサンプル画像を取得し、128x128のWebP形式に変換
- **技術**: Python 3, Pillow, requests
- **出力**: 3000枚のWebP画像（各128x128px）

### Frontend（React/Node.js）
- **役割**: 3000枚の画像をWebページに表示
- **技術**: React 19, Vite 7, Node.js
- **機能**: グリッドレイアウト、遅延読み込み、進捗表示

## 🚀 クイックスタート

### 1. バックエンドで画像を生成
```bash
cd backend
pip install -r requirements.txt
python image_converter.py
```

### 2. 画像をフロントエンドに配置
```bash
cd ../frontend
mkdir -p public/images
cp ../backend/images/*.webp public/images/
```

### 3. フロントエンド起動
```bash
cd ../frontend
npm install
npm run dev
```

### 4. ブラウザでアクセス
```
http://localhost:3000
```

## 📁 ディレクトリ構造
```
webapp/
├── backend/
│   ├── image_converter.py    # 画像取得・変換バッチ
│   ├── requirements.txt      # Python依存関係
│   ├── images/               # 生成された画像（3000枚）
│   └── README.md
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # メインコンポーネント
│   │   ├── App.css          # スタイル
│   │   ├── main.jsx         # エントリーポイント
│   │   └── index.css        # グローバルスタイル
│   ├── public/
│   │   └── images/          # 画像配置先
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
└── README.md                 # このファイル
```

## 🔧 技術仕様

### 画像要件
- **サイズ**: 128 x 128 px
- **形式**: WebP
- **枚数**: 3000枚
- **ソース**: picsum.photos API

### 機能要件
- ✅ 3000枚の画像を表示
- ✅ 遅延読み込み（Lazy Loading）
- ✅ リアルタイム進捗表示
- ✅ 読み込み時間計測
- ✅ レスポンシブデザイン

## 📊 負荷テスト項目

このシステムで以下の負荷テストが可能です：

1. **画像読み込み速度**: 3000枚の画像読み込み完了時間
2. **レンダリング性能**: ブラウザの描画性能
3. **メモリ使用量**: ブラウザのメモリ消費
4. **スクロール性能**: 大量要素のスクロール性能
5. **ネットワーク負荷**: 同時リクエスト処理

## 🎨 主な機能

### フロントエンド
- **グリッドレイアウト**: CSS Gridによる効率的な配置
- **進捗バー**: リアルタイム読み込み状況表示
- **統計情報**: 総数、読み込み済み、進捗率、完了時間
- **ホバーエフェクト**: 画像にマウスオーバーでアニメーション

### バックエンド
- **自動取得**: picsum.photos APIから画像を自動取得
- **自動変換**: 128x128にリサイズ＋WebP変換
- **進捗表示**: 100枚ごとに進捗を表示
- **エラーハンドリング**: 失敗時も処理を継続

## 📝 ライセンス
ISC

## 👤 作者
Google天才プログラマー
