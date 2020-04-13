import codecs

def set_url(request, start_index, end_index):
    url = ''
    if len(request) == 3:
        url = request[1]
    elif len(request) == 2:
        for i in range(start_index, end_index):
            url = url + request[i]
    elif len(request) == 1:
        url = request[0]
    else:
        for i in range(start_index, end_index):
            if i != end_index:
                url = url + request[i] + ' '
            else:
                url = url + request[i]
    
    return url
        
def apache_parser(file_name='access_log'):
    with codecs.open(file_name, 'r', 'utf-8', 'ignore') as f:
        log = []
        trash = []
        
        method_type = [
        'GET', 'get', 'PROPFIND', 'OPTIONS', 'SEARCH', 
        'CONNECT', 'HEAD', 'PUT', 'TRACE', 'TRACK', 'POST'
        ]
        
        protocol_type = ['HTTP/1.0','HTTP/1.1']
        
        for line in f:
            try: 
                insert = {}
            
                #タイムゾーン、remote_user, remote_logは取り除く 
                entry = line.split(' ', 5)
                insert['remote_host'] = entry[0]
                insert['time'] = entry[3].lstrip('[')
                 
                #ダブルクウォーテーション区切りで%rを抽出
                rest_entry = entry[5]
                start = rest_entry.find('"')
                double_quotation = rest_entry.count('"') - 6
                if double_quotation > 0:
                    pre_end = start
                    for i in range(double_quotation + 1):
                        end = rest_entry[pre_end+1:].find('"') + pre_end + 1
                        pre_end = end
                else:
                    end = rest_entry[start+1:].find('"') + 1 
                
                #%rをmethod, request_url, protocolに分割
                request = rest_entry[start+1:end].split()
                if request[0] in method_type:
                    if request[-1] in protocol_type:
                        insert['method'] = request[0]
                        insert['request_url'] = set_url(request, 1, len(request)-1)
                        insert['protocol'] = request[-1]
                    else:
                        #プロトコルが欠損
                        insert['method'] = request[0]
                        insert['request_url'] = set_url(request, 1, len(request))
                        insert['protocol'] = '-'
                else:
                    if request[-1] in protocol_type:
                        #メソッドが欠損
                        insert['method'] = '-'
                        insert['request_url'] = set_url(request, 0, len(request)-1)
                        insert['protocol'] = request[-1]
                    else:
                        #メソッドとプロトコルが欠損
                        insert['method'] = '-'
                        insert['request_url'] = set_url(request, 0, len(request))
                        insert['protocol'] = '-'
                
                response_byte = rest_entry[end+2:].split()
                insert['response_code'] = response_byte[0]
                insert['byte'] = response_byte[1]
                insert['referer'] = rest_entry.rsplit('"', 4)[1]
                insert['user_agent'] = rest_entry.rsplit('"', 4)[3]
               
                log.append(insert)
            except:
                #フォーマットに合わないもの
                trash.append(line)

    print('##------------parse-------------##')
    print('------------result----------')
    print(f'parsed log     : {len(log)}')
    print(f'non-parsed log : {len(trash)}')
    print('----------------------------\n')
    print('--------cannot parse--------')
    for i in range(len(trash)):
        print(trash[i])
    print('----------------------------\n')
    print('##------------------------------##\n')
    
    return log, trash
      