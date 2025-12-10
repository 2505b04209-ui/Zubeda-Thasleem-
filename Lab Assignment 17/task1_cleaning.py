# Lab 17 - Task 1: Social Media Data Cleaning (100% Working Version)
import pandas as pd
import numpy as np
import nltk
import re
from nltk.corpus import stopwords

# Download required data
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Sample dirty social media data
data = {
    'post_id': [1,2,3,4,5,6,7,8],
    'post_text': [
        'I love this!!! #awesome',
        'Check out my new phone!!!',
        'I love this!!! #awesome',           # duplicate
        'Thanks everyone for the support',
        None,                                 # missing text
        'win free iphone now click here!!!',
        'Beautiful day today',
        'win free iphone now click here!!!'   # spam duplicate
    ],
    'likes': [45, None, 120, 89, 23, 567, 78, 567],
    'shares': [12, 5, None, 20, 3, 189, 15, 189],
    'timestamp': [
        '2025-03-15 14:30:00',
        '2025-03-15 09:15:00',
        '2025-03-16 20:45:00',
        '2025-03-17 11:20:00',
        '2025-03-17 18:00:00',
        '2025-03-18 13:10:00',
        '2025-03-19 08:30:00',
        '2025-03-18 13:10:00'
    ]
}
df = pd.DataFrame(data)

print("Original dirty data:")
print(df)
print("\n" + "="*60 + "\n")

# 1. Clean the text
def clean_text(text):
    if pd.isna(text):
        return ""
    text = re.sub(r'[^a-zA-Z\s]', '', text)   # remove punctuation & emojis
    text = text.lower()
    words_list = [w for w in text.split() if w not in stop_words]
    return ' '.join(words_list)

df['post_text_clean'] = df['post_text'].apply(clean_text)

# 2. Handle missing values
df['likes'].fillna(0, inplace=True)
df['shares'].fillna(0, inplace=True)

# 3. Convert timestamp & extract features
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['weekday'] = df['timestamp'].dt.day_name()
df['is_weekend'] = df['timestamp'].dt.weekday >= 5

# 4. Detect duplicates and spam
df['is_duplicate'] = df.duplicated(subset=['post_text_clean'], keep='first')
spam_keywords = ['win', 'free', 'click', 'iphone']
df['is_spam'] = df['post_text_clean'].str.contains('|'.join(spam_keywords), case=False, na=False)

# 5. Remove duplicates and spam
clean_df = df[~(df['is_duplicate'] | df['is_spam'])].copy()
clean_df.reset_index(drop=True, inplace=True)

# Final clean dataset
final_df = clean_df[['post_text_clean', 'likes', 'shares', 'hour', 'weekday', 'is_weekend']]

# Save to CSV
final_df.to_csv('clean_social_media.csv', index=False)

print("CLEANING COMPLETED SUCCESSFULLY!")
print("\nFinal Clean Dataset:")
print(final_df)
print("\nFile saved as: clean_social_media.csv in your folder")