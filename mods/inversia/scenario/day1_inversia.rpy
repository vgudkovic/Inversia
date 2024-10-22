######################День 1:
# init:
    # define zg = Character ('Женя', color = "#00deff", what_color = "#f1d076")
    # define nn = Character ('Незнакомка', color = "#00deff", what_color = "#f1d076")
    # define sa = Character ('Саша', color = "#00deff", what_color = "#f1d076")
    # define achive_inversia = "mods/inversia/images/achive_inversia.png"

label day1_inversia:
    $ backdrop = "days"
    $ save_name = (u"Инверсия. \nДень 1")
    $ day_time()
    $ persistent.sprite_time = 'day'

    $ renpy.pause(2.5)
    
    scene black with fade2
    play music music_list["you_lost_me"]
    "Голова очень сильно болела. Я даже пошевелиться не мог — настолько невыносима была боль{w=0.3}.{w=0.3}.{w=0.3}." 
    "Какое-то время я не ощущал ни хода времени, ни пространства вокруг." 
    "Словно меня отправили в открытый космос без скафандра."
    "Темно так, будто все звёзды на небосводе погасли{w=0.3}.{w=0.3}.{w=0.3}." 
    "Хотя, может быть, я просто закрыл глаза?" 
    "Я попытался открыть их, но безуспешно.{w} Вдруг я услышал голос:"
    sa "Проснись, проснись!"
    "После этих слов я почувствовал, что тело наконец начало меня слушаться.{w} Я смог открыть глаза."
    show unblink
    $ renpy.pause(1)
    
    scene int_bus:
        blur 100
        linear 1 blur 20
        linear 2 blur 0
    play music music_list["no_tresspassing"]
    "В них ударил яркий свет, и я инстинктивно зажмурился. Проморгавшись и привыкнув к нему, я смог увидеть Сашу. Девушка сидела впереди на одном из кресел автобуса."
    sa "Стоп! Кресло? Автобус? Где это мы?"
    show InversiaMOD sa semi_sideways thoughtful pioneer close with dissolve
    "Я поднялся со своего кресла и обратился к Саше"
    zg "Саша, а где это мы, собственно?"
    sa "Могу сказать, что точно не в том белом мире{w=0.3}.{w=0.3}.{w=0.3}."

    show InversiaMOD sa semi_sideways shock pioneer close with dissolve
    "Саша осмотрела себя, свои руки и одежду. Затем перевела взгляд на меня. Бледная слегка; видно, что немного нервничает. Но держится молодцом."
    zg "Судя по всему, мы в салоне какого-то автобуса{w=0.3}.{w=0.3}.{w=0.3}."
    sa "Нет, блин, на теннисном корте!"
    
    show InversiaMOD sa semi_sideways smile pioneer close with dissolve
    "Язвительно, но без малейшей агрессии бросила Саша."
    sa "Ты в окно глянь."
    sa "Прямо пейзаж неизвестного художника."

    show bg ext_road_day with dissolve
    "Посмотреть в самом деле нашлось на что. За окном ярко светило жаркое, летнее солнце." 
    "После жуткой белизны, откуда мы с Сашей вырвались, ласковый свет солнышка был настоящим бальзамом на душу." 
    "Впереди виднелось шоссе, уходящее вдаль, куда-то за горизонт."
    "Похоже, по нему мы и добрались сюда." 
    hide bg ext_road_day with dissolve
    
    show bg ext_camp_entrance_day with dissolve
    "Рядом расположились ворота."
    "Детский лагерь? На их страже стояли две статуи, изображающие детей в приметной, запоминающейся униформе."
    "В памяти всплыли слова. Пионеры. Пионерия." 
    "Я читал что-то подобное. Когда-то, где-то." 
    "По смутным обрывкам воспоминаний, что роились в моей голове, я рассудил, что пионерия была делом далёкого прошлого."
    play music music_list["mystery_girl_v2"]
    "Лагерь старый уже, наверное."
    "Надеюсь, хоть не заброшенный; может, удастся встретить людей и хотя бы отчасти прояснить нашу ситуацию."
    scene int_bus with dissolve
    show InversiaMOD sa semi_sideways shock pioneer close with dissolve
    "Тем временем Саша осмотрела себя ещё раз и подытожила"
    sa "Автобус выглядит совсем новым{w=0.3}.{w=0.3}.{w=0.3}. Изнутри, по крайней мере."
    zg "Что ж, уже хорошо{w=0.3}.{w=0.3}.{w=0.3}. Может, тогда выйдем наружу и осмотрим местность?"
    sa "А больше вариантов-то и нет, пошли."
    stop music

    #*звук:ветер*
    play voice ambience_cold_wind_loop fadein 2.0
    #Фон: Дорога*
    scene bg ext_road_day with dissolve
    th "Как только мы вышли из автобуса, нас чуть не сбил с ног сильный порыв ветра."
    "Мы прикрыли лицо руками."
    $ renpy.pause(2, hard=True)

    stop music fadeout 2.0
    "Когда ветер поутих, мы смогли подойти поближе к воротам."

    scene ext_camp_entrance_day with dissolve
    show InversiaMOD sa front normal pioneer close with dissolve
    zg "Давай осмотрим тут всё{w=0.3}.{w=0.3}.{w=0.3}. Ты влево, я вправо. "
    sa "Хорошо. Хоть разведаем, что к чему."

    hide InversiaMOD sa front normal pioneer close with dissolve
    "Мы пошли по выбранным направлениям."

    "Пока я шёл, с одной стороны моему взору открывалась кирпичная стена, заросшая стебельками лоз и мха, а с другой — дорога, простирающаяся за горизонт." 
    "По виду я не мог понять, насколько давно эта стена была построена." 
    "Но нельзя не отметить того, что хоть на ней уже и расстелился ковёр из зарослей, на самой поверхности повреждений не было."
    
    show InversiaMOD sa front normal pioneer close with dissolve
    zg "Да. А для чего здесь эти ворота?"
    sa "«Совёнок».{w=0.2}.{w=0.2}.{w} Не знаю, но похоже на какой-то лагерь{w=0.3}.{w=0.3}.{w=0.3}."
    "Она показала на статуи пионеров и надпись на воротах: «Пионерлагерь»."
    zg "Тогда, думаю, нам стоит пойти туда. Может, нам хоть расскажут кто мы?"
    "Я подавил нервный смешок"
    
    show InversiaMOD sa front thoughtful pioneer close with dissolve
    sa "Вероятность есть."
    "Саша ответила немного отстранённо."
    "Судя по всему, её полностью захватила жажда действий."
    "Жажда ответов."
    scene ext_camp_entrance_day:
        ease 1 zoom 1.3 xcenter 0.5 ycenter 0.5
    $ renpy.pause(1, hard=True)
    play music music_list['door_to_nightmare'] fadein 3
    "Мы подошли к воротам. Я попробовал открыть их, но от моего прикосновения металл словно переместился во времени." 
    
    #Резкое приближение и возвращение камеры. Медленно заменяется фон с обычных ворот на старые.*
    scene bad_lager:
        zoom 2 xcenter 0.5 ycenter 0.5
        blur 80
        linear 0.5 blur 10
        linear 1 blur 0 
    "Ручка сильно проржавела и рассыпалась. Я отдёрнул руку и отбежал назад."
    play sound sfx_scary_sting
    scene bad_lager:
        zoom 2 xcenter 0.5 ycenter 0.5
        ease 0.3 zoom 1 xcenter 0.5 ycenter 0.5
    zg "Что за{w=0.3}.{w=0.3}.{w=0.3}. "
    "Только и смог выговорить я. "
    th "Что за чертовщина?"
    "Небо поменяло цвет, и я увидел, что и ворота, и ограда очень сильно постарели: облезла краска, фасад стены потрескался, буква «Ё» исчезла."
    th "Какого?!"
    show blink
    scene black with dissolve2
    "Я зажмурился, но вдруг кто-то потряс меня за плечо:"
    
    sa "Ауу,{w=0.3} ЖЕНЬ!{w=0.3} Очнись!" # vopr
    scene ext_camp_entrance_day:
        ease 1 zoom 2 xcenter 0.5 ycenter 0.5
        blur 100
        linear 0.5 blur 10
        linear 1 blur 0 
        ease 1.5 zoom 1 xcenter 0.5 ycenter 0.5
    hide blink
    show unblink



    #*April Rain-Chiral Allergy**" dodel
    # Появление саши после Фона
    $ renpy.pause (4, hard=True)
    show InversiaMOD sa front scared pioneer close:
        # ease 0.5 zoom 2 
        xcenter 0.5 ycenter 0.5
        blur 100
        linear 1 blur 10
        linear 0.5 blur 0 
        # ease 0.5 zoom 1 xcenter 0.5 ycenter 0.5
    "Я резко открыл глаза. Тут же взглянув на ворота, я увидел, что они снова в порядке."
    sa "Что случилось с тобой?"
    zg "Походу, этот лагерь меня невзлюбил{w=0.3}.{w=0.3}.{w=0.3}."
    sa "В каком смысле?"
    sa "Ты в порядке вообще?"
    sa "Голова не кружится?"
    zg "Ты же видела, ворота рассыпались!"
    sa "Нет, ворота как ворота, посмотри!"

    show InversiaMOD sa front shock pioneer close with dissolve
    sa "Стояли как стоят. Ты чего, Женя?{w=0.3}.{w=0.3}.{w=0.3}."
    "Саша с тревогой посмотрела на меня."
    "И вправду, ворота как ворота{w=0.3}.{w=0.3}.{w=0.3}. Ничего не постарело."
    zg "Походу, мне от страха померещилось{w=0.3}.{w=0.3}.{w=0.3}."
    # play sound shagi_s_ekhom Доработать
    show InversiaMOD sa front normal pioneer close with dissolve
    "Вдруг я услышал шаги."
    sa "Они исходят из-за ворот."
    stop sound fadeout 0.5

    play sound sfx_carousel_squeak 
    "Шаги стихли, и ворота открылись. "

    #*Постепенное P и такое же постепенное f Timid Girl**" # vopr
    play music music_list['timid_girl'] fadein 1
    
    show InversiaMOD sa front normal pioneer close:
        ease 0.5 xcenter 0.8
    $ renpy.pause(0.5)
    
    show sl normal pioneer with dissolve 
    "Из них вышла девушка."
    "Я точно не ожидал тут увидеть девушку, да и ещё красивую такую."
    "Ну и ну. "
    "Она подошла к нам и поздоровалась"
    slp "Привет, вы, наверное, нове{w=0.3}.{w=0.3}.{w=0.3}." 
    # *кашель* 
    play sound zhenschina_kashleet
    show sl normal pioneer:
        ease 0.2 ycenter 0.55
        ease 0.6 ycenter 0.50
        pause 1.0
        ease 0.2 ycenter 0.55
        ease 0.6 ycenter 0.50
    extend " только что приехали?"
    #Приближение*"
    show sl normal pioneer close with dissolve
    "Я подошёл к ней."
    zg "Да{w=0.3}.{w=0.3}.{w=0.3}."
    slp "Что же, тогда добро пожаловать!"
    show sl smile pioneer close with dspr
    "Она одарила нас широкой, задорной улыбкой. "
    show InversiaMOD sa semi_sideways thoughtful pioneer close with dissolve
    sa "А нам куда идти? Мы тут впервые."
    slp "Вам нужно к Ольге Дмитриевне. Сейчас идёте прямо, доходите до площади, дальше будут домики. Ну, спрóсите там у других, где Ольга Дмитриевна."
    slp "А мне надо идти, вам понятно?"
    show InversiaMOD sa semi_sideways smile pioneer close with dspr
    sa_zg "Да{w=0.3}.{w=0.3}.{w=0.3}. вроде." #dodel
    "Хоть она и объяснила очень доходчиво, я ничего не понял. Думаю, не стоит задерживать эту барышню. "
    slp "Я побежала, меня ждут дела, удачи вам!"
    #*Звуки ворот**"
    play sound sfx_carousel_squeak 

    show sl smile pioneer close:
        ease 1 xcenter 1.3
        pause 1.0
    show InversiaMOD sa semi_sideways smile pioneer close with dspr
    hide sl smile pioneer close with dissolve
    "И она скрылась за воротами, её золотые косы весело развевались под летним ветерком." 
    "Мы с Сашей подошли ближе. Ручки на воротинах были целыми."
    
    show InversiaMOD sa semi_sideways thoughtful2 pioneer close with dspr
    sa "Всё это о-о-очень странно{w=0.3}.{w=0.3}.{w=0.3}."
    zg "Мне тоже не нравится это место, но бежать нам некуда." 
    zg "Я не вижу другого выхода, кроме как идти туда."
    
    #конец музыки
    stop music fadeout 0.5
    "Я показал на ворота.{w} Саша кивнула." 
    # Звук испарения или чёт еще для автобуса
    play sound sfx_put_sugar_cart
    $ renpy.pause(1)
    
    #Задник ворот без автобуса*"
    show bg ext_no_bus with dissolve
    extend " Вдруг мы услышали шум и оглянулись — автобус исчез."
    
    play sound sfx_suspence_bang
    hide bg ext_no_bus with dspr
    scene ext_camp_entrance_day with dissolve
    show InversiaMOD sa front shock pioneer close with dissolve
    sa "Художественный фильм.{w=0.2}.{w=0.2}."
    zg "Да. Именно это."
    "Стоп."
    zg "Ты тоже помнишь этот фильм?"

    show InversiaMOD sa front surprise2 pioneer close with dissolve
    sa "Д-да{w=0.3}.{w=0.3}.{w=0.3}."
    "Саша растерянно поглядела на меня."
    "Я решил подбодрить её."
    zg "Видишь, потихоньку память возвращается."
    zg "Глядишь, скоро всё вспомним помаленьку{w=0.3}.{w=0.3}.{w=0.3}."

    show InversiaMOD sa front smile pioneer close with dissolve
    "Саша улыбнулась мне, но ничего не сказала."
    #*Farewell to the past**"
    play music music_list['farewell_to_the_past_full'] 
    #фон: Остановка (без автобуса)*"
    show bg ext_no_bus with dissolve
    "Автобус исчез, конечно, неизвестно куда и как"
    hide bg ext_no_bus with dissolve
    show bg ext_road_day with dissolve
    extend " , но при этом он открыл прекраснейший вид на поле.{w} Вид просто невероятный!"
    hide bg ext_road_day with dissolve
    #поворот к Саше и фон ворот*"
    scene ext_camp_entrance_day with dissolve
    show InversiaMOD sa front smile pioneer close with dissolve
    sa "Пошли к этой загадочной Ольге, Жень."
    zg "Пошли, пора уже разобраться, наконец, что к чему! "
    "Мы прошли через ворота и выдвинулись к упомянутой девушкой площади."
    scene bg ext_clubs_day at walking_inv with dissolve
    $ renpy.pause(1)
    
    scene bg ext_clubs_day with dspr
    "По дороге нам встретилось здание, похожее на склад, а подойдя к нему ещё ближе, мы смогли разглядеть вывеску: «Клубы»."
    
    show InversiaMOD sa semi_sideways normal pioneer close with dissolve
    zg "Похоже, здесь кружки по интересам обосновались."
    sa "Того же мнения, но нам надо идти к"
    play sound devushka_zevnula volume 0.8
    extend " О{w=0.1}-О{w=0.1}-О{w=0.1}-Ольге."
    "Зевок оказался заразным"
    play sound paren_zevnul volume 0.8
    extend ", и я тоже подхватил его. Мы пошли дальше."
    
    #ФОН: Домики*"
    scene bg ext_houses_day at walking_inv with dissolve
    "Вскоре нас встретили “бочки” и “треуголки” — так можно охарактеризовать домики, в которых кто-то жил{w=0.3}.{w=0.3}.{w=0.3}. наверное." 
    "Странные, однако, домики{w=0.3}.{w=0.3}.{w=0.3}." 
    "Мы шли мимо них, всюду пели птицы, а ветерок щекотал мне нос и заставлял непослушные волосы колыхаться." 
    "Красоту этого места нельзя не отметить."
    
    #Фон: Площадь*"
    scene bg ext_square_day at walking_inv with dissolve
    $ renpy.pause(1)
    scene bg ext_square_day with dissolve
    "До места назначения мы дошли быстро — похоже, что перед нами была площадь, но на ней никого не было."
    zg "Поразительно, ГЕНИАЛЬНО!! И у кого можно узнать куда идти?"
    show InversiaMOD sa front normal pioneer close with dissolve
    sa "Можно подождать — например, на скамейке посидеть."
    show InversiaMOD sa front grin pioneer close with dspr
    sa "Авось подкараулим кого."
    zg "У тебя сейчас такое лицо кровожадное было."
    "Засмеялся я."
    sa "Ну а что? Поймаю и буду допрашивать с пристрастием!"
    sa "Покуда не организуют мне кровать и приличный ужин."

    show InversiaMOD sa front smile pioneer close with dspr
    sa "Я бы чайку сейчас выпила{w=0.3}.{w=0.3}.{w=0.3}."
    "Мечтательно сказала Саша."
    sa "Только не крепкого, а то не усну."
    zg "А кофе любишь?"

    show InversiaMOD sa front scared pioneer close with dspr
    sa "Не-е-ет."
    "Скривила она носик."
    show InversiaMOD sa front surprise2 pioneer close with dspr
    sa "Да и чай крепкий как-то не очень,{w=1} фи."
    sa "Не понимаю тех, кто по три пакетика чая заваривает." 
    sa "Это уже чифир какой-то, а не приятный напиток для утренней бодрости."
    zg "Я вот кока-колу люблю{w=0.3}.{w=0.3}.{w=0.3}."

    show InversiaMOD sa front thoughtful pioneer close with dspr
    $ renpy.pause(0.5)
    
    show InversiaMOD sa front normal pioneer close with dspr
    "Саша прыснула."
    sa "С этим облом. Вряд ли нам удастся добыть бутылку другую в пионерском лагере, буржуйский напиток-таки!"
    
    show InversiaMOD sa semi_sideways thoughtful2 pioneer normal with dissolve
    "Неожиданно девушка стала крайне серьёзной."
    sa "Женя, ты ведь понимаешь, что мы могли провалиться в прошлое?"
    sa "Я не помню ни в каком году родилась, ни в каком году свалилась в то белое пространство, но я уверена в одном."
    sa "Пионеры — это прошлый для нас век."
    "Я помолчал немного, прежде чем ответить."
    zg "Рано пока делать выводы, Саш."
    zg "Не торопись, давай оглядимся, проверим, что к чему."

    show InversiaMOD sa semi_sideways thoughtful pioneer normal with dissolve
    "Саша немного расслабилась."
    sa "Да уж, чем строить безосновательные теории, давай немного посидим отдохнём."
    zg "Пока остаётся только это{w=0.3}.{w=0.3}.{w=0.3}."
        #Фон: Скамья с Сашей*" Доработать
    show None_BG_INV with dissolve
    "Сев на скамейку, мы наконец расслабились, и Саша спросила:"
    sa "Что же с нами такое произошло, что мы забыли себя? Почему?"
    #   show ext_sky_7dl with dissolve
    zg "Да кто его знает{w=0.3}.{w=0.3}.{w=0.3}."
    "Ответил я, глядя на небо."
    zg "Может, мы находимся в коме и видим своё подсознание, а может, мы умерли и сейчас в раю." 
    "Всё может быть, всё может быть{w=0.3}.{w=0.3}.{w=0.3}."
    #   hide ext_sky_7dl with dissolve
    #тёмный экран* *Фон: спящая Саша на скамье.* " Доработать
    "Мы сидели так, наверное, уже минут десять – пятнадцать, я то и дело поглядывал на Сашу."
    "Она мирно спала. Выглядело это умилительно. "
    th "Похоже, что наше приключение её сильно измотало."
    hide None_BG_INV with dissolve
    "Я тоже был измотан, однако в сон не клонило."
    "Поэтому я решил изучить площадь. "
    "Большая статуя видного деятеля этого лагеря вроде бы{w=0.3}.{w=0.3}.{w=0.3}. "
    "На постаменте было выгравировано имя: «Генда»."
    zg "Да уж{w=0.3}.{w=0.3}.{w=0.3}."
    "Жара сильно выматывала меня. Я присел обратно на скамейку, ненадолго закрыл глаза и уснул."
    stop music fadeout 2.5
    #Глаза закрылись.*
    show blink
    
    #Резкое открытие глаз* 
    #Звук крика / Доработать
    scene bg ext_square_day with vpunch
    "Разбудил меня крик, поднявшийся на площади."
    #Awakening Power
    play music music_list['awakening_power'] fadein 1
    "Позади статуи кто-то ругался — а именно две девушки, если судить по голосам." 
    "Краем глаза я заметил, что Саша тоже проснулась. "
    #   Появление ОД и Алисы* Фон ссоры Алисы и ОД
    show None_BG_INV with dissolve
    "Обойдя статую, мы увидели этих двоих. "
    "Одна из них — старшая — скорее всего, была вожатой, а та, что помладше, — пионеркой." 
    "Мы подошли поближе и смогли услышать разговор"
    mtp "Ты опять отлыниваешь от своих обязанностей?!"
    dvp "Нет. Я уже всё сделала, вот и отдыхаю!"
    mtp "Не ври!!! Славя мне сказала, что ты сбежала с работ на клумбах!   	"
    dvp "Вот ведь{w=0.3}.{w=0.3}.{w=0.3}."
    mtp "Так что ты идёшь помогать на кухне!"
    dvp "Но Ольга Дмитриевна{w=0.3}.{w=0.3}.{w=0.3}."
    mt "Никаких «но», Алиса! Пошла в столовую!"
    dv "Хорошо{w=0.3}.{w=0.3}.{w=0.3}."
    stop music fadeout 0.5
    #Алиса уходит, остаётся ОД*
    $ renpy.pause(0.5)
    hide None_BG_INV with dissolve
    
    #My Daily Life
    play music music_list['my_daily_life'] fadein 1
    "Насупившись, она пошла мимо нас в неизвестном направлении — скорее всего, к той самой столовой." 
    "Мы подошли к Ольге."
    scene bg ext_square_day with dissolve
    show InversiaMOD sa semi_sideways normal pioneer normal at right with dissolve
    show mt sad panama pioneer at left with dissolve
    sa "Здравствуйте, вы же вожатая?"
    show mt sad panama pioneer with dspr
    mt "Да, я Ольга Дмитриевна. А вы Александра и Евгений?"
    sa_zg "Да!"
    mt "Тогда пойдёмте за мной. Выдам вам ключи от домиков, и вы сможете отдохнуть после поездки."
    
    #Фон: дорога с домиками*"
    hide InversiaMOD with dissolve
    hide mt with dissolve
    "Мы последовали за вожатой."
    scene bg ext_houses_day at walking_inv with dissolve
    $ renpy.pause(1.5)
   
    #Фон: Домик ОД*"
    scene bg ext_house_of_mt_day at walking_inv with dissolve
    $ renpy.pause(0.3)
    scene bg ext_house_of_mt_day with dspr
    
    "Пройдя сквозь ряды обычных домиков, мы подошли к другому — с зелёным фасадом, что был едва видим сквозь окружавшую его сирень."
    "Ольга зашла внутрь." 
    th "Видимо, тут она и живёт." 
    show mt normal pioneer at center with dissolve
    show InversiaMOD sa semi_sideways normal pioneer normal at right with dissolve
    "Через пару минут вышла и отдала ключи от домика №28."
    mt "Это последний свободный домик. Одежду получите на складе."
    
    #Появление карты в инвентаре. появляется вкладка “карты”.* / Доработать
    #*звук появления карты*
    play sound sfx_achievement
    show InversiaMOD sa semi_sideways smile pioneer normal with dspr
    mt "Вот вам карта лагеря, она поможет вам сориентироваться."
    sa_zg "Спасибо!"
    mt "Скоро начнётся обед, поторопитесь! А мне нужно по делам."

    hide mt normal pioneer with dissolve
    "Ольга закрыла дверь и ушла в неизвестном направлении."
    #ОД уходит, фон: Домик ОД*"
    #*She Is Kind**"
    play music music_list['she_is_kind'] fadein 1
    "Ольга ушла по делам, а мы открыли карту."
    sa "Да уж{w=0.3}.{w=0.3}.{w=0.3}. лагерь не маленький. Куда пойдём?"
    zg "Давай сходим за одеждой, а потом уже в домик."
    sa "Согласна."

    #фон: площадь*"
    scene bg ext_houses_day at walking_inv with dissolve
    $ renpy.pause(1.5)
    scene bg ext_square_day at walking_inv with dissolve
    $ renpy.pause(0.3)
    scene bg ext_square_day at walking_inv with dissolve
    "По пути нам встретились немногочисленные пионеры. Путь до склада в целом проходил без помех."
    
    #Фон: медпункт*"
    scene bg ext_aidpost_day at walking_inv with dissolve
    "Неожиданно Саша нарушила тишину"
    show InversiaMOD sa semi_sideways thoughtful pioneer normal with dissolve
    sa "Скажи, тебя вся эта ситуация{w=0.3}.{w=0.3}.{w=0.3}."
    sa "Совсем не злит?"
    zg "В плане?"
    show InversiaMOD sa semi_sideways unsmile pioneer normal with dissolve
    "Саша провела пальчиком по волосам, потеребила непослушную прядь и сказала, вздёрнув носик"
    sa "Слишком они тут{w=0.3}.{w=0.3}.{w=0.3}."
    sa "Занятые какие-то{w=0.3}.{w=0.3}.{w=0.3}.{w} Не знаю, как лучше слово подобрать."
    sa "Образцовые, блин."
    sa "Хотя я и не помню ни черта, Жень, но почему-то ощущаю себя здесь на своём месте."
    sa "Может, мы пионерами были, пока память не потеряли?"
    "Саша прыснула в кулачок."
    sa "Или комсомольцами какими-нибудь."

    show InversiaMOD sa front thoughtful pioneer normal with dissolve
    "Неожиданно Саша посуровела."
    sa "Что молчишь, как пень лесной? Подумай ещё вот над чем."
    sa "Откуда мы знаем что такое пионеры?"
    sa "Ничего не помним. Ни маму с папой, ни откуда мы, ни какой год сейчас на дворе."
    sa "А то, что пионер должен быть опрятен и всегда готов — знаем на зубок!"
    sa "За формой, вон, идём куда-то{w=0.3}.{w=0.3}.{w=0.3}."
    show InversiaMOD sa front unsmile pioneer normal with dissolve
    "Голос Саши стал немного растерянным."
    sa "Зачем-то{w=0.3}.{w=0.3}.{w=0.3}."
    "Тем временем впереди показалось здание, судя по всему, нужный нам склад."
    zg "Саш, я{w=0.3}.{w=0.3}.{w=0.3}."
    sa "Ладно, пришли уже."
    "Бросила Саша."
    sa "Потом договорим."
    #фон склад(снаружи)*"
    scene ext_stock_day with dissolve
    "Мы постучались, и дверь открыла нам никто иная как Славя."
    # Открытие двери (БГ) Звук и закрытие двери
    show sl normal pioneer with dissolve
    sl "Привет вам ещё раз! Вы за вещами?"
    sa_zg "Да."
    sl "Проходите, сейчас всё выдам."
    hide sl normal pioneer with dissolve

    #   Фон: склад (внутри(с гендой))*" Доработать
    scene None_BG_INV with dissolve
    "Мы зашли на склад. Славя убежала за одеждой, и мы остались стоять в одиночестве."
    show InversiaMOD sa front unsmile pioneer normal at right with dissolve
    sa "Не понимаю{w=0.3}.{w=0.3}.{w=0.3}. Как мы потеряли память? И почему мы попали именно сюда?"
    zg "А я откуда знаю? Если у нас память отшибло."
    "Саша поёжилась."
    "Пока я пребывал в размышлениях, Славя уже принесла нам всё нужное."
    
    show sl normal pioneer with dissolve
    sa "Вот, ваши одежда и постельное бельё."
    zg "Спасибо, Славя."
    sa "Спасибо. Славя, можешь сказать, какой здесь распорядок дня?"
    show sl happy pioneer with dspr
    sl "Ну, смотри. Утром — линейка, а после неё завтрак." 
    sl "В полдень — обед, а вечером — ужин." 
    sl "Также у нас бывают мероприятия и, естественно, отдых на свежем воздухе."
    sa "Ладно{w=0.3}.{w=0.3}.{w=0.3}. Спасибо, Славя."
    "Мы уже хотели уйти, как блондинка нас окликнула"
    sl "Вы куда? Примерьте сразу, вдруг не подойдёт."
    zg "Эмм{w=0.3}.{w=0.3}.{w=0.3}. здесь?"
    show sl shy pioneer with dspr
    "Славя смутилась."
    sl "Там примерочная есть."
    "Она показала на небольшую коробку с занавеской." 
    hide sl shy pioneer with dissolve
    "Мы по очереди быстро переоделись и вышли обратно к Славе."
    show sl smile pioneer with dspr
    sl "Ой, ну как по вам шили. Удобно?"
    sa_zg "Очень.{w} Спасибо, Славь."

    show sl shy pioneer with dspr
    sl "Ой, да не за что."
    $ renpy.pause(1)
    show sl normal pioneer with dspr
    extend " Ты, кстати, Женя, почему галстук не завязал?"
    zg "А я не умею."
    sl "Ничего, научишься, давай я помогу."

    show sl normal pioneer close with dissolve
    "Славя подошла ко мне вплотную. Сердце начало биться чаще."
    $ renpy.pause(3, hard=True)
    show sl smile pioneer with dissolve
    
    sl "Вот так. Кра{w=0.2}-со{w=0.2}-та!"
    zg "Спасибо тебе ещё раз."
    sl "Да ничего."
    sa "Эй? Есть тут кто?"
    zg "Да, мы здесь."
    zg "Ладно, мы тогда пойдём обустраиваться."
    sa "Давай."
    sl "До встречи."

    #фон склад, снаружи день*"
    scene ext_stock_near_store2 at walking_inv with dissolve
    $ renpy.pause(1)
    #фон площадь день*"
    scene bg ext_square_day at walking_inv with dissolve
    $ renpy.pause(0.3)
    scene bg ext_square_day at walking_inv with dissolve

    th "Всё-таки красиво тут вечером, да и днём неплохо." 
    th "Но я, опять же, всё время ловлю себя на мысли, что мне чего-то не хватает."
    "Словно из реальности пропало что-то важное."
    "Или, скорее, кто-то."
    th "Ох, похоже, что мне даже начинает тут нравиться."
    #Фон Домика снаружи*"
    scene bg ext_house_of_sl_day at walking_inv with dissolve
    $ renpy.pause(1)
    scene bg ext_house_of_sl_day with dspr

    # orchid
    "Вот мы и дошли до нашего места жительства." 
    "Мы хотели уже зайти внутрь, как вдруг я почувствовал чьё-то присутствие." 
    "Неожиданно для себя, я на языке жестов сказал Саше"
    show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    zg "У нас хвост. Ты заходи в дом, а я осмотрюсь."
    show InversiaMOD sa semi_sideways smile pioneer normal with dspr
    sa "Хорошо, удачи."
    hide InversiaMOD sa semi_sideways smile pioneer normal with dissolve
    "Также ответив жестами, Саша зашла в домик, а я сделал вид, что иду назад." 
    "Пройдя пару метров, я залез в кусты и затаился."
    menu:
        "Не пугать шпиона":
            $ napugal_us = False
            # jump ne_napugal_day1
        "Напугать шпиона":
            $ napugal_us = True
            # jump napugal_day1

    # label ne_napugal_day1:
    if napugal_us == False:
        $ us_znakomstvo = False
        #*eat some troubles**"
        stop music
        play music music_list['eat_some_trouble'] fadein 1 
        show us laugh pioneer with dissolve
        "Не прошло и минуты, как на дорожке показалась маленькая девочка с красными, как огонь, волосами и голубыми глазами."
        show us upset pioneer with dissolve
        "Она пожала плечами и пошла назад к домику."
        hide us with dissolve
        "Я вышел из своего укрытия и посмотрел этой девочке вслед."
        jump ne_napugal_day1_prodolzhenie_inv
    # label napugal_day1:
    elif napugal_us == True:
        $ us_znakomstvo = True
        #*eat some troubles**"
        stop music
        play music music_list['eat_some_trouble'] fadein 1 
        "Посидев так минут пять, а может, и меньше, я увидел как куст возле нашего домика задёргался."
        "Я незаметно подкрался к нему сзади. "
        $ renpy.pause(0.5)
        scene bg ext_house_of_sl_day at running2 with dissolve
        show us surp2 pioneer close with dissolve
        "Прыгнув в заросли с криком «Лови Штирлица!», я выбил наблюдателя с его позиции, и мы, как бочка, покатились по дорожке."
        
        # "always ready"
        stop music
        play music music_list['always_ready']   
        $ renpy.pause(1)
        scene bg ext_house_of_sl_day at running2 with dissolve
        show us shy pioneer close with dissolve
        $ renpy.pause(1.5)
        
        scene bg ext_house_of_sl_day with dissolve
        show us shy pioneer close with dspr
        "Когда мы наконец остановились, я увидел на себе девушку." 
        "Точнее, девочку, с красными, как огонь, волосами и голубыми глазами."
        usp "Подкрадываться не хорошо!"
        zg "А шпионить тоже плохо."
        show us calml pioneer with dissolve
        "Она насупилась, но ничего не ответила. Я поднялся и спросил:"
        zg "Как тебя зовут, шпионка?"
        
        show us smile pioneer with dissolve
        us "Ульяна. А ты Женя?"
        us "Угадала. И как, интересно было?"
        us "Ну, вожатая на линейке сказала про новеньких." 
        us "Я ещё подумала, что библиотекаршу нашу так же зовут. Хотя она уже была с нами."
        zg "Понятно."
        us "Ну, мне надо идти, Алиске помогать." 
        show us grin pioneer with dissolve
        extend" Бывай."
        "Она показала мне язык и убежала."
        jump ne_napugal_day1_prodolzhenie_inv
    
label ne_napugal_day1_prodolzhenie_inv:
    "Я подошёл к нашему домику и зашёл внутрь." 
    "Саша уже расстелила постель, что мне тоже предстояло сделать."
    show ggroom with dissolve
    #*two glasses of melancholy**
    stop music
    play music music_list['two_glasses_of_melancholy'] fadein 1.0
    show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    sa "Что с хвостом?"
    zg "Всё в порядке, просто девочка шпионила за нами, проказница обычная."
    show InversiaMOD sa semi_sideways thoughtful pioneer normal with dissolve
    sa "Ясно{w=0.3}.{w=0.3}.{w=0.3}. Однако у меня назрел вопрос: откуда мы знаем язык жестов?"
    zg "Оттуда же, откуда и про пионеров, я полагаю, — хрен его знает."

    show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    sa "Твоя правда{w=0.3}.{w=0.3}.{w=0.3}. Давай пройдёмся по лагерю. Разведаем местность."
    zg "Согласен, пошли всё осмотрим.{w} Можешь только выйти на минуту?"
    sa "Хорошо. Жду на улице."
    
    hide InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    "Саша вышла наружу. Я тем временем быстро переоделся в пионерскую форму" 
    show ggroom with dissolve
    extend" и вышел следом."

    show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    $ renpy.pause(1)
    scene bg ext_houses_day at walking_inv with dissolve
    $ renpy.pause(0.5)
    scene bg ext_houses_day with dissolve
    "Мы с Сашей молча дошли до развилки, как вдруг она спросила"
    
    show InversiaMOD sa semi_sideways smile pioneer normal with dissolve
    sa "Ну что? Куда идём?"
    #Выборы должна быть карта
    # Пляж, спорт площадка, лес, пристань
    $ obhodnoi = 0
    $ disable_all_zones()
    $ set_zone("beach", "obhodnoi_D1_inv_beach") 
    $ set_zone("sport_area", "obhodnoi_D1_inv_sport_area") 
    $ set_zone("boat_station", "obhodnoi_D1_inv_boat_station") 
    
    # $ set_zone("forest", "vybor2_forest_D1_ivn") 
    $ set_zone("forest", "obhodnoi_D1_inv_forest") 
    
    $ show_map ()

# Ёбанные костыли_______________________

label obhodnoi_D1_inv_beach:

    $ disable_all_zones()

    $ set_zone("sport_area", "sport_area2_inv") 
    $ set_zone("boat_station", "boat_station_day1_inv")
    $ set_zone("beach", "beach_day1_inv")
    scene bg ext_houses_day with dissolve
    show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    "Я достал карту и заглянул в неё."
    zg "Я бы сходил на пляж."
    "Я показал пальцем на карте."
    sa "Что ж, я тогда пойду сюда! "
    "Саша показала на спортплощадку."
    zg "Хорошо, тогда до ужина?"
    show InversiaMOD sa semi_sideways smile pioneer normal with dspr
    sa "Да, до ужина."
    sa "Не вляпайся никуда."
    "Я лишь кивнул."
    hide InversiaMOD sa semi_sideways smile pioneer normal with dissolve
    "Мы разошлись. Я спокойно зашагал в сторону пляжа."

    scene bg ext_houses_day at walking_inv with dissolve
    "Было солнечно, но свежий ветерок не позволял жаре застояться."
    scene ext_square_day at walking_inv with dissolve
    "Пожалуй, это именно то, что я хотел в данный момент!" 
    jump beach_inv_day1_first_beach

label obhodnoi_D1_inv_sport_area:
    scene bg ext_houses_day with dissolve
    show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    jump sport_area_s_sashei_inv

label obhodnoi_D1_inv_boat_station:
    scene bg ext_houses_day with dissolve
    show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    "Я достал карту и заглянул в неё."
    zg "Я бы сходил на пристань."
    "Я показал пальцем на карте."
    sa "Что ж, я тогда пойду сюда! "
    "Саша показала на спортплощадку."
    zg "Хорошо, тогда до ужина?"
    show InversiaMOD sa semi_sideways smile pioneer normal with dspr
    sa "Да, до ужина."
    sa "Не вляпайся никуда."
    "Я лишь кивнул."
    hide InversiaMOD sa semi_sideways smile pioneer normal with dissolve
    "Мы разошлись. Я спокойно зашагал в сторону пристани."

    scene bg ext_houses_day at walking_inv with dissolve
    "Было солнечно, но свежий ветерок не позволял жаре застояться."
    scene ext_square_day at walking_inv with dissolve
    "Пожалуй, это именно то, что я хотел в данный момент!" 
    jump boat_station_day1_inv

label obhodnoi_D1_inv_forest:
    scene bg ext_houses_day with dissolve
    show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    "Я достал карту и заглянул в неё."
    zg "Я бы сходил в лес."
    "Я показал пальцем на карте."
    sa "Что ж, я тогда пойду сюда! "
    "Саша показала на спортплощадку."
    zg "Хорошо, тогда до ужина?"
    show InversiaMOD sa semi_sideways smile pioneer normal with dspr
    sa "Да, до ужина."
    sa "Не вляпайся никуда."
    "Я лишь кивнул."
    hide InversiaMOD sa semi_sideways smile pioneer normal with dissolve
    "Мы разошлись. Я спокойно зашагал в сторону леса."

    scene bg ext_houses_day at walking_inv
    "Было солнечно, но свежий ветерок не позволял жаре застояться."
    scene ext_square_day at walking_inv with dissolve
    "Пожалуй, это именно то, что я хотел в данный момент!" 
    jump forest_day1_inv

label obhodnoi_map_inv:
    #/* Проверка на прохождение всех точек карты 
    $ disable_all_zones()
    if beach_inv_day1 == True:
        if boat_station_day1_inv == True:
            if sport_area2_inv == True:
                $ vse_oboshol_d1_inv = True
    
    if vse_oboshol_d1_inv == False:
        if beach_inv_day1 == False:
            $ set_zone("beach", "beach_inv_day1")
        if boat_station_day1_inv == False:
            $ set_zone("boat_station", "boat_station_day1_inv")
        if sport_area2_inv == False:
            $ set_zone("sport_area", "sport_area2_inv") 
        $ show_map()
        
        return
    else:
        jump uzin_inv_d1
    #*/
#_______________________________________

label beach_inv_day1_first_beach:
    #[ (+1 алиса)что выбрал Пляж]"
    $ dv_och += 1
    jump beach_inv_day1
label beach_inv_day1:
    
    $ obhodnoi += 1
    $ beach_inv_day1 = True
    #$ disable_all_zones()
    #$ set_zone("sport_area", "sport_area2_inv") 
    #$ set_zone("boat_station", "boat_station_day1_inv") 

    # На пяже
    scene bg ext_beach_day at walking_inv with dissolve
    $ renpy.pause(0.5)
    scene bg ext_beach_day with dspr
    play voice ambience_lake_shore_day fadein 4
    "Когда я пришёл туда, на пляже никого не было."
    "Я увидел шезлонг и тут же лёг на него."
    "А солнце уже не так сильно светит{w=0.3}.{w=0.3}.{w=0.3}."
    
    show blink
    "Мне было так приятно и хорошо, что я просто прикрыл глаза и слушал шум моря.{w=0.2}.{w=0.2}."
    $ renpy.pause(3)
    dvp "Как тебе вода, новенький?"
    zg "Не лез я ещё в воду, плавок нет."
    dvp "Может, мне тебе помочь?"
    play sound sfx_borshtch
    "И в этот же момент я почувствовал на себе целый поток, как мне показалось тогда, солёной воды."
    hide blink
    show unblink
    $ renpy.pause(1.5)
    show dv laugh pioneer with dissolve
    "Рефлекторно, я открыл глаза, повернулся в сторону девушки," 
    show dv shocked pioneer close with dspr
    extend " перехватил её левую руку и крепко схватил за горло."
    dvp "Отпусти!"
    "Тоненько, как мышка, пропищала девушка, не теряя, впрочем, ноток агрессии в голосе." 
    th "Похоже, напористость — часть её характера."
    show dv angry pioneer close with dissolve
    dvp "Пусти, бл*!!"
    $ renpy.pause (2)
    show dv cry pioneer close with dissolve
    dvp "Больно, пусти{w=0.3}.{w=0.3}.{w=0.3}."
    $ renpy.pause (2)
    "Голос девочки превратился в хрип."
    dvp "Воздух.{w=0.2}.{w=0.2}. {w} Не могу.{w=0.2}.{w=0.2}.{w} Пусти.{w=0.2}.{w=0.2}."
    hide dv cry pioneer close with dissolve
    "Я, наконец одумавшись, отпустил шею девочки."
    play sound sfx_bodyfall_1
    "Та нелепо взмахнула ногами и свалилась на песок."
    "Девочке понадобилось примерно полминуты, чтобы отдышаться."
    show dv shy pioneer close with dissolve
    "Наконец переведя дыхание, она гневно уселась на землю прямо в юбке и поджала под себя ноги."
    "Юбка тут же оказалась вся в песке."

    show dv angry pioneer close with dspr
    "Уставившись на меня взглядом, полным злобы, смешанной со страхом{w=0.4}, Алиса, я наконец вспомнил её имя, я слышал его на площади, воскликнула"
    dv "Ну и что, по-твоему, ты творишь?!"
    zg "То же самое я хотел бы спросить у тебя.{w} Обливать ледяной водой отдыхающего человека!"
    "Я был чертовски зол! Впервые за сегодня решил расслабиться, а эта рыжая испортила весь кайф{w=0.3}.{w=0.3}.{w=0.3}."
    dv "Ничего особенного, можешь считать, что это было просто{w=0.3}.{w=0.3}.{w=0.3}."
    dv "Посвящение в пионеры нашего лагеря! "
    dv "Ну а ты.{w=0.2}.{w=0.2}.{w} задушить меня решил?!"
    show dv cry pioneer close with dspr
    dv "Придурок!"
    "Неожиданно на глазах Алисы выступили слёзы."
    "Да уж, неловко вышло."

    th "М-да уж, как бы я не был зол сейчас, она просто подшутила надо мной{w=0.3}.{w=0.3}.{w=0.3}.{w} И что я вообще сделал?"
    show dv cry pioneer with dissolve
    "Я немного отошёл от Алисы и смог нормально рассмотреть девушку." 
    "Янтарные, почти огненные глаза и рыжие волосы, собранные в два хвостика, сильно выделялись." 
    "Самодовольная ухмылка — обычная, судя по всему, черта её лица — пропала." 
    "Отличную фигуру нельзя не отметить — и то, как хорошо на ней сидит форма."
    "Неожиданно Алиса прокричала"
    show dv angry pioneer with dspr
    dv "С такой хваткой только на завод, гайки крутить!"
    show dv grin pioneer with dspr
    "И с невообразимым, одновременно пошловатым и злым выражением лица прошипела"
    dv "Или в колхоз, быков за яйца ловить!"
    play sound zensky_smekh
    "Девушка набрала в грудь воздуха и звонко засмеялась."
    dv "Или коров, за вымя{w=0.3}.{w=0.3}.{w=0.3}."
    zg "Зачем?"
    "Посмеявшись вдоволь, Алиса наконец немного успокоилась и поинтересовалась"
    
    show dv smile pioneer with dspr
    dv "Что «зачем»?"
    zg "Зачем корову,{w=0.5} за вымя{w=0.3}.{w=0.3}.{w=0.3}."
    play sound zensky_smekh
    dv "Алиса засмеялась пуще прежнего, до слёз на огненных глазах, к счастью, уже от смеха."
    dv "Да кто тебя знает, для дурика такого агрессивного — самое то!"
    "Я решил, что лучше будет промолчать."
    play sound muzhskoi_smekh
    "Но всё же не удержался и хихикнул Алисе в ответ."

    show dv grin pioneer with dspr
    "Алиса наконец угомонилась и лукаво посмотрела на меня."
    dv "Так-то лучше. Как тебя зовут, поехавший?"
    zg "Женя."
    dv "Я Алиса."
    dv "Ну, бывай."
    hide dv grin pioneer with dspr

    "Уже отойдя от меня на приличное расстояние, девушка остановилась."
    play sound sfx_light_candle
    "До меня донёсся лёгкий, почти невесомый, «Как Алисин смех», — мелькнуло в голове, щелчок зажигалки."
    "Моего носа достиг запах крепкого табака."
    show dv sad pioneer far:
        xcenter 0.90 ycenter 0.5
    dv "Псих."
    "Бросила Алиса, посмотрела на меня через плечо" 
    show dv normal pioneer far:
        xcenter 0.90 ycenter 0.5
        ease 1 xcenter 1.50 ycenter 0.5
    
    extend " и, напоследок сверкнув глазами, не оглядываясь, пошла прочь."
    "Я же остался и продолжил смотреть на речку, сидя на песке."
    "Лишь изредка украдкой посматривая в спину удаляющейся рыжеволосой."
    $ renpy.pause(3)
    
    # **YOU LOST ME**
    play music music_list["you_lost_me"]
    play sound sfx_hiding_in_bush
    "Вскоре я услышал шорох кустов."
    th "Наверное, Алиса хочет отомстить мне."
    scene bg ext_path_day with dissolve
    "Резко подойдя к шумевшим зарослям, я успел увидеть только небольшой силуэт, похожий на Алисин, — но это могла быть и не она."
    "Осмотрев кусты и не найдя ничего, я уж было направился обратно в лагерь, как вдруг.{w=0.2}.{w=0.2}."
    play sound sfx_bodyfall_1
    scene bg ext_path_day with vpunch
    "Я споткнулся о корягу, которую неожиданно проглядел. "
    zg "Вот блин, надо быть аккуратнее!"
    "Отряхнувшись, я пошёл дальше."
    if obhodnoi != 3:
        call obhodnoi_map_inv
    else:
        play voice sfx_dinner_horn_processed
        "А много времени уже прошло. Думаю, на сегодня хватит."
        jump uzin_inv_d1
    
label boat_station_day1_inv:
    $ obhodnoi += 1 
    $ boat_station_day1_inv = True
    #[Пристань]
    scene bg ext_boathouse_day with dissolve
    "Я спокойно шёл по пустой дорожке. Мелькали домики, расступившиеся от края на приличное расстояние."
    "Пройдя немного дальше, я снова вышел к речке. На воде стояло здание — вероятнее всего, это лодочная станция."
    "И весь этот пейзаж.{w=0.2}.{w=0.2}.{w} Он был очень красивым!"
    "Прямо идеальное место для мечтаний и сочинительства."
    "Пока я стоял и наслаждался поэтической атмосферой, где-то зазвучала гитарная мелодия."
    
    # Добавить музыку какую нибудь
    "Музыка доносилась со стороны станции, подчёркивая красоту этого места."
    "Когда я зашёл за здание, я увидел девушку, мирно игравшую на гитаре, свесив ноги за поручни и смотря вдаль."
    "Музыка замерла, и девушка повернулась ко мне."
    show mi normal pioneer with dissolve
    "Её милую азиатскую внешность нельзя было не отметить."
    "Длинные волосы, заплетённые в два хвоста, такого же цвета как её глаза — цвета морской волны."
    "Соответствует месту."
    mip "Тебе нравится пейзаж?"
    zg "Тут очень красиво."
    show mi happy pioneer with dspr
    mip "Это место вдохновляет.{w}" 
    show mi smile pioneer with dspr
    extend " Кстати, ты же новенький здесь, верно?"
    zg "Да, меня зовут Женя, а тебя?"
    mi "Меня — Мику. И давно ты уже здесь стоишь?"
    zg "Недавно. А сможешь ещё сыграть?"
    show mi smile pioneer with dspr
    mi "Тебе понравилось?!{w} Правда?!"
    zg "Да, красивая мелодия.{w=0.2}.{w=0.2}."
    mi "Меня редко просят сыграть что-то, особенно незнакомцы.{w} Ну, то есть просят, но обычно уже знакомые ребята, с лагеря."
    zg "Можно считать, что ты меня покорила."
    show mi shy pioneer with dspr
    mi "Да ладно тебе. И что мне с тобой делать? Так уж и быть, сыграю."
    "Она положила пальцы на струны, немного посидела с задумчивым видом, и вскоре из инструмента полилась ещё одна красивая мелодия."
    "{w=0.3}.{w=0.3}.{w=0.3}."

    "Она грела слух и сердце, я был готов слушать её вечно."
    "Не в прямом смысле, конечно."
    "Но всё хорошее когда-нибудь кончается. "
    "Девушка закончила играть и отложила инструмент в сторону."
    show mi shocked pioneer with dissolve
    mi "Ну как тебе?{w=1} Понравилось?{w=1} Только скажи честно."
    zg "Очень красиво, мне понравилось."

    show mi happy pioneer with dspr
    mi "Спасибо. А не хочешь ко мне в клуб заглянуть?" 
    mi "Вступишь, будем вместе играть, я тебя всему научу, тебе понравится, увидишь!"
    zg "Я не умею{w=0.3}.{w=0.3}.{w=0.3}."

    show mi smile pioneer with dspr
    mi "Ну, это не проблема, я на всём умею, могу и тебя научить, так что ты приходи, вот."
    zg "Подумаю.{w=0.2}.{w=0.2}.{w} Ладно, ещё раз спасибо, я пойду!"
    mi "Ладно, до встречи!"
    hide mi with dissolve
    "Пойду к Саше, возможно, она ещё на спортплощадке." 
    "Я отправился дальше."
    if obhodnoi != 3:
        call obhodnoi_map_inv   
    else:
        play voice sfx_dinner_horn_processed
        "А много времени уже прошло. Думаю, на сегодня хватит."
        jump uzin_inv_d1
    
label sport_area_s_sashei_inv:
    # $ obhodnoi += 1
    $ obhodnoi_odin = False
    $ sport_area2_inv = True
    "Я достал карту и заглянул в неё."
    #[Спортплощадка] 1
    zg "Я бы сходил на Спортплощадку."
    "Я показал пальцем на карте."
    show InversiaMOD sa semi_sideways smile pioneer close with dissolve
    sa "Пошли вместе!"
    scene bg ext_playground_day  at walking_inv with dissolve
    "Мы двинулись в сторону спортплощадки и вскоре дошли до футбольного поля."
    "{w=0.3}.{w=0.3}.{w=0.3}."
    jump sport_area2_inv

label sport_area2_inv:
    scene bg ext_playground_day with dissolve
    $ obhodnoi += 1
    $ obhodnoi_odin = True
    $ sport_area2_inv = True

    #[Спортплощадка] 2
    "Вскоре передо мной возникло солидно выглядящее футбольное поле."
    "На нём вовсю гоняла мяч ребятня."
    "Среди неё носилась уже знакомая мне девочка, с рыжими, как огонь, волосами."
    "Единственная девочка среди юных футболистов, но играла она куда лучше." 
    "Никому из здешних пацанов не удавалось превзойти её в беге."
    "Не удивлюсь, если она самая быстрая в лагере."
    show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    sa "А она быстрая, та, что с рыжими волосами."
    zg "Ну а как же. Других в шпионы не берут."
    show InversiaMOD sa front surprise pioneer normal with dspr
    sa "Так это она? Да ладно{w=0.3}.{w=0.3}.{w=0.3}."
    zg "Точно это она. Ульяна зовут"
    show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    sa "Понятно."
    sa "Не хочешь тоже сыграть?"
    zg "Я не люблю спорт."
    show InversiaMOD sa front surprise pioneer normal with dissolve
    sa "С чего ты это взял? Ты же ничего не помнишь о своём прошлом."
    zg "Я знаю это. Нутром чувствую!"
    show InversiaMOD sa front normal pioneer normal with dspr
    sa "А я люблю спорт — ну, я так думаю, — только вот сейчас формы нет{w=0.3}.{w=0.3}.{w=0.3}."
    zg "Значит, не в этот раз."
    "{w=0.3}.{w=0.3}.{w=0.3}."
    
    #[Если прошёл всё]
    zg "Ладно, пошли в столовую!"
    sa "Уже пора?"

    if obhodnoi == 3:
        #*звон горна
        zg "Как видишь.{w=0.2}.{w=0.2}."
        sa "Ну пошли."
        jump uzin_inv_d1
    elif obhodnoi < 3:
        #[Если не всё прошёл]
        zg "Ладно, пойду я, ещё не всё исследовал."
        call obhodnoi_map_inv

label forest_day1_inv:  
    $ obhodnoi_odin = True
    play sound ambience_forest_day
    scene bg ext_path2_day with dissolve
    "Лес здесь красив{w=0.3}.{w=0.3}.{w=0.3}."
    "Тишина, только птицы и насекомые порой прерывают её."
    "Расслабляющий шум листвы, колышущейся от ветра, и прохладный, слабый ветерок придают этому месту особый шарм."
    "В голову так и лезут мысли."
    "Странное место, непонятное. И как я вообще сюда попал?"
    "Что у нас есть?"
    "Лагерь где-то в лесу, белая комната{w=0.3}.{w=0.3}.{w=0.3}."
    "Дальше только мелочи."
    "Начнём с начала: чёрная пустота, бесконечная белая комната{w=0.3}.{w=0.3}.{w=0.3}."
    "{w=0.3}.{w=0.3}.{w=0.3}."
    "Я даже не представляю, что это или где это может быть."
    "Ну, с лагерем всё понятно, если бы не одно «но»."
    "Белая комната{w=0.3}.{w=0.3}.{w=0.3}."
    "Всё не сходится из-за чёртовой комнаты."
    "{w=0.3}.{w=0.3}.{w=0.3}."
    "Виртуальная реальность?"
    "Нет, всё здесь слишком реалистично{w=0.3}.{w=0.3}.{w=0.3}."
    "Слишком мало информации{w=0.3}.{w=0.3}.{w=0.3}."
    "{w=0.3}.{w=0.3}.{w=0.3}."
    "А что насчёт потери памяти?"
    "Я не помню ничего."
    "Не помню ни себя, ни своего имени."
    "Ну, хоть говорить помню как."
    "И это не только я, с Сашей то же самое!"
    "Получается, это не случайность{w=0.3}.{w=0.3}.{w=0.3}."
    "{w=0.3}.{w=0.3}.{w=0.3}."
    "А что если{w=0.3}.{w=0.3}.{w=0.3}."
    "Комната."
    "Потеря памяти."
    "Саша."
    "Лагерь."
    "{w=0.3}.{w=0.3}.{w=0.3}."
    "Это всё связано{w=0.3}.{w=0.3}.{w=0.3}."
    "По крайней мере, всё, кроме Саши."
    "Эксперимент? Но зачем? Тюрьма, но какая-то извращённая."
    "Потеря памяти, — просто так у обоих её быть не может!"
    "Значит, её стёрли специально?"
    "Но зачем? Какой в этом смысл? Почему бы нас просто не убить?"
    "Значит, мы нужны живыми и нужны не наши знания."
    "Зачем?!"
    play sound sfx_bodyfall_1
    scene bg ext_path2_day with vpunch
    "Вдруг ниоткуда опять появилась коряга, об которую я тут же споткнулся и повалился на землю."
    "Больно.{w=0.4} И неожиданно."
    "Я посмотрел в сторону ненавистной растительности."
    "Откуда она там вообще?"
    "Я сделал выдох и лёг на спину."
    "Дерево какое-то странное, хотя, может, мне и кажется."
    menu obratil_vnimanie:
        "Расслабиться":
            jump ne_obratil_vnimanie_inv
        "Разобраться":
            jump obratil_vnimanie_inv
        
label obratil_vnimanie_inv:
    $ obratil_vnimanie = True
    th "Нет, что-то здесь не так."
    "Я поднялся с земли и подошёл к стволу."
    "Постучав по нему, я услышал несвойственный дереву, характерный для железа звук."
    th "Ого, интересно{w=0.3}.{w=0.3}.{w=0.3}."
    "Я покрутился вокруг дерева и среди веток нашёл одну, очень сильно выделявшуюся."
    "Эта ветка была высоко, но после нескольких попыток я смог допрыгнуть до неё."
    "Ветка, как рычаг, опустилась вниз, и на обратной стороне дерева что-то открылось."
    "Я зашёл за дерево, и прямо внутри ствола нашёлся небольшой тайник."
    "Внутри лежала лишь аудиокассета, старая, на ней была надпись: «Сотый цикл»."
    th "Что это? И что с этим делать?" 
    th "Думаю, тут найдётся то, на чём можно будет эту кассету воспроизвести."
    "Я убрал её в карман и пошёл в лагерь."
    jump vibor_kasety_prodolzhenie_1D_inv
    
label ne_obratil_vnimanie_inv:
    "Расслабляет, глаза так и слипаются."
    "{w=0.3}.{w=0.3}.{w=0.3}."
    show blink
    $ renpy.pause(4)
    hide blink
    show unblink
    "Я не заметил как уснул."
    "Сколько времени? "
    "Я посмотрел в сторону солнца — оно уже уходило в закат."
    "Неплохо меня разморило{w=0.3}.{w=0.3}.{w=0.3}."
    "Я встал с земли, отряхнулся и пошёл в лагерь."
    jump vibor_kasety_prodolzhenie_1D_inv

label vibor_kasety_prodolzhenie_1D_inv:
    play voice sfx_dinner_jingle_speaker_tape
    "Пока я пытался выйти из леса, прозвучал горн, созывающий всех на обед." 
    "Я поспешил к столовой и по пути встретил Сашу."
    if (obhodnoi_odin == "True"):     
        show InversiaMOD sa front unsmile pioneer normal with dissolve
        zg "Привет, Саша. Как тебе лагерь?"
        sa "Хороший, правда я успела сходить только на площадку. А тебе?"
        zg "Красивый, особенно лес. Пошли ужинать!"
        sa "Угу."
        "Саша была какая-то поникшая."
        zg "Ты как вообще?{w} Выглядишь.{w=0.2}.{w=0.2}.{w=0.2} помятой."
        
        show InversiaMOD sa semi_sideways unsmile pioneer normal with dissolve
        "Саша скорчила грустную мину."
        sa "Смеяться не будешь?"
        zg "Не буду, а что стряслось-то?"
        sa "Обещаешь, что смеяться не будешь?"
        "Я ответил, изо всех сил пытаясь сохранить серьёзность:"
        zg "Слово пионера. Торжественно клянусь."
        sa "Ладно{w=0.3}.{w=0.3}.{w=0.3}."
        "Протянула Саша."
        "Затем, набрав полную грудь воздуха, выпалила:"

        show InversiaMOD sa front scared pioneer normal with dissolve
        sa "МЕНЯ ДОМОГАЛАСЬ ОЗАБОЧЕННАЯ МЕДСЕСТРА!!!"
        # "(Начинает играть welcome to our madhouse)"
        "Я переспросил, не веря ушам:"
        zg "Что-что?"

        show InversiaMOD sa front crying pioneer normal with dissolve
        sa "Что слышал! Озабоченная медсестричка с буферами пятого размера заманила меня в свой медпункт{w=0.3}.{w=0.3}.{w=0.3}."
        sa "И начала{w=0.3}.{w=0.3}.{w=0.3}."
        sa "Начала{w=0.3}.{w=0.3}.{w=0.3}."
        "Саша выдавила максимально страдальческим тоном:"
        $ renpy.pause(2.5, hard=True)
        sa "Осматривать{w=0.3}.{w=0.3}.{w=0.3}."
        "Тут я не выдержал" 
        "Прости, дедушка Ленин, принесённую только что святую пионерскую клятву я всё же нарушу!"
        "Я больше не могу."
        "Я сдерживал смех, но грудь моя ходила ходуном, я беззвучно открывал и закрывал рот." 
        "На глазах выступили слёзы."
        zg "Я бы на такое посмотрел, м-м-м{w=0.3}.{w=0.3}.{w=0.3}."
        "Протянул я."

        show InversiaMOD sa front angry pioneer normal with dissolve
        "Гневный крик Саши взлетел в небо, напугав даже пятнистого дятла, что мирно стучал себе по стволу."
        hide InversiaMOD sa front angry pioneer normal with dissolve
        "Недовольно посмотрев на меня, птица упорхнула."

        show InversiaMOD sa front angry pioneer normal with dissolve
        "Саша же, зайдя за ближайшее дерево, вернулась с длинной веткой."
        "И, с явно недобрыми намерениями, направилась в мою сторону."
        zg "Саша{w=0.3}.{w=0.3}.{w=0.3}. СТОЙ!"
        zg "Это я так, пошутил."
        zg "Мне правда очень жаль, ну не надо, ну не стукай!"
        show InversiaMOD sa front angry pioneer close with dissolve
        sa "Я тебе покажу{w=0.3}.{w=0.3}.{w=0.3}."
        
        "Саша всё приближалась."
        sa "Ржать надо мной{w=0.3}.{w=0.3}.{w=0.3}."
        sa "Клятвы нарушать{w=0.3}.{w=0.3}.{w=0.3}."
        sa "Допрыгался, подлец!"
        "Невероятным прыжком преодолев разделяющее нас расстояние, Саша с размаху огрела меня веткой по ноге!"
        "Веточка хоть и была тонкой и хрупкой, но моей бедной ноге показалось, что её окунули в кипящее олово."
        "Я беззвучно прохрипел равнодушному лесу:"
        zg "Мамочка{w=0.3}.{w=0.3}.{w=0.3}."
        hide InversiaMOD sa front angry pioneer close with dissolve
        "И, прихрамывая, пустился наутёк от впавшей в ярость Сашки."
        
        # Экран темнеет, затем обратно.
        scene black with dissolve
        $ renpy.pause(2)
        scene bg ext_polyana_day with dissolve

        "Спустя пару минут Сашин гнев угас."
        "Мы уселись бок о бок в небольшой лесной прогалине, на поваленном деревце — подальше ото всех, но (тут меня охватило внезапное смущение) поближе друг к другу."
        show InversiaMOD sa semi_sideways unsmile pioneer close with dissolve
        sa "Дак вот{w=0.3}.{w=0.3}.{w=0.3}."
        "Жаловалась Саша."
        sa "Иду я мимо местного медпункта, выходит из него девушка, ровесница вожатой примерно. И так, с придыханием, говорит мне."
        sa "Пионерка.{w=0.2}.{w=0.2}.{w} Ты новенькая. Пройдём со мной, сейчас же." 
        sa "Новенькие девочки обязаны пройти медосмотр.{w} Это не обсуждается."
        "Саша замолкла."
        zg "Ну, а дальше, дальше-то что было?"
        "С нетерпением спросил я."
        show InversiaMOD sa semi_sideways angry pioneer close with dissolve
        "Саша вспыхнула."
        sa "Опять веткой захотел?!"
        zg "Понял, не дурак. Молчу-молчу."

        show InversiaMOD sa semi_sideways smile pioneer close with dissolve
        "Улыбнувшись, Саша сказала:"
        sa "Пойдём уже, а то ещё ужин пропустим{w=0.3}.{w=0.3}.{w=0.3}."
        play sound ambience_forest_day fadein 1.0
        "Лес тихо шумел у нас над головами{w=0.3}.{w=0.3}.{w=0.3}."
        jump uzin_inv_d1
    elif (obhodnoi_odin == "False"):
        scene bg ext_square_day with dissolve   
        show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
        zg "Привет, Саша. Как тебе лагерь?"
        sa "Хороший, правда я успела сходить только на площадку. А что там у тебя?"
        "Она указала на торчавшую из кармана кассету."
        zg "Видимо, чья-то аудио-кассета, нашёл в лесу.{w} Её очень хорошо спрятали{w=0.3}.{w=0.3}.{w=0.3}."
        
        show InversiaMOD sa semi_sideways thoughtful pioneer normal with dspr
        sa "И где мы её послушаем?"
        zg "Возможно, найду где-то магнитофон."
        sa "Нужно будет спросить у кого-нибудь."
        jump uzin_inv_d1

label uzin_inv_d1:
    scene bg ext_dining_hall_away_day at walking_inv with dissolve
    $ renpy.pause(2)
    scene bg ext_dining_hall_near_day at walking_inv with dissolve
    $ renpy.pause(1)
    scene bg int_dining_hall_people_day with dissolve
    "Мы зашли в столовую, взяли ужин и сели за столик."
    "Обед был вполне обычный: гречка с котлетой и стакан кефира."
    "За ужином мы молчали."

    "Почему-то у меня не было особого аппетита."
    "Странная кассета, лагерь, и вообще — почему я самого себя не помню?{w=0.2}.{w=0.2}.{w=0.2}. "
    "Что? Почему? Как? Вопросов слишком много{w=0.3}.{w=0.3}.{w=0.3}."
    show InversiaMOD sa semi_sideways thoughtful pioneer close with dissolve
    sa "Чего не ешь? "
    zg "Всё это странно{w=0.3}.{w=0.3}.{w=0.3}."
    sa "В плане?"
    zg "Почему мы не помним наше прошлое?{w} Почему мы здесь, а не где-то в другом месте?"
    "Саша вздохнула."
    sa "Всё возможно. Может, мы участвуем в каком-то эксперименте или вообще погибли по неизвестным нам обстоятельствам. Всё может быть."
    zg "Но как нам это понять?"
    sa "Думаю, сперва нам надо разузнать о местоположении лагеря, времени и дате, а от этого и отталкиваться уже."
    "Логично. От бесконечного повторения одних и тех же вопросов ответы сами не найдутся — нужно собрать как можно больше информации."
    zg "Пожалуй, ты права."
    "Поужинав, мы вышли из столовой."
    scene bg ext_dining_hall_near_day with dissolve

    show InversiaMOD sa semi_sideways normal pioneer normal with dissolve
    sa "Ну что, куда пойдём?"
    zg "Честно говоря, я пойду{w=0.3}.{w=0.3}.{w=0.3}."
    $ disable_all_zones()
    $ set_zone("beach", "vybor2_beach_D1_inv") 
    $ set_zone("forest", "vybor2_forest_D1_inv") 
    $ show_map()

label vybor2_beach_D1_inv:
    scene bg ext_dining_hall_near_day with dissolve
    show InversiaMOD sa semi_sideways normal pioneer normal at right with dissolve
    
    mt "Саша, вот ты где."
    show mt normal pioneer close at left with dissolve

    "Неожиданно к нам подошла Ольга."
    show InversiaMOD sa semi_sideways smile pioneer close with dspr
    sa "Да, Ольга Дмитриевна, что случилось?"
    mt "Мне нужна помощь в здании администрации."
    sa "А с чем помочь-то?"
    show mt smile pioneer close with dissolve
    mt "Я слышала, что ты отличилась в своей школе скоростью чтения и письма{w=0.3}.{w=0.3}.{w=0.3}."
    mt "Нам нужен такой человек в канцелярии. "
    mt "Хотя бы на один-два дня."
    mt "А поскольку ты пионерка — то это для тебя долг и честь!"
    sa "Хорошо, Ольга Дмитриевна, а нам надо прямо сейчас идти?"

    show mt smile pioneer close with dspr
    mt "Да, хотя бы посмотришь на своё временное рабочее место."
    show InversiaMOD sa front smile pioneer close with dissolve
    zg "Получается, увидимся уже в домике?"
    sa "Видимо.{w} До скорого!"
    hide mt
    hide InversiaMOD
    with dissolve
    "Ольга и Саша ушли в сторону администрации, а я{w=0.3}.{w=0.3}.{w=0.3}."
    
    #ПЛЯЖ (фон: Оригинал)
    scene bg ext_beach_day with dissolve
    "По дороге к пляжу я вдруг заметил движение впереди." 
    "Где-то в глубине вдруг стрельнуло тревожное чувство: «Не попадайся на глаза!»"
    # "**Experiments in Confusion: Mick Gordon**"
    
    # "Успел: (Второе прохождение)"
    if (first_playrhrough == "False"):
        "Только я успел спрятаться в ближайших кустах, как к пирсу вышла{w=0.3}.{w=0.3}.{w=0.3}."
        "Алиса? Она провела по своему лицу и{w=0.3}.{w=0.3}.{w=0.3}."
        "Чего?! Как? Это была не Алиса, но очень похожа."
        "Лицо скрывала маска."
        "Она достала магнитофон и сказала:"
        klp "Лагерь (название из мастерской), видимо, аномальный, как и несколько других лагерей с возможными порталами в реальный мир."
        klp "Или портал-ловушка. Пока что я не обнаружила настоящего портала, и, скорее всего, он тоже ловушка лагеря."
        # "Нервный смех. "
        klp "Да когда же я найду выход!?"
        klp "Почему одни пионеры говорят, что нету этого выхода, а другие говорят, что есть?!"
        "Девушка спокойно вздохнула."
        klp "Это выбешивает! Нужно будет вернуться в лагерь и покидать дартс или поубивать зомбиульян. Ла-а-адно, запись окончена."
        klp "Лагерь (название из мастерской), цикл 676, запись 12."
        "Она убрала магнитофон, рванула к концу пирса, прыгнула в воду и{w=0.3}.{w=0.3}.{w=0.3}. пропала."
        "Я лежал в траве в полном недоумении."
        "Что вообще сейчас произошло?"
        "Кто это девушка, как она поменяла внешность?"
        "Ответов, как обычно, не было. Как не было и слов, чтобы описать моё недоумение от только что увиденного{w=0.3}.{w=0.3}.{w=0.3}."
        "Нужно будет рассказать всё Саше."
        stop music fadeout 1.0
    else:
        # Не успел: (основное)"
        play music music_list['i_want_to_play']
        "Я хотел было спрятаться в кусты, но трава была настолько скользкая, что я лишь упал, распластавшись на ней." 
        "Тут на пирс вышла Алиса."
        show dv grin pioneer close with dissolve
        dv "Чё разлёгся?"
        zg "Да вот, упал."
        show dv normal pioneer close with dspr

        dv "А чего тут делал?"
        zg "Просто гулял."
        "Я поднялся и отряхнулся."
        zg "Ходил по пляжу и наткнулся на тропу с этим пирсом. Кстати, тут очень красиво."
        dv "Ясно. Ты, кстати, перочинный ножик здесь не видел?"
        zg "Нет, а зачем он тебе? "
        dv "Ульяна посеяла где-то тут, по её словам. Да и ты тут шуршал."
        zg "Что ж, ножика здесь нет, а я уже ухожу. "
        dv "Удачи."
        hide dv with dissolve
        $ renpy.pause(1, hard=True)
        show blink
        $ renpy.pause(2, hard=True)
        hide blink
        show unblink
        scene bg ext_beach_sunset:
            blur 100
            linear 1 blur 20
            linear 2 blur 0
        $ renpy.pause(0.2)
        
        jump sunset_day1_inv

label vybor2_forest_D1_inv:
    $ pudrenitsa = True
    scene bg ext_dining_hall_near_day with dissolve
    show InversiaMOD sa semi_sideways normal pioneer normal at right with dissolve
    
    mt "Саша, вот ты где."
    show mt normal pioneer close at left with dissolve

    "Неожиданно к нам подошла Ольга."
    show InversiaMOD sa semi_sideways smile pioneer close with dspr
    sa "Да, Ольга Дмитриевна, что случилось?"
    mt "Мне нужна помощь в здании администрации."
    sa "А с чем помочь-то?"
    show mt smile pioneer close with dissolve
    mt "Я слышала, что ты отличилась в своей школе скоростью чтения и письма{w=0.3}.{w=0.3}.{w=0.3}."
    mt "Нам нужен такой человек в канцелярии. "
    mt "Хотя бы на один-два дня."
    mt "А поскольку ты пионерка — то это для тебя долг и честь!"
    sa "Хорошо, Ольга Дмитриевна, а нам надо прямо сейчас идти?"

    show mt smile pioneer close with dspr
    mt "Да, хотя бы посмотришь на своё временное рабочее место."
    show InversiaMOD sa front smile pioneer close with dissolve
    zg "Получается, увидимся уже в домике?"
    sa "Видимо.{w} До скорого!"
    hide mt
    hide InversiaMOD
    with dissolve
    "Ольга и Саша ушли в сторону администрации, а я{w=0.3}.{w=0.3}.{w=0.3}."
    
    #Лес
    scene bg ext_path2_day with dissolve
    "Кто я? Что я? Зачем и кому я нужен?"
    zg "Чем я раньше занимался? "
    zg "Почему мы оказались здесь?"
    zg "Что мы такого натворили, чтобы оказаться без памяти, без понимания, что здесь происходит?"
    zg "Вопросы, вопросы и ещё раз вопросы{w=0.3}.{w=0.3}.{w=0.3}. "
    "Я бормотал, пока шёл в лес, который так и тянул меня к себе."
    "Отыскав тихую опушку, я прилёг у ближайшего дерева и направил взгляд в небо." 
    "Звёзды только начинали появляться на небосводе."
    "Омск{w=0.3}.{w=0.3}.{w=0.3}. Омск{w=0.3}.{w=0.3}.{w=0.3}.{w} Почему я вспомнил этот город?"
    "Постепенно силы покидали меня, и я провалился в сон."
    "«До тебя город{w=0.3}.{w=0.3}.{w=0.3}. город{w=0.3}.{w=0.3}.{w=0.3}. город ф{w=0.3}.{w=0.3}.{w=0.3}.»"
    
    # *Сон*
    show blink
    $ renpy.pause(3, hard=True)
    hide blink
    show unblink
    
    scene bg ext_path2_night with dissolve
    $ renpy.pause(1)
    "Я поднялся с земли и пошёл к домику."
    # "**Typhon Voices: Mick Gordon**"
    scene bg ext_path_night at walking_inv with dissolve
    $ renpy.pause(1)
    scene bg ext_square_night at walking_inv with dissolve
    
    "Уже стемнело, и было плохо видно; лишь редкие фонари и звёзды освещали дорогу."
    scene ext_houses_night at walking_inv with dissolve
    show tuman1_inv with dissolve

    #Фон домика гг ночью / Доработать
    "Когда я добрался до жилища, я заметил появившийся словно ниоткуда туман."
    $ renpy.pause(1)
    scene ext_houses_night with dissolve
    show tuman1_inv with dissolve

    play voice sfx_bus_idle fadein 1 volume 0.7
    "Помимо него обстановку нагнетал отдалённый звук моторов и{w=0.3}.{w=0.3}.{w=0.3}." 
    play sound sfx_draw_water
    extend " плеск воды?{w} Но дождя же не было сегодня."
    "Позади себя я услышал отчётливый всплеск."
    show slime_sasha_inv:
        alpha 0.0 xcenter 0.5 ycenter 0.8
        ease 1 alpha 1.0
    "Резко повернувшись, я увидел нечто похожее на Сашу."
    nn "Ж̶̧̹̯͍̍̆̎̀е̴̨͍̻͒͠е̷͕̣̱͙̐͜е̵̨̗͔͉̥̑̈̈́ӗ̵̺͖̮̍̄̕н̴̗͚͈̠̃͠я̵̻̑я̴̹͖̈́я̸̡͍̦̬̾ ̸͓̥̆̐͆̕п̴̡̟́͑̑͝о̵͉̯͗̀͛ͅм̷̫̹́̃̓о̴̨̢̗̖̒̏͊̄͘ͅг̵̫̂̆͐͠и̴̥̰͓͝ӣ̶̒͜и̷̡̙͎͑̌"
    "Эта штука походила на слизня. Оно было чёрно-синего цвета."
    "Голос существа — смесь из женского и мужского голосов — заставлял сознание сжиматься."
    "Потому единственное, до чего я смог додуматься, так это бежать."
    scene ext_houses_night at running2
    show slime_sasha_inv:
        zoom 1 xcenter 0.5 ycenter 0.8 
        ease 2 zoom 1.2 xcenter 0.5 ycenter 0.8 
    "Бежал я со всей силы, но{w=0.3}.{w=0.3}.{w=0.3}. я и на метр не сместился."
    show slime_sasha_inv: 
        zoom 1.2 xcenter 0.5 ycenter 0.8 
        ease 2 zoom 1.4 xcenter 0.5 ycenter 0.9 
    "А существо приближалось."
    scene ext_houses_night at walking_inv
    show slime_sasha_inv: 
        zoom 1.4 xcenter 0.5 ycenter 0.9 
        ease 2 zoom 1.8 xcenter 0.5 ycenter 0.95 
    "Я попытался медленно идти назад, но тщетно. "
    show slime_sasha_inv: 
        zoom 2 xcenter 0.5 ycenter 0.95 
        ease 2 zoom 2.1 xcenter 0.5 ycenter 1.2 
    "Словно сама реальность возвращала меня за фальстарт, а слизь подходила, взывая ко мне."
    "Мой рот онемел от ужаса."
    "Оно было уже на расстоянии вытянутой руки{w}, как вдруг{w=0.3}.{w=0.3}.{w=0.3}. "
    #*тёмный экран*
    scene black with dspr
    stop voice fadeout 1
    $ renpy.pause(3, hard=True)
    

    #"*Реальность*"
    # "**Dream Aria Yu-Peng Chen.**"
    scene bg ext_path_sunset behind black
    hide black
    show unblink
    scene bg ext_path_sunset: 
        blur 100
        linear 1 blur 20
        linear 2 blur 0
    zg "АЙ! "
    "Шишка, которая меня и разбудила, лежала рядом, оставив на голове отпечаток боли."
    "Я взял её и бросил в кусты."
    th "Что это был за чёрт?{w=0.5} Бр-р-р.{w} Слизь, Саша{w=0.3}.{w=0.3}.{w=0.3}." 
    th "Что за фигня? Слава богу, что это просто сон."
    "Я поднялся и уже хотел было пойти к домику, как услышал звонок, доносящийся из тех самых кустов, в которые полетела злосчастная шишка."
    "Заглянув туда, я увидел вибрирующую и звенящую пудреницу. "
    th "Чего?! Звенящая пудреница?"
    "Я поднял коробочку и покрутил её в руке." 
    "С виду и в самом деле простая пудреница, без излишеств."
    "А ведь её содержимое может многое сказать о текущей эпохе." 
    "Я отщёлкнул крышку и{w=0.3}.{w=0.3}.{w=0.3}."
    zg "Пудреница, говоришь?{w=0.3}.{w=0.3}.{w=0.3}."
    "Внутри расположились дисплей, пара кнопок и несколько мелких отверстий — похоже, для динамика."
    "И ни одного предмета косметики{w=0.3}.{w=0.3}.{w=0.3}."
    "Найдя среди кнопок отвечающую за питание, я нажал на неё, но ничего не произошло." 
    "Понажимал ещё, задержал — без толку."
    th "Аккумулятор сдох?"
    "Я оглянулся по сторонам — никого.{w} Думаю, будет лучше взять это с собой."
    jump sunset_day1_inv

label sunset_day1_inv:
    #После выборов
    "Время было к вечеру, делать было нечего. "
    "Луна уже показалась на горизонте, а солнце почти скрылось." 
    "Я сильно устал за день, так что решил пойти домой — отдыхать!"
    scene bg ext_square_sunset at walking_inv with dissolve
    "На улице попадались пионеры, а ветер приятно дул вдоль дорожки, обдавая спину прохладой."
    scene bg ext_houses_sunset at walking_inv with dissolve
    scene ggroom at walking_inv with dissolve
    "Я приблизился к домику и вошёл, но в нём никого не оказалось." 
    "Я разлёгся на кровати."
    show blink
    
    if (first_playrhrough == "False"):
        if (pudrenitsa == "False"):
            #   "Успел: (Второе прохождение)"
            #   "**Pure Sky. Yu-Peng Chen**"
            #   "1) (если не нашёл пудреницу):"
            "Закрыв глаза, я начал размышлять"
            th "Кто эта девушка?"
            th "Угроза ли она для нас?"
            th "Что вообще тут происходит? "
            th "Не понимаю, не понимаю{w=0.3}.{w=0.3}.{w=0.3}."
            "Голова от непонимания готова взорваться!"
            "Хочется понять хоть что-то, но тебя лишь вопросами заваливают."
            "На которые ни у кого нет внятного ответа{w=0.3}.{w=0.3}.{w=0.3}."
            "Я услышал, как в дом зашли."
            hide blink with dissolve
            scene ggroom:
                blur 50
                linear 0.5 blur 10
                linear 1 blur 0 
            show unblink
            show InversiaMOD sa front normal pioneer normal with dissolve
            sa "О чём задумался?"
            "Открыв глаза, я увидел Сашу."
            zg "И тебе привет.{w} Сегодняшний день — сплошные странности." 
            zg "Не только с нашим появлением здесь, а ещё и всякой мистикой."
            show InversiaMOD sa semi_sideways thoughtful pioneer normal with dspr
            sa "Ты о чём? Рассказывай."
            "Я постарался как можно понятнее и короче рассказать о сегодняшних событиях{w=0.3}.{w=0.3}.{w=0.3}. И об истории с девушкой."
            show InversiaMOD sa semi_sideways shock pioneer normal with dspr
            sa "{w=0.3}.{w=0.3}.{w=0.3}."
            zg "Вот как-то так прошёл мой день."
            sa "Понятно{w=0.3}.{w=0.3}.{w=0.3}. прям все беды и мистика на тебя легли." 
            sa "Вообще, у меня тоже сегодня были некоторые странности."
            zg "И какие же?"

            show InversiaMOD sa front surprise pioneer close with dissolve
            sa "Я нашла вот это{w=0.3}.{w=0.3}.{w=0.3}."
            "Она достала из кармана что-то похожее на пудреницу."
            zg "Это же вроде пудреница, ничего необычного."
            sa "Погоди ты, вот{w=0.3}.{w=0.3}.{w=0.3}."
            "Саша открыла её, и тут я понял, что это не пудреница, а{w=0.3}.{w=0.3}.{w=0.3}. замаскированный передатчик."
            zg "Ничего себе.{w} Работает?"
            show InversiaMOD sa front unsmile pioneer close with dspr
            sa "Нет, что печально.{w} Видимо, батарея посажена."
            zg "Значит, тут кто-то ей пользовался и потерял. Или бросил." 
            zg "В любом случае это пока не поможет."
            show InversiaMOD sa front normal pioneer close with dspr
            sa "Что верно — то верно.{w} Уже стемнело. Давай завтра подумаем{w=0.3}.{w=0.3}.{w=0.3}. "
            zg "Согласен. Спокойной ночи!"
            sa "Да, спокойной."
            hide InversiaMOD with dissolve
            show blink
            "Я долго не мог заснуть. Всё размышлял о том, что было сегодня."
            "Непонятный лагерь, странная девушка, которая умеет маскироваться, разные видения и сны{w=0.3}.{w=0.3}.{w=0.3}."
            "У меня больше вопросов, нежели ответов. "
            "Но сну наконец-то удалось затянуть меня в свои объятия, и наступила тишина{w=0.3}.{w=0.3}.{w=0.3}."
            jump day2_inversia

        if (pudrenitsa == "True"):
            #"2) (если нашёл пудреницу):"
            "В голову лезли самые разные мысли."
            "Выключенная коммуникатор-пудреница, непонятные сны{w=0.3}.{w=0.3}.{w=0.3}."
            "Вопросы всё копятся, а ответов нет."
            "Я ещё раз попробовал включить пудреницу, но не смог." 
            th "Похоже, всё-таки аккумулятор сдох."
            "Закрыв её, я не заметил, как уснул."
            show blink
            $ renpy.pause(3, hard=True)
            
            # Проворот ручки двери
            play sound sfx_close_water_sink
            pause 0.5
            
            # Открытие двери
            play sound sfx_open_dooor_campus_1
            pause 0.5
            # Закрытие двери
            play sound sfx_close_cabinet
            pause 0.5
            "Проснулся от того, что в домик кто-то вошёл." 
            hide blink with dissolve
            scene ggroom:
                blur 50
                linear 0.5 blur 10
                linear 1 blur 0 
            show unblink
            show InversiaMOD sa front normal pioneer normal with dissolve
            "Открыв глаза, я увидел, что это Саша."
            zg "Доброй ночи, наверно{w=0.3}.{w=0.3}.{w=0.3}."
            sa "Да, доброй{w=0.3}.{w=0.3}.{w=0.3}.{w} Я разбудила?"
            zg "Нет, просто чутка отдыхал{w=0.3}.{w=0.3}.{w=0.3}.{w} Как день?"
            sa "Ну{w=0.3}.{w=0.3}.{w=0.3}.{w} Был день, вроде вполне обычный, но кое-что было очень странным{w=0.3}.{w=0.3}.{w=0.3}."
            zg "И что же?"
            show InversiaMOD sa semi_sideways thoughtful pioneer close with dissolve
            sa "Я когда после ужина пошла в сторону пляжа, я увидела Алису." 
            show InversiaMOD sa semi_sideways shock pioneer close with dissolve
            sa "Сперва она что-то записывала, а потом, что-то нажав на руке, стала не Алисой!"
            zg "Что? Ты не шутишь?"
            sa "Нет, ни капли!"
            zg "Поверить сложно, но поверю.{w} А я вот нашёл сегодня{w=0.3}.{w=0.3}.{w=0.3}."
            "Я показал Саше пудреницу."
            show InversiaMOD sa semi_sideways smile pioneer close with dissolve
            sa "Это же пудреница!"
            zg "Я сперва так же подумал, но ты посмотри."
            "Я открыл пудреницу."
            show InversiaMOD sa semi_sideways shock pioneer close with dissolve
            sa "Ничего себе. Это же коммуникатор! Он работает?"
            zg "Нет, у него батарея посажена."
            sa "Грустно, в любом случае он бы пока нам ничем бы не помог."
            zg "Да{w=0.3}.{w=0.3}.{w=0.3}.{w} Хочу предложить нам поспать, прежде чем это всё собирать воедино." 
            zg "Утро вечера мудренее."
            sa "Ага, спокойной ночи."
            "Мы разлеглись на своих кроватях." 
            "Несмотря на неутихающие мысли, сон не заставил себя долго ждать."
            show blink
            jump day2_inversia
    else: 
        jump day2_inversia