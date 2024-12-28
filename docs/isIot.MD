# IoT Manufacturer Identification Documentation

## Overview

This module contains functions to determine if a given MAC address belongs to an IoT manufacturer. It leverages the IEEE OUI database and predefined keywords for identifying IoT manufacturers.

---

## Functions

### `isIoT`

#### Description

Determines if a given MAC address belongs to an IoT manufacturer.

#### Arguments

- `mac` (str): The MAC address to validate.
- `fromDatabase` (IeeOuiDb | None, optional): An instance of the IEEE OUI database. Defaults to `None`, which initializes a new database.

#### Returns

- `bool | None`: 
  - `True` if the MAC address belongs to an IoT manufacturer.
  - `False` if it does not.
  - `None` if the provided MAC address is invalid.

#### Implementation

```python
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
```

---

## Dependencies

### Modules Used

- `IEE_OUI`
  - Provides the `IeeOuiDb` class for accessing and querying the IEEE OUI database.

- `utils`
  - Contains utility functions, including `valid` for regex validation and the `MAC_ADDRESS_REGEX_PATTERN` for MAC address validation.

- `extractIotManufacturers`
  - Provides the `getIotManufacturers` function to fetch a list of IoT manufacturers based on predefined keywords.

---

## Example Usage

### Code Example

```python
from my_module import isIoT, IeeOuiDb

# Example MAC Address
mac_address = "00:1A:2B:3C:4D:5E"

# Initialize IEEE OUI database
database = IeeOuiDb()

# Check if the MAC address belongs to an IoT manufacturer
result = isIoT(mac=mac_address, fromDatabase=database)

if result is True:
    print("This MAC address belongs to an IoT manufacturer.")
elif result is False:
    print("This MAC address does not belong to an IoT manufacturer.")
else:
    print("Invalid MAC address.")
```

### Output Example

- If the MAC address belongs to an IoT manufacturer:
  ```plaintext
  This MAC address belongs to an IoT manufacturer.
  ```

- If the MAC address does not belong to an IoT manufacturer:
  ```plaintext
  This MAC address does not belong to an IoT manufacturer.
  ```

- If the MAC address is invalid:
  ```plaintext
  Invalid MAC address.
  ```


## Notes

- The function depends on a properly initialized IEEE OUI database. If no database is provided, a new instance is created.
- IoT manufacturers are identified using a predefined list of keywords and organization names in the IEEE OUI database.

---

- [README](../README.md)
- Documentation
  - [Utils](./utils.MD)
  - [Validators](./validators.MD)
  - [IEE_OUI_DB](./IEE_OUI.MD)
  - [Command Line Interface](./cli.MD)
  - [Extract IoT Manufacturers](./extractIot.MD)
