def first_string(s):
  index = 0
  for i in range(len(s) -1, 0, -1):
    if s[i-1] != s[i]:
      index = i
      break
  
  new_s = ''
  for i in range(0, index):
    if s[i] <= s[i+1]:
      new_s += s[i]*2
    else:
      new_s += s[i]
  
  return new_s + s[index:]

def show_result(num, list_of_input):
  for i in range(num):
    print('Case #{}: {}'.format(i+1, first_string(list_of_input[i]), end='\n'))

if __name__ == '__main__':
  num = int(input())
  str_list = []
  for i in range(num):
    str_list.append(raw_input())
  show_result(num, str_list)