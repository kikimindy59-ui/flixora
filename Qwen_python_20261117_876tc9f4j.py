# Check for accidental replacement inside identifiers or strings
print('bad id?', 'renderHistory()' in open(base+'/index.html').read())
print('history back intact', "history.length>1?history.back()" in s)
print('S.history intact', 'S.history' in s)
 # Result execute error ```