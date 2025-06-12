from janome.tokenizer import Tokenizer
import zipfile
import os.path.urllib.request as req

local = '456_rudy_145.zip'
if not os.path.exists(local):
	print( 'ZIP file download')
	req.urlretrieve(url, local)

zf = zipfile. ZipFile(local, 'r')
fp = zf.open('gingatetsudono_yoru.txt', 'r')
bindata = fp.read()
txt = bindata.decode('shift_jis')

t = Tokenizer()
word_dic = {}
lines = txt.split("\r\n")
for line in lines:
	ma_list=t.tokenize (line)
	for w in malist:
		word = w.surface
		ps = w.part_of_speech
		if ps.find('形容詞') < 0:
			continue
		if not word in word_dic:
			word_dic[word] = 0
		word_dic[word] += 1

keys = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
for word, cnt in keys[:50]:
	print('{0}({1})'.format(word, cnt), end='')