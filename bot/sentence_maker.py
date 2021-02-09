# -*- coding: utf-8 -*-
import json
import markovify


class SentenceMaker:
    def __init__(self, model_fp):
        self.model = self._load_model(model_fp)

    @staticmethod
    def _load_model(model_fp):
        with open(model_fp, 'r') as model_file:
            model = json.load(model_file)
        return markovify.Text.from_json(model)

    def make_any_sentence(self):
        sentence = self.model.make_sentence()
        if sentence:
            return sentence
        else:
            return self.make_any_sentence()

    def make_sentence_for_twitter(self):
        sentence = self.model.make_short_sentence(max_chars=280)
        if sentence:
            return sentence
        else:
            return self.make_sentence_for_twitter()
