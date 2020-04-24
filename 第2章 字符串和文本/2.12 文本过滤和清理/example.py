s = 'python\fis\tawesome\r\n'
remap = {
	ord('\t') : ' ',
	ord('\f') : ' ',
	ord('\r') : None  # Deleted
}
a = s.translate(remap)
print(a)    # python is awesome\n

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
						if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)   #  python is awesome\n

c = b.translate(cmb_chrs)
print(c)	#  python is awesome\n