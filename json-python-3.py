import json

dns= [ #this is a list or array
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
    

def split_ip_func(dns):
    final_dns=[]
    array_len=len(dns) #output =2
    for i in range(array_len):
        value=dns[i]["value"] #ip for e.g: 51.158.23.31|51.158.23.32
        name=dns[i]["name"] # www or @
        ssl=dns[i]["ssl"] if "ssl" in dns[i] else "0" # 0 or 1
        status=dns[i]["status"] if "status" in dns[i] else "0" # 0 or 1 
        type1=dns[i]["type"] # A or Cname
        ttl=dns[i]["ttl"] if "ttl" in dns[i] else "60" # 60
    
       
        ip_list=value.split("|")
        ssl_list=ssl.split("|")
        ttl_list=ttl.split("|")
        status_list=status.split("|")
        
        for idx,item in enumerate(ip_list):
            
            """
            print(j,name) 
            output:
            51.158.23.3 @
            51.158.23.32 @
            51.158.23.30 @
            51.158.23.31 www
            51.158.23.32 www
            
            """
            final_dns.append({"name":name,"ssl":ssl_list[idx],"status":status_list[idx],"ttl":ttl_list[idx],"type":type1,"value":item})
            
    return final_dns          
          
          
    
    
    #print(value,name)
obj={"dns":split_ip_func(dns)}   
    
#value=dns["dns"][0]["value"]
#ip=value.split("|") #output = 3
#print(array_len)
print(split_ip_func(dns))
#print(json.dumps(obj,indent=4))