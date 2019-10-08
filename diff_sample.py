import difflib
import sys

try:
    text_file1=sys.argv[1]
    text_file2=sys.argv[2]
except Exception as e:
    print('Error'+str(e))
    print('Usage:diff_sample.py filename1 filename2')
    sys.exit()

def readline(filename):       #文件读取分隔函数
    try:
        fileHandle=open(filename,'r')
        text=fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as e:
        print('Read file Error:'+str(e))
        sys.exit()

if text_file1== " " or text_file2=="":
    print('Usage:diff_sample.py filename1 filename2')
    sys.exit()

text1_lines=readline(text_file1)
text2_lines=readline(text_file2)

d=difflib.HtmlDiff()
print(d.make_file(text1_lines,text2_lines))

