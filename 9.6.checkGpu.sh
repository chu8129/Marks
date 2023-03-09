python -c 'import torch;print(torch.device("cuda" if torch.cuda.is_available() else "cpu"))'
python -c 'import tensorflow as tf;print(tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None))'
