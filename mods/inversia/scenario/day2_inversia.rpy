label day2_inversia:
    $ backdrop = "days"
    $ save_name = (u"Инверсия. \nДень 2")
    $ day_time()
    $ persistent.sprite_time = 'day'

    $ renpy.pause(2.5)
    hide blibk
    show unblink
    scene ggroom:
        blur 100
        linear 1 blur 20
        linear 2 blur 0