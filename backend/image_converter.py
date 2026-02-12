#!/usr/bin/env python3
"""
画像取得・変換バッチスクリプト

目的:
- Web上からサンプル画像を1枚取得
- 128x128のWebP形式に変換
- 変換した画像をsample.webpとして保存
"""

import sys
import requests
from PIL import Image
from io import BytesIO
from pathlib import Path
import time


class ImageConverter:
    """画像取得・変換クラス"""
    
    def __init__(self, output_dir="images", target_size=(128, 128), output_filename="sample.webp"):
        """
        初期化
        
        Args:
            output_dir: 出力ディレクトリ
            target_size: 変換後のサイズ (width, height)
            output_filename: 出力ファイル名
        """
        self.output_dir = Path(output_dir)
        self.target_size = target_size
        self.output_filename = output_filename
        
        # 出力ディレクトリを作成
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def fetch_and_convert_image(self, retries=3):
        """
        Web上からサンプル画像を1枚取得して変換
        
        Args:
            retries: リトライ回数
            
        Returns:
            bool: 成功した場合True、失敗した場合False
        
        picsum.photos APIを使用してランダムな画像を取得
        """
        print(f"サンプル画像を取得中...")
        
        for attempt in range(retries):
            try:
                # picsum.photos APIから画像を取得
                url = "https://picsum.photos/256/256"
                
                print(f"  試行 {attempt + 1}/{retries}: {url}")
                response = requests.get(url, timeout=15)
                response.raise_for_status()
                
                print(f"  画像を取得しました（サイズ: {len(response.content)} bytes）")
                
                # 画像を変換して保存
                self.convert_and_save(response.content)
                
                print(f"✅ 成功: 画像を {self.output_filename} として保存しました")
                return True
                    
            except Exception as e:
                print(f"⚠️  エラー (試行 {attempt + 1}/{retries}): {e}", file=sys.stderr)
                if attempt < retries - 1:
                    wait_time = 2 ** attempt  # 指数バックオフ
                    print(f"  {wait_time}秒後にリトライします...")
                    time.sleep(wait_time)
                else:
                    print(f"❌ 失敗: {retries}回試行しましたが画像の取得に失敗しました", file=sys.stderr)
                    return False
        
        return False
    
    def convert_and_save(self, image_data):
        """
        画像を変換して保存
        
        Args:
            image_data: 画像データ（バイト列）
        """
        try:
            # 画像を開く
            image = Image.open(BytesIO(image_data))
            print(f"  元の画像サイズ: {image.size}, モード: {image.mode}")
            
            # RGBモードに変換（WebPで保存する際の互換性のため）
            if image.mode != 'RGB':
                image = image.convert('RGB')
                print(f"  画像モードをRGBに変換しました")
            
            # 128x128にリサイズ（アスペクト比を維持しながらクロップ）
            image = self.resize_with_crop(image, self.target_size)
            print(f"  画像を {self.target_size[0]}x{self.target_size[1]} にリサイズしました")
            
            # WebP形式で保存
            output_path = self.output_dir / self.output_filename
            image.save(output_path, 'WEBP', quality=85, method=6)
            print(f"  WebP形式で保存しました: {output_path}")
            
        except Exception as e:
            print(f"❌ エラー: 画像の変換に失敗しました: {e}", file=sys.stderr)
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
    print(f"取得枚数: 1枚")
    print(f"出力ファイル名: sample.webp")
    print("=" * 60)
    print()
    
    # 画像変換処理を実行
    converter = ImageConverter(
        output_dir=output_dir,
        target_size=(128, 128),
        output_filename="sample.webp"
    )
    
    start_time = time.time()
    success = converter.fetch_and_convert_image(retries=3)
    elapsed_time = time.time() - start_time
    
    print()
    print("=" * 60)
    if success:
        print(f"✅ 処理完了")
        print(f"処理時間: {elapsed_time:.2f}秒")
        print(f"出力ファイル: {output_dir / 'sample.webp'}")
    else:
        print(f"❌ 処理失敗")
        print(f"処理時間: {elapsed_time:.2f}秒")
        sys.exit(1)
    print("=" * 60)


if __name__ == "__main__":
    main()
