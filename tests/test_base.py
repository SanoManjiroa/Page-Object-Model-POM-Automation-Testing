import pytest

@pytest.mark.usefixtures('invoke_driver') #conftestda tuzilgan invoke funcksiyasini chaqramiz 1 martta
class BaseTest():
    pass          # Endi bu yerda configuration file ketdi tuzdik ,va uni test jarayoniga chaqrb olishni sinab kordik


