try:
    text = input('enter something')
except EOFError:
     print('why did you do an EOF on me?')
except KeyboardInterrupt:
     print('you canelled the operation')
else:
     print('you entered {0}'.format(text))