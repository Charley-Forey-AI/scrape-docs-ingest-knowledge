---
title: "Add Work Order Site Equipment | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-site-equipment"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-site-equipment"
---

# Add Work Order Site Equipment

Use this service to add equipment information to an existing Work Order Site.
WSDL: AddWOSiteEquip.jws
Method: AddWOSite_Equip
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Work Order Site Equipment Web Service adds equipment information to an existing Work Order Site.

- The Work Order site must have an Active Status.

- The Equip_ID field does not tie to the Equipment Control module.

- Duplicate Equipment codes cannot exist on the same Work Order Site.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the
 Spectrum Excel Office Add-in templates for data entry points.
Excel
Element Name
Description
Req
Type
Max
Format
Validation

Authorization_ID
Authorization ID to access the server
YES
Text
20
Data Exchange Installation Screen

GUID
Unique reference number created by programming
Text
36
** See GUID definition

B
Company_Code
Company Code
YES
Text
3
Valid Company in Spectrum.

C
Site_ID
Site code
YES
Text
10
Must have an active status
Work Order Site File Maintenance

D
Equip_ID
Equipment code
YES
Text
8
No duplicates within WO Site

E
Equip_Description
Description
Text
30

F
Equip_Type
Equipment type
YES
Text
4
Equipment Type Maintenance

G
Year_Installed
Year installed
Numeric
4
Format = CCYY

H
Make
Make
Text
20
Validated if WO Installation option is selected.

I
Model
Model
Text
20
Validated if WO Installation option is selected.

J
Serial
Serial number
Text
15

K
Location
Location
Text
20

L
Status
Equipment status
YES
Text
1
A(ctive) or I(nactive) only
