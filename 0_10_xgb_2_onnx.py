
import xgboost
import onnx
from onnxmltools.convert import convert_xgboost
from onnxmltools.convert.common import data_types

model = xgboost.Booster(model_file="xgboost_model")
model.best_ntree_limit = len(model.get_dump())
initial_type = [('float_input', data_types.FloatTensorType([None, 32]))]
booster_onnx = convert_xgboost(model, initial_types=initial_type)
onnx.save(booster_onnx, 'xgboost.onnx')


"""
# python -V
Python 3.7.7
# pip freeze|egrep "(xgboost|onnx)"
onnx==1.10.1
onnxmltools==1.9.1
onnxruntime==1.4.0
xgboost==1.2.0
"""
