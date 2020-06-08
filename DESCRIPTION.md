# NovelFacts

## 1. Fake News Detection

### 1.1 Creating the datasets

For building our Fake News dataset, we have scraped data (in the form of both text and images) from verified fact-checking websites.

### 1.2 Acceptable Inputs

Users can directly forward messages to the Whatsapp bot, or add their queries in the browser.
These messages can be in the form of -
- URL Link
- Text
- Images
- Audio

The user can also enter the news in any Regional or Foreign Languages.

### 1.3 Language Translation

We have used google translate API for interpreting different languages, and then applied further text similarity detection methods.

### 1.4 Text Similarity Detection

We have used BERT(Bidirectional Encoder Representations from Transformers) pre-trained models to calculating semantic similarity between texts.

- Model used:bert-base-nli-stsb-mean-tokens

On top of these BERT embeddings, we have calculated cosine similarity to identify any matching information across our dataset.

### 1.5 Image Similarity Detection

We have used open-cv for image processing, and calculated similarities using measures like mean square errors and structural similarity.


## 2. Integration with Twilio

We have integrated this model with Twilio which allows us to programmatically send and receive whatsapp messages using its web service APIs.

## 3. Results

After processing the data and accessing the similarities and differences, the application will return the result with the most similar news from the data set, along with detailed information like -
- Fake news title
- Similarity score (Highest percentage match with our dataset)
- Explanation
- Country of Source/Origin 
- URL of the news source

