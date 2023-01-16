from info_back_end import vowels, consonants, nn_let, special_vowels, spec_vow_key, voice_cons, vo_co_double, vo_co_undouble, dull_cons, du_co_double, du_co_undouble


def list(word):
    word_list = []
    x = 0
    for l in word:
        word_list.append(word[x])
        x += 1
    return word_list


def sound_count(word_list):
    sound_quant = 0
    letter_quant = len(word_list)
    index = 0
    for i in word_list:
        if i in consonants:
            sound_quant += 1
        elif i in vowels:
            if i in special_vowels:
                if index == 0:
                    sound_quant += 2
                elif index > 0:
                    index_let = word_list.index(i, index)
                    if word_list[index_let - 1] in nn_let or word_list[index_let - 1] in vowels:
                        sound_quant += 2
                    elif word_list[index_let - 1] in consonants:
                        sound_quant += 1
            else:
                sound_quant += 1
        elif i in nn_let:
            pass
        index += 1
    result = f'{letter_quant} букв и {sound_quant} звуков'
    return result


def every_let(word_list, hit):
    index_v = 0
    snd = []
    index = 0
    for s in word_list:
        snd1 = []
        if s in consonants:
            snd1.append(s)
            snd1.append(f'[{s}]')
            snd1.append('согласный, ')
            if s in voice_cons:
                if s in vo_co_double:
                    snd1.append('звонкиий (парный), ')
                    if s == 'ш' or s == 'ж' or s == 'ц':
                        snd1.append('твёрдый (непарный), ')
                    elif s == 'щ' or s == 'ч' or s == 'й':
                        snd1.append('мягкий (непарный), ')
                        snd1[1] = f"[{s}']"
                    elif index == 0:
                        if word_list[1] in special_vowels or word_list[1] == 'ь' or word_list[1] == 'и':
                            snd1.append('мягкий (парный), ')
                            snd1[1] = f"[{s}']"
                        else:
                            snd1.append("твёрдый (парный), ")
                    elif index > 0:
                        index_snd = word_list.index(s, index)
                        if word_list[index_snd + 1] in special_vowels or word_list[index_snd + 1] == 'ь' or word_list[index_snd + 1] == 'и':
                            snd1.append('мягкий (парный), ')
                            snd1[1] = f"[{s}']"
                        else:
                            snd1.append("твёрдый (парный), ")
                elif s in vo_co_undouble:
                    snd1.append('звонкиий (непарный), ')
                    if s == 'ш' or s == 'ж' or s == 'ц':
                        snd1.append('твёрдый (непарный), ')
                    elif s == 'щ' or s == 'ч' or s == 'й':
                        snd1.append('мягкий (непарный), ')
                        snd1[1] = f"[{s}']"
                    elif index == 0:
                        if word_list[1] in special_vowels or word_list[1] == 'ь' or word_list[1] == 'и':
                            snd1.append('мягкий (парный), ')
                            snd1[1] = f"[{s}']"
                        else:
                            snd1.append("твёрдый (парный), ")
                    elif index > 0:
                        index_snd = word_list.index(s, index)
                        if word_list[index_snd + 1] in special_vowels or word_list[index_snd + 1] == 'ь' or word_list[index_snd + 1] == 'и':
                            snd1.append('мягкий (парный), ')
                            snd1[1] = f"[{s}']"
                        else:
                            snd1.append("твёрдый (парный), ")
            elif s in dull_cons:
                if s in du_co_double:
                    snd1.append('глухой (парный), ')
                    if s == 'ш' or s == 'ж' or s == 'ц':
                        snd1.append('твёрдый (непарный), ')
                    elif s == 'щ' or s == 'ч' or s == 'й':
                        snd1.append('мягкий (непарный), ')
                        snd1[1] = f"[{s}']"
                    elif index == 0:
                        if word_list[1] in special_vowels or word_list[1] == 'ь' or word_list[1] == 'и':
                            snd1.append('мягкий (парный), ')
                            snd1[1] = f"[{s}']"
                        else:
                            snd1.append("твёрдый (парный), ")
                    elif index > 0:
                        index_snd = word_list.index(s, index)
                        if word_list[index_snd + 1] in special_vowels or word_list[index_snd + 1] == 'ь' or word_list[index_snd + 1] == 'и':
                            snd1.append('мягкий (парный), ')
                            snd1[1] = f"[{s}']"
                        else:
                            snd1.append("твёрдый (парный), ")
                elif s in du_co_undouble:
                    snd1.append('глухой (непарный), ')
                    if s == 'ш' or s == 'ж' or s == 'ц':
                        snd1.append('твёрдый (непарный), ')
                    elif s == 'щ' or s == 'ч' or s == 'й':
                        snd1.append('мягкий (непарный), ')
                        snd1[1] = f"[{s}']"
                    elif index == 0:
                        if word_list[1] in special_vowels or word_list[1] == 'ь' or word_list[1] == 'и':
                            snd1.append('мягкий (парный), ')
                            snd1[1] = f"[{s}']"
                        else:
                            snd1.append("твёрдый (парный), ")
                    elif index > 0:
                        index_snd = word_list.index(s, index)
                        if word_list[index_snd + 1] in special_vowels or word_list[index_snd + 1] == 'ь' or word_list[index_snd + 1] == 'и':
                            snd1.append('мягкий (парный), ')
                            snd1[1] = f"[{s}']"
                        else:
                            snd1.append("твёрдый (парный), ")
        elif s in vowels:
            snd1.append(s)
            index_v += 1
            snd1.append('гласный, ')
            if index_v == hit:
                snd1.append("ударный")
            elif index_v != hit:
                snd1.append("безударный")
        elif s in nn_let:
            snd1.append(s)
            snd1.append(f'[ ]')
            snd1.append('а вот ничего')
        snd.append(snd1)
        index += 1
    return snd

