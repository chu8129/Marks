dd if=/dev/zero of=./test.iso bs=1024M count=1
dd if=/root/autodl-fs/qwcache/testfile of=/dev/null bs=1G count=1 iflag=direct
dd if=/dev/zero of=/root/autodl-fs/qwcache/testfile bs=1G count=1 oflag=direct
