#!/bin/sh
path=$1
echo "start check..."
find $path -name '*.py' -not -name '*_pb2*.py' |xargs -P 2 -i isort  -fss -sl {}
find $path -name '*.py' -not -name '*_pb2*.py' |xargs -P 2 -i black -q -l 120 {}
find $path -name '*.py' -not -name '*_pb2*.py' |xargs -P 2 -i pylint -j 0 --rcfile=.pylintrc {}
find $path -name '*.py' -not -name '*_pb2*.py' |xargs -P 2 -i flake8 --config=.flake8 --statistics {}

#.flake8
#[flake8]
#ignore=E203,E501,W503,F401,F403,F811,F82,F841,N801,N802,N803,N806,F841,F403,F401,F811

#.pylintrc
#[MESSAGES CONTROL]
#disable=all
#enable=unused-import,
#       import-error,
#       ungrouped-imports,
#       wrong-import-order,
#       unused-variable,
#       #no-else-return,
#       #simplifiable-if-statement
## model 是第三方私有库
## TODO missing requirements ???
#ignored-modules=model,
#                leveldb,
#                lib.task_id
