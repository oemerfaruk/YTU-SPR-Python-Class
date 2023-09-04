def toplama(*args):
    sonuc = 0
    try:
        for i in args:
            sonuc += i
    except Exception as e:
        return e
    
    return sonuc


def carpma(*args):
    sonuc = 1
    try:
        for i in args:
            sonuc *= i
    except Exception as e:
        return e
    
    return sonuc