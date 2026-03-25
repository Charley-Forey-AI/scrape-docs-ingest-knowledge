---
title: "SM Required Tasks (vSMRequiredTasks) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/sm-required-tasks-vsmrequiredtasks"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/sm-required-tasks-vsmrequiredtasks"
---

# SM Required Tasks (vSMRequiredTasks)

 SM Required Tasks - Table vSMAgreementService
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

Task
int
Yes
Yes
###
Yes
Task number. Sequential number for tasks added to parent.

SMStandardTask
char
Yes
No
15 Characters
No
SM Standard Task. Must exist in SMStandardTask table. Required Material, Equipment and Labor that is related to SMStandardTask record will also be added.

Name
char
Yes
Yes
60 characters
Yes
Name of Task.

Description
char
Yes
No
Unlimited characters
No
Description of the Task.

ServiceSite
char
No
Yes
20 characters
No
Viewpoint import will always set this to the Service Site of the associated parent.

ServiceItem
char
Yes
No
20 characters
No
Service Item

Class
char
Yes
No
15 Characters
No
Defaults to the Class of the Service Item when provided.

Type
char
Yes
No
15 characters
No
Defaults to the Type of the Service Item when provided.

Manufacturer
char
Yes
No
20 characters
No
Defaults to the Manufacturer of the Service Item when provided.

Model
char
Yes
Yes
60 Characters
No
Defaults to the Model of the Service Item when provided.

SerialNumber
char
Yes
No
60 Characters
No
Defaults to the Serial Number of the Service Item when provided.

Agreement
char
Yes
No
15 characters
when ParentType = 9
The Agreement that the task is associated with.

AgreementRevision
int
Yes
No
###
when ParentType = 9
The Revision that the task is associated with.

AgreementService
int
Yes
Yes
###
when ParentType = 9
The Agreement Service that the task is associated with.

WorkOrder
int
Yes
No
#########
when ParentType = 7
The Work Order that the task is associated with.

WorkOrderScope
int
Yes
No
###
when ParentType = 7
The Work Order Scope that the task is associated with.

WorkOrderQuote
varchar
Yes
No
15 Characters
when ParentType = 11
The Work Order Quote that the task is associated with.

WorkOrderQuoteScope
int
No
No
###
when ParentType = 11
The Work Order Quote Scope that the task is associated with.

ItemClass
varchar
No
No
15 Characters
when ParentType = 14
The Item Class that the task is associated with.

ClassMaintenance
varchar
Yes
No
30 Characters
when ParentType = 14
The Item Class Maintenance that the task is associated with.

SourceTask
int
Yes
No
###
No
If this task is associated with an Agreement Service that comes from a Class Maintenance then this should have the Task number as it is on the related Class Maintenance Task record.

Recommended
char
Yes
Yes
Y or N
when ParentType = 14
Defaults to 'Y'. Only used for records with a parent of Class Maintenance.

ParentType
int
Yes
No
###
Yes
Indicates what parent type this record is associated with: 7=Work Order Scope, 9=Agreement Service, 11=Work Order Quote Scope, 14=Class Maintenance

Notes
varchar
Yes
No
Unlimited
No
Notes

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
