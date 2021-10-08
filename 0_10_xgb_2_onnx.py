
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



“”“
def predict(data):
        sess = onnxruntime.InferenceSession(ensure_file("***xgboost.onnx"))
        x = sess.get_inputs()[0].name
        restore = sess.get_outputs()[0].name
        data = data.values.tolist()
        prediction_value = [
            float(value[0])
            for value in sess.run([restore], {x: numpy.reshape(data, (len(data), len(data[0]))).astype(numpy.float32)})[0]
        ]
”“”
