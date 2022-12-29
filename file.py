def pass_check(a):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    try:
        assert(len(a) > 6)
        assert(any(num.isdigit() for num in a))
        assert(not a.isdigit())
        assert(a.lower().find("password") < 0)
    except:
        return False
    else:
        return True