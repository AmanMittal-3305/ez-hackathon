from flask import Flask, request, jsonify
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import textstat
import spacy
from langdetect import detect
from utils.seo_optimization import analyze_seo
from utils.sentiment_analysis import analyze_sentiment
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load language model (GPT-like model)
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# NLP pipelines for sentiment and text generation
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

# Endpoint for blog generation
@app.route('/generate_blog', methods=['POST'])
def generate_blog():
    data = request.json
    topic = data.get('topic')
    style = data.get('style', 'formal')
    keywords = data.get('keywords', [])
    sentiment = data.get('sentiment', 'neutral')
    
    # Generate blog content
    prompt = f"Write a {style} blog about {topic} using keywords: {', '.join(keywords)}"
    result = generator(prompt, max_length=500, num_return_sequences=1)
    blog_content = result[0]['generated_text']
    
    # Sentiment analysis
    sentiment_result = analyze_sentiment(blog_content)
    
    return jsonify({
        'blog': blog_content,
        'sentiment': sentiment_result
    })

# SEO Optimization route
@app.route('/seo_optimize', methods=['POST'])
def seo_optimize():
    content = request.json.get('content')
    keyword = request.json.get('keyword')
    
    seo_result = analyze_seo(content, keyword)
    
    return jsonify(seo_result)

# Multilingual support route
@app.route('/translate', methods=['POST'])
def translate():
    content = request.json.get('content')
    target_lang = request.json.get('target_lang', 'es')  # Default to Spanish
    
    # Language detection
    detected_lang = detect(content)
    
    # Example translation (to be replaced by actual translation API)
    translated_content = f"Translated ({detected_lang} to {target_lang}): " + content  # Simple mock translation
    
    return jsonify({
        'translated_content': translated_content
    })

if __name__ == '__main__':
    app.run(debug=True)
