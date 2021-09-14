#1/usr/bin/env python3

def main():
    # below is a lists of lists containing the drivers needed to connect to 
    # the switch ip address

    networklists = [['ios', '10.0.2.1'],['ios-xr', '10.0.55.1'], ['eos', '10.0.14.1']]

    for driveandip in networklists:
        print('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])

main()
