#######################################################
#
# COSC 140 Homework 3: URL checker
#
#######################################################

def urlchecker(url):
  begin = url.split('//')[0]
  if begin !='http:' and begin != 'https:':
    #print("orange")
    return False
  first_slash = url.split('//')[1]
  host_name = first_slash.split('/')[0]
  if host_name == ' ':
    #print("green")
    return False
  checker = ':'
  if checker in host_name:
    #print("purple")#checking for port
    port = host_name.split(':')[1]
    for char in port:
      if char.isdigit()!= True: 
        #print("blue")
        return False
      # if checker not in host_name:
      #   #print ("yes")
  if url.count('#') > 1 or url.count('?') > 1:
   # print("yellow")
    return False 
  if url.count('#') == 1 and url.count('?') == 1: 
    #print("red")
    result = url.find('#')
    resultII = url.find('?')
    if result > resultII:
      #print("aqua")
      return False
  if first_slash.count('/') < 1 : #or url.count(':')>1
    #print("black")
    return False 
  if first_slash.count('/') == 1 and first_slash.count(':') == 1: 
    #print("white")
    result = first_slash.find(':')
    resultII = first_slash.find ('/')
    if result > resultII: 
      #print("pink")
      return False
  if url.count(' ') > 0:
    #print("rose")
    return False
  return True  
  #Neeed to call Urls in order to check it
  #The ls needs to comehow be the URLS and then I need to check if thr http or https is in the URLS and then process that an if or else to continue to check it with the rest of the URL. 
  
    # your code should go here

  #return True

  
def testurl():
    urls = [ # valid
      ['https://example.com/', True],
      ['http://example.com/', True],
      ['http://example.com/?query', True],
      ['http://example.com/#fragment', True],
      ['http://example/', True],
      ['http://example/path/', True],
      ['http://example/path', True],
      ['https://example.com:3000/path#fragment?query', True],
      ['https://example.com/path#fragment?query', True],
      # invalid
      ['htt://example/', False],
      ['httpss://example/', False],
      ['https://example/:3000', False],
      ['https://example/?:3000?', False],
      ['https://example/?:3000#', False],
      ['https://example/xy z', False],
      ['https://example/xyz:', False],
      ['https://example', False],
    ]
    for url,expected in urls:
        if urlchecker(url) != expected:
            print(f"{url} is not valid, but your function claimed the opposite")
        else:
            print(f"{url} - ok")

testurl()