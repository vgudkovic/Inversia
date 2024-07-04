init:
#sfx
    $ inversion_pisk = "mods/inversia/sfx/inversion_pisk.mp3"
    # $ music inversion_Breath1 = "mods/inversia/music/inversion_Breath1.wav"
    $ inversion_shagi = "mods/inversia/sfx/shagi_s_ekhom.mp3"
    $ zvuk_tjazhelogo_dyhanija = "mods/inversia/sfx/zvuk_tjazhelogo_dyhanija.mp3"
    $ zenskiu_plach = "mods/inversia/sfx/zenskiu_plach.mp3"
    $ vistrel_iz_pistoleta = "mods/inversia/sfx/vistrel_iz_pistoleta.mp3"

#--------------

    #bg/cg
    image bg karidor_so_svetom = "mods/inversia/bg/karidor_so_svetom.png"
    image bg polnosty_belaya_komnata = "mods/inversia/bg/polnosty_belaya_komnata.jpg"
    image bg beliy_karidor_s_dvery = "mods/inversia/bg/beliy_karidor_s_dvery.jpg"
    image bg beliy_karidor = "mods/inversia/bg/beliy_karidor.jpg"
    image bg komnata_prolog = "mods/inversia/bg/komnata_prolog.jpg"
    image bg bad_lager = "mods/inversia/bg/bad_lager.jpg"

#--------------
    # Image
    image Achivement Prolog = "mods/inversia/images/Achivement Prolog.jpg"


#--------------
    # Sprites

    # sa - Саша 
    # Дальность - далеко (Far)
    # bent_arm - Согнутая рука

    image InversiaMOD sa bent_arm angry pioneer far = "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png"
#    image InversiaMOD sa bent_arm angry pioneer far = ConditionSwitch(
#   "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
#    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
#    True,im.Composite((296, 1080), (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png", (0,0), "mods/inversia/sprites/sa/far/bent_arm/sa_bent_arm_angry.png") )

