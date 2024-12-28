"""
Author: Anthony Tropeano
Date: 12/24/2024

Description: This module provides a class to get the IEEE OUI database as a
dictionary and provides methods to get information from the database.

Copyright: (c) 2024 Anthony Tropeano
All Rights Reserved
"""

import os
import csv
import json
import time
import pickle
import requests
from typing import Literal

from .utils import getOuiFromMac

_24_HOURS = 24 * 60 * 60
NO_UPDATED_NEEDED = "No Update Needed"
ORGANIZATION_NAME = "Organization Name"
FAILED_TO_GET_CSV_FILE = "Failed to get the csv file"
OUI_CSV_URL = "https://standards-oui.ieee.org/oui/oui.csv"
CSV_FILE_NAME = os.path.expanduser("~/NG_OUI_DB/iee_oui.csv")


class IeeOuiDb:
    """
    A class to get the IEEE OUI database as a dictionary and provides methods to
    get information from the database.

    Attributes:
    - url (str): The URL of the IEEE OUI database
    - csvFilename (str): The filename of the IEEE OUI database in CSV format
    - dbDict (dict): The IEEE OUI database as a dictionary

    Methods:
    - getDb(): Returns the IEEE OUI database as a dictionary
    - getDbUrl(): Returns the URL of the IEEE OUI database
    - getOrganizationName(mac: str): Returns the organization name of a MAC address
    - getOrganizationAddress(mac: str): Returns the organization address of a MAC address
    - getAssignment(mac: str): Returns the assignment of a MAC address
    - getRegistry(mac: str): Returns the registry of a MAC address
    - getOrganization(mac: str): Returns the organization of a MAC address
    - getOrganizationsMac(organization: str): Returns a list of MAC addresses of an
        organization
    - getOrganizations(): Returns a list of organizations
    - getOrganizationsCount(): Returns the count of organizations
    - getOrganizationsMacCount(): Returns the count of MAC addresses
    - getOrganizationsMacCountByOrganization(organization: str): Returns the count of
        MAC addresses of an organization
    - getOrganizationsMacCountByAssignment(assignment: str): Returns the count of MAC
        addresses of an assignment
    - getOrganizationsMacCountByRegistry(registry: str): Returns the count of MAC
        addresses of a registry
    - getOrganizationsByAssignment(assignment: str): Returns a list of organizations by
        assignment
    - getOrganizationsByRegistry(registry: str): Returns a list of organizations by
        registry
    - getOrganizationsByOrganization(organization: str): Returns a list of organizations
        by organization
    - getOrganizationsByOrganizationAndAssignment(organization: str, assignment: str):
        Returns a list of organizations by organization and assignment
    - getOrganizationsByOrganizationAndRegistry(organization: str, registry: str):
        Returns a list of organizations by organization and registry
    - getOrganizationsByAssignmentAndRegistry(assignment: str, registry: str): Returns
        a list of organizations by assignment and registry
    - getOrganizationsByOrganizationAssignmentAndRegistry(organization: str, assignment:
        str, registry: str): Returns a list of organizations by organization, assignment,
        and registry
    """

    def __init__(self) -> None:
        self.url: str = OUI_CSV_URL
        self.csvFilename: str = self._getIeeOuiDbAsCsv(self.url)
        self.dbDict: dict = self._convertCsvToDict(self.csvFilename)

    def getDb(self) -> dict:
        """Returns the IEEE OUI database as a dictionary

        Returns:
            dict: The IEEE OUI database as a dictionary
        """
        return self.dbDict

    def getDbUrl(self) -> str:
        """Returns the URL of the IEEE OUI database"""
        return self.url

    def getOrganizationName(self, mac: str) -> str | Literal["Unknown"]:
        """Returns the organization name of a MAC address

        Args:
            mac (str): The MAC address to get the organization name of
        Returns:
            str | Literal["Unknown"]: The organization name of a MAC address or "Unknown"
        """
        try:
            oui = getOuiFromMac(mac=mac)
            return self.dbDict[oui][ORGANIZATION_NAME]
        except KeyError:
            return "Unknown"

    def getOrganizationAddress(self, mac: str) -> str | Literal["Unknown"]:
        """Returns the organization address of a MAC address

        Args:
            mac (str): The MAC address to get the organization address of
        Returns:
            str | Literal["Unknown"]: The organization address of a MAC address or "Unknown"
        """
        try:
            oui = getOuiFromMac(mac=mac)
            return self.dbDict[oui]["Organization Address"]
        except KeyError:
            return "Unknown"

    def getAssignment(self, mac: str) -> str | Literal["Unknown"]:
        """Returns the assignment of a MAC address

        Args:
            mac (str): The MAC address to get the assignment of
        Returns:
            str | Literal["Unknown"]: The assignment of a MAC address or "Unknown"
        """
        try:
            oui = getOuiFromMac(mac=mac)
            return self.dbDict[oui]["Assignment"]
        except KeyError:
            return "Unknown"

    def getRegistry(self, mac: str) -> str | Literal["Unknown"]:
        """Returns the registry of a MAC address

        Args:
            mac (str): The MAC address to get the registry of
        Returns:
            str | Literal["Unknown"]: The registry of a MAC address or "Unknown"
        """
        try:
            oui = getOuiFromMac(mac=mac)
            return self.dbDict[oui]["Registry"]
        except KeyError:
            return "Unknown"

    def getOrganization(self, mac: str) -> str | Literal["Unknown"]:
        """Returns the organization of a MAC address

        Args:
            mac (str): The MAC address to get the organization of
        Returns:
            str | Literal["Unknown"]: The organization of a MAC address or "Unknown"
        """
        try:
            oui = getOuiFromMac(mac=mac)
            return self.dbDict[oui]
        except KeyError:
            return "Unknown"

    def getOrganizationsMac(self, organization: str) -> list[str]:
        """Returns a list of MAC addresses of an organization

        Args:
            organization (str): The name of the organization to get the MAC addresses of

        Returns:
            list[str]: A list of MAC addresses registered to the organization
        """
        orgsMacs: list[str] = []
        for mac in self.dbDict:
            if organization.lower() in self.dbDict[mac][ORGANIZATION_NAME].lower():
                orgsMacs.append(mac)
        return orgsMacs

    def getOrganizations(self) -> list[str]:
        """Returns a list of organizations registered in the database"""

        organizations: set = set()
        for mac in self.dbDict:
            organizations.add(self.dbDict[mac][ORGANIZATION_NAME])
        myList: list[str] = list(organizations)
        myList.sort()
        return myList

    def getOrganizationsCount(self) -> int:
        """Returns the number of organizations registered in the database"""
        return len(self.getOrganizations())

    def getOrganizationsMacCount(self) -> int:
        """Returns the number of MAC addresses registered in the database"""
        return len(self.dbDict)

    def getOrganizationsMacCountByOrganization(self, organization: str) -> int:
        """Returns the number of MAC addresses registered to an organization

        Args:
            organization (str): The name of the organization to get the MAC addresses of

        Returns:
            int: The number of MAC addresses registered to the organization
        """
        count: int = 0
        for oui in self.dbDict:
            if organization.lower() in self.dbDict[oui][ORGANIZATION_NAME].lower():
                count += 1
        return count

    def getOrganizationsMacCountByAssignment(self, assignment: str) -> int:
        """Returns the number of MAC addresses registered to an assignment

        Args:
            assignment (str): The assignment to get the MAC addresses of

        Returns:
            int: The number of MAC addresses registered to the assignment
        """
        count: int = 0
        for oui in self.dbDict:
            if self.dbDict[oui]["Assignment"] == assignment:
                count += 1
        return count

    def getOrganizationsMacCountByRegistry(self, registry: str) -> int:
        """Returns the number of MAC addresses registered to a registry

        Args:
            registry (str): The name of the registry containing the MAC addresses

        Returns:
            int: The number of MAC addresses registered to the registry
        """
        count: int = 0
        for oui in self.dbDict:
            if self.dbDict[oui]["Registry"] == registry:
                count += 1
        return count

    def getOrganizationsByAssignment(self, assignment: str) -> list[str]:
        """Returns a list of organizations by assignment

        Args:
            assignment (str): The assignment to get the organizations of

        Returns:
            list[str]: A list of organizations by assignment
        """
        organizations: list[str] = []
        for oui in self.dbDict:
            if self.dbDict[oui]["Assignment"] == assignment:
                organizations.append(self.dbDict[oui][ORGANIZATION_NAME])
        return organizations

    def getOrganizationsByRegistry(self, registry: str) -> list[str]:
        """Returns a list of organizations by registry

        Args:
            registry (str): The name of the registry

        Returns:
            list[str]: A list of organizations contained in the registry
        """
        organizations: list[str] = []
        for oui in self.dbDict:
            if self.dbDict[oui]["Registry"] == registry:
                organizations.append(self.dbDict[oui][ORGANIZATION_NAME])
        return organizations

    def getOrganizationsByOrganization(self, organization: str) -> list[dict[str, str]]:
        """Returns a list of organizations registered to an organization

        Args:
            organization (str): The name of the organization to get the organizations of

        Returns:
            list[dict[str,str]]: A list of organizations registered to the organization
        """
        organizations: list[dict[str, str]] = []
        for oui in self.dbDict:
            if organization.lower() in self.dbDict[oui][ORGANIZATION_NAME].lower():
                organizations.append(self.dbDict[oui])
        return organizations

    def getOrganizationsByOrganizationAndAssignment(
        self, organization: str, assignment: str
    ) -> list[str]:
        """Returns a list of organizations by organization and assignment

        Args:
            organization (str): The name of the organization
            assignment (str): The assignment to look for

        Returns:
            list[str]: A list of organizations by organization and assignment
        """
        organizations: list[str] = []
        for oui in self.dbDict:
            if (
                organization.lower() in self.dbDict[oui][ORGANIZATION_NAME].lower()
                and self.dbDict[oui]["Assignment"] == assignment
            ):
                organizations.append(self.dbDict[oui])
        return organizations

    def getOrganizationsByOrganizationAndRegistry(
        self, organization: str, registry: str
    ) -> list[str]:
        """Returns a list of organizations by organization and registry

        Args:
            organization (str): The name of the organization
            registry (str): The name of the registry

        Returns:
            list[str]: A list of organizations within the registry matching the organization name
        """
        organizations: list[str] = []
        for oui in self.dbDict:
            if (
                organization.lower() in self.dbDict[oui][ORGANIZATION_NAME].lower()
                and self.dbDict[oui]["Registry"] == registry
            ):
                organizations.append(self.dbDict[oui])
        return organizations

    def getOrganizationsByAssignmentAndRegistry(
        self, assignment: str, registry: str
    ) -> list[str]:
        """Returns a list of organizations by assignment and registry

        Args:
            assignment (str): The assignment to look for
            registry (str): The name of the registry

        Returns:
            list[str]: A list of organizations within the registry matching the assignment
        """
        organizations: list[str] = []
        for oui in self.dbDict:
            if (
                self.dbDict[oui]["Assignment"] == assignment
                and self.dbDict[oui]["Registry"] == registry
            ):
                organizations.append(self.dbDict[oui][ORGANIZATION_NAME])
        return organizations

    def getOrganizationsByOrganizationAssignmentAndRegistry(
        self, organization: str, assignment: str, registry: str
    ) -> list[str]:
        """Returns a list of organizations by organization, assignment, and registry

        Args:
            organization (str): The name of the organization
            assignment (str): The assignment to look for
            registry (str): The name of the registry

        Returns:
            list[str]: A list of organizations within the registry matching the
            organization name, assignment, and registry
        """
        organizations: list[str] = []
        for oui in self.dbDict:
            if (
                organization.lower() in self.dbDict[oui][ORGANIZATION_NAME].lower()
                and self.dbDict[oui]["Assignment"] == assignment
                and self.dbDict[oui]["Registry"] == registry
            ):
                organizations.append(self.dbDict[oui])

        return organizations

    def _getIeeOuiDbAsCsv(self, url: str) -> str:
        """Get the IEEE OUI database as a CSV file and save it to the filesystem

        Args:
            url (str): The URL of the IEEE OUI database

        Returns:
            str: The filename of the CSV file or relevant error message

        Note:
            The IEEE OUI database is saved to the filesystem for future use if
            it is not present on the filesystem or if it has not been updated
            in the last 24 hours.

            Data is saved to the ~/homeSecurityAppliance/ directory.
        """

        def fetch() -> None | Literal["Failed to get the csv file"]:
            response: requests.Response = requests.get(
                url, headers={"User-Agent": "Mozilla/5.0"}
            )
            if response.status_code != 200:
                return FAILED_TO_GET_CSV_FILE

            if not os.path.exists(os.path.dirname(CSV_FILE_NAME)):
                os.makedirs(os.path.dirname(CSV_FILE_NAME))

            with open(CSV_FILE_NAME, "wb") as file:
                file.write(response.content)

        if os.path.exists(CSV_FILE_NAME):
            if time.time() - os.path.getmtime(CSV_FILE_NAME) > _24_HOURS:
                fetch()
            else:
                return NO_UPDATED_NEEDED
        else:
            fetch()
        return CSV_FILE_NAME

    def _convertCsvToDict(self, fileName: str) -> dict[str, dict[str, str]]:
        """Convert the IEEE OUI database from a CSV file to a dictionary

        Args:
            fileName (str): The filename of the CSV file

        Returns:
            dict[str, dict[str, str]]: The IEEE OUI database as a dictionary

        Note:
            The CSV data is read from the file system and converted to a dictionary.
            The dictionary is then saved as a JSON and pickle file for future use.

            Data is saved to the ~/homeSecurityAppliance/ directory.
        """
        index: int = 0
        d: dict[str, dict[str, str]] = {}
        jsonFileName: str = fileName.replace(".csv", ".json")
        pickleFileName: str = fileName.replace(".csv", ".pkl")

        # if the file is not found, return an empty dictionary
        if fileName == FAILED_TO_GET_CSV_FILE:
            return d

        # if an update is not needed, load the pickle file
        if fileName == NO_UPDATED_NEEDED:
            pickleFileName = CSV_FILE_NAME.replace(".csv", ".pkl")
            with open(pickleFileName, "rb") as file:
                return pickle.load(file)

        # else read the csv file and convert it to a dictionary
        with open(fileName, "r", encoding="utf-8") as file:
            reader = csv.reader(file, quotechar='"', delimiter=",")
            for line in reader:
                if index > 0:
                    d[line[1].replace("-", "")] = {
                        "Registry": line[0].strip(),
                        "Assignment": line[1].strip(),
                        "Organization Name": line[2].strip(),
                        "Organization Address": line[3].strip(),
                    }

                index += 1

        # save the dictionary as a json and pickle file
        with open(jsonFileName, "w", encoding="utf-8") as file:
            file.write(json.dumps(d, indent=4))

        with open(pickleFileName, "wb") as file:
            pickle.dump(d, file)

        return d
