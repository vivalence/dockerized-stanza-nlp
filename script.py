from flask import Flask, request, jsonify
import asyncio
import stanza
import logging
import json
import os
from stanza.resources.common import DEFAULT_MODEL_DIR

app = Flask(__name__, static_url_path='', static_folder=os.path.abspath(os.path.dirname(__file__)))


pipelineCache = dict()


def get_file(path):
    res = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    print(res)
    return res

@app.route('/nlp', methods=['POST'])
def get_data():
    global pipelineCache

    try:
        langfrom = request.form.get('langfrom')
        stringnlp = request.form.get('stringnlp')
        annotations = request.form.get('annotations')
        stanza.download(langfrom)

	#pos,upos,ner,lemma,depparse,parse
        processors = 'tokenize,mwt,pos,lemma,depparse'
#        nlp = stanza.Pipeline(lang=langfrom, processors=processors, download_method=None)
        
        if langfrom not in pipelineCache:
            pipelineCache[langfrom] = stanza.Pipeline(lang=langfrom, processors=annotations, use_gpu=False)
        #nlp = stanza.Pipeline(lang=langfrom, processors=annotations)
        doc = pipelineCache[langfrom](stringnlp)

        # Convert Span objects to dictionaries
        serializable_entities = [
            {
                "text": entity.text,
                "type": entity.type,
                "start_char": entity.start_char,
                "end_char": entity.end_char
            }
            for entity in doc.entities
        ]

        annotated_sentences = []
        for sentence in doc.sentences:
            tokens = []
            deps = []
            for word in sentence.words:
                tokens.append({'index': word.id, 'word': word.text, 'lemma': word.lemma, 'pos': word.xpos, 'upos': word.upos, 'feats': word.feats, 'ner': word.parent.ner if word.parent.ner is None or word.parent.ner == 'O' else word.parent.ner[2:]})
                deps.append({'dep': word.deprel, 'governor': word.head, 'governorGloss': sentence.words[word.head-1].text,
                'dependent': word.id, 'dependentGloss': word.text})
            annotated_sentences.append({'basicDependencies': deps, 'tokens': tokens})
            if hasattr(sentence, 'constituency') and sentence.constituency is not None:
                annotated_sentences[-1]['parse'] = str(sentence.constituency)

        return json.dumps({'sentences': annotated_sentences,'entities':serializable_entities})
    except Exception as e:
        print(e)
        return jsonify({"error": "Internal Server Error","err":e}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
