# Frontend - 画像表示負荷テスト

## 概要
同じ128x128 WebP画像を3000枚同時に表示し、Webページの負荷をテストするReactアプリケーション。

## 技術スタック
- React 19
- Vite 7
- Node.js

## セットアップ

### 必要な準備
1. バックエンドで画像を生成:
```bash
cd ../backend
pip install -r requirements.txt
python image_converter.py
```

2. 画像をフロントエンドのpublicディレクトリにコピー:
```bash
cd ../frontend
mkdir -p public/images
cp ../backend/images/sample.webp public/images/
```

### 依存関係のインストール
```bash
npm install
```

### 開発サーバーの起動
```bash
npm run dev
```

ブラウザで `http://localhost:3000` にアクセス

### ビルド
```bash
npm run build
```

## 機能
- 同じ画像を3000枚同時にグリッドレイアウトで表示
- 画像の遅延読み込み（Lazy Loading）
- リアルタイム読み込み進捗表示
- 読み込み完了時間の計測
- レスポンシブデザイン
- ホバーエフェクト

## パフォーマンス最適化
- WebP形式による高圧縮
- 128x128の小さいサイズ
- ブラウザのネイティブ遅延読み込み機能を使用
- CSS Gridによる効率的なレイアウト
- **単一画像ファイルの大量表示によるブラウザキャッシュの最大活用**
- 進捗更新の最適化（100件ごと）

## 負荷テストの特徴
- 同じ画像を3000枚同時に表示することで、ブラウザのキャッシュ効率を測定
- 3000個のDOM要素の同時レンダリング性能を評価
- スクロール時のパフォーマンスを検証
