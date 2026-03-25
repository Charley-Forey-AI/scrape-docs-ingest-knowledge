---
title: "Purchase Order Items (POIB) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/purchase-order-items-poib"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/purchase-order-items-poib"
---

#  Purchase Order Items (POIB)

[Purchase Order Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/purchase-order---sample-text-file)

Purchase Order Items - Table bPOIB

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
PO Company number.Must exist in HQCO.

Mth
bMonth
No
Yes
MM/YY
yes
Viewpoint import will set the month to be the same as the header.

BatchId
bBatchID
No
Yes
##########
yes
Viewpoint Import will create next BatchId.

BatchSeq
int
No
Yes
##########
yes
Viewpoint Import will always generate the next Batch Sequence.

POItem
smallint
Yes
Yes
###
yes
Unique number identifying the line for this invoice.

BatchTransType
char
No
Yes
1 Character
yes
Viewpoint Import Default will always set this value to "A" for additions.

LineType
tinyint
Yes
Yes
#
yes
Specify the line type: 1=Job, 2=Inventory, 3=Expense, 4=Equipment, 5=Work Order

PostToCo
bCompany
Yes
Yes
### - 0 to 999
No
Viewpoint Job Cost, EM, or Inventory company in which job/phase/cost type, equipment, or material/location information for this invoice item must be valid, and where expense posts.

JCCo

Used for processing within Vista™, but not used for imports.

Job
bJob
Yes
Yes
10 Characters
no
Viewpoint job to be charged for this invoice item

PhaseGroup
bGroup
Yes
Yes
###
no
Phase Group used to qualify the job/phase/cost type information.Pulled from bHQCO based on JC Co#.

Phase
bPhase
Yes
Yes
20 Characters
no
Viewpoint phase to for this invoice item.

JCCType
bJCCType
Yes
Yes
###
no
Viewpoint Job Cost cost type for this invoice item.

EMCo

Used for processing within Vista software, but not used for imports.

WO
bWO
Yes
Yes
##########.##
no
Viewpoint work order (as set up in EM Work Orders) to which this invoice item applies.Line type must be set to 5 for WO.

WOItem
bItem
Yes
Yes
#####
no
Viewpoint work order item to which this invoice item applies.

Equip
bEquip
Yes
Yes
10 Characters
no
Viewpoint equipment (from EM Equipment) for this
 invoice item.

EMGroup
bGroup
Yes
Yes
###
no
EM Group used to qualify the work order/equipment information.Pulled from bHQCO based on EM Co#.

CostCode
bCostCode
Yes
Yes
10 Characters
no
Viewpoint equipment cost code (as defined in EM Cost Codes) for this invoice item.

EMCType
bEMCType
Yes
Yes
###
no
Viewpoint equipment cost type (as defined in EM Cost Types) for this invoice item.

CompType
varchar
Yes
Yes
10 Characters
no
Viewpoint component type (from EM Component Types) for the equipment, if applicable.

Component
varchar
Yes
Yes
10 Characters
no
Viewpoint component for the equipment information.

INCo

Used for processing within Vista™, but not used for imports.

Loc
bLoc
Yes
Yes
##########.###
no
Inventory location for which this material was purchased. Location must be set up in Viewpoint IN Location Setup, and material must be assigned to this location in IN Materials.

MatlGroup
bGroup
Yes
Yes
###
no
Material Group used to qualify the material information.Pulled from bHQCO based on IN Co#.

Material
bMatl
Yes
Yes
20 Characters
no
Viewpoint material for this invoice item.

GLCo
bCompany
Yes
Yes
### - 0 to 999
yes
Viewpoint GL company for this invoice item.

GLAcct
bGLAcct
Yes
Yes
20 Characters
yes
Viewpoint GL account for this invoice item.

Description
bDesc
Yes
No
30 Characters
no
Description of this invoice item.

UM
bUM
Yes
Yes
3 Characters
no
valid unit of measure for this invoice item. LS (lump sum), Units, Unit Cost, and ECM are skipped.

Units
bUnits
Yes
No
##########.###
yes
Number of units for this invoice item.

UnitCost
bUnitCost
Yes
No
##########.#####
yes
Cost per unit for this invoice item.

ECM
bECM
Yes
Yes
1 Character
no
Qualifies the unit cost.  "E" =per each  "C" = per hundred  "M" = per thousand.

GrossAmt
bDollar
Yes
No
##########.##
yes
Total amount for this invoice item.

MiscAmt
bDollar
Yes
No
##########.##
yes
Freight or other miscellaneous charges. If you enter Y in the Inc field (MiscYN), the amount entered here will be included in this line’s total. However, this amount is not included when taxes, discounts, or retainage are calculated for this line.

MiscYN
bYN
Yes
Yes
1 Character
yes
Freight/Misc amount (MiscAmt) is to be included in the invoice line total.

TaxCode
bTaxCode
Yes
Yes
10 Characters
no
Viewpoint tax code (HQ Tax Codes) for this invoice item.

TaxType
tinyint
Yes
Yes
#
no
Viewpoint tax type for this item where 1 = Sales Tax, 2 = Use Tax, and 3=VAT

Notes
bNotes
Yes
No
Text
no
Note column

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
