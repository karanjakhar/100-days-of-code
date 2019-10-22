from nltk import word_tokenize, pos_tag, ne_chunk, sent_tokenize


#data processing
words = []
with open('entity_detection_data.txt','r') as f:
	data = f.read()
	print(data)
	data = sent_tokenize(data)
	print(data)
	for d in data:
		words += word_tokenize(d)
	print(words)
	data = pos_tag(words)
	print(data)
	data = ne_chunk(data)

 
print(data)
