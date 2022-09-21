from os import popen

def terminal(KEY, symbol, v): return popen(f'echo \'{KEY}{symbol}{v}\' | bc').read().strip()

def fac(n): return 1 if n == 0 else fac(n-1) * n

def filter(fill,ASKEY,cipher): 
    if ( f := ''.join(fill[-1:]) ) in cipher and cipher[f] != 0: cipher[f]=cipher[f]-1
    cipher = ''.join([ k*v for k,v in cipher.items() ])
    D = len(cipher)
    return cipher[int( terminal(terminal(terminal(ASKEY,'*',D),'/',fac(D)),'%',D) )]

def token(ASKEY,cipher): 
    fill=[] 
    ciph = dict(sorted({k:cipher.count(k) for k in set(cipher)}.items())) 
    [ fill.append( filter(fill,ASKEY,ciph) ) for _ in cipher ] 
    return ''.join(fill)

def assort(cipher):
    ASKEY = 0
    abc = ''.join(sorted(cipher))
    def check(cipher,ASKEY,abc,i): return terminal(ASKEY, '+', ((abc.index(cipher[i],i)-i)*fac(dpf:=len(cipher)-i)/dpf) )
    for i in range(len(cipher)): 
        print( '#', i, ' ', abc, "|", cipher, ' @ ', ASKEY )
        ASKEY = check(cipher,ASKEY,abc,i)
        abc = token(ASKEY,cipher)
    return int(float(ASKEY))

def algorism(dec, sys):
    sign = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if sys > len(sign): return print('ERROR: The \'algorism\' function doesn\'t accept a second parameter greater than 36.')
    def logic(dec): return ''.join([sign[(dec//(sys**div))%sys] for div in range(5*len(str(dec)),-1,-1)])
    def removeExtraZero(out):
        for k in out:
            if k=='0': out= out.replace('0','',1)
            else: break
        return out if out !='' else '0'
    return removeExtraZero(logic(dec))

def prime():
    keys = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
    type = {i:0 for i in set(keys)}
    values = [2,3,5,7]
    d = 1
    while len(values) < len(keys): [ [ (values.append(num) if num not in values and [num%p==0 for p in values].count(True)==0 else None) for num in [(10*d)+1,(10*d)+3,(10*d)+7,(10*d)+9] ] ] ; d+=1
    for k,v in zip(keys,values[0:len(keys)]): type[k]+=v
    return type

def scrambler(enContent, dct): 
    SCKEY = 1
    reqDict = {}
    for k in enContent: reqDict[k] = { 'ident':dct[k], 'score':1 if k not in reqDict else reqDict[k]['score']+1 }
    for v in list(reqDict.values()): SCKEY *= v['ident']**v['score']
    return SCKEY

def decoder(dct, SCKEY):
    deContent = ''
    for k,v in dct.items():
        while True:
            if terminal(SCKEY, '%', v) == '0':
                deContent += k
                SCKEY = terminal(SCKEY, '/', v)
            if terminal(SCKEY, '%', v) != '0': break
    return ''.join(sorted(deContent))

if __name__ == "__main__":

    dct = prime()
    enContent = 'HOWDY DEAR GUEST' # LETS BE FRIENDS AND DO GOOD
    ASKEY = assort(enContent)
    SCKEY = scrambler(enContent, dct)
    deContent = token( ASKEY, decoder(dct, SCKEY) )

    print( f'We get 🔑 ({algorism(sys=36, dec=SCKEY)}) by encrypting this data: <{enContent}>' )
    print( f'We get 🔑 ({algorism(sys=36, dec=ASKEY)}) which is needed for the correct character order of the received data!')
    print( f'Decrypting 🔑, we get the following data: <{deContent}>' )