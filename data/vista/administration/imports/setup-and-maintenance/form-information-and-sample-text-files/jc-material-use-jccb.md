---
title: "JC Material Use (JCCB) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-material-use-jccb"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-material-use-jccb"
---

#  JC Material Use (JCCB)

Job Material Use - Table JCCB

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
Yes
### - 0 to 999
yes
Job Cost Company number. Must exist in HQCO.

Mth
bMonth
No
No
MM/YY
yes

BatchId
bBatchID
No
No
##########
yes
Viewpoint Import will create next BatchId.

BatchSeq
int
No
No
##########
yes
Viewpoint Import will always generate the next Batch Sequence.

Source
bSource
No
Yes
10 Characters
yes
Viewpoint Import will always set this value to "JCMatUse".

TransType
char
Yes
Yes
1 Character
yes
Viewpoint Import will always set this value to "A" for additions.

CostTrans
bTrans
No
No
#######
no
Not Needed.

Job
bJob
Yes
No
10 Characters
no
Specify the job (JC Jobs) to which the material cost
 will be posted.

PhaseGroup
bGroup
Yes
Yes
1 Character
yes
Phase Group used to qualify Phase code.Pulled from bHQCO based on JC Co#.Not editable.

Phase
bPhase
Yes
Yes
###
yes
Specify the phase (from JC Phases) to which the
 material cost will be posted. If using locked phases feature, must be a
 valid job phase (JC Job Phases).

CostType
bJCCType
Yes
Yes
###
yes
Specify the cost type to which the material cost
 will be posted. Must be a valid cost type specified for the phase (JC
 Phases) or job phase (JC Job Phases).

ActualDate
bDate
Yes
Yes
MM/DD/YY
yes
Specify the date that will become the Actual Date in Job Cost for this transaction.

JCTransType
varchar
Yes
Yes
2 Characters
yes
The JC type identifies whether you are posting for stocked or miscellaneous materials. "IN" — This type is used when you are posting costs for materials sold from your own inventory (those materials set up in IN Location Materials). When selected, additional fields are available that allow you to specify the IN company and location from which the materials were sold. Units posted in this program will update the on-hand quantity and records in Inventory. Although a non-standard unit of measure can be used during entry, Inventory will be updated in the standard unit of measure using the conversion factor specified for the non-standard unit of measure. "MI" — This type is used when posting costs for miscellaneous materials. Miscellaneous materials include those set up in HQ Materials or, if materials are not being validated (Validate Material option in JC Company Parameters checked), any material can be used.

Description
bTransDesc
Yes
Yes
60 Characters
no

GLCo
bCompany
Yes
Yes
###
yes
Phase to be expensed with these earnings.Null if not posted to a Job.Can be null even if Job is entered, if "Allow No Phase" option in bPRCO is flagged.Earnings will not be expensed to the JC unless Job and Phase are both entered.

GLTransAcct
bGLAcct
Yes
Yes
20 Characters
yes
GL account to charge with this cost adjustment.

GLOffsetAcct
bGLAcct
Yes
Yes
20 Characters
yes
Offset Account for Cost entry

PstUM
bUM
Yes
Yes
3 Characters
yes
Equipment revenue code.Optional, only available if posting equipment usage with a job costed timecard.

PstUnits
bUnits
Yes
No
#########.###
yes

PstUnitCost
bUnitCost
Yes
Yes
###########.#####
yes
Unit Cost being charged the job.

PstECM
bECM
Yes
Yes
1 Characters
yes
Indicate what quantity the unit price represents. "E" = Per Each, "C" = Per Hundred, "M" = Per Thousand.

Cost
bDollar
Yes
Yes
##########.##
yes
Total Cost being charged the job.

MatlGroup
bGroup
Yes
Yes
###
yes
Material Group used to qualify the Material code.Pulled from bHQCO based on IN Co # or JC Co#.Not editable.

Material
bMatl
Yes
No
20 Characters
yes
Material Code for this transaction.

INCo
bCompany
Yes
Yes
###
no
Inventory company from which the specified material was sold.

Loc
bLoc
Yes
No
10 Characters
no
Location for this transaction.

TaxType
tinyint
Yes
Yes
#
no
Set to 2 for Use Tax.

TaxGroup
bGroup
Yes
Yes
###
no
Tax Group used to qualify the Tax code. Pulled from bHQCO based on JC Co#. Not editable.

TaxCode
bTaxCode
Yes
Yes
10 Characters
no
Tax code for calculating use tax.

TaxBasis
bDollar
Yes
Yes
#########.##
no
Tax Basis.

TaxAmt
bDollar
Yes
Yes
##########.##
no
Tax Amount.

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
