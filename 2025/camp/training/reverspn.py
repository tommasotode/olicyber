bs = '''63



7C



77



7B



F2



6B



6F



C5



30



01



67



2B



FE



D7



AB



76



CA



82



C9



7D



FA



59



47



F0



AD



D4



A2



AF



9C



A4



72    r



C0



B7



FD



93



26    &



36    6



3F    ?



F7



CC



34    4



A5



E5



F1



71    q



D8



31    1



15



04



C7



23    #



C3



18



96



05



9A



07



12



80



E2



EB



27    '



B2



75    u



09



83



2C    ,



1A



1B



6E    n



5A    Z



A0



52    R



3B    ;



D6



B3



29    )



E3



2F



84



53    S



D1







ED



20     



FC



B1



5B    [



6A    j



CB



BE



39    9



4A    J



4C    L



58    X



CF



D0



EF



AA



FB



43    C



4D    M



33    3



85



45    E



F9



02



7F



50    P



3C    <



9F



A8



51    Q



A3



40    @



8F



92



9D



38    8



F5



BC



B6



DA



21    !



10



FF



F3



D2



CD



0C



13



EC



5F    _



97



44    D



17



C4



A7



7E    ~



3D    =



64    d



5D    ]



19



73    s



60    `



81



4F    O



DC



22    "



2A    *



90



88



46    F



EE



B8



14



DE



5E    ^



0B



DB



E0



32    2



3A    :



0A



49    I



06



24    $



5C



C2



D3



AC



62    b



91



95



E4



79    y



E7



C8



37    7



6D    m



8D



D5



4E    N



A9



6C    l



56    V



F4



EA



65    e



7A    z



AE



08



BA



78    x



25    %



2E    .



1C



A6



B4



C6



E8



DD



74    t



1F



4B    K



BD



8B



8A



70    p



3E    >



B5



66    f



48    



03



F6



0E



61    a



35    5



57    W



B9



86



C1



1D



9E



E1



F8



98



11



69    i



D9



8E



94



9B



1E



87



E9



CE



55    U



28    (



DF



8C



A1



89



0D



BF



E6



42    B



68    



41    A



99



2D    -



0F



B0



54    T



BB



16'''

a = [0, 4, 6, 2, 5, 1, 3, 7]

b = []
for i in bs.split('\n\n\n\n'):
    b.append(int.from_bytes(bytes.fromhex(i[:2].lower())))

key = 0xDEADBEEFCAFEBABE

enc_flag = bytes.fromhex("613D9554F622DB60BDF86C1FD986743D70F80816D9616555E88C161DA708640C7E1F2A289B3ABD4EF85DAE164114BD0A")

def invperm(perm):
    inv = [0] * len(perm)
    for j, i in enumerate(perm):
        inv[i] = j
        
    return inv

def invtable(subst):
    inv = [0] * len(subst)
    for i, val in enumerate(subst):
        inv[val] = i

    return inv

inv_a = invperm(a)
inv_b = invtable(b)

def revtransfblock(out_block):
    out_bytes = list(out_block)
    c = [inv_b[b_val] for b_val in out_bytes]
    tmp_b = [ c[a[j]] for j in range(8) ]
    tmp_int = int.from_bytes(bytes(tmp_b), byteorder='little')
    orig_int = tmp_int ^ key

    return orig_int.to_bytes(8, byteorder='little')

def revtransf(enc_flag):
    orig = bytearray()
    for i in range(6):
        block = enc_flag[i*8:(i+1)*8]
        orig_block = revtransfblock(block)
        orig.extend(orig_block)

    return bytes(orig)


flag = revtransf(enc_flag)
print(flag.decode())