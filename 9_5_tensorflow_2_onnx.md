```
python -m tf2onnx.convert   --checkpoint ./model.ckpt.meta   --output ./ad_effect.onnx   --inputs x:0 --outputs restore:0
```
```
python -m tf2onnx.convert --saved-model ./keypoint_classifier/keypoint_classifier_mouse.pb/ --output ./model.onnx --opset 15
```
