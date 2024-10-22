init:
    $ config.developer = True
    $ mods["d2_inv_logic"]=u"День Z" # Название мода

# Переменная для пасхалки
    $ music_club_pash_d2_inv = False
    $ clubs_pash_d2_inv = False
    $ aidpost_pash_d2_inv = False
    $ library_pash_d2_inv = False

    # Счетчик площадок
    $ prohod_d2 = 0
    $ full_prohod = False

    # Счетчик пасхалки
    $ pash_prov_d2_inv = ""

    # Переменные для пасхалки
    $ pash_music = "P"
    $ pash_clubs = "A"
    $ pash_aidpost = "S"
    $ pash_library = "H"

label d2_inv_logic:
    scene black
    if prohod_d2 == 0:
        "Надо собрать подписи!"
    else:
        "Едем дальше!"

    # Первичная проверка
    if music_club_pash_d2_inv == True:
        if clubs_pash_d2_inv == True:
            if aidpost_pash_d2_inv == True:
                if library_pash_d2_inv == True:
                    $ full_prohod = True
# Задаем нужные нам зоны с ссылками на лейблы
    # Вторичная проверка
    $ disable_all_zones()
    if prohod_d2 < 4:
        if full_prohod == False:
            if music_club_pash_d2_inv == False:
                    # Музклуб
                $ set_zone("music_club","d2_music_club_inv")
            if clubs_pash_d2_inv == False:
                    # Клубы
                $ set_zone("clubs","d2_clubs_inv")
            if aidpost_pash_d2_inv == False:
                    # Медпункт
                $ set_zone("medic_house","d2_medic_house_inv")
            if library_pash_d2_inv == False:
                    # Библиотека
                $ set_zone("library","d2_library_inv")
    else: # Добавляем else
        if full_prohod == True:
            scene black
            jump d2_pash_prov

    $ show_map()
 
label d2_pash_prov: # Добавляем лейбл-проверку
    scene black
    "Похоже, что ты прошел все локации. Давай посмотрим, что у тебя получилось собрать!"

# Проверяем сбор слова-пасхалки
    if pash_prov_d2_inv == "PASH":
        "Gracias, вы заслужили пасхалку!"
        jump d2_inv_logic
    else:
        "Хуй вам, а не пасхалка, сударь!"
        jump d2_inv_logic


# Лейблы для зон карты
label d2_music_club_inv:
    scene black
    "Ты зашел в музклуб и получил подпись у Мику."
    $ music_club_pash_d2_inv = True
    $ prohod_d2 += 1
    $ pash_prov_d2_inv += pash_music
    jump d2_inv_logic

label d2_clubs_inv:
    scene black
    "Получена подпись граждан кибернетиков."
    $ clubs_pash_d2_inv = True
    $ prohod_d2 += 1
    $ pash_prov_d2_inv += pash_clubs
    jump d2_inv_logic

label d2_medic_house_inv:
    scene black
    "Получена мм... подпись Виолы."
    $ aidpost_pash_d2_inv = True
    $ prohod_d2 += 1
    $ pash_prov_d2_inv += pash_aidpost
    jump d2_inv_logic

label d2_library_inv:
    scene black
    "Получена подпись Жени. Задание выполнено с особой жестокостью."
    $ library_pash_d2_inv = True
    $ prohod_d2 += 1
    $ pash_prov_d2_inv += pash_library
    jump d2_inv_logic