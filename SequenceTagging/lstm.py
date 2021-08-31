#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create By qiuwen(mail:chu8129@gmail.com) @ 2021-08-31 17:37:32



import sys
sys.path.append("./")

import logging
logger = logging.getLogger("root")

import tensorflow

class BiLstmCrf:
    def build(self):
        model = tensorflow.keras.models.Sequential()
        model.add(tensorflow.keras.layers.Embedding(self.vocab_size, self.embedding_size))
        model.add(tensorflow.keras.layers.Bidirectional(tensorflow.keras.layers.LSTM(self.tag_size, return_sequence=True, active="tanh"), merge_mode="sum"))
        model.add(tensorflow.keras.layers.Bidirectional(tensorflow.keras.layers.LSTM(self.tag_size, return_sequence=True, active="softmax"), merge_mode="sum"))
        # https://www.tensorflow.org/addons/api_docs/python/tfa/layers/CRF
        import  tensorflow_addons
        model.add(tensorflow_addons.layers.CRF(self.tag_size, name="crf")[0])
        model.compile(tensorflow.keras.optimizers.Adam(learning_rate=self.learning_rate, loss={"crf": crf.get_loss}))
        self.model = model

    def __init__(self):
        self.context_label = [] # add

        self.vocab_dict = {}
        self.tag_dict = {}
        self.generate_base_data()

        self.vocab_size = max(self.vocab_dict.values())
        self.embedding_size = 128
        self.tag_size = max(self.tag_dict.values())

        self.model = None

        self.build()

    def generate_base_data(self):
        from functools import reduce
        vocab_set = reduce(lambda data_set, content:set(self.split(content)) | data_set, map(lambda cells:cells[0], iter(self.context_label)), set())
        self.vocab_dict = dict(_[::-1] for _ in enumerate(sorted(vocab_set),start=1))
        tag_set = reduce(lambda data_set, content:set(self.split(content)) | data_set, map(lambda cells:cells[1], iter(self.context_label)), set())
        self.tag_dict = dict(_[::-1] for _ in enumerate(sorted(tag_set),start=1))

    def fit(self, X, y, epochs=100, transParam=None):
        return self.model.fit(X, y, epochs=epochs, callbacks=[tensorflow.keras.callbacks.TensorBoard(log_dir="logs", histogram_freq=1)])


