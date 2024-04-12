repoid=${1}
path=`realpath ./${2}`
filename=${3}
repoType=${4}
echo $path
strings="from huggingface_hub import hf_hub_download, snapshot_download;snapshot_download(token='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', repo_type='${repoType}', repo_id='${repoid}', force_download=False, resume_download=False, local_dir='${path}', cache_dir='${path}', local_dir_use_symlinks=False, allow_patterns='${filename}');"
echo ${strings}
export HF_ENDPOINT=https://hf-mirror.com
`python -c "${strings}" `

# bash **download.sh repoid repoid "*" model/data
