counter = 0
ip_list = []

with open('www.trendybelly.com.log') as file:
    f = open('request_500.txt', 'a')
    for line in file:
        line = line.strip()
        parsed_line = line.split()
        ip = parsed_line[0]
        status_code = parsed_line[8]
        request = parsed_line[5]
        if ip not in ip_list:
            ip_list.append(ip)
        if status_code == '500':
            f.write(line + '\n')
        elif status_code == '200' and 'GET' in request:
            counter += 1
    f.close()
print(counter)
print(', '.join(ip_list))
