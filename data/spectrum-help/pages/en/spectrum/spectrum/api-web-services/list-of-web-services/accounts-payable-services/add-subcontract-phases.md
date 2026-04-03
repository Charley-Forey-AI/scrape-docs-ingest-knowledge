---
title: "Add Subcontract Phases | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/add-subcontract-phases"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/add-subcontract-phases"
---

# Add Subcontract Phases

 Use this service to add or update existing Subcontract Phase information for the defined fields only.
WSDL: UpdateSubcontractPhases.jws
Method: UpdateSubcontractPhases
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Subcontract-Phases information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Payable

- System Administration > Installation > Accounts Payable > Subcontract

- System Administration > Installation > Accounts Payable > Vendor File
 Maintenance

- System Administration > Installation > Job Cost > Installation

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > General Ledger > G/L Master File Maintenance

## Assumptions and Dependencies

- The Subcontract-Phase Web Service adds or updates existing Subcontract information for the defined fields only.

- The unique combination of the following must exist in order to change the data otherwise create a new subcontract phase. The standard Spectrum logic will automatically default any missing information when looking for an existing Subcontract Phase detail.

- Company_Code

- Vendor_code

- Subcontract_number

- Phase_Code

- Cost_type

- Bid_Item_Number

- Duplicates cannot exist in the Phase Detail of the Subcontract record for the required fields.

- The same Phase/Cost Type can exist on the Subcontract as long as the Billing Items are unique.

- The standard GL Account logic will be used for validation for the Job and Cost type defaults.

- If the Phase_Code and Cost_Type are blank then it will default from the Subcontract if they are defined otherwise these fields will be required.

- If the Phase_Code and Cost_Type are defined and the following fields are blank then they will default from the Phase_Code:

- Bid_Item_Number

- Bill_Description

- Unit_Of_Measure

- Rentention_Flag

- Unit_Price

- The Bid_Item_Number field will use the first two characters as the Billing Group if the Job is a unit price Job.

- For Unit Price Subcontracts, if a phase price type is set to Job default or Unit Price then only the UM (unit of measure) of LS (lump sum) can change the record to a Fixed Price amount. All other Job Phase price types act as a fixed price.

- The Unit of Measure's price method controls the fields (dollars and quantity) that can be populated. If it is defined as Fixed Price then only the Orginal_Contract_Amount field will be updated and all other fields will be ignored.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

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
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Vendor_Code
Vendor Code
YES
Text
10
Vendor

D
Subcontract_Number
Subcontract Number
YES
Text
10
No duplicate combination of Vendor and Subcontract number.

E
Phase_Code
Phase
Text
20
No dashes. Must exist on the Job and required if not defined on Subcontract. ** See Assumptions and Dependencies.
Phases

F
Cost_Type
Cost type
Text
3
Must exist on the Job and required if not defined on Subcontract. ** See Assumptions and Dependencies.
Cost Type

G
Bid_Item_Number
Billing ItemÂ
Text
10
The billing item is broken into Group and Item for Unit Price jobs. The first 2 characters will be defined as the Group when the Job is Unit Price. ** See Assumptions and Dependencies.

H
Bill_Description
Description
Text
25
** See Assumptions and Dependencies.

I
Unit_Of_Measure
Unit of Measure
Text
3
** See Assumptions and Dependencies.

J
Retention_Flag
Retainage?
Text
1
(Y)es or (N)o. Defaults to N if blank or based on Phase. ** See Assumptions and Dependencies.

K
Unit_Price
Unit Price
Numeric
12
Allows negatives. Format = -6.4 ** See Assumptions and Dependencies.

L
Original_Contract_Quantity
Original Quantity
Numeric
12
Allows negatives. Format = -8.2

M
Original_Contract_Amount
Original Amount
Numeric
13
If Unit_Price and Original_Contract_Quantity are populated then Original_Contract_Amount is calculated. Allows negatives. Format = -9.2 ** See Assumptions and Dependencies.
