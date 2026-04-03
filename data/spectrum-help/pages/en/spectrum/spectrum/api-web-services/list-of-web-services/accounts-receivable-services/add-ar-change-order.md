---
title: "Add AR Change Order | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-ar-change-order"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-ar-change-order"
---

# Add AR Change Order

Use this service to import Accounts Receivable Change Order information.
WSDL: ARChangeOrder.jws
Method: ARChangeOrder
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing AR Change Order information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Receivable

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Accounts Receivable > Customers

- System Administration > Installation > Accounts Receivable > Contract

- System Administration > Installation > Accounts Receivable > Contract Schedule of Values

- System Administration > Installation > Accounts Receivable > Change Order Status

- System Administration > Installation > Accounts Receivable > Change Request

- System Administration > Installation > Job Cost > Jobs

## Assumptions and Dependencies

- The AR Change Order Web service adds or updates existing Change Orders information for the defined fields only.

- The Web Service will not create new phase or Billing Items automatically.

- The Web Service follows the majority of the same logic as manually entering a Change Order with the exceptions of the data defined here. The Spectrum Help files can be used for troubleshooting errors along with the details defined here.

- The unique combination of the Company Code, Job, Customer and Change Order # must exist in the defined Company code to change the data provided and NOT be tied to a draw request or change request. If not then it will create a new Change Order.

- To add multiple detail lines to a Change Order the Company Code, Job, Customer and Change Order # must be defined for each record along with the following fields to define the Header information:

- Description

- Status_Code

- Change_Order_Date

- Approved_Date

- Approved_Days

- Fee_Percent

- Fee_Amount

- The Fee_Percent and Fee_Amount fields

- They defaults from the Change Request but can be overwritten.

- If the Fee_Percent and Fee_Amount are both populated, then the Fee_Percent will be used and the Fee_Amount will be calculated.

- If the Fee_Amount field is defined and a Change Request is being added in the same record with a Fee associated, the defined Fee_Amount value in this record will be used. It will not be added to the Change Request associated Fee.

- Adding Change Requests to a Change Order.

- The Change Request Number is defined then its associated records will appear within the defined tabs on the Change Order when reviewing from within Spectrum.

- The billing item cannot be blank within the change request and must be modified on the change request.

- The Phase and Cost Type for the Pricing Add-on must be defined on the Change Request.

- The Web service will not create billing items automatically.

- The Change Request cannot be added if Change Order is tied to a draw request.

- To change billing dollars the following fields must be defined along with the correct dollar fields based on the Job type:

- Job_Number

- Customer_Code

- Change_Order_Number

- CO_Billing_Group_Code

- CO_Billing_Item_Code

- The type of the Job defines how the billing item will be defined in the layout

- Unit Price contract's require both the billing group and billing item to be defined with a max number of 10 characters between the two fields.

- Fixed Price contracts require only the billing item field be populated in the layout with a max number of 10 characters. The 'Group' fields will be ignored if defined.

- The Billing_Item_Code must exist for the Contract in order to be added or changed.

- The fields defined on the Billing Tab are used to add charges to the Change Order itself.

- The Unit of Measure in the Billing Tab will default from the Schedule of Values for the defined Billing Item.

- This Web Service will ignore the defined Workflow process in Spectrum.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
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
Valid Company in Spectrum

C
Job_Number
Job
YES
Text
10
Unique combination of Job, Customer and Change Order Number. * See Assumption and Dependencies.
Job

D
Customer_Code
Customer
YES
Text
10
Unique combination of Job, Customer and Change Order Number. * See Assumption and Dependencies.
Customer

E
Change_Order_Number
Change Order #
Text
8
Unique combination of Job, Customer and Change Order Number. * See Assumption and Dependencies.

F
Description
Description
Text
250

G
Status_Code
Current Status
Text
2
Required if creating a new Change Order.
Change Order Status Codes

H
Change_Order_Date
Origination Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010) If blank then defaults to AR Current processing date.
Must be within the A/R processing date range.

I
Approved_Date
Approved Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)
Must be within the A/R processing date range.

J
Approved_Days
Approved Days
Numeric
4
Whole numbers only. Positive numbers only and can be blank. Format = 4

K
Fee_Percent
Fee %
Numeric
6
Positive numbers only. Format = 3.2 * See Assumptions and Dependencies.

L
Fee_Amount
Fee Amount
Numeric
14
Allows negative numbers. Format = -8.2 * See Assumptions and Dependencies.

M
Change_Request_Number
Change Request Number
Text
8
Must exist for Job/Customer combination. Cannot be tied to existing Change Order#. Must have all details defined. * See Assumptions and Dependencies.
Change Request

N
CO_Billing_Group_Code
Billing Group
Numeric
2
Define the CO_Billing_Group_Code and CO_Billing_Item_Code for Unit Price jobs. * See Assumptions and Dependencies.
Contract Schedule of Value

O
CO_Billing_Item_Code
Billing Item
Numeric
10
For Fixed Price Jobs define the Billing Item and leave the CO_Billing_Group_Code blank. * See Assumptions and Dependencies.
Contract Schedule of Value

P
Additional_Description
Additional Description
Text
40
Defaults from Billing_Item_Code if left blank

Q
Unit_Price
Unit Price
Numeric
11
Required for Unit Price Jobs only. Allows negative numbers and can be blank. Format = -5.4 *See Assumptions and Dependencies.

R
Quantity
Quantity
Numeric
11
Required for Unit Price Jobs only. Allows negative numbers and can be blank. Format = -7.2 * See Assumptions and Dependencies.

S
Revenue
Amount
Numeric
14
Calculated for Unit Price Jobs and rounds to 2 decimal places. Allows Negative numbers. Format = -10.2 * See Assumptions and Dependencies.
