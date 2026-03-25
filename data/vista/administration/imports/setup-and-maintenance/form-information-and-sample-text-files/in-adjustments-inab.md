---
title: "IN Adjustments (INAB) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/in-adjustments-inab"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/in-adjustments-inab"
---

#  IN Adjustments (INAB)

[IN Adjustments Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/in-adjustments-sample-text-file)

IN Adjustments - INAB

 Columns that are typically used for importing are in yellow

Column Name
Type
Importable
Default Available
Length & Scale
Required
Comments

Co
bCompany
Y
Y

No

GLAcct
bGLAcct
Y
Y

Yes

Mth
bMonth
Y
N

Yes

BatchId
bBatchID
N
N

Yes

BatchSeq
int
N
N

Yes

BatchTransType
char
Y
Y

Yes

INTrans
int
Y
N

No

ActDate
bDate
Y
Y

Yes

Loc
bLoc
Y
N

Yes

Material
bMatl
Y
N

Yes

UM
bUM
Y
Y

Yes

Units
bUnits
Y
Y

Yes

UnitCost
bUnitCost
Y
Y

Yes

ECM
bECM
Y
Y

Yes

TotalCost
bDollar
Y
N

Yes

Description
bDesc
Y
N

No

MatlGroup
bGroup
Y
Y

Yes

GLCo
bCompany
Y
Y

Yes

BatchType
varchar
Y
Y

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
