import { useState, useEffect, useRef, useCallback } from 'react'
import './App.css'
import { IMAGE_BASE64 } from './imageData'

function App() {
  const [loadedCount, setLoadedCount] = useState(0)
  const [startTime, setStartTime] = useState(null)
  const [loadTime, setLoadTime] = useState(null)
  const imageCount = 3000
  const loadedRef = useRef(0)
  const hasImageLoadedOnce = useRef(false)

  useEffect(() => {
    // 計測開始
    setStartTime(Date.now())
  }, [])

  const handleImageLoad = useCallback(() => {
    // Base64データの場合は即座に読み込まれる
    if (!hasImageLoadedOnce.current) {
      hasImageLoadedOnce.current = true
      console.log('✅ Base64画像が読み込まれました（データURIスキーム）')
    }

    loadedRef.current += 1
    const newCount = loadedRef.current
    
    // 進捗更新（パフォーマンスのため100件ごと）
    if (newCount % 100 === 0 || newCount === imageCount) {
      setLoadedCount(newCount)
    }
    
    // 全ての画像が読み込まれたら計測終了
    if (newCount === imageCount && startTime) {
      const endTime = Date.now()
      const duration = (endTime - startTime) / 1000
      setLoadTime(duration)
      setLoadedCount(imageCount)
      console.log(`🎉 すべての画像の読み込みが完了しました（${duration.toFixed(2)}秒）`)
    }
  }, [startTime, imageCount])

  const handleImageError = useCallback(() => {
    console.error(`❌ Base64画像の読み込みに失敗`)
  }, [])

  // Base64データを使用（配列を生成）
  const imagePath = IMAGE_BASE64
  const displayCount = imageCount

  return (
    <div className="app">
      <header className="header">
        <h1>🖼️ 画像表示負荷テスト (Base64版)</h1>
        <p className="subtitle">Base64データURIで同じ画像を{imageCount.toLocaleString()}枚同時に表示</p>
        <div className="stats">
          <div className="stat-item">
            <span className="stat-label">表示枚数:</span>
            <span className="stat-value">{imageCount.toLocaleString()}枚</span>
          </div>
          <div className="stat-item">
            <span className="stat-label">読み込み済み:</span>
            <span className="stat-value">{loadedCount.toLocaleString()}枚</span>
          </div>
          <div className="stat-item">
            <span className="stat-label">進捗:</span>
            <span className="stat-value">
              {((loadedCount / imageCount) * 100).toFixed(2)}%
            </span>
          </div>
          {loadTime && (
            <div className="stat-item complete">
              <span className="stat-label">完了時間:</span>
              <span className="stat-value">{loadTime.toFixed(2)}秒</span>
            </div>
          )}
        </div>
        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{ width: `${(loadedCount / imageCount) * 100}%` }}
          />
        </div>
      </header>

      <main className="gallery">
        {Array.from({ length: displayCount }).map((_, index) => (
          <div key={index} className="image-container">
            <img
              src={imagePath}
              alt={`Image ${index + 1}`}
              className="gallery-image"
              loading="lazy"
              onLoad={handleImageLoad}
              onError={handleImageError}
            />
          </div>
        ))}
      </main>

      <footer className="footer">
        <p>WebP形式 | 128x128px | Base64データURIで{imageCount.toLocaleString()}枚同時表示</p>
        <p className="note">💡 Base64エンコードされた画像データをHTMLに直接埋め込み（Data URIスキーム）</p>
        <p className="note">📦 データサイズ: 約5.7KB (Base64) / 元画像: 4.2KB (WebP)</p>
      </footer>
    </div>
  )
}

export default App
