from NG_OUI_DB.validators import (
    ALPHANUMERIC_ASCII_REGEX_PATTERN,
    MAC_ADDRESS_REGEX_PATTERN,
    valid,
)


def test_AlphaNumericAsciiRegexPattern():
    assert valid(ALPHANUMERIC_ASCII_REGEX_PATTERN, "abc123") is not None
    assert valid(ALPHANUMERIC_ASCII_REGEX_PATTERN, "abc 123") is not None
    assert valid(ALPHANUMERIC_ASCII_REGEX_PATTERN, "abc@123") is None
    assert valid(ALPHANUMERIC_ASCII_REGEX_PATTERN, "abc123>") is None


def test_MacAddressRegexPattern() -> None:
    assert valid(MAC_ADDRESS_REGEX_PATTERN, "00:00:00:00:00:00") is not None
    assert valid(MAC_ADDRESS_REGEX_PATTERN, "00-00-00-00-00-00") is not None
    assert valid(MAC_ADDRESS_REGEX_PATTERN, "00:00:00:00:00") is None
    assert valid(MAC_ADDRESS_REGEX_PATTERN, "00-00-00-00-00") is None
    assert valid(MAC_ADDRESS_REGEX_PATTERN, "00:00:00:00:00:00:00") is None
    assert valid(MAC_ADDRESS_REGEX_PATTERN, "00-00-00-00-00-00-00") is None
    assert valid(MAC_ADDRESS_REGEX_PATTERN, "00:00:00:00:00:00:") is None
    assert valid(MAC_ADDRESS_REGEX_PATTERN, "00-00-00-00-00-00-") is None
    assert valid(MAC_ADDRESS_REGEX_PATTERN, "00:00:00:00:00:00:") is None
