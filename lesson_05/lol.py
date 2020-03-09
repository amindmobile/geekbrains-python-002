lol = [[0]*3]*3
print(lol)
fir, sec, thr = lol
fir[0] = 1
sec[1] = 2
thr[2] = 3
print(lol)


# old_print = print
# print_fd = open(...)
# def print(*args, *kwargs):
#     if 'file' in kwargs: return old_print(*args, **kwargs)
#     else: return old_print(*args, file=print_fd, **kwargs)
#
# Направит все принты в указанный файл, если параметр file не указан.
# Иными словами это весь вывод скрипта направит в файл