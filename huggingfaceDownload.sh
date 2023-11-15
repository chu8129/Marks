path=`realpath ./`
strings="from huggingface_hub import hf_hub_download, snapshot_download;snapshot_download(repo_id='${1}', force_download=True, resume_download=False, local_dir='${path}', cache_dir='${path}', local_dir_use_symlinks=False);"
echo ${strings}
`python -c "${strings}" `
