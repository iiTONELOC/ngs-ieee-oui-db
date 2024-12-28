from re import Match, match

# The regex pattern for an Alphanumeric ASCII string
ALPHANUMERIC_ASCII_REGEX_PATTERN = r"^[a-zA-Z0-9\s]+$"

# The regex pattern for a device's MAC address
MAC_ADDRESS_REGEX_PATTERN = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"


def valid(withPattern: str, againstValue: any) -> Match[str] | None:
    """Validate a value against a pattern

    Args:
        withPattern (str): A regex pattern to validate against
        againstValue (any): The value to validate

    Returns:
        re.Match[str] | None: A match object if the value is valid, None otherwise
    """
    return match(withPattern, againstValue)
