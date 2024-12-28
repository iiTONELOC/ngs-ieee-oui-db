# Constants

## `ALPHANUMERIC_ASCII_REGEX_PATTERN`

- **Description**: A regex pattern for validating an alphanumeric ASCII string (including spaces).
- **Pattern**: `^[a-zA-Z0-9\s]+$`

## `MAC_ADDRESS_REGEX_PATTERN`

- **Description**: A regex pattern for validating a device's MAC address.
- **Pattern**: `^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$`

---

## Function: `valid`

### Description

Validates a value against a provided regex pattern.

### Parameters

- **`withPattern` (str)**: The regex pattern to validate against.
- **`againstValue` (any)**: The value to validate.

### Returns

- **`re.Match[str] | None`**: 
  - Returns a match object if the value is valid according to the regex pattern.
  - Returns `None` if the value is invalid.

### Example Usage

```python
# Validate an alphanumeric string
pattern = ALPHANUMERIC_ASCII_REGEX_PATTERN
value = "Hello123"
result = valid(withPattern=pattern, againstValue=value)
if result:
    print("Valid input!")
else:
    print("Invalid input.")

# Validate a MAC address
pattern = MAC_ADDRESS_REGEX_PATTERN
value = "00:1A:2B:3C:4D:5E"
result = valid(withPattern=pattern, againstValue=value)
if result:
    print("Valid MAC address!")
else:
    print("Invalid MAC address.")

```

### Notes

- This function utilizes the re.match function from Python's re module.
- If the againstValue is not a string, the function may throw an error due to type mismatch.


---

- [README](../README.md)
- Documentation
  - [Utils](./utils.MD)
  - [IEE_OUI_DB](./IEE_OUI.MD)
  - [Is IoT Device](./isIot.MD)
  - [Command Line Interface](./cli.MD)
  - [Extract IoT Manufacturers](./extractIot.MD)
