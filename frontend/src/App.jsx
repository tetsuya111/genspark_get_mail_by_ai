import { useState, useEffect, useRef, useCallback } from 'react'
import './App.css'

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
    // 最初の1回だけ実際の画像読み込みが発生する（ブラウザキャッシュ）
    if (!hasImageLoadedOnce.current) {
      hasImageLoadedOnce.current = true
      console.log('✅ 画像が読み込まれました（以降はキャッシュから表示）')
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
    console.error(`❌ 画像の読み込みに失敗: /images/sample.webp`)
  }, [])

  // 同じ画像パスを3000回使用（配列を生成）
  const imagePath = '/images/sample.webp'
  const displayCount = imageCount

  return (
    <div className="app">
      <header className="header">
        <h1>🖼️ 画像表示負荷テスト</h1>
        <p className="subtitle">同じ画像を{imageCount.toLocaleString()}回表示</p>
        <div className="stats">
          <div className="stat-item">
            <span className="stat-label">表示回数:</span>
            <span className="stat-value">{imageCount.toLocaleString()}回</span>
          </div>
          <div className="stat-item">
            <span className="stat-label">読み込み済み:</span>
            <span className="stat-value">{loadedCount.toLocaleString()}回</span>
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
        <p>WebP形式 | 128x128px | 単一画像を{imageCount.toLocaleString()}回表示</p>
        <p className="note">💡 同じ画像を繰り返し使用することでブラウザキャッシュの効果を測定</p>
      </footer>
    </div>
  )
}

export default App
