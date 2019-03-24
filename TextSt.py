from fuzzywuzzy import fuzz
import fuzzywuzzy
import dict, re, xlrd, xlwt, fuzzy_search


# ЗАМЕНА ПО НЕЧЁТКОМУ ПОИСКУ
def fuzzy_replace(str_a, str_b, orig_str):
    length = len(str_a.split())
    splitted = orig_str.split()
    for i in range(len(splitted) - length + 1):
        test = " ".join(splitted[i:i + length])
        if fuzzy_search.fsearch(str_a, orig_str) > 75:
            before = " ".join(splitted[:i])
            after = " ".join(splitted[i + 1:])
            return before + " " + str_b + " " + after


# ОТКРЫТИЕ ФАЙЛА И ЗАПОЛНЕНИЕ СПИСКА ЗНАЧЕНИЯМИ
def fileopen():
    sheet = xlrd.open_workbook('input.xlsx').sheet_by_index(0)
    number = [int(sheet.row_values(rownum)[0]) for rownum in range(1, sheet.nrows)]
    values = [re.sub('\s+', ' ',
                     sheet.row_values(rownum)[1].strip().replace('.', '').replace(',', '').replace(
                         '\n', ' ').replace(' ', '').lower()) for rownum in range(1, sheet.nrows)]
    return number, values


number, values = fileopen()
dict = dict.main()
wb = xlwt.Workbook()
ws = wb.add_sheet('Список операций')

for i in range(len(values)):
    x = values[i]
    for key in dict:
        if fuzzy_search.fsearch(key, x):
            x = re.sub(dict[key][0], dict[key][1], x.replace('маш', 'м'))
    ws.write(i, 0, number[i])
    ws.write(i, 1, x)

wb.save('output.xls')
