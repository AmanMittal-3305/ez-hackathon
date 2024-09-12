import React, { useState } from 'react';
import axios from 'axios';
import './App.css';  // Link to an external CSS file for better styling

function App() {
  const [topic, setTopic] = useState('');
  const [style, setStyle] = useState('formal');
  const [keywords, setKeywords] = useState('');
  const [blog, setBlog] = useState('');
  const [seoData, setSeoData] = useState(null);
  const [translation, setTranslation] = useState('');

  const generateBlog = async () => {
    try {
      const response = await axios.post('http://localhost:5000/generate_blog', {
        topic,
        style,
        keywords: keywords.split(',')
      });
      setBlog(response.data.blog);
    } catch (error) {
      console.error(error);
    }
  };

  const checkSEO = async () => {
    try {
      const response = await axios.post('http://localhost:5000/seo_optimize', {
        content: blog,
        keyword: keywords.split(',')[0]
      });
      setSeoData(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const translateContent = async (targetLang) => {
    try {
      const response = await axios.post('http://localhost:5000/translate', {
        content: blog,
        target_lang: targetLang
      });
      setTranslation(response.data.translated_content);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="app-container">
      <h1 className="title">AI Blog Generator</h1>

      <div className="input-section">
        <input 
          className="input-field" 
          value={topic} 
          onChange={(e) => setTopic(e.target.value)} 
          placeholder="Enter Blog Topic" 
        />
        
        <select 
          className="dropdown" 
          value={style} 
          onChange={(e) => setStyle(e.target.value)}
        >
          <option value="formal">Formal</option>
          <option value="casual">Casual</option>
          <option value="technical">Technical</option>
        </select>

        <input 
          className="input-field" 
          value={keywords} 
          onChange={(e) => setKeywords(e.target.value)} 
          placeholder="Enter Keywords (comma-separated)" 
        />

        <button className="generate-btn" onClick={generateBlog}>
          Generate Blog
        </button>
      </div>

      {blog && (
        <div className="blog-output">
          <h2>Generated Blog</h2>
          <p>{blog}</p>
        </div>
      )}

      <div className="seo-section">
        <h2>SEO Check</h2>
        <button className="check-seo-btn" onClick={checkSEO}>Check SEO</button>
        {seoData && (
          <div>
            <p><strong>Keyword Density:</strong> {seoData.keyword_density}</p>
            <p><strong>Readability Score:</strong> {seoData.readability_score}</p>
          </div>
        )}
      </div>

      
    </div>
  );
}

export default App;
