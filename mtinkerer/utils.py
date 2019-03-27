import sys

def dir_slash():
    slash = '/'
    if 'win' in sys.platform: slash = '\\'
    return slash
