
TMPDIR=/dev/shm pip3 install --cache-dir=/dev/shm -U torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cu121
TMPDIR=/dev/shm pip3 install --cache-dir=/dev/shm -U pip install vllm==0.4.1
TMPDIR=/dev/shm pip3 install --cache-dir=/dev/shm -U git+https://github.com/huggingface/transformers.git
TMPDIR=/dev/shm pip3 install --cache-dir=/dev/shm -U git+https://github.com/huggingface/peft.git
TMPDIR=/dev/shm pip3 install --cache-dir=/dev/shm -U git+https://github.com/Dao-AILab/flash-attention.git --no-build-isolation
