s = 'My sName is Julia'

if 'Nama' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

# Конструкция 'Name' in s возвращает просто True или False, a find() возвращает индекс первого вхождения подстроки в строку и -1,
# если подстрока не найдена. Обычно в автотестах достаточно использовать in, потому что это более читабельный вариант.