---
title: "HQ Materials (HQMT) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/hq-materials-hqmt"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/hq-materials-hqmt"
---

#  HQ Materials (HQMT)

[HQ Materials Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/hq-materials---sample-text-file)

Trade Service - HQ Materials - bHQMT

 Columns that are typically used for importing are in yellow

Column Name
Type
Importable
Default Available
Length & Scale
Required
Comments

MatlGroup
bGroup
Yes
Yes
0-255
Yes

Material
bMatl
Yes
No
20 characters
Yes

Category
varchar
Yes
No
10 characters
Yes

Description
bDesc
Yes
No
30 characters
No

StdUM
bUM
Yes
No
3 characters
Yes

Cost
bUnitCost
Yes
Yes
num(9,16)
Yes

CostECM
bECM
Yes
Yes
1 char
Yes

Price
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

PayDiscType
char
Yes
Yes
1 char
Yes

Notes
bNotes
Yes
No
255 characters
No
Up to 255 characters

PayDiscRate
bUnitCost
Yes
Yes
num(9,16)
Yes

PurchaseUM
bUM
Yes
Yes
1 char
Yes

SalesUM
bUM
Yes
Yes
1 char
Yes

MetricUM
bUM
Yes
No
1 char
No

WeightConv
bUnits
Yes
No
num(9,12)
No

Stocked
bYN
Yes
Yes
1 char
Yes

Taxable
bYN
Yes
Yes
1 char
Yes

MatlPhase
bPhase
Yes
No
20 characters
No

MatlJCCostType
bJCCType
Yes
No
0-255
No

HaulPhase
bPhase
Yes
No
20 characters
No

HaulJCCostType
bJCCType
Yes
No
0-255
No

HaulCode
bHaulCode
Yes
No
10 characters
No

Active
bYN
Yes
Yes
1 char
Yes

Type
char
Yes
Yes
1 char
Yes

PriceServiceId
varchar
Yes
No
30 characters
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
