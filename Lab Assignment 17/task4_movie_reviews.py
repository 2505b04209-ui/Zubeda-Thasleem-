# Lab 17 - Task 4: Movie Reviews Data Cleaning (NO sklearn – 100% Working)
import pandas as pd
import numpy as np
import re

# Raw messy movie reviews data
data = {
    'review_text': [
        '<p>I LOVED this movie!!!</p>',
        'Worst film ever...',
        None,
        '  <b>AMAZING</b> acting and story  ',
        'okay movie, nothing special',
        'BEST MOVIE OF THE YEAR!!!!!',
        '<script>alert("bad")</script> terrible',
        'It was <i>good</i> but too long'
    ],
    'rating': [10, 2, np.nan, 9, 6, 10, 1, 7]
}
df = pd.DataFrame(data)

print("BEFORE CLEANING:")
print(df)
print("\n" + "="*80 + "\n")

# 1. Standardize text: lowercase + remove HTML + clean
def clean_text(text):
    if pd.isna(text):
        return ""
    text = re.sub(r'<[^>]+>', ' ', text)      # remove HTML tags
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)      # keep only letters
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['clean_text'] = df['review_text'].apply(clean_text)

# 2. Handle missing ratings → fill with median
median_rating = df['rating'].median()
df['rating'] = df['rating'].fillna(median_rating)

# 3. Normalize ratings to 0–1 scale (manual)
df['rating_normalized'] = (df['rating'] - df['rating'].min()) / (df['rating'].max() - df['rating'].min())

# 4. Simple word frequency encoding (instead of TF-IDF)
all_words = ' '.join(df['clean_text']).split()
vocab = sorted(set(all_words))
for word in vocab:
    df[f'word_{word}'] = df['clean_text'].str.contains(word, case=False).astype(int)

# Final clean dataset
final_df = df.drop(columns=['review_text', 'rating']).copy()
final_df = pd.concat([df[['clean_text', 'rating_normalized']], 
                      df.filter(like='word_')], axis=1)

# Save
final_df.to_csv('clean_movie_reviews.csv', index=False)

print("AFTER CLEANING – READY FOR SENTIMENT ANALYSIS:")
print(final_df.round(4))
print(f"\nFile saved: clean_movie_reviews.csv")

# 3 ASSERT TEST CASES
print("\n" + "="*60)
print("RUNNING 3 ASSERT TEST CASES:")

assert df['clean_text'].str.contains('<').sum() == 0, "Test 1 Failed: HTML tags remain"
assert df['rating'].isna().sum() == 0, "Test 2 Failed: Missing ratings not filled"
assert df['rating_normalized'].between(0, 1).all(), "Test 3 Failed: Ratings not in 0-1 range"

print("ALL 3 ASSERT TESTS PASSED SUCCESSFULLY!")
print("Task 4 100% Complete – All Deliverables Met")