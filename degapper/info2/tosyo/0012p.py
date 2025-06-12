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