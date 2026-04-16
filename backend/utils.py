import re
import keyword
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Python keywords (do NOT replace)
keywords = set(keyword.kwlist)

# Remove comments
def remove_comments(code):
    code = re.sub(r'#.*', '', code)  # Python comments
    code = re.sub(r'//.*', '', code)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    return code

# Normalize variable names
def normalize_variables(code):
    tokens = re.findall(r'\b[a-zA-Z_]\w*\b', code)

    mapping = {}
    count = 1

    normalized_code = code

    for token in tokens:
        if token not in keywords and token not in mapping:
            mapping[token] = f"var{count}"
            count += 1

    for original, new in mapping.items():
        normalized_code = re.sub(r'\b' + original + r'\b', new, normalized_code)

    return normalized_code

# Full preprocessing
def preprocess(code):
    code = remove_comments(code)
    code = normalize_variables(code)
    code = re.sub(r'\s+', ' ', code)  # remove extra spaces
    return code.strip()

# Main similarity function
def calculate_similarity(codes):
    processed = [preprocess(code) for code in codes]

    vectorizer = TfidfVectorizer(token_pattern=r'\b\w+\b')
    tfidf_matrix = vectorizer.fit_transform(processed)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    return similarity_matrix.tolist()