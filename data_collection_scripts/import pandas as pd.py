import string
from nltk.corpus import stopwords

# Convert all text to lowercase
df['transcript'] = df['transcript'].str.lower()

# Remove punctuation
df['transcript'] = df['transcript'].str.translate(str.maketrans('', '', string.punctuation))

# Remove stop words
stop = stopwords.words('english')
df['transcript'] = df['transcript'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
