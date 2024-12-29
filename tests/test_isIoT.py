from NG_OUI_DB import IeeOuiDb
from NG_OUI_DB.isIoT import isIoT


def test_isIoT():
    db = IeeOuiDb()
    # Xerox Corporation
    assert isIoT("00:00:00:00:00:00", fromDatabase=db) is False
    # Belkin International Inc.
    assert isIoT("D8:EC:5E:00:00:00", fromDatabase=db) is True
