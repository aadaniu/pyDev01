"""
split and interactively page a string or file of text
"""
def more(text, numlines=15):
    lines = text.splitlines() #  like split('\n') but no ''  at end，去除空行
    while   lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input('More?') not in ['y', 'Y']: break
#只有当该文件作为模块运行时，才会复制变量为__name__ == '__main__'
#模块被其它模块导入时，则不会执行
#from more import more
if __name__ == '__main__':
    import sys # when run, not imported
    more(open(sys.argv[1]).read(), 10) # page contents of file on cmdline
    
    
    
    
    
    