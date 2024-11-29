init:
    # $ renpy.music.register_channel("ambience", "sound2", True)
    # $ renpy.music.register_channel("sfx", "sound3", True)
#---------------------------------------------------
    # Персонажи 
    define zg = Character (u"Женя", color = "#00deff", what_color = "#f1d076")
    define nn = Character(u"Незнакомка", color = "#00deff", what_color = "#f1d076")
    define sa = Character (u"Саша", color = "#00deff", what_color = "#f1d076")
    define sa_zg = Character (u"Саша и Женя", color = "#14b21b", what_color = "#f1d076")
    define kl = Character (u"Кловер", color = "#240fc4", what_color = "#f1d076")
    define klp = Character (u"Незнакомка", color = "#240fc4", what_color = "#f1d076")
#-------------# 
    # Переменные
    $ dv_och = 0
    $ obhodnoi = 0
    $ obhodnoi_d2 = False

    $ beach_inv_day1 = False
    $ boat_station_day1_inv = False
    $ vse_oboshol_d1_inv = False
    $ sport_area2_inv = False

    #______Костыльные переменные
    # Для пасхалки
    $ proverka = None
    $ muzic_club_pash_d2_inv = False 
    $ clubs_pash_d2_inv = False 
    $ aidpost_pash_d2_inv = False 
    $ library_pash_d2_inv = False
    $ pash_d2_inv = False

    # Прохождение карты в целом
    $ muzic_club_d2_inv = False 
    $ clubs_d2_inv = False 
    $ aidpost_d2_inv = False 
    $ library_d2_inv = False 

    #______
#-------------------------
    # Переменная для пасхалки День 2.
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
#--------------------

    $ napugal_us = None
    $ us_znakomstvo = None
    $ pudrenitsa = False
    $ obratil_vnimanie_inv = False
    $ first_playrhrough = False
    $ obhodnoi_odin = None

    $ config.developer = True
#-------------# 
    #sfx
    $ inversion_pisk = "mods/inversia/sfx/inversion_pisk.mp3"
    # $ music inversion_Breath1 = "mods/inversia/music/inversion_Breath1.wav"
    $ inversion_shagi = "mods/inversia/sfx/shagi_s_ekhom.mp3"
    $ zvuk_tjazhelogo_dyhanija = "mods/inversia/sfx/zvuk_tjazhelogo_dyhanija.mp3"
    $ zenskiu_plach = "mods/inversia/sfx/zenskiu_plach.mp3"
    $ vistrel_iz_pistoleta = "mods/inversia/sfx/vistrel_iz_pistoleta.mp3"
    $ zhenschina_kashleet = "mods/inversia/sfx/zhenschina_kashleet.mp3"
    $ devushka_zevnula = "mods/inversia/sfx/devushka_zevnula.mp3"
    $ paren_zevnul = "mods/inversia/sfx/paren_zevnul.mp3"
    $ zensky_smekh = "mods/inversia/sfx/zensky_smekh.mp3"
    $ muzhskoi_smekh = "mods/inversia/sfx/muzhskoi_smekh.mp3"
    $ sirena_d2_inv = "mods/inversia/sfx/sirena_d2_inv.ogg"
    
#-------------------------------------------------#
# bg/cg
#--------------# Главное меню / Пролог
    image main_menu_inv = "mods/inversia/bg/main_menu_inv.jpg"
    image None_BG_INV = "mods/inversia/bg/None_BG_INV.jpg"

    image temnyi_koridor = "mods/inversia/bg/temnyi_koridor.webp"
    image karidor_so_svetom = "mods/inversia/bg/karidor_so_svetom.png"
    image polnosty_belaya_komnata = "mods/inversia/bg/polnosty_belaya_komnata.jpg"
    image beliy_karidor_s_dvery = "mods/inversia/bg/beliy_karidor_s_dvery.jpg"
    image beliy_karidor = "mods/inversia/bg/beliy_karidor.jpg"
    image komnata_prolog = "mods/inversia/bg/komnata_prolog.jpg"
    image bad_lager = "mods/inversia/bg/bad_lager.jpg"
    image creepy_komnata = "mods/inversia/bg/creepy_komnata.jpg"
    image chernaja_komnata_s_dvery = "mods/inversia/bg/chernaja_komnata_s_dvery.jpg"
#--------------#

#------------- Домики гг    
    image int_ggroom_day = "mods/inversia/bg/int_ggroom_day.jpg"
    image int_ggroom_sunset = "mods/inversia/bg/int_ggroom_sunset.jpg"
    image int_ggroom_night_light = "mods/inversia/bg/int_ggroom_night_light.jpg"

    image ext_ggroom_day = "mods/inversia/bg/ext_ggroom_day.jpg"
    image ext_ggroom_sunset = "mods/inversia/bg/ext_ggroom_sunset.jpg"
    image ext_ggroom_night = "mods/inversia/bg/ext_ggroom_night.jpg"

    image ext_sky_7dl = "mods/inversia/bg/ext_sky_7dl.jpg"
#------------- Домики гг    
    
#---------- Умывальники 
    image bg ext_washstand_sunset = "mods/inversia/bg/ext_washstand_sunset.png"
    image bg ext_washstand2_sunset = "mods/inversia/bg/ext_washstand2_sunset.png"
#---------- Умывальники 

    #Склад закрытый
    image ext_stock_day = "mods/inversia/bg/ext_stock_day.jpg"
    #Склад открытый 
    image ext_stock_near_store2 = "mods/inversia/bg/ext_stock_near_store2.jpg"

    image ext_houses_night = "mods/inversia/bg/ext_houses_night_7dl.jpg"

    image bg ext_houses_sunset = "mods/inversia/bg/ext_houses_sunset.jpg"



#--------------# 
    # Image
    image Achivement Prolog = "mods/inversia/image/Achivement Prolog.jpg"
    # Туман
    image tuman1_inv = "mods/inversia/image/tuman1_inv.png"
    
    # Саша - Слайм
    #   image slime_sasha_inv = "mods/inversia/image/Slime Sasha.png"
    image slime_sasha_inv = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((348, 1080), (0,0), "mods/inversia/image/Slime Sasha.png", (0,0), "mods/inversia/image/Slime Sasha.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((348, 1080), (0,0), "mods/inversia/image/Slime Sasha.png", (0,0), "mods/inversia/image/Slime Sasha.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((348, 1080), (0,0), "mods/inversia/image/Slime Sasha.png", (0,0), "mods/inversia/image/Slime Sasha.png") )

#--------------# 
# Трансформы / анимации
    #Бег. Задать в коде используем фон и at running. Scene bg ext_house_of_mt_day at running with dissolve
    transform running:
        pos (0,0)
        linear 0.1 pos (-3,-1)
        linear 0.1 pos (0,0)
        pos (0,0)
        linear 0.1 pos (3,-1)
        linear 0.1 pos (0,0)
        repeat
    #Анимация БЫСТРОГО бега
    transform running2:
        pos (0,0)
        linear 0.1 pos (-5,-1)
        linear 0.1 pos (0,0)
        pos (0,0)
        linear 0.1 pos (5,-1)
        linear 0.1 pos (0,0)
        repeat
    
    transform walking_inv:
        block:
            zoom 1.1 xcenter 0.5 ycenter 0.5
        block:
            ease 0.4 xoffset 0 yoffset 0
            ease 0.4 xoffset 15 yoffset 25
            ease 0.4 xoffset 0 yoffset 0
            ease 0.4 xoffset -10 yoffset 25
        repeat
#--------------
    # Sprites

    # sa - Саша 
# Дальность - далеко (Far) # bent_arm - Согнутая рука
    image InversiaMOD sa bent_arm angry pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png") )
    
    image InversiaMOD sa bent_arm crying pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_crying.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_crying.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_crying.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_crying.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_crying.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_crying.png") )

    image InversiaMOD sa bent_arm crying2 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_crying2.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_crying2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_crying2.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_crying2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_crying2.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_crying2.png") )
    
    image InversiaMOD sa bent_arm embarrassed pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_embarrassed.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_embarrassed.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_embarrassed.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_embarrassed.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_embarrassed.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_embarrassed.png") )

    image InversiaMOD sa bent_arm happy pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_happy.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_happy.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_happy.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_happy.png") )

    image InversiaMOD sa bent_arm normal pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_normal.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_normal.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_normal.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_normal.png") )

    image InversiaMOD sa bent_arm scared pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_scared.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_scared.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_scared.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_scared.png") )

    image InversiaMOD sa bent_arm shock pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_shock.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_shock.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_shock.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_shock.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_shock.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_shock.png") )

    image InversiaMOD sa bent_arm smile pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_smile.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_smile.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_smile.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_smile.png") )

    image InversiaMOD sa bent_arm surprise pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_surprise.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_surprise.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_surprise.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_surprise.png") )

    image InversiaMOD sa bent_arm tears_on_eyes pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_tears_on_eyes.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_tears_on_eyes.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_tears_on_eyes.png") )

    image InversiaMOD sa bent_arm thoughtful pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_thoughtful.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_thoughtful.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_thoughtful.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_thoughtful.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_thoughtful.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_thoughtful.png") )

    image InversiaMOD sa bent_arm thoughtful2 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_thoughtful2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_thoughtful2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_thoughtful2.png") )

    image InversiaMOD sa bent_arm unsmile pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_unsmile.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_unsmile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_unsmile.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_unsmile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_unsmile.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_unsmile.png") )
    
# Дальность - далеко (Far) # Front - Лицом к герою
    image InversiaMOD sa front angry pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_angry.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_angry.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_angry.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_angry.png") )
    
    image InversiaMOD sa front crying pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_crying.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_crying.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_crying.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_crying.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_crying.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_crying.png") )
    
    image InversiaMOD sa front crying2 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_crying2.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_crying2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_crying2.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_crying2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_crying2.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_crying2.png") )
    
    image InversiaMOD sa front embarrassed pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_embarrassed.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_embarrassed.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_embarrassed.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_embarrassed.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_embarrassed.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_embarrassed.png") )

    image InversiaMOD sa front grin pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_grin.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_grin.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_grin.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_grin.png") )

    image InversiaMOD sa front happy pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_happy.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_happy.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_happy.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_happy.png") )

    image InversiaMOD sa front normal pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_normal.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_normal.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_normal.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_normal.png") )

    image InversiaMOD sa front scared pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_scared.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_scared.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_scared.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_scared.png") )

    image InversiaMOD sa front shock pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_shock.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_shock.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_shock.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_shock.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_shock.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_shock.png") )

    image InversiaMOD sa front smile pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_smile.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_smile.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_smile.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_smile.png") )

    image InversiaMOD sa front smile2 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_smile2.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_smile2.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_smile2.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_smile2.png") )

    image InversiaMOD sa front surprise pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_surprise.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_surprise.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_surprise.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_surprise.png") )

    image InversiaMOD sa front surprise2 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_surprise2.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_surprise2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_surprise2.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_surprise2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_surprise2.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_surprise2.png") )

    image InversiaMOD sa front thoughtful pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_thoughtful.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_thoughtful.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_thoughtful.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_thoughtful.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_thoughtful.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_thoughtful.png") )

    image InversiaMOD sa front unsmile pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_unsmile.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_unsmile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_unsmile.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_unsmile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/front/sa_front_unsmile.png", (0,0), "mods/inversia/sprites/sa/far/front/sa_front_unsmile.png") )

# Дальность - далеко (Far) # semi_sideways - Полу-боком
    image InversiaMOD sa semi_sideways angry pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_angry.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_angry.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_angry.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_angry.png") )
    
    image InversiaMOD sa semi_sideways crying pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_crying.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_crying.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_crying.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_crying.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_crying.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_crying.png") )
    
    image InversiaMOD sa semi_sideways crying2 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_crying2.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_crying2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_crying2.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_crying2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_crying2.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_crying2.png") )
    
    image InversiaMOD sa semi_sideways embarrassed pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_embarrassed.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_embarrassed.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_embarrassed.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_embarrassed.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_embarrassed.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_embarrassed.png") )
    
    image InversiaMOD sa semi_sideways happy pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_happy.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_happy.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_happy.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_happy.png") )
    
    image InversiaMOD sa semi_sideways normal pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_normal.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_normal.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_normal.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_normal.png") )
 
    image InversiaMOD sa semi_sideways scared pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_scared.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_scared.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_scared.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_scared.png") )

    image InversiaMOD sa semi_sideways shock pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_shock.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_shock.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_shock.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_shock.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_shock.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_shock.png") )

    image InversiaMOD sa semi_sideways smile pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_smile.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_smile.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_smile.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_smile.png") )

    image InversiaMOD sa semi_sideways surprise pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_surprise.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_surprise.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_surprise.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_surprise.png") )

    image InversiaMOD sa semi_sideways tears_on_eyes pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_tears_on_eyes.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_tears_on_eyes.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_tears_on_eyes.png") )

    image InversiaMOD sa semi_sideways thoughtful pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_thoughtful.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_thoughtful.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_thoughtful.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_thoughtful.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_thoughtful.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_thoughtful.png") )

    image InversiaMOD sa semi_sideways thoughtful2 pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_thoughtful2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_thoughtful2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_thoughtful2.png") )

    image InversiaMOD sa semi_sideways unsmile pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_unsmile.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_unsmile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_unsmile.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_unsmile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_unsmile.png", (0,0), "mods/inversia/sprites/sa/far/semi_sideways/sa_semi_sideways_unsmile.png") )

#-------- 
# Normal - средняя дистанция # bent_arm - согнутая рука
    image InversiaMOD sa bent_arm angry pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_angry.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_angry.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_angry.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_angry.png") )
    
    image InversiaMOD sa bent_arm crying pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_crying.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_crying.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_crying.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_crying.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_crying.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_crying.png") )

    image InversiaMOD sa bent_arm crying2 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_crying2.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_crying2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_crying2.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_crying2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_crying2.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_crying2.png") )
    
    image InversiaMOD sa bent_arm embarrassed pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_embarrassed.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_embarrassed.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_embarrassed.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_embarrassed.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_embarrassed.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_embarrassed.png") )

    image InversiaMOD sa bent_arm happy pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_happy.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_happy.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_happy.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_happy.png") )

    image InversiaMOD sa bent_arm normal pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_normal.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_normal.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_normal.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_normal.png") )

    image InversiaMOD sa bent_arm scared pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_scared.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_scared.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_scared.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_scared.png") )

    image InversiaMOD sa bent_arm shock pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_shock.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_shock.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_shock.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_shock.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_shock.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_shock.png") )

    image InversiaMOD sa bent_arm smile pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_smile.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_smile.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_smile.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_smile.png") )

    image InversiaMOD sa bent_arm surprise pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_surprise.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_surprise.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_surprise.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_surprise.png") )

    image InversiaMOD sa bent_arm tears_on_eyes pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_tears_on_eyes.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_tears_on_eyes.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_tears_on_eyes.png") )

    image InversiaMOD sa bent_arm thoughtful pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_thoughtful.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_thoughtful.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_thoughtful.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_thoughtful.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_thoughtful.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_thoughtful.png") )

    image InversiaMOD sa bent_arm thoughtful2 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_thoughtful2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_thoughtful2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_thoughtful2.png") )

    image InversiaMOD sa bent_arm unsmile pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_unsmile.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_unsmile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_unsmile.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_unsmile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_unsmile.png", (0,0), "mods/inversia/sprites/sa/normal/bent_arm/sa_bent_arm_unsmile.png") )
    
# Normal - средняя дистанция # Front - Лицом к герою
    image InversiaMOD sa front angry pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_angry.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_angry.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_angry.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_angry.png") )
    
    image InversiaMOD sa front crying pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_crying.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_crying.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_crying.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_crying.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_crying.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_crying.png") )
    
    image InversiaMOD sa front crying2 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_crying2.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_crying2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_crying2.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_crying2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_crying2.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_crying2.png") )
    
    image InversiaMOD sa front embarrassed pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_embarrassed.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_embarrassed.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_embarrassed.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_embarrassed.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_embarrassed.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_embarrassed.png") )

    image InversiaMOD sa front grin pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_grin.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_grin.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_grin.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_grin.png") )

    image InversiaMOD sa front happy pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_happy.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_happy.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_happy.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_happy.png") )

    image InversiaMOD sa front normal pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_normal.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_normal.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_normal.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_normal.png") )

    image InversiaMOD sa front scared pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_scared.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_scared.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_scared.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_scared.png") )

    image InversiaMOD sa front shock pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_shock.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_shock.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_shock.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_shock.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_shock.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_shock.png") )

    image InversiaMOD sa front smile pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_smile.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_smile.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_smile.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_smile.png") )

    image InversiaMOD sa front smile2 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_smile2.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_smile2.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_smile2.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_smile2.png") )

    image InversiaMOD sa front surprise pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_surprise.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_surprise.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_surprise.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_surprise.png") )

    image InversiaMOD sa front surprise2 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_surprise2.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_surprise2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_surprise2.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_surprise2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_surprise2.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_surprise2.png") )

    image InversiaMOD sa front thoughtful pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_thoughtful.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_thoughtful.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_thoughtful.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_thoughtful.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_thoughtful.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_thoughtful.png") )

    image InversiaMOD sa front unsmile pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_unsmile.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_unsmile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_unsmile.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_unsmile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_unsmile.png", (0,0), "mods/inversia/sprites/sa/normal/front/sa_front_unsmile.png") )

# Normal - средняя дистанция # semi_sideways - Полу-боком
    image InversiaMOD sa semi_sideways angry pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_angry.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_angry.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_angry.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_angry.png") )
    
    image InversiaMOD sa semi_sideways crying pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_crying.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_crying.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_crying.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_crying.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_crying.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_crying.png") )
    
    image InversiaMOD sa semi_sideways crying2 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_crying2.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_crying2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_crying2.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_crying2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_crying2.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_crying2.png") )
    
    image InversiaMOD sa semi_sideways embarrassed pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_embarrassed.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_embarrassed.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_embarrassed.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_embarrassed.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_embarrassed.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_embarrassed.png") )
    
    image InversiaMOD sa semi_sideways happy pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_happy.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_happy.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_happy.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_happy.png") )
    
    image InversiaMOD sa semi_sideways normal pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_normal.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_normal.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_normal.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_normal.png") )
 
    image InversiaMOD sa semi_sideways scared pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_scared.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_scared.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_scared.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_scared.png") )

    image InversiaMOD sa semi_sideways shock pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_shock.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_shock.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_shock.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_shock.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_shock.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_shock.png") )

    image InversiaMOD sa semi_sideways smile pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_smile.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_smile.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_smile.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_smile.png") )

    image InversiaMOD sa semi_sideways surprise pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_surprise.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_surprise.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_surprise.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_surprise.png") )

    image InversiaMOD sa semi_sideways tears_on_eyes pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_tears_on_eyes.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_tears_on_eyes.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_tears_on_eyes.png") )

    image InversiaMOD sa semi_sideways thoughtful pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_thoughtful.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_thoughtful.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_thoughtful.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_thoughtful.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_thoughtful.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_thoughtful.png") )

    image InversiaMOD sa semi_sideways thoughtful2 pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_thoughtful2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_thoughtful2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_thoughtful2.png") )

    image InversiaMOD sa semi_sideways unsmile pioneer normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_unsmile.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_unsmile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_unsmile.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_unsmile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((493, 1080), (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_unsmile.png", (0,0), "mods/inversia/sprites/sa/normal/semi_sideways/sa_semi_sideways_unsmile.png") )

#-----------
# close - близко # bent_arm - согнутая рука
    image InversiaMOD sa bent_arm angry pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_angry.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_angry.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_angry.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_angry.png") )
    
    image InversiaMOD sa bent_arm crying pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_crying.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_crying.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_crying.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_crying.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_crying.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_crying.png") )

    image InversiaMOD sa bent_arm crying2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_crying2.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_crying2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_crying2.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_crying2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_crying2.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_crying2.png") )
    
    image InversiaMOD sa bent_arm embarrassed pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_embarrassed.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_embarrassed.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_embarrassed.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_embarrassed.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_embarrassed.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_embarrassed.png") )

    image InversiaMOD sa bent_arm happy pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_happy.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_happy.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_happy.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_happy.png") )

    image InversiaMOD sa bent_arm normal pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_normal.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_normal.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_normal.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_normal.png") )

    image InversiaMOD sa bent_arm scared pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_scared.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_scared.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_scared.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_scared.png") )

    image InversiaMOD sa bent_arm shock pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_shock.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_shock.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_shock.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_shock.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_shock.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_shock.png") )

    image InversiaMOD sa bent_arm smile pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_smile.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_smile.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_smile.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_smile.png") )

    image InversiaMOD sa bent_arm surprise pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_surprise.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_surprise.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_surprise.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_surprise.png") )

    image InversiaMOD sa bent_arm tears_on_eyes pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_tears_on_eyes.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_tears_on_eyes.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_tears_on_eyes.png") )

    image InversiaMOD sa bent_arm thoughtful pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_thoughtful.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_thoughtful.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_thoughtful.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_thoughtful.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_thoughtful.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_thoughtful.png") )

    image InversiaMOD sa bent_arm thoughtful2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_thoughtful2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_thoughtful2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_thoughtful2.png") )

    image InversiaMOD sa bent_arm unsmile pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_unsmile.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_unsmile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_unsmile.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_unsmile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_unsmile.png", (0,0), "mods/inversia/sprites/sa/close/bent_arm/sa_bent_arm_unsmile.png") )
    
# close - близко # Front - Лицом к герою
    image InversiaMOD sa front angry pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_angry.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_angry.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_angry.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_angry.png") )
    
    image InversiaMOD sa front crying pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_crying.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_crying.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_crying.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_crying.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_crying.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_crying.png") )
    
    image InversiaMOD sa front crying2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_crying2.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_crying2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_crying2.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_crying2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_crying2.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_crying2.png") )
    
    image InversiaMOD sa front embarrassed pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_embarrassed.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_embarrassed.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_embarrassed.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_embarrassed.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_embarrassed.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_embarrassed.png") )

    image InversiaMOD sa front grin pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_grin.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_grin.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_grin.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_grin.png") )

    image InversiaMOD sa front happy pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_happy.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_happy.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_happy.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_happy.png") )

    image InversiaMOD sa front normal pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_normal.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_normal.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_normal.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_normal.png") )

    image InversiaMOD sa front scared pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_scared.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_scared.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_scared.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_scared.png") )

    image InversiaMOD sa front shock pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_shock.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_shock.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_shock.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_shock.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_shock.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_shock.png") )

    image InversiaMOD sa front smile pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_smile.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_smile.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_smile.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_smile.png") )

    image InversiaMOD sa front smile2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_smile2.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_smile2.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_smile2.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_smile2.png") )

    image InversiaMOD sa front surprise pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_surprise.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_surprise.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_surprise.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_surprise.png") )

    image InversiaMOD sa front surprise2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_surprise2.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_surprise2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_surprise2.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_surprise2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_surprise2.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_surprise2.png") )

    image InversiaMOD sa front thoughtful pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_thoughtful.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_thoughtful.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_thoughtful.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_thoughtful.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_thoughtful.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_thoughtful.png") )

    image InversiaMOD sa front unsmile pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_unsmile.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_unsmile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_unsmile.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_unsmile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/front/sa_front_unsmile.png", (0,0), "mods/inversia/sprites/sa/close/front/sa_front_unsmile.png") )

# close - близко # semi_sideways - Полу-боком
    image InversiaMOD sa semi_sideways angry pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_angry.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_angry.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_angry.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_angry.png") )
    
    image InversiaMOD sa semi_sideways crying pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_crying.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_crying.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_crying.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_crying.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_crying.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_crying.png") )
    
    image InversiaMOD sa semi_sideways crying2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_crying2.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_crying2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_crying2.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_crying2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_crying2.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_crying2.png") )
    
    image InversiaMOD sa semi_sideways embarrassed pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_embarrassed.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_embarrassed.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_embarrassed.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_embarrassed.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_embarrassed.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_embarrassed.png") )
    
    image InversiaMOD sa semi_sideways happy pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_happy.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_happy.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_happy.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_happy.png") )
    
    image InversiaMOD sa semi_sideways normal pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_normal.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_normal.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_normal.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_normal.png") )
 
    image InversiaMOD sa semi_sideways scared pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_scared.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_scared.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_scared.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_scared.png") )

    image InversiaMOD sa semi_sideways shock pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_shock.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_shock.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_shock.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_shock.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_shock.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_shock.png") )

    image InversiaMOD sa semi_sideways smile pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_smile.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_smile.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_smile.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_smile.png") )

    image InversiaMOD sa semi_sideways surprise pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_surprise.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_surprise.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_surprise.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_surprise.png") )

    image InversiaMOD sa semi_sideways tears_on_eyes pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_tears_on_eyes.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_tears_on_eyes.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_tears_on_eyes.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_tears_on_eyes.png") )

    image InversiaMOD sa semi_sideways thoughtful pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_thoughtful.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_thoughtful.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_thoughtful.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_thoughtful.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_thoughtful.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_thoughtful.png") )

    image InversiaMOD sa semi_sideways thoughtful2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_thoughtful2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_thoughtful2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_thoughtful2.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_thoughtful2.png") )

    image InversiaMOD sa semi_sideways unsmile pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_unsmile.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_unsmile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_unsmile.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_unsmile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((658, 1080), (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_unsmile.png", (0,0), "mods/inversia/sprites/sa/close/semi_sideways/sa_semi_sideways_unsmile.png") )


#-----------------------------------------------------------------------------------------------
    $ config.developer = True
    
    $ mods["inv_main_menu"]=u"{font=mods/inversia/Sriracha.ttf}{size=36}{color=2af90a}Инверсия {/color}{/size}{/font}" # Название мода

label inv_main_menu:

    window hide

    call screen inv_main_menu
    screen inv_main_menu:
        
        tag test
        modal True 
         
        # show main_menu_inv with dissolve
        
        textbutton "Читать Пролог":
            xpos 0.3 ypos 0.3 
            text_idle_color "#fff" text_hover_color "#aaa" text_size 60 text_font "font=mods/inversia/Sriracha.ttf"
            action Call("prolog_inversia", transition=dissolve)

        textbutton "Читать 1 День":
            xpos 0.4 ypos 0.3 
            text_idle_color "#fff" text_hover_color "#aaa" text_size 60 text_font "font=mods/inversia/Sriracha.ttf"
            action Call("day1_inversia", transition=dissolve)
        
        #textbutton "Настройки":
        #    xpos 0.5 ypos 0.3 
        #    text_idle_color "#fff" text_hover_color "#aaa" text_size 60 text_font "font=mods/inversia/Sriracha.ttf"
        #    action Call("day1_inversia", transition=dissolve)
        
        textbutton "Выйти в главное меню":
            xpos 0.6 ypos 0.3 
            text_idle_color "#fff" text_hover_color "#aaa" text_size 60 text_font "font=mods/inversia/Sriracha.ttf"
            action MainMenu(With(transition))
        
        textbutton "Выйти из игры":
            xpos 0.6 ypos 0.3 
            text_idle_color "#fff" text_hover_color "#aaa" text_size 60 text_font "font=mods/inversia/Sriracha.ttf"
            action Quit(confirm=True)
        




label prolog_inversia:
    $ backdrop = "days"
    $ save_name = (u"Инверсия. \nПролог.")
    $ prolog_time()
    $ persistent.sprite_time = 'day'
    
    scene black with dissolve
    "Безжизненный мрак залил собой всё вокруг."

    #Звук в тунеле "Пустое пространство с эхом"
    play music ambience_camp_center_day fadein 2.0 loop
    play sound inversion_pisk fadein 2.0 loop

    "В ушах застыл неописуемо сильный писк неведомого мне происхождения."
    "Быть может, где-то неподалёку что-то взорвалось. Или же меня хорошенько так огрели по голове."
    "Пускай писк всё не унимался, ему не удалось помешать моим мыслям устремиться наружу."
    "Честно скажу, собственные мысли бесили меня не меньше, чем чёртов писк."
    "В голову лезли ненужные опасения, страх и даже любопытство."
    "Хотя казалось бы, чего может быть любопытного в моём положении?"
    "Но желание узнать, что всё-таки со мной происходит, было слишком велико."
    "Потому было лишь вопросом времени, когда я попытаюсь распахнуть свои глаза, в надежде освободиться от оков мрака."
    "И как итог – ничего."
    stop sound fadeout 2
    #dodel

    #play music inversion_Breath1 
    "Всё та же бесконечная пустота, что словно засасывала меня всё глубже и глубже." 
    "Сколько бы я не пытался, результат был один."
    "Любопытство отошло на второй план. Теперь моим сознанием правили ужас и страх..."
    "И нет, дело даже не в том, что вокруг меня царит кромешный мрак. С этим, как раз, я более чем смирился."
    "Вопрос в другом: кто же всё-таки этот \"Я\"?"
    "Я совершенно не знаю, что за чертовщина здесь происходит!"
    zg "Где я, чёрт возьми?!"
    "Крикнул я в пустоту, но обратно ко мне, резонируя с противным писком в ушах, вернулась лишь равнодушная тишина."
    "Не знаю, надеялся ли я найти выход из загадочной тьмы, или же мне просто хотелось хоть чем-то себя занять."
    "Нет, мне всё же хотелось сбежать. "
    "Куда-нибудь из этой темноты..."
    "Как можно дальше."
    "Бездействие постепенно разъедало меня изнутри."
    $ renpy.pause (2)
    "Тут меня осенило."
    "Я ведь чувствую свои руки."
    "Ноги."
    "Пусть мои глаза здесь и не помощники, но я же могу идти!"
    "Авось, добреду куда.."
    "Я пошёл по наитию, выставив впереди себя руку, словно слепой."
    stop music fadeout 2
    play sound inversion_shagi
    "Тишину нарушали лишь мои шаги."
    "По крайней мере, слуха меня не лишили…"
    "Не знаю, сколько я брёл вот так..."
    "Может, пару минут, а может, и пару лет."
    "Но сколько бы я ни шёл, вокруг меня царила всё та же монотонная картина."
    "Отчаяние постепенно овладевало мной. Но зато от терзающей меня паники не осталось и следа."
    
    # "выключить писк и дыхание"
    play music inversion_pisk fadein 0.5 loop
    play sound zvuk_tjazhelogo_dyhanija fadein 1.0 loop
    "Чем дольше я вглядывался в мрак, тем больше мрак находил лазеек ко мне в душу."
    "Ещё и добавилось неприятное чувство в груди, словно меня что-то колит, усиливавшееся с каждым шагом..."
    
    #Смена БГ
    scene karidor_so_svetom with dissolve
    "И стоило мне только смириться со своим положением, как яркий луч пронзил мои отвыкшие от света глаза."
    "Совру, если скажу, что я не был этому рад. Я тут же бросился в сторону таинственного света, подарившего мне надежду."
    
    #Смена БГ"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene polnosty_belaya_komnata with dissolve
    "Этот луч вывел меня прямиком в незнакомую мне белую комнату."
    zg "Здесь есть кто-нибудь?"
    "Мой голос эхом пронёсся по загадочному помещению, отскакивая от светящихся белым стен."
    "Прежде чем изучать комнату, я решил осмотреть своё тело.{w} Может, удастся найти подсказку о том, кто я и как я сюда попал."
    "На мне был надет не то халат, не то смирительная рубашка, неуклюже завязанная на поясе." 
    "На груди, к моей радости, был прикреплён небольшой бейджик."
    th "Так вот что кололо меня в грудь.{w} Одной загадкой меньше."
    "На бейджике было фото незнакомого мне мужчины и, по видимому, его имя-фамилия."
    "Евгений Зощенко. Внизу также стояла дата — 2017 год."
    "Всякий раз, когда я пытался выбить из своей башки хоть капельку воспоминаний, в уши возвращался едкий писк, причиняя мне адскую боль."
    "Я совершенно не знал, я ли это на фото, или же кто-то решил надо мной подшутить, прикрепив именной бейдж совершенно другого человека." 
    "В сознание вновь начали возвращаться вопросы."
    th "Почему же я не помню ничего из своего прошлого?{w} Неужели амнезия?{w} Но из-за чего?!"
    "Я поспешно проверил голову на наличие каких-либо ушибов и повреждений.{w} Благо ничего найти мне не удалось."
    th "Ладно, в любом случае, стоя тут, я ничего не узнаю." 
    th "Надо двигаться дальше. Может, мне удастся найти хоть что-то, что меня заинтересует."
    th "Или даже кого-то..."
    
    scene beliy_karidor with dissolve
    $ renpy.pause (1)
    "Не знаю, сколько бы я так бесцельно ходил, настороженно оглядываясь по сторонам каждую секунду."
    "Я словно плутал по кругу. Белые стены уже начинали давить на психику своим противным свечением, от чего я даже испытал мимолётное желание вернуться в ту тёмную пустоту."
    "Но пути назад уже не было. Раз уж я начал идти, то дойду до конца!"
    
    scene beliy_karidor_s_dvery with dissolve
    # Фон белого каридора с дверью
    $ renpy.pause (1)
    "К счастью, моё старание окупилось, ведь в конце белоснежного коридора меня ждала дверь."
    "Любопытство снова взяло надо мной верх, и я распахнул её."
    
    #Смена БГ"
    scene komnata_prolog with dissolve
    "Передо мной открылся вид на таинственную комнату."
    "Я бы не сказал, что здесь было уютно, но необходимая мебель по типу кроватей, стульев и огромного стола, стоящего прямо в центре помещения, имелась."
    "Удивительно, но я не сразу заметил девушку, стоящую у одной из кроватей.{w} С души словно камень свалился..."
    
    # Появление саши
    show InversiaMOD sa semi_sideways thoughtful2 pioneer far with dissolve
    "Девушка выглядела огорчённой и даже озабоченной чем-то."
    "Но оно и понятно — я и сам напряжён сейчас."
    "На вид ей было всего лет шестнадцать-восемнадцать.. Совру, если скажу, что особой привлекательностью она не отличалась..." 
    
    "Я невольно залюбовался ей."
    "Волосы оттенка тёмного, выдержанного коньяка. Лицо приятной овальной формы, чуть вытянутое."
    "Довольно высокая для девушки, при моих ста восьмидесяти пяти она лишь сантиметров на десять-двенадцать ниже меня, если смотреть навскидку."
    "Фигура стройная и подтянутая. Хорошая грудь, размер третий, не меньше."
    "Мысленно я дал себе по рукам."
    th "И кто тут ещё озабоченный?.."
    "Сейчас совсем не до этого."
    "Тем не менее я не мог отогнать навязчивую мысль — на этот раз уже о себе самом."
    "Я так быстро и чётко, с первого взгляда оценил её. Особые приметы, вероятный уровень физической подготовки. Откуда это во мне?"
    th "Кем я был? Что я делал?"
    th "Может быть, я полицейский?"
    th "Топ. Я помню кто такой полицейский, что это за профессия, и, к примеру, разбудил бы меня кто посреди ночи пару дней спустя, бьюсь об заклад, я бы смог в точности пересказать приметы незнакомки."
    "Но при всём при этом..."
    "Я не помню..."
    "Кто же, собственно, Я?"
    "Усилием воли отогнав паническую атаку, я приказал себе заняться делом."
    "Пора наладить контакт с незнакомкой."
    
    #Спрайт нормал
    show InversiaMOD sa semi_sideways thoughtful2 pioneer normal with dissolve
    "Я аккуратно сделал пару шагов в её направлении.{w} Мне совсем не хотелось испугать её."
    scene komnata_prolog with vpunch
    show InversiaMOD sa front thoughtful pioneer normal with dissolve
    "Но как бы я не пытался двигаться бесшумно, девушка всё же услышала и резко повернулась ко мне. "
    
    "Теперь испугался уже я."
    "Чего-чего, а такой быстрой реакции я не ожидал. А ведь я даже не единого звука не издал..."
    "Не знаю, чьим умениям я удивлялся больше — своим или девушки, но в комнате тем временем повисло неловкое молчание."
    "Я уж хотел было заговорить с ней, но так и не нашёл что сказать."
    "Однако девушка взяла ситуацию в свои руки."
    show InversiaMOD sa front surprise pioneer normal with dissolve

    nn "Евгений..."
    "Неужели она знает кто я такой? Может, мне удастся выведать у неё что-то."
    zg "Мы знакомы?"
    show InversiaMOD sa bent_arm tears_on_eyes pioneer normal with dissolve

    "Но девушка лишь показала пальцем себе на грудь, где располагался такой же бейдж, как и у меня."
    "Честно говоря, я о нём уже и забыл.{w} На её табличке было написано имя — Александра."
    "Фото совпадало с её внешностью. И раз уж она ничего не стала спрашивать, скорее всего, фото на моём бейдже тоже достоверно..."
    "Я протянул девушке руку в знак знакомства." 
    
    show InversiaMOD sa front thoughtful pioneer normal with dissolve
    "Она, недоверчиво посмотрев на меня, всё же ответила."
    zg "Что ж, раз уж мы познакомились, не расскажешь, что здесь происходит?"
    "Я уселся на стул возле стола и решил как следует расспросить девушку.{w} Мне хотелось узнать как можно больше."
    
    show InversiaMOD sa front unsmile pioneer normal with dissolve
    sa "Прости, но я без понятия..."
    zg "Как давно ты здесь?"
    sa "Я не считала. Может, день, а может, и больше..."
    "С каждой секундой, что я смотрел на лицо девушки, мне всё больше казалась её внешность знакомой."
    "Словно я видел её раньше, но никак не могу вспомнить, где..."
    zg "Белый бесконечный коридор, — ты тоже через него проходила?"
    "Девушка еле заметно кивнула.{w} Похоже, мы с ней в одной лодке."
    "И чёрт его знает, как из неё теперь выбираться."
    hide InversiaMOD sa front unsmile pioneer normal with dissolve
    "Я решил осмотреть комнату. Мало ли удастся откопать что-то."
    "Саша неотрывно сверлила меня взглядом, словно боясь потерять из виду.{w} Это немного напрягало."
    "Я решил нарушить воцарившуюся тишину."
    show InversiaMOD sa front unsmile pioneer normal with dissolve
    zg "Ты осматривалась здесь?"
    show InversiaMOD sa front surprise pioneer normal with dissolve
    sa "Немного..."
    zg "Что же, тогда буду рад, если поможешь."
    "На намёки и джентльменство время тратить я не хотел, а лишняя пара рук не помешает."
    hide InversiaMOD sa front surprise pioneer normal with dissolve
    "..."
    # Скрытие спрайта 
    
    # Появление спрайта
    $ renpy.pause(4)
    show InversiaMOD sa front normal pioneer normal with dissolve
    "Вдвоём мы обыскали комнату вдоль и поперёк."
    "Много времени это, благо, не заняло, однако принесло свои плоды."
    "В руках у меня оказалась небольшая бумажка, которую я откопал в подушке одной из кроватей."
    show InversiaMOD sa front smile pioneer normal with dissolve
    "Я сразу же показал Саше свою находку. У неё на лице промелькнула еле заметная улыбка."
    show InversiaMOD sa front normal pioneer normal with dissolve
    
    zg "Лишь за столом переговоров открывается истина."
    "Послание оказалось куда скромнее, чем я мог себе представить. Это разочаровало."
    show InversiaMOD sa semi_sideways thoughtful pioneer normal with dissolve
    sa "Как думаешь, что это значит?"
    zg "Думаю, истина — это выход отсюда. А вот стол переговоров..."
    "Мы одновременно посмотрели на тот самый большой стол, что стоял посреди комнаты."
    "Я хотел было поднять его, но у меня не получилось." 
    "Он был то ли прибит к полу, то ли был чертовски тяжёлым."
    zg "Значит, есть что-то на нём..."
    "И ведь правда, на одной из его ножек располагалась незаметная кнопка, которую я еле смог нащупать."
    "После нажатия на неё на столе открылись непонятные ячейки, хаотично разбросанные по всей его площади."
    show InversiaMOD sa semi_sideways shock pioneer normal with dissolve
    sa "Это рисунок!"
    "Воскликнула Саша. А ведь точно, его только нужно собрать..."
    ".{w=0.1}.{w=0.1}."

    show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    "Отлично! Мне всё же удалось решить этот ребус, пускай я и потратил на это прилично времени."
    "После того как картинка собралась воедино, одна из стен сместилась вверх, открывая ещё одну загадочную дверь."
    
    show InversiaMOD sa semi_sideways unsmile pioneer normal with dissolve
    "Я уже хотел открыть её, но Саша вдруг села на кровать и отрешённо посмотрела куда-то вдаль."
    "Похоже, ей было тяжело собраться с мыслями."
    "Надо было помочь ей сконцентрироваться. Поэтому я подошёл к Саше и сел рядом."
label vibor_prolog:
    scene komnata_prolog with dspr
    show InversiaMOD sa semi_sideways unsmile pioneer close with dissolve
    sa "Я ничего не понимаю, одни вопросы и ни одного ответа. Только эти чёртовы загадки..."
    zg "Может, это проверка? Да и если мы остановимся на полпути, мы многое потеряем."
    zg "Я не буду настаивать. Если хочешь, ты можешь остаться."
    "Девушка молча смотрела в пол и лишь спустя пару минут прошептала."
    
    show InversiaMOD sa front crying pioneer close with dissolve
    sa "Решай ты..."
    "Ей и правда тяжело сейчас, раз она позволила выбирать незнакомцу..."
    "Но если мы останемся здесь, то ни черта не добьёмся..."
    
#Выбор."
    menu:
        "Пойти вместе":
            jump prodolzhenie_inv
        "Пойти одному":
            jump bad_end_inv


label prodolzhenie_inv:
    ".{w=0.1}.{w=0.1}."
    scene komnata_prolog with dspr
    show InversiaMOD sa front embarrassed pioneer close with dissolve
    zg "Думаю, да, больше же некуда."
    "Я, конечно, не уверен, но куда ещё идти-то, в конце концов?"
    "Мы неспешно открыли дверь. Войдя в неё, мы снова оказались в тёмной комнате. {w} И стоило нам моргнуть, как..."
    show blink
    $ renpy.pause(0.5, hard=True)
    scene black with dissolve
    jump day1_inversia

label bad_end_inv:
    #"КАТАПУЛЬТНАЯ КОНЦОВКА"
    scene komnata_prolog with dspr
    show InversiaMOD sa front surprise2 pioneer close with dissolve
    zg "Пока ты останешься здесь."
    zg "Двигаться вперёд вместе слишком опасно."
    zg "Я пойду вперёд, разведаю обстановку."
    zg "Ты тут не пропадёшь, не амбар какой-нибудь всё-таки."
    zg "Полноценная комната."
    zg "Кровать, стол, может, и поесть где-нибудь, что-нибудь найдёшь."
    
    show InversiaMOD sa front unsmile pioneer close with dissolve
    "Повисла неловкая тишина."
    zg "Ну... Я пошёл."
    "Саша даже не подняла голову."
    
    hide InversiaMOD sa front unsmile pioneer close with dissolve
    "Я сделал несколько шагов к двери, и услышал сзади её тихий шёпот."
    sa "Я сгнию здесь..."
    "Я обернулся и удивлённо посмотрел на неё."
    
    show InversiaMOD sa front crying pioneer close with dissolve
    sa "Зарубки буду на стене делать..."
    sa "Ждать..."
    sa "Может, придёт кто..."

    #"“звук: женские всхлипывания”"
    play music zenskiu_plach fadein 3
    "Саша всхлипнула."
    sa "Спасёт..."
    zg "Саша..."
    zg "Ты останешься здесь, так безопаснее. Я пойду вперёд. Узнаю что к чему."
    "Я старался говорить с ней ласково, как с маленьким ребёнком."
    th "Надо успокоить её."
    th "Надеюсь, мой тон не слишком снисходителен."
    zg "Мы же решили, вместе."
    stop music
    "Саша вскинула голову."

    show InversiaMOD sa front angry pioneer close with dissolve
    sa "Это ты решил!"
    sa "Не я!"
    "С неожиданным гневом и отчаянием прокричала девушка."
    "Я почувствовал, что начинаю закипать в ответ."
    show InversiaMOD sa front unsmile pioneer close with dissolve
    zg "Александра."
    "Как можно спокойней сказал я."
    zg "Соберись."
    zg "Перестань говорить глупости, всё с тобой будет хорошо."
    show InversiaMOD sa front crying pioneer close with dissolve
    "Я поневоле начал язвить."
    "То ли оттого, что сам глубоко внутри был до чертиков напуган, то ли оттого, что в словах Саши я почувствовал... наглость?"
    th "Я в одной лодке с ней."
    th "Напуганный, ничего не помнящий."
    th "Что она возомнила о себе?"
    th "Попыталась спихнуть всю ответственность на меня."
    th "А когда я решил — и решил в её пользу, дав ей возможность остаться здесь в безопасности, а не тащиться со мной неизвестно куда, — она, видите ли, недовольна."
    th "Разнылась ещё."
    th "Безвольная клуша."
    th "А я ведь на секунду подумал, что мы похожи, увидев уровень её реакции и бдительности."
    th "Дурак наивный."
    zg "Чего ты боишься, Сашенька?"
    zg "Думаешь, злые дяди вломятся с пистолетами, утащат куда?"
    zg "Может, оно и в самом деле к лучшему. Всяко получше будет, чем сидеть здесь в безысходности."
    
    show InversiaMOD sa front crying2 pioneer close with dissolve
    "Саша плакала уже навзрыд."
    "Я понимал, что стоит остановиться, я вёл себя как последний подонок."
    "Измываться над плачущей девушкой, перепуганной неизвестностью, окружающей её…"
    "Моя самооценка стремительно падала куда-то на дно той тёмной пустоты."
    "Следом за моей совестью."
    "Мне нужно было остановиться."
    "Но я не мог. Просто не мог."
    "Весь мой страх, вся злость на моё положение вырвались наружу и затопили рассудок."
    "Саша изо всех сил вцепилась тонкими пальчиками в простыню кровати, на которой сидела."
    sa "Ты.{w=0.1}.{w=0.1}.{w} ТЫ..."
    "Повторяла и повторяла она."

    show InversiaMOD sa front unsmile pioneer close with dissolve
    "Затем девушка вдруг подняла голову, посмотрела на меня заплаканными глазами и совершенно спокойно сказала:"
    sa "Иди."
    sa "Я тут сама как-нибудь."
    sa "Справлюсь...{w=1} Иди, раз уж собрался."
    "Она поёрзала на кровати."
    sa "Чая, как видишь, нет — попили бы на дорожку."

    show InversiaMOD sa front embarrassed pioneer close with dissolve
    "Она усмехнулась."
    sa "Иди."

    hide InversiaMOD sa front embarrassed pioneer close with dissolve
    "Забравшись с ногами на кровать и обхватив себя руками, она отвернулась от меня."
    "Я, не оглядываясь, пошёл прочь."
    "И мне было всё равно, смотрела ли она мне вслед."
    $ renpy.pause (2)
    scene creepy_komnata with dissolve
    "Я уже практически добрался до двери, когда обратил внимание, что на противоположной от выхода стене виднеется еле заметный просвет."
    "Я не придал этому никакого значения, вместо этого предположив, что просвет остался после ремонта."
    $ renpy.pause (2)
    
    # тревожная музыка типа как в пиле :3
    play music music_list["orchid"]
    th "Стоп."
    th "Ремонт? Какой ещё ремонт?"
    th "В таком странном месте, жуткой комнате посреди чёрной пустоты?"
    
    # Звук: оглушающий скрип
    play sound sfx_carousel_squeak
    "Неожиданно сзади раздался противный, калечащий уши скрип."
    scene chernaja_komnata_s_dvery with vpunch
    "Я молниеносно обернулся."
    "На месте просвета образовалась дверь!"
    "Готов поклясться, секунду назад тут не было ничего!"
    show mi rage pioneer with dissolve
    "Из образовавшегося прохода вышла девушка."
    # По желанию добавить play sound sfx_scary_sting
    "Я оцепенел."
    "В её руке был пистолет!"
    "Каким-то внутренним чутьём я понял, что это настоящее боевое оружие."
    "Хоть незнакомка и держала его чуть небрежно, расслабленно, словно малыш держащий в руке хлопушку или сахарную вату."
    hide mi rage pioneer with dissolve
    show dv rage pioneer with dspr
    "А её лицо.."
    hide dv rage pioneer with dspr
    show sl angry pioneer with dspr
    "ЕЁ ЛИЦО!"
    hide sl angry pioneer with dspr
    show mz rage pioneer with dspr
    "Оно менялось."
    hide mz rage pioneer with dspr
    show mt rage pioneer with dspr
    "Каждую секунду!"
    hide mt rage pioneer with dspr
    show dv rage pioneer with dspr
    "Передо мной стояла рыжая девушка с задиристым взглядом."
    hide dv rage pioneer with dspr
    show us angry pioneer with dspr
    "Секунда — и лицо сменилось на совсем ещё девочку, с ясными синими глазами."
    hide us angry pioneer with dspr
    show un rage pioneer with dspr
    "Ещё секунда — печальное зеленоглазое лицо, полное вселенской тоски."
    hide un rage pioneer with dspr
    show sl angry pioneer with dspr
    "Миг — и её сменила валькирия, чьё лицо обрамляли золотые косы."
    hide sl angry pioneer with dspr
    show sh rage pioneer with dspr
    "Затем — и вовсе мужское лицо, строго смотрящее из под очков."
    hide sh rage pioneer with dspr
    show mz rage pioneer with dspr
    "Незнакомка нарушила молчание."
    hide mz rage pioneer with dspr
    show mz rage pioneer with dspr
    nn "Самое глупое решение из всех — разделиться."
    hide mz rage pioneer with dspr
    show mi rage pioneer with dspr
    "Она посмотрела на меня полубезумным взглядом."
    hide mi rage pioneer with dspr
    show sl angry pioneer with dspr
    nn "Ты что, кино не смотришь, зайчик?"
    hide sl angry pioneer with dspr
    show dv rage pioneer with dspr
    "Её взгляд прожигал меня насквозь. Мысли в голове словно окаменели."
    hide dv rage pioneer with dspr
    $ renpy.pause (2)

    show mi rage pioneer with dspr
    nn "Впрочем, ничего личного."
    hide mi rage pioneer with dspr
    "Она со скоростью света вскинула пистолет."
    show un rage pioneer with dspr
    zg "Подожди..."
    hide un rage pioneer with dspr
    "Только и успел промямлить я..."
    scene black with dissolve2
    show blink 
    #"Звук выстрела"
    play sound vistrel_iz_pistoleta
    #СМЭРТ :)
    $ renpy.pause (5)
    #И звук ачивки)
    play sound sfx_achievement
    show Achivement Prolog at achievement_trans
    with dspr
    $ renpy.pause (3)
    hide Achivement Prolog
    $ renpy.pause (5)
    jump vibor_prolog
    return 0