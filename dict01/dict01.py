#!/usr/bin/env python3

def main():
    ## create a dictionary
    switch = {'hostname': 'sw-01', 'ip': '10.0.0.1', 'version': 'cisco'}

    ## display parts of the dictionary
    print( switch['hostname'] )
    print( switch['ip'] )

    ## request a 'fake' key
    #print( switch['version'] )

    ## request a 'fake' key with .get() method
    print( "First test - .get()" )
    print( switch.get('lynx') )

    print( "Second test - .get()" )
    print( switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!") )

    print( "Third test - .get()" )
    print( switch.get('version') )
    
    print( "Fourth test - .get()" )
    print( switch.keys() )

    print( "Fifth test - .get()" )
    print( switch.values() )

    print( "Sixth test - .pop()" )
    switch.pop('version')
    print( switch.keys() )
    print( switch.values() )

    print( "Seventh test - ADD a new value" )
    switch['adminlogin'] = 'karl08'
    print( switch.keys() )
    print( switch.values() )

    print( "Eighth test - ADD a new value" )
    switch['password'] = 'qwrety'
    print( switch.keys() )
    print( switch.values() )

main()

