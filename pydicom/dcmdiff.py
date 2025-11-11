import difflib

from pydicom import examples

print(__doc__)

rep = []

#print(examples.mr)
temp = examples.mr

for ds in [examples.mr, examples.ct]:
    '''
    Loop through two examples - one an MRI and one a CT scan
    '''
    lines = str(ds).split('\n')
    lines = [line + '\n' for line in lines]
    rep.append(lines)

diff = difflib.Differ()
for line in diff.compare(rep[0], rep[1]):
    if(line[0] != '?'):
        print(line)


    
