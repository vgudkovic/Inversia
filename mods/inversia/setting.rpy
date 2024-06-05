init -1 python:
    characters_inversia = { # Словарь с персонажами
        # основные
        "narrator":[None, None],
        "th":[None, None],
        "me":[u"Семён", "#E1DD7D"],
        # персонажи оригинала
        "mi":[u"Мику", "#00DEFF"],
        "us":[u"Ульяна", "#FF3200"],
        "dv":[u"Алиса", "#FFAA00"],
        "mt":[u"Ольга Дмитриевна", "#00EA32"],
        "mz":[u"Женя", "#4A86FF"],
        "sh":[u"Шурик", "#FFF226"],
        "sl":[u"Славя", "#FFD200"],
        "el":[u"Электроник", "#FFFF00"],
        "un":[u"Лена", "#B956FF"],
        "cs":[u"Виола", "#A5A5FF"],
        "pi":[u"Пионер", "#E60000"],
        "uv":[u"Юля", "#4EFF00"],
        "voice":[u"Голос", "#e1dd7d"],
        # новые персонажи
        zg = ['Женя', color = "#00deff", what_color = "#f1d076"]
        nn = ['Незнакомка', color = "#00deff", what_color = "#f1d076"]
        sa = ['Саша', color = "#00deff", what_color = "#f1d076"]
        }

init python:
    def chars_define_inversia(kind=adv):
        gl = globals()
        if kind == nvl:
            who_suffix = ":"
            ctc = "ctc_animation_nvl"
        else:
            who_suffix = ""
            ctc = "ctc_animation"
        what_color = "#FFDD7D" # Цвет текста персонажа
        drop_shadow = (2, 2) # Наложение тени на текст
        for i, j in characters_inversia.items():
            if i == "narrator":
                gl[i] = Character(None, kind=kind, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
            elif i == "th":
                gl[i] = Character(None, kind=kind, what_color=what_color, what_drop_shadow=drop_shadow, what_prefix="~ ", what_suffix=" ~", ctc=ctc, ctc_position="fixed")
            else:
                gl[i] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                # Добавлено дополнительное объявление персонажей, которые будут сохранять оригинальный цвет имени персонажа, но изменять его имя.
                # Полезно, когда ГГ в моде ещё не знаком с новыми пионерами, но забивать словарь мусором не хочется.
                # Пример использования - "new_v" - имя "Новый персонаж" меняется на "Голос", "new_pm" - "Пионер", "new_pg" - "Пионерка"
                gl[i+"_v"] = Character(u"Голос", kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                gl[i+"_pm"] = Character(u"Пионер", kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                gl[i+"_pg"] = Character(u"Пионерка", kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
            if renpy.mobile:
                colors[i] = {'night': j[1], 'sunset': j[1], 'day': j[1], 'prolog': j[1]}
                names[i] = j[0]
                store.names_list.append(i)

    def set_mode_inversia(mode=adv): # Переключение между ADV и NVL режимами
        nvl_clear()
        chars_define_inversia(kind=mode)
        if renpy.mobile:
            if mode == adv:
                set_mode_adv()
            else:
                set_mode_nvl()

    def set_name_inversia(name, value, mode=adv): # Изменение имени персонажа
        characters_inversia[name][0] = value
        chars_define_inversia(mode)
        if renpy.mobile:
            if mode == nvl:
                set_mode_nvl()
            else:
                set_mode_adv()

    def set_char_color_inversia(name, value, mode=adv): # Изменение цвета имени персонажа
        characters_inversia[name][1] = value
        chars_define_inversia(mode)
        if renpy.mobile:
            if mode == nvl:
                set_mode_nvl()
            else:
                set_mode_adv()
