set ts=4
set nu
set expandtab
set encoding=utf-8
set termencoding=utf-8
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
colorscheme desert
syntax on
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
    call append(5, "") 
    call append(6, "") 
    call append(7, "import logging")
    call append(8, "logger = logging.getLogger(\"root\")")
    call append(9, "") 
    call append(10, "filename=\"\"")
    call append(11, "lines = [line.strip(\"\\n\").split(\"\\t\") for line in open(filename).readlines()]")
    call append(12, "") 
    call append(13, "def deal(line):")
    call append(14, "") 
    call append(15, "") 
    call append(16, "") 
    call append(17, "with open(filename.rsplit(\".\")[0] + \"_format_result.tsv\", \"w\") as fw:")
    call append(18, "    [fw.write(\"\\t\".join(map(lambda s: s.replace(\"\\t\", \" \"), deal(line))) + \"\\n\") for line in lines]")
    normal G
    normal o
"    normal o
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
" autocmd BufWrite *.py call SetLastModifiedTime(-1)
" autocmd bufnewfile *.py call SetLastModifiedTime(-1)
