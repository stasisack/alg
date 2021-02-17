import os
path = 'C:\учеба,работа'

def obxod(path, level = 1):
    print( 'Level', level, 'Context', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
           print('спускаемся', path +'\\'+i)
           obxod(path + '\\' + i, level+1)
           print('возращаемся в ', path )
obxod(path)
