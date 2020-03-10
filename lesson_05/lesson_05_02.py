# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file_to_work = 'lesson_05_02.txt'


def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line


lines, words, letters = 0, 0, 0
line_len = []

for line in read_lines(file_to_work):
    line_len.append(line.split(" "))
    lines += 1
    letters += len(line)
    words += len(line.split())
for line in line_len:
    print(f'В строке: "{" ".join(map(str, line)).rstrip()}" {len(line)} слов(а).')

print(f"Строк всего: {lines}")
print(f"Слов всего: {words}")
print(f"Букв всего: {letters}")
print(f"Всего всего: {letters + words + lines}")
