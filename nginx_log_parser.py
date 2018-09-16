counter=0
ip_list=[]

with open('www.trendybelly.com.log') as file:
    for line in file:
        line=line.strip()
        ip_list.append(line[:line.find(' [')])
        left_request_name=line.find('"')+1
        right_request_name=line.find(' /')
        name_request=line[left_request_name:right_request_name]
        left_status_code=line.find('HTTP/1.1" ')+10
        right_status_code=line.find('HTTP/1.1" ')+13
        name_status_code=line[left_status_code:right_status_code]
        if name_status_code=='500':
            with open('requests_500.txt','a') as f:
                f.write(line+'\n')
        elif name_status_code=='200' and name_request=='GET':
            counter+=1
print(counter)
print(*set(ip_list),sep=', ')

    
                         
                 

