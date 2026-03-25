---
title: "SM Required Material (vSMRequiredMaterial) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/sm-required-material-vsmrequiredmaterial"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/sm-required-material-vsmrequiredmaterial"
---

# SM Required Material (vSMRequiredMaterial)

SM Required Material - Table vSMAgreementService
Columns that are typically used for importing are in yellow

Column Name
Type
Importable
Default Available
Length & Scale
Required
Comments

SMCo
company
Yes
No
### - 0 to 999
Yes
Service Management Company number. Must exist in HQCO.

EntitySeq
int
No
No
#########
No
EnitiySeq automatically set by Viewpoint upload process.

Seq
int
Yes
Yes
###
Yes
Material sequence. Sequential number for material added to parent.

Service
int
No
No
###
No

Task
char
Yes
No
Unlimted Characters
No
Description of the Task.

ServiceSite
char
No
Yes
20 Characters
No
Viewpoint import will always set this to the Service Site of the associated parent.

ServiceItem
char
Yes
No
20 Characters
No
Service Item

SMPartType
char
Yes
No
15 Characters

PartType or Material is required, but both are not allowed.

MatlGroup
bGroup
No
Yes
#

Material
char
Yes
No
20 Characters

PartType or Material is required, but both are not allowed.

MatlQty
decimal
Yes
No
#########.###
When Material has a value.

UM
bUM
Yes
Yes
3 Characters
When Material has a value.
Defaults to StdUM from HQMaterials

CostECM
char
Yes
Yes
1 Character
When Material has a value.
E for Each, C for 100, M for 1000. Defaults to CostECM from HQMaterials

CostRate
decimal
Yes
Yes
###########.#####
When Material has a value.
Defaults to Cost from HQMaterials

CostTotal
decimal
Yes
Yes
##########.##
When Material has a value.
Set to MatlQty * CostRate adjusted for ECM.

Notes
char
Yes
No
Unlimited
No

ParentType
int
Yes
No
#
Yes
7=Work Order, 9=Agreement Service, 11=Work Order Quote Scope, 12=SM Standard Task, 14=Class Maintenance

Agreement
char
Yes
No
15 Characters
When ParentType=9

AgreementRevision
int
Yes
No
###
When ParentType=9

AgreementService
int
Yes
No
###
When ParentType=9

WorkOrder
int
Yes
No
############
When ParentType=7

WorkOrderScope
int
Yes
No
###
When ParentType=7

WorkOrderQuote
char
Yes
No
15 Characters
When ParentType=11

WorkOrderQuoteScope
int
Yes
No
###
When ParentType=11

SMStandardTask
char
Yes
No
15 Characters
When ParentType=12

ItemClass
char
Yes
No
15 Characters
When ParentType=14

ClassMaintenance
char
Yes
No
30 Chatacrters
When ParentType=14

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
