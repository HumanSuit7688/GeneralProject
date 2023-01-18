from Fonetic.Modules.info_back_end import  vowels, consonants, nn_let, special_vowels, spec_vow_key, voice_cons, vo_co_double, vo_co_undouble, dull_cons, du_co_double, du_co_undouble, vo_co_doub, du_co_doub


def list(word):
    word_list = []
    for i in word:
        word_list.append(i)
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
    word_list.append(' ')
    index_v = 0
    snd = []
    index = 0
    for s in word_list:
        snd1 = []
        if s in consonants:
            snd1.append(f'{s} - ')
            snd1.append(f'[{s}] - ')
            snd1.append('согласный, ')
            if s in voice_cons:
                if s in vo_co_double:
                    index_vo = word_list.index(s, index)
                    if word_list[index_vo+1] == ' ':
                        snd1.append('глухой (парный), ')
                        a = vo_co_doub.get(s)
                        snd1[1] = f'[{a}] - '
                        if a == 'ш' or a == 'ж' or a == 'ц':
                            snd1.append('твёрдый (непарный), ')
                        elif a == 'щ' or a == 'ч' or a == 'й':
                            snd1.append('мягкий (непарный), ')
                            snd1[1] = f"[{a}'] - "
                        # elif index == 0:
                        #     if word_list[1] in special_vowels or word_list[1] == 'ь' or word_list[1] == 'и':
                        #         snd1.append('мягкий (парный), ')
                        #         snd1[1] = f"[{a}'] - "
                        #     else:
                        #         snd1.append("твёрдый (парный), ")
                        elif index > 0:
                            index_snd = word_list.index(s, index)
                            if word_list[index_snd + 1] in special_vowels or word_list[index_snd + 1] == 'ь' or \
                                    word_list[index_snd + 1] == 'и':
                                snd1.append('мягкий (парный), ')
                                snd1[1] = f"[{a}'] - "
                            else:
                                snd1.append("твёрдый (парный), ")
                    # snd1.append('звонкиий (парный), ')
                    elif word_list[index_vo + 1] in dull_cons:
                        snd1.append('глухой (парный), ')
                        a = vo_co_doub.get(s)
                        snd1[1] = f'[{a}] - '
                        if a == 'ш' or a == 'ж' or a == 'ц':
                            snd1.append('твёрдый (непарный), ')
                        elif a == 'щ' or a == 'ч' or a == 'й':
                            snd1.append('мягкий (непарный), ')
                            snd1[1] = f"[{a}'] - "
                        elif index == 0:
                            if word_list[1] in special_vowels or word_list[1] == 'ь' or word_list[1] == 'и':
                                snd1.append('мягкий (парный), ')
                                snd1[1] = f"[{a}'] - "
                            else:
                                snd1.append("твёрдый (парный), ")
                        elif index > 0:
                            index_snd = word_list.index(s, index)
                            if word_list[index_snd + 1] in special_vowels or word_list[index_snd + 1] == 'ь' or \
                                    word_list[index_snd + 1] == 'и':
                                snd1.append('мягкий (парный), ')
                                snd1[1] = f"[{a}'] - "
                            else:
                                snd1.append("твёрдый (парный), ")
                    else:
                        snd1.append('звонкиий (парный), ')
                        if s == 'ш' or s == 'ж' or s == 'ц':
                            snd1.append('твёрдый (непарный), ')
                        elif s == 'щ' or s == 'ч' or s == 'й':
                            snd1.append('мягкий (непарный), ')
                            snd1[1] = f"[{s}'] - "
                        elif index == 0:
                            if word_list[1] in special_vowels or word_list[1] == 'ь' or word_list[1] == 'и':
                                snd1.append('мягкий (парный), ')
                                snd1[1] = f"[{s}'] - "
                            else:
                                snd1.append("твёрдый (парный), ")
                        elif index > 0:
                            index_snd = word_list.index(s, index)
                            if word_list[index_snd + 1] in special_vowels or word_list[index_snd + 1] == 'ь' or word_list[index_snd + 1] == 'и':
                                snd1.append('мягкий (парный), ')
                                snd1[1] = f"[{s}'] - "
                            else:
                                snd1.append("твёрдый (парный), ")
                elif s in vo_co_undouble:
                    snd1.append('звонкиий (непарный), ')
                    if s == 'ш' or s == 'ж' or s == 'ц':
                        snd1.append('твёрдый (непарный), ')
                    elif s == 'щ' or s == 'ч' or s == 'й':
                        snd1.append('мягкий (непарный), ')
                        snd1[1] = f"[{s}'] - "
                    elif index == 0:
                        if word_list[1] in special_vowels or word_list[1] == 'ь' or word_list[1] == 'и':
                            snd1.append('мягкий (парный), ')
                            snd1[1] = f"[{s}'] - "
                        else:
                            snd1.append("твёрдый (парный), ")
                    elif index > 0:
                        index_snd = word_list.index(s, index)
                        if word_list[index_snd + 1] in special_vowels or word_list[index_snd + 1] == 'ь' or word_list[index_snd + 1] == 'и':
                            snd1.append('мягкий (парный), ')
                            snd1[1] = f"[{s}'] - "
                        else:
                            snd1.append("твёрдый (парный), ")
            elif s in dull_cons:
                if s in du_co_double:
                    index_du = word_list.index(s, index)
                    if word_list[index_du+1] in voice_cons:
                        snd1.append('звонкий (парный), ')
                        a = du_co_doub.get(s)
                        snd1[1] = f'[{a}] - '
                        if s == 'ш' or s == 'ж' or s == 'ц':
                            snd1.append('твёрдый (непарный), ')
                        elif s == 'щ' or s == 'ч' or s == 'й':
                            snd1.append('мягкий (непарный), ')
                            snd1[1] = f"[{a}'] - "
                        elif index == 0:
                            if word_list[1] in special_vowels or word_list[1] == 'ь' or word_list[1] == 'и':
                                snd1.append('мягкий (парный), ')
                                snd1[1] = f"[{a}'] - "
                            else:
                                snd1.append("твёрдый (парный), ")
                        elif index > 0:
                            index_snd = word_list.index(s, index)
                            if word_list[index_snd + 1] in special_vowels or word_list[index_snd + 1] == 'ь' or \
                                    word_list[index_snd + 1] == 'и':
                                snd1.append('мягкий (парный), ')
                                snd1[1] = f"[{a}'] - "
                            else:
                                snd1.append("твёрдый (парный), ")
                    else:
                        snd1.append('глухой (парный), ')
                        if s == 'ш' or s == 'ж' or s == 'ц':
                            snd1.append('твёрдый (непарный), ')
                        elif s == 'щ' or s == 'ч' or s == 'й':
                            snd1.append('мягкий (непарный), ')
                            snd1[1] = f"[{s}'] - "
                        elif index == 0:
                            if word_list[1] in special_vowels or word_list[1] == 'ь' or word_list[1] == 'и':
                                snd1.append('мягкий (парный), ')
                                snd1[1] = f"[{s}'] - "
                            else:
                                snd1.append("твёрдый (парный), ")
                        elif index > 0:
                            index_snd = word_list.index(s, index)
                            if word_list[index_snd + 1] in special_vowels or word_list[index_snd + 1] == 'ь' or word_list[index_snd + 1] == 'и':
                                snd1.append('мягкий (парный), ')
                                snd1[1] = f"[{s}'] - "
                            else:
                                snd1.append("твёрдый (парный), ")
                elif s in du_co_undouble:
                    snd1.append('глухой (непарный), ')
                    if s == 'ш' or s == 'ж' or s == 'ц':
                        snd1.append('твёрдый (непарный), ')
                    elif s == 'щ' or s == 'ч' or s == 'й':
                        snd1.append('мягкий (непарный), ')
                        snd1[1] = f"[{s}'] - "
                    elif index == 0:
                        if word_list[1] in special_vowels or word_list[1] == 'ь' or word_list[1] == 'и':
                            snd1.append('мягкий (парный), ')
                            snd1[1] = f"[{s}'] - "
                        else:
                            snd1.append("твёрдый (парный), ")
                    elif index > 0:
                        index_snd = word_list.index(s, index)
                        if word_list[index_snd + 1] in special_vowels or word_list[index_snd + 1] == 'ь' or word_list[index_snd + 1] == 'и':
                            snd1.append('мягкий (парный), ')
                            snd1[1] = f"[{s}'] - "
                        else:
                            snd1.append("твёрдый (парный), ")
        elif s in vowels:
            if s in special_vowels:
                snd1.append(s)
                ie = ["[й'] - ", "согласный, ", "звонкий (непарный), ", "мягкий (непарный)"]
                if index == 0:
                    snd1.append(ie)
                    snd_vow = spec_vow_key.get(s)[1]
                    snd1.append(f"[{snd_vow}] - ")
                elif index > 0:
                    index_let = word_list.index(s, index)
                    if word_list[index_let - 1] in nn_let or word_list[index_let - 1] in vowels:
                        snd1.append(ie)
                        snd_vow = spec_vow_key.get(s)[1]
                        snd1.append(f"[{snd_vow}] - ")
                    elif word_list[index_let - 1] in consonants:
                        snd_vow = spec_vow_key.get(s)[1]
                        snd1.append(f"{snd_vow}")
            else:
                snd1.append(f'{s} - ')
                snd1.append(f'[{s}] - ')
            index_v += 1
            snd1.append('гласный, ')
            if index_v == hit:
                snd1.append("ударный")
            elif index_v != hit:
                snd1.append("безударный")
        elif s in nn_let:
            snd1.append(f'{s} - ')
            snd1.append(f'[ ] - ')
            snd1.append('а вот ничего')
        else:
            pass
        snd.append(snd1)
        index += 1
    return snd

