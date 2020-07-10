import telnetlib

def checkproxy(ip,port):
    try:
        telnetlib.Telnet(ip, port=port, timeout=4)
        print(ip+':'+port+'有效')
        return True
    except:
        print(ip+':'+port+'无效')
        return False

