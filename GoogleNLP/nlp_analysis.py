# Imports the Google Cloud client library
from google.cloud import language_v1
from flask import jsonify
import json
import sys
import os

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = u"Morus, a genus of flowering plants in the family Moraceae, consists of diverse species of deciduous trees commonly known as mulberries, growing wild and under cultivation in many temperate world regions."
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the entity and sentiment of the text
response = client.analyze_entity_sentiment(request={'document': document})

# initialize the array to insert dictionary of entity,sentiment
results = []

for ent in response.entities:
    res = dict()
    res['Entity'] = ent.name
    res['Score'] = ent.sentiment.score * ent.sentiment.magnitude
    results.append(res)

for i in range(len(results)):
    print(results[i])

print("==========================")

# detect entity of the text
response2 = client.analyze_entities(request={'document': document})
for entity in response.entities:
    print("----------")
    print('Entity Name: {0}'.format(entity.name))
    print('Metadata: {0}'.format(entity.metadata))
    print('Salience: {0}'.format(entity.salience))

print("==========================")

# classify content feature of the text
response = client.classify_text(request={'document': document})

results = []

for cat in response.categories:
    res = dict()
    res['Category'] = cat.name
    res['Score'] = cat.confidence
    results.append(res)

for i in range(len(results)):
    print(results[i])
