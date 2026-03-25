---
title: "SM Agreements (vSMAgreement) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/sm-agreements-vsmagreement"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/sm-agreements-vsmagreement"
---

# SM Agreements (vSMAgreement)

 SM Agreements - Table vSMAgreement
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

Agreement
char
Yes
No
15 Characters
Yes
Agreement Number (Alphanumeric)

AgreementType
char
Yes
No
15 Characters
Yes
Agreement Type. Must exist in SMAgreementType.

Revision
int
No
Yes
###
Yes
Only new Agreements can be imported so Viewpoint import will always set the revision number to 1.

RevisionType
tinyint
No
Yes
###
Yes
Viewpoint Import will always set this value to "0" for new.

Description
char
Yes
No
60 Characters
No
Description of the agreement.

CustGroup
tinyint
Yes
No
###
Yes
Viewpoint import will always set this to the Customer Group assigned in HQ Company Setup for the SMCo value in the Headquarters module

Customer
int
Yes
No
##########
Yes
Customer number. Must exist in the SMCustomer table.

CustomerPO
varchar
Yes
No
30 Characters
No
Customer purchase order number. A value here will be put on all PM Work Order Scopes created from the agreement, and will appear on the customer invoices.

EffectiveDate
bDate
Yes
No
MM/DD/YY
Yes
The date the Agreement becomes effective. The service dates for the PM Work Orders will be calculated from this date using the scheduling pattern specified on the Agreement Service.

ExpirationDate
bDate
Yes
No
MM/DD/YY
Yes
The date the Agreement ends. PM Work Orders will be scheduled using the scheduling pattern defined on the Agreement Service up to an din cluding this date.

AutoRenew
bYN
No
Yes
1 Character
Yes
The Auto Renew flag is currently not used and defaults to N.

RateTemplate
varchar
Yes
No
10 Characters
No
The Rate Template will be used to calculate the billable rate for any add-on T&M work orders that have a Pricing Method of T&M and are marked to Use Agreement Rates.

AgreementPrice
bDollar
Yes
No
##########.##
No
Phase Group used to qualify Phase code. Pulled from bHQCO based on JC Co#. Not editable.

ReportID
int
Yes
No
#####
No
The Report ID overrides that default Agreement Invoice report.

DateCreated
bDate
Yes
Yes
MM/DD/YY
No
Must be a valid date. Defaults to the current date.

RevenueRecognition
bYN
Yes
Yes
1 Character
Yes
Must be a Y or N. Defaults to N.

Notes
varchar
Yes
No
500 Characters
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
