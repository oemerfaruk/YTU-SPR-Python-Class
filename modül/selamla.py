def selamlama(name):
    try:
        if type(name) != str:
            raise Exception("Argüman string olmalı")
        else: return "Merhaba {}".format(name)
    except Exception as e:
        return e
    

def bye(name):
    try:
        if type(name) != str:
            raise Exception("Argüman string olmalı")
        else: return "Görüşürüz {}".format(name)
    except Exception as e:
        return e
    