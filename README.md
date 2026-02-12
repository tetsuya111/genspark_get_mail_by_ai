# 画像表示負荷テストシステム

## 🎯 目的
画像表示によりWebページの負荷テストを行うシステム

## 📋 システム構成

### Backend（Python）
- **役割**: Web上からサンプル画像を1枚取得し、128x128のWebP形式に変換
- **技術**: Python 3, Pillow, requests
- **出力**: 1枚のWebP画像（128x128px）

### Frontend（React/Node.js）
- **役割**: 同じ画像を3000枚同時に表示してWebページの負荷テスト
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
cp ../backend/images/sample.webp public/images/
```

### 3. フロントエンド起動
```bash
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
│   ├── screenshot_capture.py # スクリーンショット取得スクリプト
│   ├── requirements.txt      # Python依存関係
│   ├── images/               # 生成された画像（1枚）
│   │   └── sample.webp      # 変換後の画像
│   └── README.md
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # メインコンポーネント
│   │   ├── App.css          # スタイル
│   │   ├── main.jsx         # エントリーポイント
│   │   └── index.css        # グローバルスタイル
│   ├── public/
│   │   └── images/          # 画像配置先
│   │       └── sample.webp  # 表示用画像
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
├── sample/
│   ├── images/              # サンプル画像
│   │   └── sample.webp     # 参照用サンプル画像
│   └── README.md            # サンプル画像の説明
└── README.md                 # このファイル
```

## 🔧 技術仕様

### 画像要件
- **サイズ**: 128 x 128 px
- **形式**: WebP
- **取得枚数**: 1枚
- **表示枚数**: 3000枚（同じ画像を同時に表示）
- **ソース**: picsum.photos API

### 機能要件
- ✅ 同じ画像を3000枚同時に表示
- ✅ 遅延読み込み（Lazy Loading）
- ✅ リアルタイム進捗表示
- ✅ 読み込み時間計測
- ✅ レスポンシブデザイン

## 📊 負荷テスト項目

このシステムで以下の負荷テストが可能です：

1. **画像読み込み速度**: 同じ画像を3000枚同時に表示する際の読み込み完了時間
2. **レンダリング性能**: ブラウザの描画性能（3000個のDOM要素の同時レンダリング）
3. **メモリ使用量**: ブラウザのメモリ消費（同一画像の参照効率）
4. **スクロール性能**: 大量要素のスクロール性能
5. **キャッシュ効率**: 同一画像ファイルの繰り返し参照によるブラウザキャッシュ効果

## 🎨 主な機能

### フロントエンド
- **グリッドレイアウト**: CSS Gridによる効率的な配置
- **進捗バー**: リアルタイム読み込み状況表示
- **統計情報**: 総数、読み込み済み、進捗率、完了時間
- **ホバーエフェクト**: 画像にマウスオーバーでアニメーション
- **単一画像の大量表示**: 同じ画像を3000枚同時に効率的に表示

### バックエンド
- **自動取得**: picsum.photos APIから画像を1枚取得
- **自動変換**: 128x128にリサイズ＋WebP変換
- **エラーハンドリング**: 失敗時のリトライ処理
- **シンプルな実装**: 1枚のみの処理で高速実行

## 📝 ライセンス
ISC

## 👤 作者
Google天才プログラマー
