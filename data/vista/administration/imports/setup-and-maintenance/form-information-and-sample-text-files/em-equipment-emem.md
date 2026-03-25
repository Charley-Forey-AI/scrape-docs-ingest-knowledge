---
title: "EM Equipment (EMEM) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/em-equipment-emem"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/em-equipment-emem"
---

#  EM Equipment (EMEM)

[EM
 Equipment Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/em-equipment---sample-text-file)

Table 1. EM Equipment - EMEMColumn NameTypeImportableDefault AvailableLength & ScaleRequiredComments
EMCo
bCompany
Yes
Y
1-255
Yes

Equipment
bEquip
Yes
N
10
Yes

Location
varchar
Yes
N
10
No

Type
char
Yes
Y
1
Yes

Department
bDept
Yes
N
10
Yes

Category
bCat
Yes
N
10
Yes

Manufacturer
varchar
Yes
N
20
No

Model
varchar
Yes
N
20
No

ModelYr
char
Yes
N
6
No

VINNumber
varchar
Yes
N
40
No

Description
bDesc
Yes
N
30
No

Status
char
Yes
Y
1
Yes

OdoReading
bHrs
Yes
Y
numeric
Yes

OdoDate
bDate
Yes
N

No

ReplacedOdoReading
bHrs
Yes
Y
numeric
Yes

ReplacedOdoDate
bDate
Yes
N

No

HourReading
bHrs
Yes
Y
numeric
Yes

HourDate
bDate
Yes
N

No

ReplacedHourReading
bHrs
Yes
Y
numeric
Yes

ReplacedHourDate
bDate
Yes
N

No

MatlGroup
bGroup
Yes
Y
1-255
No

FuelMatlCode
bMatl
Yes
N
20
No

FuelCapacity
bHrs
Yes
Y
numeric
Yes

FuelCapUM
bUM
Yes
N
3
No

FuelUsed
bUnits
Yes
Y
numeric
Yes

EMGroup
bGroup
Yes
Y
1-255
No

FuelCostCode
varchar
Yes
N
10
No

FuelCostType
tinyint
Yes
N
1-255
No

LastFuelDate
bDate
Yes
N

No

AttachToEquip
bEquip
Yes
N
10
No

AttachPostRevenue
bYN
Yes
Y
1
No

JCCo
bCompany
Yes
Y
1-255
No

Job
bJob
Yes
N
10
No

PhaseGrp
bGroup
Yes
Y
1-255
No

UsageCostType
bJCCType
Yes
N
1-255
No

WeightUM
bUM
Yes
N
1
No

WeightCapacity
bHrs
Yes
Y
numeric
Yes

VolumeUM
bUM
Yes
N
1
No

VolumeCapacity
bHrs
Yes
Y
numeric
Yes

Capitalized
bYN
Yes
Y
1
No

LicensePlateNo
varchar
Yes
N
10
No

LicensePlateState
bState
Yes
N
2
No

LicensePlateExpDate
bDate
Yes
N

No

IRPFleet
varchar
Yes
N
10
No

CompOfEquip
bEquip
Yes
N
10
No

ComponentTypeCode
varchar
Yes
N
10
No

CompUpdateHrs
bYN
Yes
Y
1
No

CompUpdateMiles
bYN
Yes
Y
1
No

CompUpdateFuel
bYN
Yes
Y
1
No

PostCostToComp
bYN
Yes
Y
1
No

PRCo
bCompany
Yes
Y
1-255
No

Operator
bEmployee
Yes
N
integer
No

Shop
varchar
Yes
N
20
No

GrossVehicleWeight
bHrs
Yes
Y
numeric
Yes

TareWeight
bUnits
Yes
Y
numeric
Yes

Height
varchar
Yes
N
20
No

Wheelbase
varchar
Yes
N
20
No

NoAxles
tinyint
Yes
Y
1-255
Yes

Width
varchar
Yes
N
20
No

OverallLength
varchar
Yes
N
20
No

HorsePower
varchar
Yes
N
20
No

TireSize
varchar
Yes
N
20
No

OwnershipStatus
varchar
Yes
Y
20
No

InServiceDate
bDate
Yes
N

No

ExpLife
tinyint
Yes
Y
1-255
Yes

ReplCost
bDollar
Yes
Y
numeric
Yes

CurrentAppraisal
bDollar
Yes
Y
numeric
Yes

SoldDate
bDate
Yes
N

No

SalePrice
bDollar
Yes
Y
numeric
Yes

PurchasedFrom
varchar
Yes
N
30
No

PurchasePrice
bDollar
Yes
Y
numeric
Yes

PurchDate
bDate
Yes
N

No

APCo
bCompany
Yes
N
1-255
No

VendorGroup
bGroup
Yes
N
1-255
No

LeasedFrom
bVendor
Yes
N
integer
No

LeaseStartDate
bDate
Yes
N

No

LeaseEndDate
bDate
Yes
N

No

LeasePayment
bDollar
Yes
Y
numeric
Yes

LeaseResidualValue
bDollar
Yes
Y
numeric
Yes

ARCo
bCompany
Yes
N
1-255
No

CustGroup
bGroup
Yes
N
1-255
No

Customer
bCustomer
Yes
N
integer
No

CustEquipNo
varchar
Yes
N
20
No

MSTruckType
varchar
Yes
N
10
No

RevenueCode
bRevCode
Yes
N
10
No

Notes
bNotes
Yes
N
text
No

MechanicNotes
bNotes
Yes
N
text
No

JobDate
bDate
Yes
N

No

FuelType
char
Yes
Y
1
Yes

UpdateYN
bYN
Yes
Y
1
Yes

ShopGroup
bGroup
Yes
Y
1-255
Yes

IFTAState
bState
Yes
N
2
No

UniqueAttchID
uniqueidentifier
No
N

No

LastUsedDate
bDate
Yes
N

No

Table Guidelines
The definition of each of the table’s columns is outlined below.

- Column Name – The name of the column/field in the database table.

- Type – The column’s SQL data type. Types starting with a “b” are Viewpoint defined data types.

- Importable – The field is available for import.

- Default Available – Indicated if a programmatic default value is available for this field. Defaults use the same logic as a posting program to determine a value.

- Length and Scale – Indicates the format of the field.

- Required – Indicates if the data is required.
A hard coded default value can be specified in IM Template; when importing files this value overwrites the imported value.
Note:Use the Template Detail tab in the IM Template form to add any additional fields for importing.
