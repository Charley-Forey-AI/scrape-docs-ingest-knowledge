---
title: "AR Change Request - Blank Bill Item Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/ar-change-request---blank-bill-item-update"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/ar-change-request---blank-bill-item-update"
---

# AR Change Request - Blank Bill Item Update

 Use this service to update Accounts Receivable Change Request information. This service will update one blank bill item at a time created on an existing change request.
WSDL: ARChngReqBlankBIUpdate.jws
Method: ARChngReqBlankBIUpdate
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing AR Change Request information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Receivable

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Accounts Receivable > Customers

- System Administration > Installation > Accounts Receivable > Contract

- System Administration > Installation > Accounts Receivable > Contract Schedule of Values

- System Administration > Installation > Accounts Receivable > Change Request

- System Administration > Installation > Accounts Receivable > Change Request Status

- System Administration > Installation > Accounts Receivable > Pricing Add-ons

- System Administration > Installation > Accounts Payable > Vendor

- System Administration > Installation > Accounts Payable > Subcontract

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

## Assumptions and Dependencies

- The AR Change Request Blank Bill Item Update Web service will update one blank bill item at a time created on an existing Change Requests.

- The Job, Customer, Contract and Change Request must exist in order to update the Blank Bill Item code.

- The Bill Item code details cannot be changed via the web service once the Bill Item has been updated.

- If the Sequence number is blank then it will update the earliest number.

- The Description fields default from the Billing Item define on the Contracts Schedule of Values.

- Unit Price Jobs

- Require the Billing Group and Billing Item defined.

- Requires the Quantity to be defined as the Unit Price is defaulted and the Revenue amount will be calculated.

- Fixed Price Jobs

- Require the Billing Item to be defined.

- Requires the Revenue to be defined.

- The Revenue Amount will be validated (via calculation) to see if it is valid for the Job and the information provided.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
Excel
Field Name
Description
Req
Type
Max
Format
Validation

B
Company_Code
Company Code
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Job_Number
Job
YES
Text
10
Unique combination of Job, Customer and Change Request Number. * See Assumption and Dependencies.
Job

D
Customer_Code
Customer
YES
Text
10
Unique combination of Job, Customer and Change Request Number. * See Assumption and Dependencies.
Customer

E
Change_Request_Number
Change Request #
YES
Text
8
Unique combination of Job, Customer and Change Request Number. * See Assumption and Dependencies.

F
Sequence
Line number
Numeric
3
if blank updates the earliest blank sequence number found.

G
CR_Billing_Group_Code
Billing Group
Text
2
Define the CR_Billing_Group_Code and CR_Billing_Item_Code for Unit Price jobs. * See Assumptions and Dependencies.
Contract Schedule of Value

H
CR_Billing_Item_Code
Billing Item
Text
11
For Fixed Price Jobs define the Billing Item and leave the CR_Billing_Group_Code blank. * See Assumptions and Dependencies.
Contract Schedule of Value

I
CR_Billing_Item_Description
Billing Item Description
Text
30
Defaults from Billing_Item_Code if left blank. Otherwise overwrite.

J
CR_Additional_Description
Additional Description
Text
40
Defaults from Billing_Item_Code if left blank. Otherwise overwrite.

K
CR_Quantity
Quantity
Numeric
11
Required for Unit Price Jobs only. Allows negative numbers and can be blank. Format = -7.2 * See Assumptions and Dependencies.
For Unit Price Contracts the calculated Revenue will be validated.

L
CR_Revenue
Billing Amount
Numeric
14
Calculated for Fixed Price Jobs and rounds to 2 decimal places. Allows Negative numbers. Format = -10.2 * See Assumptions and Dependencies.
The quantity will be calculated for Unit Price Contracts if the Revenue is defined and the Quantity is blank.
