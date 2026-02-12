import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [loadedCount, setLoadedCount] = useState(0)
  const [startTime, setStartTime] = useState(null)
  const [loadTime, setLoadTime] = useState(null)
  const imageCount = 3000

  useEffect(() => {
    // 計測開始
    setStartTime(Date.now())
  }, [])

  const handleImageLoad = () => {
    const newCount = loadedCount + 1
    setLoadedCount(newCount)
    
    // 全ての画像が読み込まれたら計測終了
    if (newCount === imageCount && startTime) {
      const endTime = Date.now()
      const duration = (endTime - startTime) / 1000
      setLoadTime(duration)
    }
  }

  const handleImageError = (index) => {
    console.error(`画像の読み込みに失敗: image_${String(index).padStart(4, '0')}.webp`)
  }

  // 画像パスの配列を生成
  const imagePaths = Array.from({ length: imageCount }, (_, i) => {
    const filename = `image_${String(i).padStart(4, '0')}.webp`
    return `/images/${filename}`
  })

  return (
    <div className="app">
      <header className="header">
        <h1>🖼️ 画像表示負荷テスト</h1>
        <div className="stats">
          <div className="stat-item">
            <span className="stat-label">総画像数:</span>
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
              <span className="stat-label">読み込み完了時間:</span>
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
        {imagePaths.map((path, index) => (
          <div key={index} className="image-container">
            <img
              src={path}
              alt={`Image ${index}`}
              className="gallery-image"
              loading="lazy"
              onLoad={handleImageLoad}
              onError={() => handleImageError(index)}
            />
          </div>
        ))}
      </main>

      <footer className="footer">
        <p>WebP形式 | 128x128px | {imageCount.toLocaleString()}枚</p>
      </footer>
    </div>
  )
}

export default App
