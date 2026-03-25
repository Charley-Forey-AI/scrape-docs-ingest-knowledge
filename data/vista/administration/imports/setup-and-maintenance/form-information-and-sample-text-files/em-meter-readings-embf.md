---
title: "EM Meter Readings (EMBF) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/em-meter-readings-embf"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/em-meter-readings-embf"
---

#  EM Meter Readings (EMBF)

[EM Meter Readings Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/em-meter-readings---sample-text-file)

EM Meter Readings - EMBF

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
YES
YES

YES

Mth
bMth
YES
YES

YES

BatchId
bBatchID
YES
NO

YES

BatchSeq
integer
YES
NO

YES

BatchTransType
char
YES
NO
1
YES

EMTrans
bTrans
YES
NO

YES

ActualDate
bDate
YES
YES

YES

Equipment
bEquip
YES
NO

YES

Description
bDesc
YES
YES
30
YES

PreviousHourMeter
bHrs
YES
YES
10.2
YES

CurrentHourMeter
bHrs
YES
YES
10.2
YES

MeterHrs
bHrs
YES
YES
10.2
YES

PreviousOdometer
bHrs
YES
YES
10.2
YES

CurrentOdometer
bHrs
YES
YES
10.2
YES

MeterMiles
bHrs
YES
YES
10.2
YES

MeterReadDate
bDate
YES
YES

YES

PreviousTotalHourMeter
bHrs
YES
YES
10.2
YES

CurrentTotalHourMeter
bHrs
YES
YES
10.2
YES

PreviousTotalOdometer
bHrs
YES
YES
10.2
YES

CurrentTotalOdometer
bHrs
YES
YES
10.2
YES

Source
bSource
YES
YES

YES

EMTransType
varchar
YES
YES
10
YES

GLCo
bCompany
YES
YES

YES

INStkUnitCost
bUnitCost
YES
YES

YES

UnitPrice
bUnitCost
YES
YES

YES

AutoUsage
bYN
YES
YES

YES

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
