---
title: "JC Progress Entry (JCPP) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-progress-entry-jcpp"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-progress-entry-jcpp"
---

#  JC Progress Entry (JCPP)

[JC Progress Entry Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-progress-entry---sample-text-file)

JC Progress Entry - JCPP

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
Yes
N
### - 0 to 999
Yes
 Job Cost Company number.Must exist in HQCO.

Mth
bMonth
No
N
MM/YY
Yes

BatchId
bBatchIDt
No
N
##########
Yes
 Viewpoint Import will create next BatchId.

BatchSeq
int
No
N
##########
Yes
 Viewpoint Import will always generate the next Batch Sequence.

ActualDate
bDate
Yes
N
MM/DD/YYYY
Yes
 Date Progress entries are made.

Job
bJob
Yes
N
10
Yes
 Job to be expensed with Cost, Units, or Hours.

PhaseGroup
bGroup
No
Y
###
Yes
 Phase Group used to qualify Phase code.Pulled from bHQCO based on JC Co#.Not editable.

Phase
bPhase
Yes
N
20
Yes
 Phase to be expensed with Cost, Units, or Hours.

CostType
bJCCType
Yes
N
###
Yes
 Cost Type to be expensed with Cost, Units, or Hours.

UM
bUM
Yes
Y
3
No
 Unit of Measure.

ActualUnits
bUnits
Yes
Y
###########.###
No
 Number of newly completed units on this phase/cost type. The system will automatically calculate the Total Completed and Total Percent. If you prefer, you can enter Total Complete or Total Percent and let the system calculate the newly completed units.

ProgressCmplt
bRate
Yes
Y

No
 Total Percent Complete entered as a rate where .50 is 50% complete.

PRCo
bCompany
Yes
Y
### - 0 to 999
No
 Payroll Company for Crew postings.

Crew
bCrew
Yes
N
10
No
 Crew for progress posting.

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
