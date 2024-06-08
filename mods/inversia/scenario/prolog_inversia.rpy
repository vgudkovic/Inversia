init:
    define zg = Character (u"Женя", color = "#00deff", what_color = "#f1d076")
    define nn = Character(u"Незнакомка", color = "#00deff", what_color = "#f1d076")
    define sa = Character (u"Саша", color = "#00deff", what_color = "#f1d076")
    define sa_zg = Character (u"Саша и Женя", color = "#ff00f7", what_color = "#f1d076")

    $ config.developer = True

    #sfx
    $ inversion_pisk = "mods/inversia/sfx/inversion_pisk.mp3"
    # $ music inversion_Breath1 = "mods/inversia/music/inversion_Breath1.wav"
    $ inversion_shagi = "mods/inversia/sfx/shagi_s_ekhom.mp3"
    $ zvuk_tjazhelogo_dyhanija = "mods/inversia/sfx/zvuk_tjazhelogo_dyhanija.mp3"
    $ zenskiu_plach = "mods/inversia/sfx/zenskiu_plach.mp3"
    $ vistrel_iz_pistoleta = "mods/inversia/sfx/vistrel_iz_pistoleta.mp3"
    
    #bg/cg
    image karidor_so_svetom = "mods/inversia/bg/karidor_so_svetom.png"
    image polnosty_belaya_komnata = "mods/inversia/bg/polnosty_belaya_komnata.jpg"
    image beliy_karidor_s_dvery = "mods/inversia/bg/beliy_karidor_s_dvery.jpg"
    image beliy_karidor = "mods/inversia/bg/beliy_karidor.jpg"
    image komnata_prolog = "mods/inversia/bg/komnata_prolog.jpg"

    # Image
    image Achivement Prolog = "mods/inversia/images/Achivement Prolog.jpg"
    
    $ mods["prolog_inversia"]=u"Инверсия" # Название мода
    # define zg = Character ('Женя', color = "#00deff", what_color = "#f1d076")
    # define nn = Character ('Незнакомка', color = "#00deff", what_color = "#f1d076")
    # define sa = Character ('Саша', color = "#00deff", what_color = "#f1d076")
    # define achive_inversia = "mods/inversia/images/achive_inversia.png"

label prolog_inversia:
    $ backdrop = "days"
    $ save_name = (u"Инверсия \n Пролог.")
    
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
    stop music fadeout 2
    stop sound fadeout 2
    #dodel




    #play music inversion_Breath1 
    "Всё та же бесконечная пустота, что словно засасывала меня всё глубже и глубже. Сколько бы я не пытался, результат был один."
    "Любопытство отошло на второй план. Теперь моим сознанием правили ужас и страх..."
    "И нет, дело даже не в том, что вокруг меня царит кромешный мрак. С этим, как раз, я более чем смирился."
    'Вопрос в другом: кто же всё-таки этот "Я"? '
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
    play music inversion_shagi
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
    "Прежде чем изучать комнату, я решил осмотреть своё тело. Может, удастся найти подсказку о том, кто я и как я сюда попал."
    "На мне был надет не то халат, не то смирительная рубашка, неуклюже завязанная на поясе. На груди, к моей радости, был прикреплён небольшой бейджик."
    "Так вот что кололо меня в грудь. Одной загадкой меньше."
    "На бейджике было фото незнакомого мне мужчины и, по видимому, его имя-фамилия."
    "Евгений Зощенко. Внизу также стояла дата — 2017 год."
    "Всякий раз, когда я пытался выбить из своей башки хоть капельку воспоминаний, в уши возвращался едкий писк, причиняя мне адскую боль."
    "Я совершенно не знал, я ли это на фото, или же кто-то решил надо мной подшутить, прикрепив именной бейдж совершенно другого человека. В сознание вновь начали возвращаться вопросы."
    th "Почему же я не помню ничего из своего прошлого? Неужели амнезия? Но из-за чего?!"
    "Я поспешно проверил голову на наличие каких-либо ушибов и повреждений. Благо ничего найти мне не удалось."
    "Ладно, в любом случае, стоя тут, я ничего не узнаю. Надо двигаться дальше. Может, мне удастся найти хоть что-то, что меня заинтересует."
    "Или даже кого-то..."
    
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
    "Удивительно, но я не сразу заметил девушку, стоящую у одной из кроватей. С души словно камень свалился..."
    
    # Появление саши
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
    "Я аккуратно сделал пару шагов в её направлении. Мне совсем не хотелось испугать её."
    "Но как бы я не пытался двигаться бесшумно, девушка всё же услышала и резко повернулась ко мне. "
    "Теперь испугался уже я."
    "Чего-чего, а такой быстрой реакции я не ожидал. А ведь я даже не единого звука не издал..."
    "Не знаю, чьим умениям я удивлялся больше — своим или девушки, но в комнате тем временем повисло неловкое молчание."
    "Я уж хотел было заговорить с ней, но так и не нашёл что сказать."
    "Однако девушка взяла ситуацию в свои руки."
    nn "Евгений..."
    "Неужели она знает кто я такой? Может, мне удастся выведать у неё что-то."
    zg "Мы знакомы?"
    "Но девушка лишь показала пальцем себе на грудь, где располагался такой же бейдж, как и у меня."
    "Честно говоря, я о нём уже и забыл. На её табличке было написано имя — Александра."
    "Фото совпадало с её внешностью. И раз уж она ничего не стала спрашивать, скорее всего, фото на моём бейдже тоже достоверно..."
    "Я протянул девушке руку в знак знакомства. Она, недоверчиво посмотрев на меня, всё же ответила."
    zg "Что ж, раз уж мы познакомились, не расскажешь, что здесь происходит?"
    "Я уселся на стул возле стола и решил как следует расспросить девушку. Мне хотелось узнать как можно больше."
    sa "Прости, но я без понятия..."
    zg "Как давно ты здесь?"
    sa "Я не считала. Может, день, а может, и больше..."
    "С каждой секундой, что я смотрел на лицо девушки, мне всё больше казалась её внешность знакомой."
    "Словно я видел её раньше, но никак не могу вспомнить, где..."
    zg "Белый бесконечный коридор, — ты тоже через него проходила?"
    "Девушка еле заметно кивнула. Похоже, мы с ней в одной лодке."
    "И чёрт его знает, как из неё теперь выбираться."
    "Я решил осмотреть комнату. Мало ли удастся откопать что-то."
    "Саша неотрывно сверлила меня взглядом, словно боясь потерять из виду. Это немного напрягало."
    "Я решил нарушить воцарившуюся тишину."
    zg "Ты осматривалась здесь?"
    sa "Немного..."
    zg "Что же, тогда буду рад, если поможешь."
    "На намёки и джентльменство время тратить я не хотел, а лишняя пара рук не помешает."
    # Скрытие спрайта 
    
    # Появление спрайта
    $ renpy.pause(4)
    "Вдвоём мы обыскали комнату вдоль и поперёк."
    "Много времени это, благо, не заняло, однако принесло свои плоды."
    "В руках у меня оказалась небольшая бумажка, которую я откопал в подушке одной из кроватей."
    "Я сразу же показал Саше свою находку. У неё на лице промелькнула еле заметная улыбка."
    zg "Лишь за столом переговоров открывается истина."
    "Послание оказалось куда скромнее, чем я мог себе представить. Это разочаровало."
    sa "Как думаешь, что это значит?"
    zg "Думаю, истина — это выход отсюда. А вот стол переговоров..."
    "Мы одновременно посмотрели на тот самый большой стол, что стоял посреди комнаты."
    "Я хотел было поднять его, но у меня не получилось. Он был то ли прибит к полу, то ли был чертовски тяжёлым."
    zg "Значит, есть что-то на нём..."
    "И ведь правда, на одной из его ножек располагалась незаметная кнопка, которую я еле смог нащупать."
    "После нажатия на неё на столе открылись непонятные ячейки, хаотично разбросанные по всей его площади."
    sa "Это рисунок!"
    "Воскликнула Саша. А ведь точно, его только нужно собрать..."
    
    "Отлично! Мне всё же удалось решить этот ребус, пускай я и потратил на это прилично времени."
    "После того как картинка собралась воедино, одна из стен сместилась вверх, открывая ещё одну загадочную дверь."
    "Я уже хотел открыть её, но Саша вдруг села на кровать и отрешённо посмотрела куда-то вдаль."
    "Похоже, ей было тяжело собраться с мыслями."
    "Надо было помочь ей сконцентрироваться. Поэтому я подошёл к Саше и сел рядом."
    sa "Я ничего не понимаю, одни вопросы и ни одного ответа. Только эти чёртовы загадки..."
    zg "Может, это проверка? Да и если мы остановимся на полпути, мы многое потеряем."
    zg "Я не буду настаивать. Если хочешь, ты можешь остаться."
    "Девушка молча смотрела в пол и лишь спустя пару минут прошептала."
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
    zg "Думаю, да, больше же некуда."
    "Я, конечно, не уверен, но куда ещё идти-то, в конце концов?"
    "Мы неспешно открыли дверь. Войдя в неё, мы снова оказались в тёмной комнате. {w} И стоило нам моргнуть, как..."
    jump day1_inversia

label bad_end_inv:
    #"КАТАПУЛЬТНАЯ КОНЦОВКА"
    zg "Пока ты останешься здесь."
    zg "Двигаться вперёд вместе слишком опасно."
    zg "Я пойду вперёд, разведаю обстановку."
    zg "Ты тут не пропадёшь, не амбар какой-нибудь всё-таки."
    zg "Полноценная комната."
    zg "Кровать, стол, может, и поесть где-нибудь, что-нибудь найдёшь."
    "Повисла неловкая тишина."
    zg "Ну... Я пошёл."
    "Саша даже не подняла голову."
    "Я сделал несколько шагов к двери, и услышал сзади её тихий шёпот."
    sa "Я сгнию здесь..."
    "Я обернулся и удивлённо посмотрел на неё."
    sa "Зарубки буду на стене делать..."
    sa "Ждать..."
    sa "Может, придёт кто..."
    play music zenskiu_plach fadein 3
    "Саша всхлипнула."

    #"“звук: женские всхлипывания”"
    sa "Спасёт..."
    zg "Саша..."
    zg "Ты останешься здесь, так безопаснее. Я пойду вперёд. Узнаю что к чему."
    "Я старался говорить с ней ласково, как с маленьким ребёнком."
    th "Надо успокоить её."
    th "Надеюсь, мой тон не слишком снисходителен."
    zg "Мы же решили, вместе."
    stop music
    "Саша вскинула голову."
    sa "Это ты решил!"
    sa "Не я!"
    "С неожиданным гневом и отчаянием прокричала девушка."
    "Я почувствовал, что начинаю закипать в ответ."
    zg "Александра."
    "Как можно спокойней сказал я."
    zg "Соберись."
    zg "Перестань говорить глупости, всё с тобой будет хорошо."
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
    "Саша плакала уже навзрыд."
    "Я понимал, что стоит остановиться, я вёл себя как последний подонок."
    "Измываться над плачущей девушкой, перепуганной неизвестностью, окружающей её…"
    "Моя самооценка стремительно падала куда-то на дно той тёмной пустоты."
    "Следом за моей совестью."
    "Мне нужно было остановиться."
    "Но я не мог. Просто не мог."
    "Весь мой страх, вся злость на моё положение вырвались наружу и затопили рассудок."
    "Саша изо всех сил вцепилась тонкими пальчиками в простыню кровати, на которой сидела."
    sa "Ты... ТЫ..."
    "Повторяла и повторяла она."
    "Затем девушка вдруг подняла голову, посмотрела на меня заплаканными глазами и совершенно спокойно сказала:"
    sa "Иди."
    sa "Я тут сама как-нибудь."
    sa "Справлюсь... Иди, раз уж собрался."
    "Она поёрзала на кровати."
    sa "Чая, как видишь, нет — попили бы на дорожку."
    "Она усмехнулась."
    sa "Иди."
    "Забравшись с ногами на кровать и обхватив себя руками, она отвернулась от меня."
    "Я, не оглядываясь, пошёл прочь."
    "И мне было всё равно, смотрела ли она мне вслед."
    $ renpy.pause (2)
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
    
    "Я молниеносно обернулся."
    "На месте просвета образовалась дверь!"
    "Готов поклясться, секунду назад тут не было ничего!"
    "Из образовавшегося прохода вышла девушка."
    # По желанию добавить play sound sfx_scary_sting
    "Я оцепенел."
    "В её руке был пистолет!"
    "Каким-то внутренним чутьём я понял, что это настоящее боевое оружие."
    "Хоть незнакомка и держала его чуть небрежно, расслабленно, словно малыш держащий в руке хлопушку или сахарную вату."
    "А её лицо.."
    "ЕЁ ЛИЦО!"
    "Оно менялось."
    "Каждую секунду!"
    "Передо мной стояла рыжая девушка с задиристым взглядом."
    "Секунда — и лицо сменилось на совсем ещё девочку, с ясными синими глазами."
    "Ещё секунда — печальное зеленоглазое лицо, полное вселенской тоски."
    "Миг — и её сменила валькирия, чьё лицо обрамляли золотые косы."
    "Затем — и вовсе мужское лицо, строго смотрящее из под очков."
    "Незнакомка нарушила молчание."
    nn "Самое глупое решение из всех — разделиться."
    "Она посмотрела на меня полубезумным взглядом."
    nn "Ты что, кино не смотришь, зайчик?"
    "Её взгляд прожигал меня насквозь. Мысли в голове словно окаменели."
    $ renpy.pause (2)

    nn "Впрочем, ничего личного."
    "Она со скоростью света вскинула пистолет."
    zg "Подожди..."
    "Только и успел промямлить я..."
    #"Звук выстрела"
    play sfx vistrel_iz_pistoleta
    #СМЭРТ :)
    $ renpy.pause (5)
    #И звук ачивки)
    play sound sfx_achievement
    show Achivement Prolog at achievement_trans
    with dspr
    $ renpy.pause (3)
    hide Achivement Prolog
    return 0