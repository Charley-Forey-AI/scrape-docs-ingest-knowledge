---
title: "IN Materials (INMT) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/in-materials-inmt"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/in-materials-inmt"
---

#  IN Materials (INMT)

[IN Materials Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/in-materials---sample-text-file)

Trade Service - IN Materials - bINMT

 Columns that are typically used for importing are in yellow

Column Name
Type
Importable
Default Available
Length & Scale
Required
Comments

INCo
tinyint
Yes
Yes
0-255
Yes

Loc
bLoc
Yes
No
10 char
Yes

Material
bMatl
Yes
No
20 char
Yes

AuditYN
bYN
Yes
No
1 char
Yes

LastCost
bUnitCost
Yes
Yes
num(9,16)
Yes

LastECM
bECM
Yes
Yes
1 char
Yes

LastVendor
bVendor
Yes
No
± 2,147,483,648
No

LowStock
bUnits
Yes
Yes
num(9,12)
Yes

ReOrder
bUnits
Yes
Yes
num(9,12)
Yes

WeightConv
bUnits
Yes
Yes
num(9,12)
Yes

PhyLoc
varchar
Yes
No
30 char
No

LastCntDate
bDate
Yes
No
Date
No

CostPhase
bPhase
Yes
No
20 char
No

Active
bYN
Yes
Yes
1 char
Yes

AutoProd
bYN
Yes
Yes
1 char
Yes

GLUnits
bYN
Yes
Yes
1 char
Yes

AvgCost
bUnitCost
Yes
Yes
num(9,16)
Yes

AvgECM
bECM
Yes
Yes
1 char
Yes

StdCost
bUnitCost
Yes
Yes
num(9,16)
Yes

StdECM
bECM
Yes
Yes
1 char
Yes

StdPrice
bUnitCost
Yes
Yes
num(9,16)
Yes

PriceECM
bECM
Yes
Yes
1 char
Yes

CustRate
bRate
Yes
Yes
num(5,8)
Yes

JobRate
bRate
Yes
Yes
num(5,8)
Yes

InvRate
bRate
Yes
Yes
num(5,8)
Yes

EquipRate
bRate
Yes
Yes
num(5,8)
Yes

OnHand
bUnits
Yes
Yes
num(9,12)
Yes

Notes
bNotes
Yes
No
up to 255 char
No

Alloc
bUnits
Yes
Yes
num(9,12)
Yes

OnOrder
bUnits
Yes
Yes
num(9,12)
Yes

RecvdNInvcd
bUnits
Yes
Yes
num(9,12)
Yes

Booked
bUnits
Yes
Yes
num(9,12)
Yes

LastCostUpdate
bDate
Yes
No
Date
No

MatlGroup
bGroup
Yes
Yes
0-255
Yes

VendorGroup
bGroup
Yes
No
0-255
No

PhaseGroup
bGroup
Yes
No
0-255
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
