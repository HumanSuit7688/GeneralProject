import config
import asyncio
from aiogram import Bot, Dispatcher, types
from Fonetic.Handlers.fonetic import register_handlers_fonetic


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def main():
    register_handlers_fonetic(dp)
    await dp.skip_updates()
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())




# word = input()
# word_list = list(word)
#
# print(sound_count(word_list))
# ev_let = every_let(word_list, 2)
# index = 0
# for p in ev_let:
#     if p[0] in special_vowels:
#         if p[0] in special_vowels and p[1] in vowels:
#             print(f'{p[0]} - [{p[1]}] - {p[2]}{p[3]}')
#         elif p[0] in special_vowels:
#             x = f'{p[0]} - '
#             for d in p[1]:
#                 x += d
#             print(x)
#             print(f'  - {p[2]}{p[3]}{p[4]}')
#     else:
#         y = ''
#         for a in p:
#             y += a
#         print(y)
#     index += 1
#
