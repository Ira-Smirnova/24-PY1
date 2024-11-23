def count_letters(some_text):
    work_text = ''.join(some_text.lower().split())
    dict_letters = {}
    for simbol in work_text:
        if simbol.isalpha():
            if dict_letters.get(f'{simbol}') != None:
                current_value = dict_letters.get(f'{simbol}')
                dict_letters[f'{simbol}'] = current_value + 1
            else:
                dict_letters[f'{simbol}'] = 1
    return dict_letters



def calculate_frequency(count_letters_dict):
    common_count_letters = 0
    frequency_letters_dict = {}
    for counts in count_letters_dict.values():
        common_count_letters += counts
    for letter, letter_count in count_letters_dict.items():
        letter_frequency = letter_count / common_count_letters
        frequency_letters_dict[f'{letter}'] = letter_frequency
    return frequency_letters_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

main_str_count_letters = count_letters(main_str)
for letter, frequency in calculate_frequency(main_str_count_letters).items():
   print(f'{letter}: {frequency:.2f}')

