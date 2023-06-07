set ts=4
set nowrap
set nobackup
set nowritebackup
set noswapfile
set nu
set expandtab
let &termencoding=&encoding
set fileencodings=utf-8,gbk
colorscheme desert
syntax off 
filetype plugin on
"install vim-nox-py2 to suppoert py2 
autocmd FileType python set omnifunc=pythoncomplete#Complete
autocmd FileType JavaScript set omnifunc=javascriptcomplete#CompleteJS
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags
autocmd FileType css set omnifunc=csscomplete#CompleteCSS
autocmd FileType xml set omnifunc=xmlcomplete#CompleteTags
autocmd FileType PHP set omnifunc=phpcomplete#CompletePHP
autocmd FileType c set omnifunc=ccomplete#Complete

"auto indent
set autoindent

fun FileHeader()
    call setline(1, "#!/usr/bin/env python")
    call append(1, "# -*- coding: utf-8 -*-")
    call append(2, "") 
    call append(3, "") 
    call append(4, "__author__ = \"qwwang(mail:chu8129@gmail.com) @ " . strftime('%Y-%m-%d %T', localtime()) . "\"")
    normal G
    normal o
    normal o
endfun

autocmd bufnewfile *.py call FileHeader()

" modify the last modified time of a file
fun SetLastModifiedTime(lineno)
    let modif_time = strftime( '%a %b %d %H:%M:%S %Y', getftime(bufname('%')) )
    let line = '# Last Modified : '.modif_time
    if a:lineno == "-1"
        call setline(3, line)
    else
        call append(a:lineno, line)
    endif
endfun

map the SetLastModifiedTime command automatically
autocmd BufWrite *.py call SetLastModifiedTime(-1)
autocmd bufnewfile *.py call SetLastModifiedTime(-1)
