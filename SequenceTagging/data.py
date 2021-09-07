#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create By qiuwen(mail:chu8129@gmail.com) @ 2021-08-31 18:38:37


import sys

sys.path.append("./")

import logging

logger = logging.getLogger("root")


import keras
import numpy
import jieba
from collections import Counter
from functools import reduce
import json


class TextGenerator(keras.utils.Sequence):
    def __init__(self, batch_size, max_length=128, vocab_max=100000):

        self.max_length = max_length
        self.batch_size = batch_size
        self.vocab_size_max = vocab_max

        self.data_list = []

        self.vocab_size = None
        self.vocab_to_index = None
        self.index_to_vocab = None
        self.label_size = None
        self.label_to_index = None
        self.index_to_label = None

        self.data_size = None

    def init(self, file_path, train=True):

        with open(file_path) as fr:
            for line in fr:
                data = line.strip("\n").split("\t")
                self.data_list.append((self.cut_word(data[1]), data[0]))

        self.data_size = len(self.data_list)

        if not train:
            return

        label_set = reduce(
            lambda data_set, content: set(content.strip()) | data_set,
            map(lambda cells: cells[1], iter(self.data_list)),
            set(),
        )
        self.label_to_index = dict(_[::-1] for _ in enumerate(sorted(label_set), start=0))
        self.index_to_label = dict(_[::-1] for _ in self.label_to_index.items())
        self.label_size = max(self.index_to_label.keys()) + 1

        word_set = dict(
            reduce(lambda s1, s2: s1 + s2, map(lambda string: Counter(string[0].split()), self.data_list),).most_common(
                self.vocab_size_max
            )
        )
        self.vocab_to_index = dict(_[::-1] for _ in enumerate(sorted(word_set), start=1))
        self.index_to_vocab = dict(_[::-1] for _ in self.vocab_to_index.items())
        self.vocab_size = max(self.index_to_vocab.keys()) + 1

        with open("params", "w") as fw:
            fw.write(json.dumps([self.vocab_to_index, self.index_to_vocab, self.label_to_index, self.index_to_label,]))

    def cut_word(self, line):
        return " ".join(jieba.cut(line))

    def __len__(self):
        return int(self.data_size / self.batch_size) + 1

    def __getitem__(self, index):
        sentence_label_list = self.data_list[index * self.batch_size : (index + 1) * self.batch_size]
        sentence_list = [_[0] for _ in sentence_label_list]
        label_list = [_[1] for _ in sentence_label_list]
        return self.transform_data(sentence_list, label_list)

    def split(self, text):
        return list(jieba.lcut(text))

    def transform_data(self, sentence_list, label_list):
        x_vec = numpy.zeros([len(sentence_list), self.max_length], dtype=numpy.uint8)
        y_vec = numpy.zeros([len(label_list), self.max_length, self.label_size], dtype=numpy.uint8)

        for index, sentence in enumerate(sentence_list):
            x_words = [word for word in sentence.split()]
            onehotindex_charindex_list = [
                (self.vocab_to_index[word], index) for index, word in enumerate(x_words) if word in self.vocab_to_index
            ]
            for onehot_index, char_index in onehotindex_charindex_list:
                x_vec[index][char_index] = onehot_index

        for index, labels in enumerate(label_list):
            for char_index, label in enumerate(labels):
                label_value = self.label_to_index[label]
                y_vec[index][char_index][label_value] = 1
        return x_vec, y_vec
