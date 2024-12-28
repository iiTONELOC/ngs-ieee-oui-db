# Utils

## `getMacAddress()`

**Description**  
Prompts the user to enter a valid MAC address and ensures the input is a valid MAC address format using the `MAC_ADDRESS_REGEX_PATTERN`.

**Returns** 

- `str`: The validated MAC address entered by the user.

**Example Usage**
```python
mac_address = getMacAddress()
print(f"Validated MAC Address: {mac_address}")
```

---

## `getAlphaNumericString(msg: str)`

**Description**  
Prompts the user to enter a string that only contains alphanumeric characters (and spaces). The input is validated using the `ALPHANUMERIC_ASCII_REGEX_PATTERN`.

**Parameters**
- `msg` (str): The message prompt to display to the user.

**Returns**  
- `str`: The validated alphanumeric string entered by the user.

**Example Usage**  
```python
organization_name = getAlphaNumericString(msg="Enter the Organization Name: ")
print(f"Organization Name: {organization_name}")
```

---

## `getOrgName()`

**Description**  
Prompts the user to enter the organization name using `getAlphaNumericString`.

**Returns**  
- `str`: The validated organization name entered by the user.

**Example Usage**  
```python
org_name = getOrgName()
print(f"Organization Name: {org_name}")
```

---

## `getAssignment()`

**Description**  
Prompts the user to enter an assignment using `getAlphaNumericString`.

**Returns**  
- `str`: The validated assignment entered by the user.

**Example Usage**  
```python
assignment = getAssignment()
print(f"Assignment: {assignment}")
```

---

## `getRegistry()`

**Description**  
Prompts the user to enter a registry using `getAlphaNumericString`.

**Returns**  
- `str`: The validated registry entered by the user.

**Example Usage**  
```python
registry = getRegistry()
print(f"Registry: {registry}")
```

---

## `getOuiFromMac(mac: str)`

**Description**  
Takes a MAC address, removes any hyphens or colons, and returns the first 6 characters of the MAC address, which is the OUI (Organizationally Unique Identifier).

**Parameters**  
- `mac` (str): The MAC address to process.

**Returns**  
- `str`: The OUI part of the MAC address.

**Example Usage**  
```python
mac = "00:1A:2B:3C:4D:5E"
oui = getOuiFromMac(mac)
print(f"OUI: {oui}")
```

---

## `jsonWithProperIndent(dict: dict, indent=int, startingIndent=0)`

**Description**  
Formats a dictionary into a JSON string with proper indentation, including nested dictionaries.

**Parameters**  
- `dict` (dict): The dictionary to format into JSON.
- `indent` (int): The number of spaces for indentation.
- `startingIndent` (int): The starting level of indentation.

**Returns**  
- `str`: The formatted JSON string.

**Example Usage**  
```python
data = {"name": "John", "address": {"city": "New York", "state": "NY"}}
formatted_json = jsonWithProperIndent(data, indent=4, startingIndent=0)
print(formatted_json)
```

---

## `printArrayWithProperIndent(arr: list, indent=int, startingIndent=0)`

**Description**  
Formats a list into a JSON-style array string with proper indentation.

**Parameters**  
- `arr` (list): The list to format into JSON array.
- `indent` (int): The number of spaces for indentation.
- `startingIndent` (int): The starting level of indentation.

**Returns**  
- `str`: The formatted JSON-style array string.

**Example Usage**  
```python
items = ["apple", "banana", "cherry"]
formatted_array = printArrayWithProperIndent(items, indent=4, startingIndent=0)
print(formatted_array)
```
---

- [README](../README.md)
- Documentation
  - [Validators](./validators.MD)
  - [IEE_OUI_DB](./IEE_OUI.MD)
  - [Is IoT Device](./isIot.MD)
  - [Command Line Interface](./cli.MD)
  - [Extract IoT Manufacturers](./extractIot.MD)
