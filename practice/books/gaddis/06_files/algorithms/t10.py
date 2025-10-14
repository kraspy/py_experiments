try:
    х = float('abc123')
    print(х)
except IOError:
    print('Этот программный код вызвал ошибку IOError. ')
except ZeroDivisionError:
    print('Этoт программный код вызвал ошибку ZeroDivisionError. ')
except:
    print('Произошла ошибка.')
    print('Конец.')
