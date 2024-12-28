import os
import json
import pickle

from .IEE_OUI import IeeOuiDb

IOT_MAN_JSON_FILE = os.path.expanduser("~/NG_OUI_DB/iot_manufacturers.json")
IOT_MAN_PICKLE_FILE = IOT_MAN_JSON_FILE.replace(".json", ".pkl")
IOT_KEYWORDS = [
    "smart",
    "iot",
    "esp",
    "tuya",
    "nest",
    "broadlink",
    "sonoff",
    "hue",
    "wyze",
    "arlo",
    "ecobee",
    "eufy",
    "philips",
    "ikea",
    "fitbit",
    "xiaomi",
    "withings",
    "samsung",
    "lg",
    "sony",
    "media",
    "netgear",
    "tp-link",
    "ubiquiti",
    "honeywell",
    "ring",
    "bose",
    "logitech",
    "belkin",
    "alexa",
    "google home",
    "homekit",
    "lifx",
    "govee",
    "wyze cam",
    "lutron",
    "eero",
    "orbi",
    "linksys",
    "garmin",
    "whoop",
    "polar",
    "schlage",
    "august",
    "kwikset",
    "zigbee",
    "z-wave",
    "tado",
    "bosch",
    "sensor",
    "automation",
    "hub",
    "gateway",
    "tracker",
]


def getIotManufacturers(fromDatabase: IeeOuiDb | None = None) -> set[str]:
    """Get suspected IOT Manufacturers from the IEE OUI DB

    Args:
        fromDatabase (IeeOuiDb | None, optional): Initialized DB. Defaults to None.

    Returns:
         set[str]: The unique set of IOT Manufacturers

    Note:
        The IOT Manufacturers are determined by the IOT_KEYWORDS list.
        If the organization name contains any of the IOT_KEYWORDS,
        it is added to the set of IOT Manufacturers.

        The IOT Manufacturers are persisted to a JSON file and a pickle file
        for easy loading. The files are saved in the user's home directory in
        a folder called NG_OUI_DB.
    """
    iotManufacturers = set()
    ieeOuiDb: IeeOuiDb = IeeOuiDb() if fromDatabase is None else fromDatabase

    # loop over all the IEE OUI DB entries, if the organization name contains
    # any of the IOT_KEYWORDS, add it to the set of IOT Manufacturers
    for mac in ieeOuiDb.dbDict:
        organization = ieeOuiDb.dbDict[mac]["Organization Name"]

        for keyword in IOT_KEYWORDS:
            if keyword in organization.lower():
                iotManufacturers.add(organization)
                break

    # persist the IOT Manufacturers to a JSON file
    with open(IOT_MAN_JSON_FILE, "w") as f:
        json.dump(list(iotManufacturers), f, indent=4)

    # Also save a pickle file for easy loading
    with open(IOT_MAN_PICKLE_FILE, "wb") as f:
        pickle.dump(iotManufacturers, f)

    return iotManufacturers
