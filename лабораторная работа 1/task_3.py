size_disk_mb = 1.44 # Мб
page_book = 100
line_page = 50
simbol_line = 25
size_simbol_bt = 4 #байт

size_disk_bt = size_disk_mb * 1024 * 1024 #переводим размер диска из мегабайт в байты
size_book_bt = page_book * line_page * simbol_line * size_simbol_bt #вычисляем размер книги в байтах
count_book = round(size_disk_bt // size_book_bt) #вычисляем количество книг, помещающихся на дискету

print("Количество книг, помещающихся на дискету:", count_book)
