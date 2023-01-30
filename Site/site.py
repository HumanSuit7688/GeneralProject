import flet as ft
from Fonetic.Modules.func_back_end import sound_count, list, every_let
from Fonetic.Modules.info_back_end import special_vowels, vowels


def fonetic(page: ft.Page):
    # page.title('Fonetic')

    def main_func(e):
        word = prompt.value[:-2]
        hit = int(prompt.value[-1:])
        word_list = list(word)
        amount_sl = sound_count(word_list)
        main_sl = every_let(word_list, hit)
        output = ''
        try:
            index = 0
            for p in main_sl:
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

        word_text.value = (f'{amount_sl}\n'
                           f'{output}')
        page.update()

    prompt = ft.TextField(hint_text='Ваше слово', shift_enter=True, on_submit=main_func)
    word_text = ft.Text(size=24, value=f'')

    x = ft.Column(controls=[
        ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
            ft.Text(size=20, value='Привет, я могу сделать для тебя фонетический разбор слова!\n'
                    'Тебе нужно написать слово с маленькой буквы и через пробел номер ударного слога\n'
                    'Вот так: "слово n"')
        ]),
        ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
            prompt,
            ft.ElevatedButton(text='>>',
                              on_click=main_func,
                              )
        ]),
        ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
            word_text
        ])
    ])
    page.add(x)
    page.update()


ft.app(target=fonetic, view=ft.WEB_BROWSER)
