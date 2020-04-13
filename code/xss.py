def xss(log):
    keywords = [
        'script>', 'script&gt;',
        '<img', '&lt;img',
        '<div', '&lt;div',
        '<iframe', '&lt;iframe', 
        '<object', '&lt;object',
        '<a', '&lt;a',
        '<style', '&lt;style',
        '<link', '&lt;link',
        '<body', '&lt;body'
     ]
    
    keywords_in_line = [0 for i in range(len(log))]
    
    for i in range(len(log)):
        for j in range(len(keywords)):
            if keywords[j] in log[i]['request_url'].lower():
                keywords_in_line[i] += 1
    
    xss_log = {}
    for i in range(len(log)):
        if keywords_in_line[i] != 0:
            xss_log[i] = keywords_in_line[i]
    
    xss_log_sorted = sorted(xss_log.items(), key=lambda x:x[1], reverse=True)
    
    print()
    print('##--------XSS--------##')
    print(f'total : {len(xss_log)}\n')
    print('n   | hit | request_url')
    i = 1
    for element in xss_log_sorted:
        num = element[1]
        index = element[0]
        output_url = log[index]['request_url']
        print(f'{i:<3} | {num:<3} | {output_url}')
        i += 1
    print('##-------------------##')

