from NG_OUI_DB import IeeOuiDb, OUI_CSV_URL

db = IeeOuiDb()


sampleData = {
    "00:00:00": {
        "Registry": "MA-L",
        "Assignment": "000000",
        "Organization Name": "XEROX CORPORATION",
        "Organization Address": "M/S 105-50C WEBSTER NY US 14580",
    },
    "50:1A:C5": {
        "Registry": "MA-L",
        "Assignment": "501AC5",
        "Organization Name": "Microsoft",
        "Organization Address": "1 Microsoft Way Redmond Washington US 98052",
    },
    "70:9E:29": {
        "Registry": "MA-L",
        "Assignment": "709E29",
        "Organization Name": "Sony Interactive Entertainment Inc.",
        "Organization Address": "1-7-1 Konan Minato-ku Tokyo JP 108-0075",
    },
}

xeroxOUIs = [
    "000000",
    "000001",
    "000002",
    "000003",
    "000004",
    "000005",
    "000006",
    "000007",
    "000008",
    "000009",
    "0000AA",
    "9C934E",
    "E84DEC",
]


def test_getDb():
    _db: dict = db.getDb()

    assert _db is not None
    assert type(_db) is dict


def test_getDbUrl():
    _url: str = db.getDbUrl()

    assert _url is not None
    assert type(_url) is str
    assert _url == OUI_CSV_URL


def test_getOrganizationName():
    for key in sampleData:
        assert db.getOrganizationName(key) == sampleData[key]["Organization Name"]


def test_getOrganizationAddress():
    for key in sampleData:
        assert db.getOrganizationAddress(key) == sampleData[key]["Organization Address"]


def test_getAssignment():
    for key in sampleData:
        assert db.getAssignment(key) == sampleData[key]["Assignment"]


def test_getRegistry():
    for key in sampleData:
        assert db.getRegistry(key) == sampleData[key]["Registry"]


def test_getOrganization():
    for key in sampleData:
        assert db.getOrganization(key) == {
            "Registry": sampleData[key]["Registry"],
            "Assignment": sampleData[key]["Assignment"],
            "Organization Name": sampleData[key]["Organization Name"],
            "Organization Address": sampleData[key]["Organization Address"],
        }


def test_getOrganizationsMac():
    assert sorted(db.getOrganizationsMac("XEROX CORPORATION")) == sorted(xeroxOUIs)


def test_getOrganizations():
    assert len(db.getOrganizations()) >= 19491


def test_getOrganizationsCount():
    assert db.getOrganizationsCount() >= 19491


def test_getOrganizationsMacCount():
    assert db.getOrganizationsMacCount() >= 36671


def test_getOrganizationsMacCountByOrganization():
    assert db.getOrganizationsMacCountByOrganization("XEROX CORPORATION") == len(
        xeroxOUIs
    )
    assert db.getOrganizationsMacCountByOrganization("Microsoft") == 104
    assert (
        db.getOrganizationsMacCountByOrganization("Sony Interactive Entertainment Inc.")
        == 39
    )


def test_getOrganizationsMacCountByAssignment():
    assert db.getOrganizationsMacCountByAssignment("000000") == 1
    assert db.getOrganizationsMacCountByAssignment("501AC5") == 1
    assert db.getOrganizationsMacCountByAssignment("709E29") == 1


def test_getOrganizationsMacCountByRegistry():
    assert db.getOrganizationsMacCountByRegistry("MA-L") >= 36671


def test_getOrganizationsByAssignment():
    assert db.getOrganizationsByAssignment("000000") == ["XEROX CORPORATION"]
    assert db.getOrganizationsByAssignment("501AC5") == ["Microsoft"]
    assert db.getOrganizationsByAssignment("709E29") == [
        "Sony Interactive Entertainment Inc."
    ]


def test_getOrganizationsByRegistry():
    assert len(db.getOrganizationsByRegistry("MA-L")) >= 36671


def test_getOrganizationsByOrganization():
    orgs: list[dict[str, str]] = db.getOrganizationsByOrganization("XEROX CORPORATION")
    assert len(orgs) == len(xeroxOUIs)

    for org in orgs:
        assert org["Assignment"] in xeroxOUIs
        assert org["Organization Name"].lower() == "XEROX CORPORATION".lower()


def test_getOrganizationsByOrganizationAndAssignment():
    orgs: list[dict[str, str]] = db.getOrganizationsByOrganizationAndAssignment(
        "XEROX CORPORATION", "000000"
    )
    assert len(orgs) == 1

    for org in orgs:
        assert org["Assignment"] == "000000"
        assert org["Organization Name"] == "XEROX CORPORATION"
        assert org["Organization Address"] == "M/S 105-50C WEBSTER NY US 14580"


def test_getOrganizationsByOrganizationAndRegistry():
    orgs: list[dict[str, str]] = db.getOrganizationsByOrganizationAndRegistry(
        "XEROX CORPORATION", "MA-L"
    )
    assert len(orgs) == len(xeroxOUIs)

    for org in orgs:
        assert org["Assignment"] in xeroxOUIs
        assert org["Organization Name"].lower() == "XEROX CORPORATION".lower()


def test_getOrganizationsByAssignmentAndRegistry():
    orgs: list[str] = db.getOrganizationsByAssignmentAndRegistry("000000", "MA-L")
    assert len(orgs) == 1

    for org in orgs:
        assert org == "XEROX CORPORATION"


def test_getOrganizationsByOrganizationAssignmentAndRegistry():
    orgs: list[dict[str, str]] = db.getOrganizationsByOrganizationAssignmentAndRegistry(
        "XEROX CORPORATION", "000000", "MA-L"
    )

    assert len(orgs) == 1

    for org in orgs:
        assert org["Assignment"] == "000000"
        assert org["Organization Name"].lower() == "XEROX CORPORATION".lower()
