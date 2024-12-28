# Function: `runAsCLI`

Provides a Command-Line Interface (CLI) for the IEEE OUI Database.

## Description

This function initializes the IEEE OUI database, retrieves or creates the database as needed, and provides a menu-driven interface for user interaction. The CLI allows users to interact with the database through various menu options, handling updates and caching.

## Parameters

None

## Exceptions

- **KeyboardInterrupt**: Allows for graceful termination of the program when the user interrupts with `Ctrl+C`.
- **Exception**: Catches unexpected errors, logs the traceback, and terminates the program with an error message.

## Attributes

- **retrievedFromCache (bool)**: Indicates whether the database was retrieved from the cache.
- **startTime (float)**: The starting time of the process.
- **endTime (float)**: The ending time of the process.
- **elapsedTimeInSeconds (float)**: Total elapsed time to retrieve or create the database.

## Workflow

1. **Initialize the Database**:
   - Creates an instance of the `IeeOuiDb` class.
   - Retrieves the database as a dictionary.
   - Checks if the database was retrieved from the cache or generated.

2. **Display Database Details**:
   - Number of records in the database.
   - URL of the IEEE OUI database.
   - Last updated timestamp.
   - Time elapsed during database creation or retrieval.

3. **Interactive CLI**:
   - Displays a menu with options for interacting with the database.
   - Waits for user input to process the choice.
   - Provides feedback and allows continuous interaction.

4. **Graceful Exit**:
   - Handles user-initiated termination (`KeyboardInterrupt`).
   - Logs unexpected errors and terminates safely.

## Example Output

Number of Records Found: 12345  
URL: [https://standards-oui.ieee.org/oui/oui.csv](https://standards-oui.ieee.org/oui/oui.csv)  
Last Updated: Mon Dec 25 12:34:56 2023 (Retrieved from Cache)  
Elapsed Time: 0.1234567890 seconds

## Notes

- The function relies on helper functions like `showMenu` and `handleMenuChoice` for menu display and processing.
- If the CSV file fails to download or update, the program exits with an appropriate error message.

---

- [README](../README.md)
- Documentation
  - [Utils](./utils.MD)
  - [IEE_OUI_DB](./IEE_OUI.MD)
  - [Is IoT Device](./isIot.MD)
  - [Validators](./validators.MD)
  - [Extract IoT Manufacturers](./extractIot.MD)
