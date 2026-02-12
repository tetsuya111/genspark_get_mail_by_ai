#!/usr/bin/env python3
"""
画像取得・変換バッチスクリプト

目的:
- Web上からサンプル画像を取得
- 128x128のWebP形式に変換
- 3000枚の画像を生成
"""

import os
import sys
import requests
from PIL import Image
from io import BytesIO
from pathlib import Path
import time


class ImageConverter:
    """画像取得・変換クラス"""
    
    def __init__(self, output_dir="images", target_size=(128, 128), target_count=3000):
        """
        初期化
        
        Args:
            output_dir: 出力ディレクトリ
            target_size: 変換後のサイズ (width, height)
            target_count: 生成する画像の枚数
        """
        self.output_dir = Path(output_dir)
        self.target_size = target_size
        self.target_count = target_count
        
        # 出力ディレクトリを作成
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def fetch_sample_images(self):
        """
        Web上からサンプル画像を取得
        
        picsum.photos APIを使用してランダムな画像を取得
        """
        print(f"サンプル画像を{self.target_count}枚取得中...")
        
        for i in range(self.target_count):
            try:
                # picsum.photos APIから画像を取得
                # ランダムな画像を取得するため、URLにシード値を含める
                url = f"https://picsum.photos/256/256?random={i}"
                
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                # 画像を変換して保存
                self.convert_and_save(response.content, i)
                
                # 進捗表示
                if (i + 1) % 100 == 0:
                    print(f"進捗: {i + 1}/{self.target_count} 枚完了")
                
                # APIレート制限対策（軽微な待機）
                if (i + 1) % 50 == 0:
                    time.sleep(0.5)
                    
            except Exception as e:
                print(f"警告: 画像{i}の取得に失敗しました: {e}", file=sys.stderr)
                # エラーが発生しても続行
                continue
        
        print(f"完了: {self.target_count}枚の画像を処理しました")
    
    def convert_and_save(self, image_data, index):
        """
        画像を変換して保存
        
        Args:
            image_data: 画像データ（バイト列）
            index: 画像のインデックス
        """
        try:
            # 画像を開く
            image = Image.open(BytesIO(image_data))
            
            # RGBモードに変換（WebPで保存する際の互換性のため）
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # 128x128にリサイズ（アスペクト比を維持しながらクロップ）
            image = self.resize_with_crop(image, self.target_size)
            
            # WebP形式で保存
            output_path = self.output_dir / f"image_{index:04d}.webp"
            image.save(output_path, 'WEBP', quality=85, method=6)
            
        except Exception as e:
            print(f"エラー: 画像{index}の変換に失敗しました: {e}", file=sys.stderr)
            raise
    
    def resize_with_crop(self, image, target_size):
        """
        アスペクト比を維持しながらリサイズし、中央をクロップ
        
        Args:
            image: PIL Image オブジェクト
            target_size: ターゲットサイズ (width, height)
            
        Returns:
            リサイズ・クロップされた画像
        """
        # 元の画像サイズ
        original_width, original_height = image.size
        target_width, target_height = target_size
        
        # アスペクト比を計算
        original_ratio = original_width / original_height
        target_ratio = target_width / target_height
        
        # リサイズ後のサイズを計算
        if original_ratio > target_ratio:
            # 幅が広い場合：高さを基準にリサイズ
            new_height = target_height
            new_width = int(original_width * (target_height / original_height))
        else:
            # 高さが高い場合：幅を基準にリサイズ
            new_width = target_width
            new_height = int(original_height * (target_width / original_width))
        
        # リサイズ
        image = image.resize((new_width, new_height), Image.LANCZOS)
        
        # 中央をクロップ
        left = (new_width - target_width) // 2
        top = (new_height - target_height) // 2
        right = left + target_width
        bottom = top + target_height
        
        image = image.crop((left, top, right, bottom))
        
        return image


def main():
    """メイン処理"""
    print("=" * 60)
    print("画像取得・変換バッチスクリプト")
    print("=" * 60)
    
    # スクリプトのディレクトリを取得
    script_dir = Path(__file__).parent
    output_dir = script_dir / "images"
    
    print(f"出力ディレクトリ: {output_dir}")
    print(f"画像サイズ: 128x128")
    print(f"出力形式: WebP")
    print(f"生成枚数: 3000")
    print("=" * 60)
    
    # 画像変換処理を実行
    converter = ImageConverter(
        output_dir=output_dir,
        target_size=(128, 128),
        target_count=3000
    )
    
    start_time = time.time()
    converter.fetch_sample_images()
    elapsed_time = time.time() - start_time
    
    print("=" * 60)
    print(f"処理時間: {elapsed_time:.2f}秒")
    print("=" * 60)


if __name__ == "__main__":
    main()
