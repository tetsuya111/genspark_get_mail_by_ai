# サンプル画像

このディレクトリには、画像表示負荷テストシステムで使用されるサンプル画像が含まれています。

## 📁 ディレクトリ構造

```
sample/
└── images/
    └── sample.webp    # 負荷テスト用のサンプル画像（128x128px）
```

## 🖼️ 画像情報

### sample.webp
- **サイズ**: 128 x 128 px
- **形式**: WebP (VP8エンコーディング)
- **ファイルサイズ**: 約4.2KB
- **用途**: フロントエンドで3000枚同時表示する負荷テスト
- **生成方法**: `backend/image_converter.py` で自動生成

## 📖 使用方法

このサンプル画像は、以下の手順で使用されます：

1. **バックエンドで生成**
   ```bash
   cd backend
   python image_converter.py
   ```

2. **フロントエンドにコピー**
   ```bash
   cd frontend
   mkdir -p public/images
   cp ../backend/images/sample.webp public/images/
   # または
   cp ../sample/images/sample.webp public/images/
   ```

3. **フロントエンドで表示**
   - 同じ画像を3000個の`<img>`タグで参照
   - ブラウザキャッシュの効果を測定
   - DOM要素の大量レンダリング性能を評価

## 🎯 負荷テストの特徴

- **単一画像の繰り返し表示**: 同じ画像ファイルを3000回参照
- **ブラウザキャッシュ効果**: 1回のダウンロード(4.2KB)で3000枚分の表示
- **DOM要素数**: 3000個の画像コンテナ + 3000個のimg要素
- **レンダリング**: Lazy Loadingで段階的に表示

## 📝 注意事項

- このディレクトリの画像は参照用のサンプルです
- 実際の使用時は `backend/image_converter.py` で新しい画像を生成してください
- 生成された画像は毎回異なる内容になります（picsum.photos APIを使用）
