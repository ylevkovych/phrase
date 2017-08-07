'''
exception helper
'''

def prn(e):
    '''
    print exception info
    '''

    if (e):
        print('Exception occured:')

    for info in e:
        print ('\t',info)