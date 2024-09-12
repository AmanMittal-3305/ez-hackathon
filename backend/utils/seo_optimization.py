import textstat

def analyze_seo(content, keyword):
    keyword_density = content.lower().count(keyword.lower()) / len(content.split())
    readability_score = textstat.flesch_reading_ease(content)
    
    return {
        'keyword_density': keyword_density,
        'readability_score': readability_score
    }
