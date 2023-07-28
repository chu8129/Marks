#### Cannot update while running on a read-only volume
```
理解
  mac的安全机制问题
sudo chown $USER ~/Library/Caches/com.microsoft.VSCode.ShipIt/*
xattr -dr com.apple.quarantine /Applications/Visual\ Studio\ Code.app
```
