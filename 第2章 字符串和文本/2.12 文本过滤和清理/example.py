s = 'python\fis\tawesome\r\n'
remap = {
	ord('\t') : ' ',
	ord('\f') : ' ',
	ord('\r') : None  # Deleted
}
a = s.translate(remap)
print(a)    # python is awesome\n