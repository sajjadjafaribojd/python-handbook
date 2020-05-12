import json

dns={ #this is a object
        "dns": [
            {
                "name": "@",
                 "ssl": "1|2|3",
                "status": "11|22|33",
                "ttl": "10|20|30",
                "type": "A",
                "value": "51.158.23.3|51.158.23.32|51.158.23.30"
            },
            {
                "name": "www",
                "ssl": "100|200",
                "status": "51|52",
                "ttl": "90|91",
                "type": "A",
                "value": "51.158.23.31|51.158.23.32"
            }
        ]
    }

final_dns=[]
array_len=len(dns["dns"]) #output =2
for i in range(array_len):
    value=dns["dns"][i]["value"]
    name=dns["dns"][i]["name"]
    ssl=dns["dns"][i]["ssl"]
    status=dns["dns"][i]["status"]
    type1=dns["dns"][i]["type"]
    ttl=dns["dns"][i]["ttl"]
  
    ip_list=value.split("|")
    ssl_list=ssl.split("|")
    ttl_list=ttl.split("|")
    status_list=status.split("|")
    for idx,item in enumerate(ip_list):
          #print(j,name)
        final_dns.append({"name":name,"ssl":ssl_list[idx],"status":status_list[idx],"ttl":ttl_list[idx],"type":type1,"value":item})
          
          
          
    
    
    #print(value,name)
obj={"dns":final_dns}   
    
value=dns["dns"][0]["value"]
ip=value.split("|") #output = 3
#print(array_len)

print(json.dumps(obj,indent=4))