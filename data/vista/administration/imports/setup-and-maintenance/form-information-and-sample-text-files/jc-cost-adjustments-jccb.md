---
title: "JC Cost Adjustments (JCCB) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-cost-adjustments-jccb"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-cost-adjustments-jccb"
---

#  JC Cost Adjustments (JCCB)

Job Cost Entry - Table bJCCB

Columns that are typically used for importing are in yellow

Column Name
Type
Importable
Default Available
Length & Scale
Required
Comments

JCCo
bCompany
Yes
No
### - 0 to 999
Yes
Job Cost Company number.Must exist in HQCO.

Mth
bMonth
No
No
MM/YY
Yes

BatchTransType
char
No
Yes
1 Character
Yes
Bidtek Import will always set this value to "A" for additions.

PostDate
bDate
Yes
No
MM/DD/YYYY
Yes
Date entries are made.

Job
bJob
Yes
No
10 Characters
Yes
Job to be expensed with Cost, Units, or Hours.

PhaseGroup
bGroup
No
Yes
###
Yes
Phase Group used to qualify Phase code.Pulled from bHQCO based on JC Co#.Not editable.

Phase
bPhase
Yes
No
20 Characters
Yes
Phase to be expensed with Cost, Units, or Hours.

CostType
bJCCType
Yes
No
###
Yes
Cost Type to be expensed with Cost, Units, or Hours.

GLCo
bCompany
Yes
Yes
###
Yes
GL Company to be expensed with Cost.

Description
bDesc
Yes
No
60 Characters
No

TransAcct
bGLAcct
Yes
Yes
20 Characters
Yes
GL Account to be expensed with Cost

OffsetAcct
bGLAcct
Yes
No
20 Characters
No
GL Offset Account to be used with Cost.

UM
bUM
Yes
Yes
3 Characters
No
Unit of Measure.

Hours
bHrs
Yes
No
########.##
No
Hours worked.

Units
bUnits
Yes
No
###########.###
No
Units worked in terms of Unit of Measure.

Dollars
bDollar
Yes
No
##########.##
No
Cost Amount

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
