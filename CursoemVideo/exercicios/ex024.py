cid = str(input('Digite o nome de uma cidade: ')).strip()
cid = cid.upper()
if(cid.find('SANTO') == 0):
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')