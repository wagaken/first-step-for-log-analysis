def csrf(log):
    import collections

    RF = []
    for element in log:
        RF.append(element['referer'])
        
    RF_count = collections.Counter(RF)
    RF_count_sorted = sorted(RF_count.items(), key=lambda x:x[1], reverse=True)
    
    print('##------------------CSRF------------------##\n')
    print('----------referer count----------')
    print('{:<70} | {:<6}'.format('referer','count'))
    total = len(log)
    for key,value in RF_count_sorted:
        print(f'{key:<70} | {value:<6}')
    print('---------------------------------\n')
    
    print('search request.\ninput referer.\n')
    search_referer = input()
    
    request = []
    IP = []
    for element in log:
        if element['referer'] == search_referer:
            request.append(element['request_url'])
            IP.append(element['remote_host'])
    
    request_count = collections.Counter(request)
    IP_count = collections.Counter(IP)
    request_count_sorted = sorted(request_count.items(), key=lambda x:x[1], reverse=True)
    IP_count_sorted = sorted(IP_count.items(), key=lambda x:x[1], reverse=True)
    
    print('----------request count----------')
    print('{:<70} | {:<6}'.format('request_url','count'))
    print_result(request_count_sorted)
    print('---------------------------------\n')
    print('-------------IP count------------')
    print('{:<70} | {:<6}'.format('IP','count'))
    print_result(IP_count_sorted)
    print('---------------------------------\n')
    print('##----------------------------------------##\n')
    
    

def print_result(count_sorted):
    i = 0
    for key,value in count_sorted:
        if i > 10: break
        print(f'{key:<70} | {value:<6}')
        i += 1
    