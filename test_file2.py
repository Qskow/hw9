import file2

def test_lenght():                    
    assert file2.string("qwe") == True

def test_min_lenght():                    
    assert file2.name("q") == False

def test_numbers():                    
    assert file2.name("Maxim") == True

def test_numbers():                    
    assert file2.name(123) == False

def test_int():                    
    assert file2.area(13) == 530.929158456675

def test_float():                    
    assert file2.area(3.15) == 31.172453105244717







