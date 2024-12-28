import traceback
from typing import LiteralString

from .validators import (
    valid,
    MAC_ADDRESS_REGEX_PATTERN,
    ALPHANUMERIC_ASCII_REGEX_PATTERN,
)

PROMPT = "Enter your choice: "
MAC_PROMPT = "Enter the MAC Address: "


def getMacAddress() -> str:
    """Get the MAC Address from the user

    Returns:
        str: MAC Address
    """
    mac = input(MAC_PROMPT)
    # validate the input
    while not valid(withPattern=MAC_ADDRESS_REGEX_PATTERN, againstValue=mac):
        print("Invalid MAC Address")
        mac = input(MAC_PROMPT)
    return mac


def getAlphaNumericString(msg: str) -> str:
    """Get an alphanumeric string from the user

    Args:
        msg (str): The message to display to the user

    Returns:
        str: The alphanumeric string
    """
    s = input(msg)

    while not valid(withPattern=ALPHANUMERIC_ASCII_REGEX_PATTERN, againstValue=s):
        print("Invalid Input")
        s = input(msg)
    return s


def getOrgName() -> str:
    """Get the Organization Name from the user

    Returns:
        str: The Organization Name
    """
    return getAlphaNumericString(msg="\nEnter the Organization Name: ")


def getAssignment() -> str:
    """Get the Assignment from the user

    Returns:
        str: The Assignment or OUI
    """
    return getAlphaNumericString(msg="\nEnter the Assignment: ")


def getRegistry() -> str:
    """Get the Registry from the user

    Returns:
        str: The Registry
    """
    return getAlphaNumericString(msg="\nEnter the Registry: ")


def getOuiFromMac(mac: str) -> str:
    """Get the OUI from the MAC Address

    Args:
        mac (str): The MAC Address

    Returns:
        str: The OUI of the MAC Address with any delimiters removed in uppercase
    """
    mac = mac.replace(":", "").replace("-", "")
    return mac[:6].upper()


def jsonWithProperIndent(dict: dict, indent: int, startingIndent=0) -> str:
    """Adds indentation properly to a json string

    Args:
        dict (dict): The dictionary to format
        indent (int): Amount of spacing to add.
        startingIndent (int, optional): Amount of spacing to add around the opening and closing {}. Defaults to 0.

    Returns:
        str: _description_
    """
    # format the json manually so that the brackets are indented if needed
    if dict == {} or dict == "Unknown":
        return ""
    try:
        indent: int = startingIndent + indent

        s: LiteralString = " " * startingIndent + "{\n"
        for key in dict:
            s += " " * indent + f'"{key}": '
            if type(dict[key]) == dict:
                s += jsonWithProperIndent(
                    dict=dict[key], indent=indent, startingIndent=indent
                )
            else:
                s += f'"{dict[key]}"'
            s += ",\n"
        s += " " * startingIndent + "}"

        return s
    except Exception:
        print(traceback.format_exc())
        return ""


def printArrayWithProperIndent(arr: list, indent: int, startingIndent=0) -> str:
    """Formats Arrays similar to jsonWithProperIndent

    Args:
        arr (list): The array to format
        indent (int, optional): Amount of spacing to add.
        startingIndent (int, optional): Amount of spacing to add around the opening and closing []. Defaults to 0.

    Returns:
        str: The formatted string
    """
    # format the data manually so that the brackets are indented if needed
    indent = startingIndent + indent

    s: LiteralString = " " * startingIndent + "[\n"
    for item in arr:
        s += " " * indent + f'"{item}"'
        s += ",\n"
    s += " " * startingIndent + "]"

    return s
