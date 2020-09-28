```
究竟多少人相互抄袭不确认的。。。一个git submodule遍地都是执行不下去，顺序有问题，mmp
To remove a submodule you need to:
Delete the relevant section from the .gitmodules file.
Stage the .gitmodules changes git add .gitmodules
Delete the relevant section from .git/config.
Run git rm --cached path_to_submodule (no trailing slash).
Run rm -rf .git/modules/path_to_submodule (no trailing slash).
Commit git commit -m "Removed submodule "
Delete the now untracked submodule files rm -rf path_to_submodule
```


```
增加master分支
git submodule add  --force -b master git@git.***/commonproto.git commonproto
```
