a = 'A'
b = 'B'
c = 1.1

#formato = 'a={} b={} c={}'.format(a, b, c)

#mesma coisa apaenas usando outra forma
string = 'b={nome2} a={nome1} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)