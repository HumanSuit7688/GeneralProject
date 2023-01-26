from aiogram import Dispatcher, types
from Fonetic.Modules.func_back_end import sound_count, every_let, list
from Fonetic.Modules.info_back_end import special_vowels, vowels


async def cmd_start(msg: types.Message):
    await msg.answer("Привет, я могу сделать тебе фонетический разбор слова\n"
                     "Используй команду '/f', напиши своё слово через пробел и еще через пробел n-ый ударный слог\n"
                     "Пример: '/f слово n'")


async def cmd_fonetic(msg: types.Message):
    hit = int(msg.text[-1:])
    word = msg.text[3:-2]
    word_list = list(word)
    await msg.answer(f'{word} - {sound_count(word_list)}')
    ev_let = every_let(word_list, hit)
    output = ''
    try:
        index = 0
        for p in ev_let:
            if p[0] in special_vowels:
                if p[0] in special_vowels and p[1] in vowels:
                    output += (f'{p[0]} - [{p[1]}] - {p[2]}{p[3]}\n')
                elif p[0] in special_vowels:
                    x = f'{p[0]} - '
                    for d in p[1]:
                        x += d
                    output += (f'{x}\n')
                    output += (f'   - {p[2]}{p[3]}{p[4]}\n')
            else:
                y = ''
                for a in p:
                    y += a
                output += (f'{y}\n')
            index += 1
    except:
        pass
    await msg.answer(output)


def register_handlers_fonetic(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_fonetic, commands='f')
