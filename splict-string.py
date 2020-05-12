import re

txt=" nignx, config error "
result=txt.split()
print(result) #['nignx', 'config', 'error']

ipPattern=re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

value="51.158.23.31|51.158.23.32|51.158.23.33"
value2="51.158.23.31@"
ips=value.split("|")
#print(type(ip)) #output list

def checkIP(ips):
    cnt=1
    for ip in ips:
        
        print(ip)
        if ipPattern.match(ip):
            print(cnt)
            if  cnt==len(ips):
                print(cnt)
                return True,""
        else:
            return False,"A record value most be ip address"
        cnt=cnt+1
print(checkIP(ips))