a='http://www.example.com/test?p=1&q=2'
protocol=a.split('://')
host=protocol[1].split('/')[0]
others=protocol[1].split('/')[1]
print('protocol: {0}'.format(protocol[0]))
print('host: {0}'.format(host))
print('others: {0}'.format(others))