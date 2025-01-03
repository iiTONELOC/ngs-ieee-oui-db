# IOT Manufacturers Identification Script Documentation

## Overview

This script identifies suspected IoT manufacturers from the IEEE OUI database based on a predefined set of keywords. It provides functionality to extract, filter, and persist this data for future use.

---

## Constants

### `IOT_MAN_JSON_FILE`

- **Type**: `str`
- **Description**: Path to the JSON file where the IoT manufacturers list will be saved. It defaults to a file in the user's home directory: `~/NG_OUI_DB/iot_manufacturers.json`.

### `IOT_MAN_PICKLE_FILE`

- **Type**: `str`
- **Description**: Path to the pickle file where the IoT manufacturers set will be serialized. This path is derived from `IOT_MAN_JSON_FILE` by replacing `.json` with `.pkl`.

### `IOT_KEYWORDS`

- **Type**: `list[str]`
- **Description**: A list of keywords used to identify IoT manufacturers from the organization names in the IEEE OUI database.
- **Example**:
  ```python
  [
      "smart", "iot", "esp", "tuya", "nest", "broadlink",
      "sonoff", "hue", "wyze", "arlo", "ecobee", "eufy",
      "philips", "ikea", "fitbit", "xiaomi", "withings",
      "samsung", "lg", "sony", "media", "netgear",
      "tp-link", "ubiquiti", "honeywell"
  ]
  ```

---

## Function: `getIotManufacturers`

### Definition

```python
def getIotManufacturers(fromDatabase: dict | None = None) -> set[str]:
```

### Purpose

Extracts and identifies IoT manufacturers from the IEEE OUI database using predefined keywords, and persists the data in JSON and pickle formats.

### Parameters

- `fromDatabase` (optional):
  - **Type**: `dict | None`
  - **Description**: A pre-initialized IEEE OUI database dictionary. If not provided, a new instance of `IeeOuiDb` will be created.

### Returns

- **Type**: `set[str]`
- **Description**: A set of unique IoT manufacturer names identified from the database.

### Logic

1. **Initialization**:
   - Creates an instance of `IeeOuiDb` if `fromDatabase` is not provided.
   - Initializes an empty set `iotManufacturers` to store results.

2. **Database Iteration**:
   - Loops through all entries in the IEEE OUI database.
   - Checks if the organization name contains any keyword from `IOT_KEYWORDS` (case-insensitive).
   - Adds matching organization names to the `iotManufacturers` set.

3. **Persistence**:
   - Saves the `iotManufacturers` set as a JSON file at `IOT_MAN_JSON_FILE`.
   - Serializes the `iotManufacturers` set as a pickle file at `IOT_MAN_PICKLE_FILE`.

4. **Return Value**:
   - Returns the `iotManufacturers` set.

### Example Usage

```python
from .IEE_OUI import IeeOuiDb

iotManufacturers = getIotManufacturers()
print("IoT Manufacturers:", iotManufacturers)

# Expected Output
[
    "Audiotonix Group Limited",
    "Algolith",
    "Samsung Electronics Co., Ltd.",
    "Trident IoT",
    "Shenzhen Trylong Smart Science and Technology Co., Ltd.",
    "Honeywell Connected Building",
    "Creatix Polymedia Ges Fur Kommunikaitonssysteme",
    "Circle Media Inc",
    "SmartThings, Inc.",
    "JLG Industries, Inc.",
    "Addrek Smart Solutions",
    "Fihonest communication co.,Ltd",
    "SMART Modular Technologies",
    "Stonestreet One LLC",
    "PHILIPS APELDOORN B.V.",
    "Samsung Electronics Co., Ltd",
    "Shenzhen  Tongfang Multimedia  Technology Co.,Ltd.",
    "Smartronix, Inc.",
    "Shark Multimedia Inc.",
    "Jiangsu Cynray IOT Co., Ltd.",
    "BIOTRONIK GmbH & Co",
    "RACAL-MILGO INFORMATION SYS..",
    "Honeywell (China) Co., LTD",
    "Hisense broadband multimedia technology Co.,Ltd",
    "KLG Smartec",
    "Cybiotronics (Far East) Limited",
    "MEDIA GLOBAL LINKS CO., LTD.",
    "EMC Electronic Media Communication SA",
    "Speed Dragon Multimedia Limited",
    "SMART High Reliability Solutions, Inc.",
    "Finest Security Systems Co., Ltd",
    "Keltron IOT Corp.",
    "Beijing Xiaomi Electronics Co.,Ltd",
    "Shenzhen Atsmart Technology Co.,Ltd.",
    "SmartRG Inc",
    "Leie IOT technology Co., Ltd",
    "LG INTERNATIONAL CORP.",
    "99IOT Shenzhen co.,ltd",
    "PERSONAL MEDIA CORP.",
    "Arria Live Media, Inc.",
    "Media Streaming Networks Inc",
    "InnoVISION Multimedia Ltd.",
    "Mediatek Corp.",
    "LG Display",
    "Hangzhou Sciener Smart Technology Co., Ltd.",
    "Philips Lifeline",
    "Multimedia Pacific Limited",
    "SONY Visual Products Inc.",
    "NOKIA MULTIMEDIA TERMINALS",
    "Hypermedia Systems",
    "Qingdao Hisense Smart Life Technology Co., Ltd",
    "MediaCell, Inc.",
    "ESPRIT SYSTEMS",
    "Espotel Oy",
    "MultiMedia LANs, Inc.",
    "Samsung Electronics Co., Ltd., Memory Division",
    "Ubiquiti Inc",
    "TP-Link Systems Inc.",
    "Philips CFT",
    "Honeywell Analytics",
    "Suzhou SmartChip Semiconductor Co., LTD",
    "DATAMEDIA CORPORATION",
    "Samsung Electronics",
    "Smart Solution, Inc",
    "NETGEAR",
    "Sony Home Entertainment&Sound Products Inc",
    "Smartron India Pvt ltd",
    "Shenzhen Amediatech Technology Co., Ltd.",
    "Amedia Networks Inc.",
    "Nanwang Multimedia Inc.,Ltd",
    "PHILIPS ANALYTICAL X-RAY B.V.",
    "Patriot Memory",
    "CARLO GAVAZZI LTD",
    "NOVAMEDIA INNOVISION SP. Z O.O.",
    "Zettamedia Korea",
    "Sony Corporation",
    "Philips Healthcare PCCI",
    "NEXGEN Mediatech Inc.",
    "NEW MEDIA CORPORATION",
    "TP-Link Corporation Limited",
    "Belgian Monitoring Systems bvba",
    "EHOOME IOT PRIVATE LIMITED",
    "TSMART Inc.",
    "ZPA Smart Energy a.s.",
    "WiMedia Alliance",
    "SmartAnt Telecom",
    "ESPOD Ltd.",
    "Philips CareServant",
    "Fitbit, Inc.",
    "Smart iBlue Technology Limited",
    "Shenzhen Smarteye Digital Electronics Co., Ltd",
    "WiZ IoT Company Limited",
    "Dongguan Lingjie IOT Co., LTD",
    "PhaseSpace",
    "China Mobile Iot Limited company",
    "Eddy Smart Home Solutions Inc.",
    "Prism Media Products Limited",
    "Nest Labs Inc.",
    "Shandong USR IOT Technology Limited",
    "Respironics, Inc.",
    "Shenzhen All-Smartlink Technology Co.,Ltd.",
    "smart-electronic GmbH",
    "SMART Technologies, Inc.",
    "Hilger u. Kern GMBH",
    "S NET MEDIA",
    "FutureSmart Networks, Inc.",
    "Algolware Corporation",
    "Nanjing CAS-ZDC IOT SYSTEM CO.,LTD",
    "Innomedia Technologies Pvt. Ltd.",
    "Smartmatic Corporation",
    "Stage Tec Entwicklungsgesellschaft für professionelle Audiotechnik mbH",
    "ARLOTTO COMNET, INC.",
    "TP-LINK TECHNOLOGIES CO.,LTD.",
    "Sony Interactive Entertainment Inc.",
    "LG Chem",
    "Technicolor Delivery Technologies Belgium NV",
    "Newport Media Inc.",
    "OOO InProMedia",
    "Smarty (HZ) Information Electronics Co., Ltd",
    "LG Electronics (Mobile Communications)",
    "Beijing H-IoT Technology Co., Ltd.",
    "LG Electronics NV",
    "Premier Technolgies, Inc",
    "Honeywell Life Safety",
    "Philips Oral Healthcare, Inc.",
    "SMART Temps LLC",
    "LGE",
    "SMARTSAN SYSTEMS, INC.",
    "COMING MEDIA CORP.",
    "GentechMedia.co.,ltd.",
    "S-Information Technolgy, Co., Ltd.",
    "Media Devices Co., Ltd.",
    "Medialink-i,Inc",
    "SECURITAS DIRECT ESPAÑA, SAU",
    "LG-Ericsson Co.,Ltd.",
    "HUEY CHIAO INTERNATIONAL CO., LTD.",
    "SmarteBuilding",
    "Mediaport USA",
    "Smart Energy Instruments Inc.",
    "GLOBO Multimedia Sp. z o.o. Sp.k.",
    "Media Technology Systems Inc",
    "BodyMedia, Inc.",
    "Shenzhen MeiG Smart Technology Co.,Ltd",
    "Smartrove Inc",
    "Honeywell Safety Products (Shanghai) Co.,Ltd",
    "Monsoon Multimedia, Inc",
    "KE Knestel Elektronik GmbH",
    "Toshiba Samsung Storage Technolgoy Korea Corporation",
    "smartAC.com, Inc.",
    "GESPAC, S.A.",
    "I Smart Cities HK Ltd",
    "Zhong Ge Smart Technology Co., Ltd.",
    "Xenon Smart Teknoloji Ltd.",
    "VOISMART",
    "eSpace",
    "DIAMOND MULTIMEDIA",
    "Shenzhen Honesty Electronics Co.,Ltd.",
    "Elgama-Elektronika Ltd.",
    "Walnut Media Network",
    "Visualgate Systems, Inc.",
    "MACKIE Engineering Services Belgium BVBA",
    "GWD Media Limited",
    "Bosch Car Multimedia (Wuhu) Co. Ltd.",
    "Shenzhen Smart Device Technology Co., LTD.",
    "Alge-Timing GmbH",
    "Smartlabs, Inc.",
    "Inventec Multimedia & Telecom Corporation",
    "Mediabridge Products, LLC.",
    "PHILIPS ELECTRONICS UK LTD",
    "IoT Diagnostics",
    "SAMSUNG Electronics. Co. LTD",
    "Medialogic Corp.",
    "Digital Multimedia Technology Co., Ltd",
    "FRONTIER SMART TECHNOLOGIES LTD",
    "SmartShare Systems",
    "ecobee inc",
    "d&b audiotechnik GmbH",
    "FAST media integrations AG",
    "Algo Communication Products Ltd",
    "ESP SYSTEMS, LLC",
    "SONY TEKTRONIX CORP.",
    "Honeywell GmbH",
    "Robert Bosch Smart Home GmbH",
    "Suzhou Mobydata Smart System Co.,Ltd.",
    "Day One Digital Media Limited",
    "WaveSplitter Technologies, Inc.",
    "Welgate Co., Ltd.",
    "iSmart Alarm, Inc.",
    "Honeywell",
    "APEXSHA SMARTTECH PRIVATE LIMITED",
    "Dawon Media Inc.",
    "SmartDrive Systems Inc.",
    "Honeywell SPS",
    "Junger Audio-Studiotechnik GmbH",
    "Smart electronic GmbH",
    "IOTTECH Corp",
    "Harman Multimedia",
    "VSE valencia smart energy",
    "Zhejiang Nurotron Biotechnology Co.",
    "Media Serve Co., Ltd.",
    "Liteon, Mobile Media Solution SBU",
    "CARLO GAVAZZI CONTROLS SPA-Controls Division",
    "Ademco Smart Homes Technology(Tianjin)Co.,Ltd.",
    "MediaSputnik",
    "Philips Consumer Communications",
    "N.V. PHILIPS INDUSTRIAL ACTIVITIES",
    "NeoMedia Europe AG",
    "Wyze Labs Inc",
    "CreNova Multimedia Co., Ltd",
    "IoT Security Group, SL",
    "TP Vision Belgium NV",
    "EGEMEN Bilgisayar Muh San ve Tic LTD STI",
    "PHILIPS BROADBAND NETWORKS",
    "Honest Technology Co., Ltd",
    "SmartOptics AS",
    "Samsung Electronics.,LTD",
    "Shenzhen Chilink IoT Technology Co., Ltd.",
    "DLG Automação Industrial Ltda",
    "Micropoint Biotechnologies,Inc.",
    "Sling Media, Inc.",
    "LG ELECTRONICS INC",
    "e-SMARTCOM  INC.",
    "Lyngbox Media AB",
    "Digital Media Cartridge Ltd.",
    "ACTIVA MULTIMEDIA",
    "SHENYANG TONGFANG MULTIMEDIA TECHNOLOGY COMPANY LIMITED",
    "NESTAR COMMUNICATIONS, INC",
    "LG INFORMATION & COMM.",
    "Malgn Technology Co., Ltd.",
    "Tilgin AB",
    "VTLinx Multimedia Systems, Inc.",
    "TransMedia Communications, Inc.",
    "Smartisan Digital Co., Ltd",
    "Ericsson-LG Enterprise",
    "Fasttel - Smart Doorphones",
    "Data Respons A/S",
    "Micromedia AG",
    "Espera-Werke GmbH",
    "Canesta Inc.",
    "F1MEDIA",
    "AMALGAMATED WIRELESS(AUS) LTD",
    "Smartcom - Bulgaria AD",
    "IoT Company Solucoes Tecnologicas Ltda",
    "Honeywell CMSS",
    "KDD Media Will Corporation",
    "Shenzhen elink smart Co., ltd",
    "Haiguang Smart Device Co.,Ltd.",
    "DIGITAL TELEMEDIA CO.,LTD.",
    "InnoMediaLogic, Inc.",
    "Complete Media Systems",
    "MediaQ",
    "OutSmart Power Systems, Inc.",
    "SmartRG, Inc.",
    "smart light technology",
    "ScioTeq bvba",
    "PHILIPS MULTIMEDIA NETWORK",
    "Jinan USR IOT Technology Co., Ltd.",
    "iota Computing, Inc.",
    "SHENZHEN DIYANG SMART TECHNOLOGY CO.,LTD.",
    "Arlo Technology",
    "Thomson Telecom Belgium",
    "3NOD MULTIMEDIA(SHENZHEN)CO.,LTD",
    "Point Multimedia Systems",
    "Philips Patient Monitoring",
    "AireSpider Networks",
    "Millennia Media inc.",
    "Honeywell Environmental & Combustion Controls (Tianjin) Co., Ltd.",
    "AME Optimedia Technology Co., Ltd.",
    "GLOBESPAN SEMICONDUCTOR, INC.",
    "Beijing Nari Smartchip Microelectronics Company Limited",
    "Real Digital Media",
    "Dream-Multimedia-Tv GmbH",
    "LG Electronics",
    "MEDIAEDGE Corporation",
    "Philips Lighting BV",
    "Philips Medical Systems - Cardiac and Monitoring Systems (CM",
    "MediaChorus, Inc.",
    "ALGORITHMICS LTD.",
    "ASMedia Technology Inc.",
    "NANJING IOT SENSOR TECHNOLOGY CO,LTD",
    "ALGORITHMS SOFTWARE PVT. LTD.",
    "Timespace Technology",
    "Qingdao Haier Multimedia Limited.",
    "Algorithmix GmbH",
    "MEDIASTAR CO., LTD.",
    "Bilkon Bilgisayar Kontrollu Cih. Im.Ltd.",
    "U-MEDIA Communications, Inc.",
    "CARLO GAVAZZI, INC.",
    "Jinan USR IOT Technology Limited",
    "XtremeSpectrum, Inc.",
    "LG ELECTRONICS",
    "Imedia Semiconductor Corp.",
    "e-Smart Systems Pvt. Ltd",
    "LG Innotek",
    "Guangdong UNIPOE IoT Technology Co.,Ltd.",
    "China Mobile IOT Company Limited",
    "Alert Metalguard ApS",
    "Honeywell Fire System (Shanghai) Co,. Ltd.",
    "Worldsmart Retech",
    "Tuya Smart Inc.",
    "APRO MEDIA CO., LTD",
    "Hangzhou BroadLink Technology Co., Ltd",
    "Honeywell Security (China) Co., Ltd.",
    "Hirschmann Multimedia B.V.",
    "RELIA TECHNOLGIES",
    "HITACHI-LG DATA STORAGE INC",
    "Universal Media Corporation /Slovakia/ s.r.o.",
    "Hyeco Smart Tech Co.,Ltd",
    "Ingespace",
    "SAMSUNG ELECTRONICS",
    "KUNIMI MEDIA DEVICE Co., Ltd.",
    "eflow Inc. / Smart Device Planning and Development Division",
    "SECURITE COMMUNICATIONS / HONEYWELL",
    "YAMATAKE-HONEYWELL CO., LTD.",
    "Briot International",
    "Smart Cube., Ltd",
    "InnoMedia, Inc.",
    "Hangzhou Hylin IoT Techonology Co.,Ltd.",
    "Smartlink Network Systems Limited",
    "SmartCap Technologies",
    "SMARTBRIDGES PTE. LTD.",
    "Smarteh d.o.o.",
    "SmartDoor Systems, LLC",
    "NetMedia, Inc.",
    "NESTAR SYSTEMS INCORPORATED",
    "Smartware",
    "MEDIATRIX TELECOM",
    "ADVANCED-VISION TECHNOLGIES CORP.",
    "Broadlink Pty Ltd",
    "Siemens NV (Belgium)",
    "INDRA ESPACIO S.A.",
    "Philips",
    "D&R Electronica Weesp BV",
    "Media System Planning Corp.",
    "IoT Tech Limited",
    "MEDIAFIRE CORPORATION",
    "SAMSUNG HEAVY INDUSTRIES CO., LTD.",
    "Smartchip Integrated Inc.",
    "ULTIMEDIA Co Ltd,",
    "Interval Media",
    "Smartmatic Corp",
    "AVerMedia Information Inc.",
    "SmartSynch, Inc",
    "PROVIDEO Multimedia Co. Ltd.",
    "TP Vision Belgium N.V. - innovation site Brugge",
    "TP-LINK CORPORATION PTE. LTD.",
    "Sony Imaging Products & Solutions Inc.",
    "Xiamen Cheerzing IOT Technology Co.,Ltd.",
    "PSS Belgium N.V.",
    "MoCA (Multimedia over Coax Alliance)",
    "Shenzhen Xinghai Iot Technology Co.,Ltd",
    "TableTop Media (dba Ziosk)",
    "Elgar Electronics Corp.",
    "Xiotech Corporation",
    "IKEA of Sweden AB",
    "HiteVision Digital Media Technology Co.,Ltd.",
    "Xiamen Milesight IoT Co., Ltd.",
    "AXCENT Media AG",
    "Taijin Media Co., Ltd.",
    "Applied Media Technologies Corporation",
    "SMART Storage Systems",
    "LS(LG) Industrial Systems co.,Ltd",
    "Honeywell International Inc",
    "Intellimedia Systems Ltd",
    "MOMENTUM IOT",
    "MOLDAT WIRELESS TECHNOLGIES",
    "Smart Innovation LLC",
    "ExtremeSpeed Inc.",
    "Algorab S.r.l.",
    "Lexar Media, Inc.",
    "Sony Video & Sound Products Inc.",
    "Espec Corp.",
    "Media Numerics Limited",
    "Beijing Xiaomi Mobile Software Co., Ltd",
    "Aurora Multimedia Corp.",
    "Honeywell Video Systems",
    "Samsung Thales",
    "WaveSpan Corporation",
    "SMARTO",
    "Smartisan Technology Co., Ltd.",
    "Xiaomi Communications Co Ltd",
    "GiBahn Media",
    "Iota, Inc.",
    "MediaTek Inc.",
    "TOLLGRADE COMMUNICATIONS, INC.",
    "Nestle Purina PetCare",
    "Cezzer Multimedia Technologies",
    "SmarTire Systems Inc.",
    "Espressif Inc.",
    "s.m.s smart microwave sensors GmbH",
    "Hisense Broadband Multimedia Technology Co.,Ltd.",
    "Hangzhou BroadLink Technology Co.,Ltd",
    "LookX Digital Media BV",
    "ESP",
    "Shenzhen Smart Intelligent Technology Co.Ltd",
    "ALLGON AB",
    "Coax Media",
    "Smart Empire Investments Limited",
    "BSMediasoft Co., Ltd.",
    "Hunantv.com Interactive Entertainment Media Co.,Ltd.",
    "tickIoT Inc.",
    "Honeywell Co., Ltd. (KOREA)",
    "Micronik Multimedia",
    "ELGIN S.A.",
    "Shanghai Smart System Technology Co., Ltd",
    "TEIMA Audiotex S.L.",
    "Samsung Electronics Co., Ltd. ARTIK",
    "SmartCow AI Technologies Taiwan Ltd.",
    "Eclipse (HQ Espana) S.L.",
    "SAMSUNG TECHWIN CO.,LTD",
    "Smart Code(shenzhen)Technology Co.,Ltd",
    "Smartlabs",
    "FAST MULTIMEDIA AG",
    "Beijing Xiaomi Electronics Co., Ltd.",
    "Dazzle Multimedia, Inc.",
    "Philips Electronics Nederland BV",
    "LGS Innovations, LLC",
    "JIWUMEDIA CO., LTD.",
    "IN ONE SMART TECHNOLOGY(H,K,)LIMITED",
    "Xi'an HISU Multimedia Technology Co.,Ltd.",
    "Kinestral Technologies, Inc.",
    "PharmaSmart LLC",
    "Smartvue Corporation",
    "Wuhan Qianyang Iotian Technology Co., Ltd",
    "Interactive Multimedia eXchange Inc.",
    "ALGOSYSTEM Co., Ltd.",
    "New Media Life",
    "TELGEN CORPORATION",
    "Withings",
    "Access Media SPA",
    "ELL-IoT Inc",
    "Multimedia & Communication Technology",
    "CardioTek B.V.",
    "Samsung Semiconductor Inc.",
    "SHENZHEN HONGDE SMART LINK TECHNOLOGY CO., LTD",
    "Hitachi-LG Data Storage Korea, Inc",
    "Shenzhen Honesty Electronics Co.,Ltd",
    "Synelec Telecom Multimedia",
    "Sony Computer Entertainment America",
    "Honeywell Environmental & Combustion Controls",
    "NIHON MEDIA TOOL INC.",
    "NEOSMART Corp.",
    "ATMedia GmbH",
    "SAMSUNG ELECTRO MECHANICS CO., LTD.",
    "Vivint Smart Home",
    "PENTA MEDIA CO., LTD.",
    "MaxMedia Technology Limited",
    "BEHRINGER Spezielle Studiotechnik GmbH",
    "XIAOMI Electronics,CO.,LTD",
    "NSSLGlobal Technologies AS",
    "MEDIA4, INC.",
    "LG Electornics",
    "Samsung Electronics Co.,Ltd",
    "V One Multimedia Pte Ltd",
    "Fitbit Inc.",
    "HONEYWELL-DATING",
    "SAMSUNG ELECTRO-MECHANICS(THAILAND)",
    "SatCom Media Corporation",
    "LG CNS",
    "WORLD MEDIA AND TECHNOLOGY Corp.",
    "Oasis Media Systems LLC",
]
```

---

## Notes

- The script uses a case-insensitive search to match keywords within organization names.
- The results are persisted in both JSON and pickle formats to support flexible loading options.

---

- [README](../README.md)
- Documentation
  - [Utils](./utils.MD)
  - [IEE_OUI](./IEE_OUI.MD)
  - [Is IoT Device](./isIot.MD)
  - [Validators](./validators.MD)
  - [Command Line Interface](./cli.MD)
