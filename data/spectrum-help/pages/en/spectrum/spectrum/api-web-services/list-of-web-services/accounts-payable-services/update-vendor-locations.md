---
title: "Update Vendor Locations | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/update-vendor-locations"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/update-vendor-locations"
---

# Update Vendor Locations

Use this service to create a new Vendor Location code or update an existing Vendor Location code.
WSDL: UpdateVendor_Locations.jws
Method: UpdateVendor_Locations
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Vendor-Locations information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Payable

- System Administration > Installation > Accounts Payable > Vendor

- System Administration > Installation > Accounts Payable > Vendor Locations

## Assumptions and Dependencies

- The Vendor code must exist in the defined Company code.

- The Vendor-Location web service will either create a new Location code or update an existing Location code.

- To add a new Location_Code, leave this field blank and it will use the next available numeric sequence number.

- To change information, define the unique Vendor_Code and Location_Code fields in the layout. This will update all the detail information provided.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout

- If the Status is blank and a new Location is being created it will default to be Active.

- The Default_Payment_Loc field selection can only exist with one Location code. If defined it the layout it will change the Vendor default logic to use that code.

- The Default_Purchase_Loc field selections can only exist with one Location code. If defined it the layout it will change the Vendor default logic to use that code.

- If the Location_Status is Inactive then the Default_Payment_Loc and Default_Purchase_Loc fields default to N and are not available on the screen.

- Records cannot be updated when user is locking the entry screen.

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
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Vendor_Code
Vendor Code
YES
Text
10
Vendor Code must exist for the defined Company Code.

D
Location_Code
Location code
Text
4
Unique combination of Vendor code and Location code. If blank auto populate with next available number. If exists then modify data otherwise add new location.
Vendor Location

E
Location_Name
Location name
Text
30
Required if creating a new Location code.

F
Loc_Telephone
Location telephone
Numeric
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
Remove the dashes from format when sending to Spectrum.

G
Loc_Fax
Location fax
Numeric
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
Remove the dashes from format when sending to Spectrum.

H
Loc_Addr_1
Location Address 1
Text
30

I
Loc_Addr_2
Location Address 2
Text
30

J
Loc_Addr_City
Location city
Text
25

K
Loc_Addr_State
Location state/province
Text
2
2 character postal abbreviation

L
Loc_Addr_Zip
Location postal code
Text
10

M
Loc_Addr_Country
Location country
Text
25

N
Location_Remarks
Location remarks
Text
250

O
Default_Payment_Loc
Default payment location?
Text
1
(Y)es or(N)o only. Defaults to N if left blank. Ignore if Status is Inactive.
Exists for only one Location code and will overwrite current setting if defined.

P
Default_Purchase_Loc
Default 'purchase from' location?
Text
1
(Y)es or(N)o only. Defaults to N if left blank. Ignore if Status is Inactive.
Exists for only one Location code and will overwrite current setting if defined.

Q
Location_Status
Location status
Text
1
'A'ctive or 'I'nactive. Defaults to A if left blank.
