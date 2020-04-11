def check_request(log):

    method_type = [
        'GET', 'get', 'PROPFIND', 'OPTIONS', 
        'SEARCH', 'CONNECT', 'HEAD', 'PUT', 
        'TRACE', 'TRACK', 'POST'
        ]
    
    protocol_type = ['HTTP/1.0', 'HTTP/1.1']
    
    method = []
    url = []
    protocol = []
    
    for element in log:
        request = element['request'].split()
        check_entry = [
            request[-1], element['response_code'], 
            element['byte'], element['referer'], element['user_agent']
            ]
        if request[0] not in method_type:
            method.append(element)
        if request[-1] not in protocol_type:
            url.append(element)
        
        flag = False
        for i in range(len(protocol_type)):
            for j in range(len(check_entry)):
                if protocol_type[i] in check_entry[j]:
                    flag = True
                    continue
        
        if not flag:
            protocol.append(element)
    
        
    print('##-----------欠損データ---------##')
    print(f'Total       : {len(method) + len(url) + len(protocol)}')
    print(f'HTTP method : {len(method)}')
    print(f'URL         : {len(url)}')
    print(f'Protocol    : {len(protocol)}\n')
    print('-----missing method-----')
    print_result(method)
    print('-------missing url------')
    print_result(url)
    print('##------------------------------##\n')
    
    
def print_result(type):
    for i in range(len(type)):
        line = type[i].values()
        output = ''
        count = 0
        for parts in line:
            if count < 4: 
                count += 1
                continue
            output += parts
            output += ' '
        print(output)
    print('------------------------\n')

    
from apache_parser import apache_parser
log,trash = apache_parser()
check_request(log)
