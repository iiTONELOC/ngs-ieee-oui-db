from .IEE_OUI import IeeOuiDb
from .utils import valid, MAC_ADDRESS_REGEX_PATTERN
from .extractIotManufacturers import getIotManufacturers


def isIoT(mac: str, fromDatabase: IeeOuiDb | None = None) -> bool | None:
    """Determine if the MAC Address belongs to an IOT Manufacturer

    Args:
        mac (str): The MAC Address
        fromDatabase (IeeOuiDb | None, optional): Initialized DB. Defaults to None.

    Returns:
        bool: True if the MAC Address belongs to an IOT Manufacturer, False otherwise
    """

    if not valid(withPattern=MAC_ADDRESS_REGEX_PATTERN, againstValue=mac):
        return None

    fromDatabase = IeeOuiDb() if fromDatabase is None else fromDatabase
    IotManufacturers = getIotManufacturers(fromDatabase=fromDatabase)

    organization = fromDatabase.getOrganizationName(mac=mac)

    found = False

    for iotManufacturer in IotManufacturers:
        if organization.lower() in iotManufacturer.lower():
            found = True
            break

    return found
