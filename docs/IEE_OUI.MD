# IEEE OUI Database Class

A class to get the IEEE OUI database as a dictionary and provides methods to get information from the database.

## Attributes

- **url** (`str`): The URL of the IEEE OUI database.
- **csvFilename** (`str`): The filename of the IEEE OUI database in CSV format.
- **dbDict** (`dict`): The IEEE OUI database as a dictionary.

## Methods

### Database Access

- **`getDb()`**  
  Returns the IEEE OUI database as a dictionary.

- **`getDbUrl()`**  
  Returns the URL of the IEEE OUI database.

### MAC Address Information

- **`getOrganizationName(mac: str)`**  
  Returns the organization name of a MAC address.

- **`getOrganizationAddress(mac: str)`**  
  Returns the organization address of a MAC address.

- **`getAssignment(mac: str)`**  
  Returns the assignment of a MAC address.

- **`getRegistry(mac: str)`**  
  Returns the registry of a MAC address.

- **`getOrganization(mac: str)`**  
  Returns the organization of a MAC address.

### Organization Queries

- **`getOrganizationsMac(organization: str)`**  
  Returns a list of MAC addresses of an organization.

- **`getOrganizations()`**  
  Returns a list of organizations.

- **`getOrganizationsCount()`**  
  Returns the count of organizations.

### MAC Address Count Queries

- **`getOrganizationsMacCount()`**  
  Returns the count of MAC addresses.

- **`getOrganizationsMacCountByOrganization(organization: str)`**  
  Returns the count of MAC addresses of an organization.

- **`getOrganizationsMacCountByAssignment(assignment: str)`**  
  Returns the count of MAC addresses of an assignment.

- **`getOrganizationsMacCountByRegistry(registry: str)`**  
  Returns the count of MAC addresses of a registry.

### Organization Filtering by Assignment or Registry

- **`getOrganizationsByAssignment(assignment: str)`**  
  Returns a list of organizations by assignment.

- **`getOrganizationsByRegistry(registry: str)`**  
  Returns a list of organizations by registry.

- **`getOrganizationsByOrganization(organization: str)`**  
  Returns a list of organizations by organization.

- **`getOrganizationsByOrganizationAndAssignment(organization: str, assignment: str)`**  
  Returns a list of organizations by organization and assignment.

- **`getOrganizationsByOrganizationAndRegistry(organization: str, registry: str)`**  
  Returns a list of organizations by organization and registry.

- **`getOrganizationsByAssignmentAndRegistry(assignment: str, registry: str)`**  
  Returns a list of organizations by assignment and registry.

- **`getOrganizationsByOrganizationAssignmentAndRegistry(organization: str, assignment: str, registry: str)`**  
  Returns a list of organizations by organization, assignment, and registry.

### NOTE

When initialized, the object will save data to `~/NG_OUI_DB/`. This data includes:

- Downloaded database from IEE as a .csv file `iee_oui.csv`
- JSON file for interopability `iee_oui.json`
- Pickle file for easy reloading `iee_oui.pkl`

---

- [README](../README.md)
- Documentation
  - [Utils](./utils.MD)
  - [Is IoT Device](./isIot.MD)
  - [Validators](./validators.MD)
  - [Command Line Interface](./cli.MD)
  - [Extract IoT Manufacturers](./extractIot.MD)
