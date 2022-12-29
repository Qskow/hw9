import file

def test_lenght():
    assert file.pass_check('qwe12') == False

def test_numbers():
    assert file.pass_check('123456') == False

def test_symbols():
    assert file.pass_check('qweasdzxc') == False

def test_pass():
    assert file.pass_check('PaSsWoRd') == False

def test_true():
    assert file.pass_check('MyPass123qwe') == True

