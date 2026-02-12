# Frontend (Base64版) - 画像表示負荷テスト

## 概要
Base64エンコードされた画像データ（Data URIスキーム）を使用して、同じ128x128 WebP画像を3000枚同時に表示し、Webページの負荷をテストするReactアプリケーション。

## 技術スタック
- React 19
- Vite 7
- Node.js

## 🎯 Base64版の特徴

### 通常版との違い
| 項目 | 通常版 (frontend) | Base64版 (frontend_b64) |
|------|------------------|------------------------|
| 画像の読み込み | 外部ファイル (`/images/sample.webp`) | Base64データURI（HTML埋め込み） |
| HTTPリクエスト | 1回（初回のみ） | 0回（埋め込み済み） |
| データサイズ | 4.2KB (WebP) | 5.7KB (Base64) |
| キャッシュ | ブラウザキャッシュ使用 | HTMLに直接埋め込み |
| 初期ロード | 画像ファイルのダウンロード待ち | JSバンドルに含まれる |

### メリット
- ✅ HTTPリクエスト削減（画像ファイルへのリクエストが不要）
- ✅ 初期表示が高速（画像がJSバンドルに含まれる）
- ✅ オフライン対応が容易
- ✅ デプロイが簡単（画像ファイルの配置が不要）

### デメリット
- ❌ データサイズが約33%増加（Base64エンコードのオーバーヘッド）
- ❌ JSバンドルサイズが増加
- ❌ ブラウザキャッシュの効果が測定できない

## セットアップ

### 依存関係のインストール
```bash
npm install
```

### 開発サーバーの起動
```bash
npm run dev
```

ブラウザで `http://localhost:3001` にアクセス

### ビルド
```bash
npm run build
```

## 機能
- Base64データURIで同じ画像を3000枚同時にグリッドレイアウトで表示
- 画像の遅延読み込み（Lazy Loading）
- リアルタイム読み込み進捗表示
- 読み込み完了時間の計測
- レスポンシブデザイン
- ホバーエフェクト

## パフォーマンス最適化
- Base64エンコードされた画像データをJSモジュールとして分離
- 同じData URIを3000回参照
- ブラウザのネイティブ遅延読み込み機能を使用
- CSS Gridによる効率的なレイアウト
- 進捗更新の最適化（100件ごと）

## 負荷テストの特徴
- Base64データURIの大量使用によるメモリ効率を測定
- DOM要素の大量レンダリング性能を評価（3000個のDOM要素）
- スクロール時のパフォーマンスを検証
- HTTPリクエスト0回での画像表示性能を測定

## ファイル構成

```
frontend_b64/
├── src/
│   ├── App.jsx          # メインコンポーネント（Base64対応）
│   ├── App.css          # スタイル
│   ├── imageData.js     # Base64エンコードされた画像データ
│   ├── main.jsx         # エントリーポイント
│   └── index.css        # グローバルスタイル
├── package.json
├── vite.config.js       # Vite設定（ポート3001）
└── README.md            # このファイル
```

## Base64画像データの生成方法

画像をBase64エンコードするには、バックエンドのPythonスクリプトを使用します：

```python
import base64
from pathlib import Path

# 画像を読み込んでBase64エンコード
image_path = Path("sample/images/sample.webp")
with open(image_path, "rb") as f:
    image_data = f.read()
    
base64_data = base64.b64encode(image_data).decode('utf-8')
data_uri = f"data:image/webp;base64,{base64_data}"

# JSファイルに保存
output_path = Path("frontend_b64/src/imageData.js")
with open(output_path, "w") as f:
    f.write(f"export const IMAGE_BASE64 = '{data_uri}';\n")
```

## 比較テスト

通常版（frontend）とBase64版（frontend_b64）を両方起動して、パフォーマンスを比較できます：

```bash
# 通常版
cd frontend
npm run dev  # http://localhost:3000

# Base64版
cd ../frontend_b64
npm run dev  # http://localhost:3001
```

## 技術的な詳細

- **Data URIスキーム**: `data:image/webp;base64,<Base64データ>`
- **エンコード効率**: 元画像4.2KB → Base64 5.7KB（約33%増加）
- **メモリ使用**: 同じData URI文字列を3000回参照（メモリ効率良好）
- **レンダリング**: ブラウザが自動的にBase64をデコードして画像として表示
