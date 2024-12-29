import os
import time
import traceback

from NG_OUI_DB import (
    IeeOuiDb,
    CSV_FILE_NAME,
    NO_UPDATED_NEEDED,
    FAILED_TO_GET_CSV_FILE,
)
from .utils import (
    getOrgName,
    getRegistry,
    getAssignment,
    getMacAddress,
    jsonWithProperIndent,
    arrayWithProperIndent,
)

PROMPT = "Enter your choice: "
MAC_PROMPT = "Enter the MAC Address: "


def handleMenuChoice(choice: str, database: IeeOuiDb) -> None:
    print()
    match choice:
        case "1":
            mac: str = getMacAddress()
            print(f"\n  {database.getOrganizationName(mac=mac)}")
        case "2":
            mac: str = getMacAddress()
            print(f"\n  {database.getOrganizationAddress(mac=mac)}")
        case "3":
            mac: str = getMacAddress()
            print(f"\n  {database.getAssignment(mac=mac)}")
        case "4":
            mac: str = getMacAddress()
            print(f"\n  {database.getRegistry(mac=mac)}")
        case "5":
            mac: str = getMacAddress()
            print(
                f"\n{jsonWithProperIndent(dict=database.getOrganization(mac=mac),
                    indent=4,
                    startingIndent=2
                )}"
            )
        case "6":
            organization: str = getOrgName()
            print(f"\n{database.getOrganizationsMac(organization=organization)}")
        case "7":
            print(
                f"\n{arrayWithProperIndent(arr=database.getOrganizations(), indent=4)}"
            )
        case "8":
            print(f"\n  {database.getOrganizationsCount()}")
        case "9":
            print(f"\n  {database.getOrganizationsMacCount()}")
        case "10":
            organization = getOrgName()
            print(
                f"\n  {database.getOrganizationsMacCountByOrganization(organization=organization)}"
            )
        case "11":
            assignment = getAssignment()
            print(
                f"\n  {database.getOrganizationsMacCountByAssignment(assignment=assignment)}"
            )
        case "12":
            registry = getRegistry()
            print(
                f"\n  {database.getOrganizationsMacCountByRegistry(registry=registry)}"
            )
        case "13":
            assignment = getAssignment()
            print(f"\n  {database.getOrganizationsByAssignment(assignment=assignment)}")
        case "14":
            registry = getRegistry()
            print(f"\n  {database.getOrganizationsByRegistry(registry=registry)}")
        case "15":
            organization = getOrgName()
            print(
                f"\n  {database.getOrganizationsByOrganization(organization=organization)}"
            )
        case "16":
            organization = getOrgName()
            assignment = getAssignment()
            print(
                f"\n {database.getOrganizationsByOrganizationAndAssignment(
                        organization=organization,
                        assignment=assignment
                    )}"
            )
        case "17":
            organization = getOrgName()
            registry = getRegistry()
            print(
                f"\n {database.getOrganizationsByOrganizationAndRegistry(
                        organization=organization,
                        registry=registry
                    )}"
            )
        case "18":
            assignment = getAssignment()
            registry = getRegistry()
            print(
                f"\n {database.getOrganizationsByAssignmentAndRegistry(
                    assignment=assignment,
                    registry=registry
                    )}"
            )
        case "19":
            organization = getOrgName()
            assignment = getAssignment()
            registry = getRegistry()
            print(
                f"\n {database.getOrganizationsByOrganizationAssignmentAndRegistry(
                        organization=organization,
                        assignment=assignment,
                        registry=registry
                    )}"
            )
        case "q":
            exitProgram(0)
        case _:
            print("Invalid Selection")


def showMenu() -> None:
    options: list[str] = [
        "Get Organization Name from MAC Address",
        "Get Organization Address from MAC Address",
        "Get Assignment from MAC Address",
        "Get Registry from MAC Address",
        "Get Organization from MAC Address",
        "Get Organization's Mac Addresses by Organization Name",
        "Get Organizations List",
        "Get Organizations Count",
        "Get Organizations Mac Count",
        "Get Organizations Mac Count By Organization",
        "Get Organizations Mac Count By Assignment",
        "Get Organizations Mac Count By Registry",
        "Get Organizations By Assignment Name",
        "Get Organizations By Registry Name",
        "Get Organizations By Organization Name",
        "Get Organizations By Organization And Assignment Name",
        "Get Organizations By Organization And Registry Name",
        "Get Organizations By Assignment And Registry Name",
        "Get Organizations By Organization Assignment And Registry Name",
    ]

    print("\nIEE OUI DB Menu:")
    for i, option in enumerate(options):
        print(f"  {i+1}. {option}")


def exitProgram(code: int) -> None:
    print("\nExiting...")
    exit(code)


def runAsCLI() -> None:
    """Provides a CLI interface for the IEE OUI Database."""
    retrievedFromCache = False
    startTime: float = time.time()

    ouiDb = IeeOuiDb()
    dbDict: dict = ouiDb.getDb()
    filename: str = ouiDb.csvFilename

    if filename == FAILED_TO_GET_CSV_FILE:
        print("Failed to get the csv file")
        exit(1)

    if filename == NO_UPDATED_NEEDED:
        retrievedFromCache = True
        filename = CSV_FILE_NAME

    endTime: float = time.time()
    elapsedTimeInSeconds: float = endTime - startTime

    print(
        f"\n{'-' * 80}\n\n"
        f"Number of Records Found: {len(dbDict)}\n"
        f"URL: {ouiDb.getDbUrl()}\n"
        f"Last Updated: {time.ctime(os.path.getmtime(filename))} "
        f"{'(Retrieved from Cache)' if retrievedFromCache else 'DB Created Successfully'}\n"
        f"Elapsed Time: {elapsedTimeInSeconds:.10f} seconds"
    )

    try:
        while True:
            showMenu()
            choice: str = input("Enter your choice: ")
            handleMenuChoice(choice=choice, database=ouiDb)
            input("\nPress Enter to continue...")
            print("-" * 80)
    except KeyboardInterrupt:
        exitProgram(0)
    except Exception:
        print(f"An error occurred: {traceback.format_exc()}")
        exitProgram(1)
