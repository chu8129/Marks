### 删除submodules问题
```
究竟多少人相互抄袭不确认的。。。一个git submodule遍地都是执行不下去，顺序有问题，mmp
注意顺序

To remove a submodule you need to:
1、Delete the relevant section from the .gitmodules file.
  Stage the .gitmodules changes git add .gitmodules
2、Delete the relevant section from .git/config.
3、Run git rm --cached path_to_submodule (no trailing slash).
4、Run rm -rf .git/modules/path_to_submodule (no trailing slash).
5、Commit git commit -m "Removed submodule "
6、Delete the now untracked submodule files rm -rf path_to_submodule
```

```
增加master分支
git submodule add  --force -b master git@git.***/commonproto.git commonproto
```


### 出现clone同步问题
```
# git clone https://huggingface.co/lmsys/vicuna-13b-delta-v0
Cloning into 'vicuna-13b-delta-v0'...
fatal: unable to access 'https://huggingface.co/lmsys/vicuna-13b-delta-v0/': gnutls_handshake() failed: Error in the pull function.


先检查网络，有可能是代理问题，先重试多几次
git config --global http.sslBackend openssl，可能不支持
git config --global http.sslBackend gnutls
```
### git branch问题
```
# git branch
error: cannot run less: No such file or directory
* main
# git config --global core.pager 'vim -'
#
```
