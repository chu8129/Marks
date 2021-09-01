#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create By qiuwen(mail:chu8129@gmail.com) @ 2021-08-31 17:37:32



import sys
sys.path.append("./")

import logging
logger = logging.getLogger("root")

import tensorflow
from data import TextGenerator

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
        data_generater = TextGenerator(128).init("data")

        self.vocab_dict = data_generater.vocab_to_index
        self.tag_dict = data_generater.label_to_index

        self.vocab_size = max(self.vocab_dict.values())
        self.embedding_size = 128
        self.tag_size = max(self.tag_dict.values())

        self.model = None
        self.build()


    def fit(self, X, y, epochs=100, transParam=None):
        return self.model.fit(X, y, epochs=epochs, callbacks=[tensorflow.keras.callbacks.TensorBoard(log_dir="logs", histogram_freq=1)])


