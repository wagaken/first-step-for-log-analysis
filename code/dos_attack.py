def dos_attack(log, threshold=0.02):
    import matplotlib.pyplot as plt
    
    IP_sorted = IP_num(log, threshold)
    index, value, IP_request = IP_per_time(log)
    
    print_result(IP_sorted, index, value, len(log), threshold)
    
    #グラフを表示
    IP_request.plot()
    plt.show()
    plt.close()
    

def IP_per_time(log):
    import pandas as pd
    
    df = pd.DataFrame(log)
    IP = df['remote_host']
    IP.index = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
    
    #リクエストを1分ごとにカウント
    IP_request = IP.resample('T').count()
    IP_request_sorted = IP_request.sort_values(ascending=False)
    index = IP_request_sorted.index
    value = IP_request_sorted.values
    
    return index, value, IP_request
    

def IP_num(log, threshold):
    import collections
    
    IP = []
    for line in log:
        IP.append(line['remote_host'])
    
    #リクエスト数が多いIPアドレス順にソート
    IP_num = collections.Counter(IP)
    IP_sorted = IP_num.most_common()
    
    return IP_sorted


def print_result(IP_sorted, index, value, total, threshold):
    print()
    print('##----------------------DoS-------------------##\n')
    print('-------number of requests by IP-------')
    print('IP              | num   | ratio')
    for line in IP_sorted:
        IP_address = line[0]
        num = line[1]
        if num/total > threshold:
            percentage = '{:.2%}'.format(num / total)
            print(f'{IP_address:<15} | {num:<5} | {percentage:<5}')
        else:
            break
    print('-------------------------------------\n')
    print('----number of requests per minute----')
    print('datetime            | num   | ratio')
    for i in range(10):
        datetime = index[i]
        num = value[i]
        percentage = '{:.2%}'.format(num / total)
        print(f'{datetime} | {num:<5} | {percentage:<5}')
    print('-------------------------------------\n')
    print('##--------------------------------------------##\n')
    

