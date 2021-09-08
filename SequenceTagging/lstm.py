#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create By qiuwen(mail:chu8129@gmail.com) @ 2021-08-31 17:37:32


import sys

sys.path.append("./")

import logging

logger = logging.getLogger("root")

import tensorflow
import tensorflow_addons
from data import TextGenerator


class BiLstmCrf:
    def build(self):
        input_ = tensorflow.keras.Input(shape=(self.max_length,))
        embedding_ = tensorflow.keras.layers.Embedding(
            self.vocab_size, self.embedding_size, input_length=self.max_length, mask_zero=True
        )(input_)
        lstm_1_ = tensorflow.keras.layers.Bidirectional(
            tensorflow.keras.layers.LSTM(
                self.tag_size, return_sequences=True, recurrent_dropout=0.3, activation="tanh"
            ),
            merge_mode="sum",
        )(embedding_)
        lstm_ = tensorflow.keras.layers.Bidirectional(
            tensorflow.keras.layers.LSTM(
                self.tag_size, return_sequences=True, recurrent_dropout=0.3, activation="softmax"
            ),
            merge_mode="sum",
        )(lstm_1_)
        # https://www.tensorflow.org/addons/api_docs/python/tfa/layers/CRF
        """
        decoded_sequence, potentials, sequence_length, chain_kernel = tensorflow_addons.layers.CRF(
            self.tag_size, name="crf"
        )(lstm_)
        model = tensorflow.keras.Model(input_, potentials)
        """
        model = tensorflow.keras.Model(input_, lstm_)
        model.compile(
            optimizer=tensorflow.keras.optimizers.RMSprop(learning_rate=0.3),
            loss=tensorflow_addons.losses.SigmoidFocalCrossEntropy(),
        )
        print(model.summary())
        self.model = model

    def __init__(self):
        self.batch_size = 128
        self.max_length = 10
        self.epochs = 100

        self.data_generater = TextGenerator(self.batch_size, self.max_length)
        self.data_generater.init("data.tsv")

        self.max_length = self.data_generater.max_length

        self.vocab_dict = self.data_generater.vocab_to_index
        self.tag_dict = self.data_generater.label_to_index

        self.vocab_size = self.data_generater.vocab_size
        self.tag_size = self.data_generater.label_size

        self.embedding_size = 64

        self.model = None
        self.build()

    def fit(self):
        for _ in range(self.epochs):
            for index in range(len(self.data_generater)):
                x, y = self.data_generater[index]
                self.model.fit(
                    tensorflow.convert_to_tensor(x),
                    tensorflow.convert_to_tensor(y),
                    epochs=1,
                    batch_size=self.batch_size,
                    callbacks=[tensorflow.keras.callbacks.TensorBoard(log_dir="logs", histogram_freq=1)],
                )
        self.model.save("finalmodel.h5")


if __name__ == "__main__":
    model = BiLstmCrf()
    model.fit()
