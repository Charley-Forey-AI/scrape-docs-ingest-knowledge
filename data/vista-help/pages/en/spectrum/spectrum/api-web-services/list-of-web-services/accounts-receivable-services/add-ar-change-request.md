---
title: "Add AR Change Request | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-ar-change-request"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-ar-change-request"
---

# Add AR Change Request

Use this service to import Accounts Receivable Change Request information.
WSDL: ARChangeRequest.jws
Method: ARChangeRequest
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing AR Change Request information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Receivable

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Accounts Receivable > Customers

- System Administration > Installation > Accounts Receivable > Contract

- System Administration > Installation > Accounts Receivable > Contract Schedule of Values

- System Administration > Installation > Accounts Receivable > Change Request Status

- System Administration > Installation > Accounts Receivable > Pricing Add-ons

- System Administration > Installation > Accounts Payable > Vendor

- System Administration > Installation > Accounts Payable > Subcontract

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

## Assumptions and Dependencies

- The AR Change Request Web service adds or updates existing Change Requests information for the defined fields only.

- The Web Service will not create new phase or Billing Items automatically, therefore the Phase/Cost type and Billing Item codes defined in this web services will be required to add or change data.

- The Web Service follows the majority of the same logic as manually entering a Change Request with the exceptions of the data defined here. The Spectrum Help files can be used for troubleshooting errors along with the details defined here.

- The unique combination of the Company Code, Job, Customer and Change Request # must exist in the defined Company code to change the data provided. If not then it will create a new Change Request.

- If the Change_Request_Number is left blank then the number will be auto created.

- To add multiple detail lines to a Change Request the Company Code, Job, Customer and Change Request # must be defined for each record along with the following fields to define the Header information:

- Description

- Status

- Cost_Reimbursable_Flag

- Origination_Date

- Approved_Date

- Fee_Percent

- Fee_Amount

- To change data within the Change Request then it must have all the Header information AND The exact information for the given 'section' (that is, costs, markups, pricing add-ons and billings) that is defined

- If multiple duplicate cost or revenue lines exist, then the web service will update the first record.

- Cost Tab must have:

- CR_Phase_Code

- CR_Cost_Type

- Subcontractor_Code

- Subcontractor_Number

- Sub_Bid_Group_Item_Code

- Sub_Bid_Item_Code

- Revenue Tab must have:

- CR_Billing_Group_Code

- CR_Billing_Item_Code

- The Status of the Change Request controls the following

- The Cost Reimbursable option

- Access to the Cost tab information

- Access to override the Markups and Add-ons tabs

- If Billing information is needed or not. Status codes with Action type of 3, 4 or 5 on a Fixed Price Job can be blank.

- The Approved_Date can only be defined if the status is Approved or Executed.

- The Fee Percent defaults from the Pricing Defaults for Contract Changes if not defined in the record. If defined in the record then it can be overwritten.

- If the Fee_Percent and Fee_Amount are both populated, then the Fee_Percent will be used and the Fee_Amount will be calculated.

- The CR_Phase_Code and CR_Cost_Type combination must exist and not have a completed status.

- The CR_ Phase_Code and CR_ Cost_Type are required if the Subcontractor detail provided in the record are valid.

- Any data defined for a Subcontract will appear on the Subcontract Change Order Log.

- A Billing Item can exists within the Change Request as part of a Subcontract Costs and/or as part of the Billing section. The type of Job or Subcontract defines how the billing item will be defined in the layout.

- Unit Price contract's require both the billing group and billing items to be defined with a max number of 10 characters between the two fields. This applies to the Subcontract and Contract fields.

- Fixed Price contracts require only the billing item field be populated in the layout with a max number of 10 characters. The 'Group' fields will be ignored if defined.

- If the Subcontractor_Code and Subcontract_Number are blank then any data defined for the Subcontract information fields will be ignored.

- The CR_Billing_Group_Code and CR_Billing_Item_Code must exist for the Contract in order to be added or changed.

- The CR_Billing_Group_Code and CR_Billing_Item_Code are blank then the other fields associated with the Billing tab will be ignored.

- For unit price jobs the following will apply to the CR_Unit_Price, CR_Quantity and CR_Revenue.

- Two of the above fields must be populated.

- If any two fields are populated, then they will be used to calculate the other value.

- CR_Unit_Price will default from the Contract if left blank in the web service and it exists on the contract.

- If CR_Revenue is defined then it will be ignored if both the CR_Unit_Price and CR_Quantity are defined.

- All fields will be ignored if the CR_Billing_Group_Code and CR_Billing_Item_Code are blank.

- The Unit of Measure in the Billing Tab will default from the Schedule of Values for the defined Billing Item.

- The number of Billing entries per Change Request cannot exceed 990 records.

- Markups and Add-ons tabs on the Change Request are populated from the Contracts Pricing Default page.

- The Change Request status dictates if the amounts can be modified.

- User cannot add new Markups or Add-ons codes via a Change Request.

- Markup values are added when the associated Cost entry is made to the Change Request or the Markup must already exist on the Change Request.

- The Pricing Add-on information

- The contract controls the Pricing Add-ons that are allowed to be added to the Change Request.

- A phase and cost type is required for each Pricing Add-on to be used on Change Requests.

- The Phase and Cost type are defined on the Contract or within the Change Request.

- The Pricing Defaults on the Contract are AUTOMATICALLY added to the Change Request AND need to have the Phase/Cost type defined on the contract in order to prevent errors when being added to the Change Order.

- If the Quotation_Submitted_Date is blank, it will default from the Origination_Date if the Change Request is for Costs only and not billed.

- This Web Service will work with the defined Workflow process in Spectrum.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- Default Billing Total, when selected, will insert a 'Billing Total' line with the same amount as the total cost.

- Change Request must be flagged as Cost Reimbursement

- Change Request Status Action Type of 4 required.

- Single billing line only, no billing item can be defined.

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
Text
8
Unique combination of Job, Customer and Change Request Number. If left blank then a new number will be auto-created. * See Assumption and Dependencies.

F
CR_Description
Description
Text
250

G
CR_Status
Current Status
Text
2
Required if creating a new Change Request. The 'action type' of the status code controls the fields that can be added or updated.
Change Request Status

H
Cost_Reimbursable_Flag
Cost Reimbursable
Text
1
(Y)es or (N)o only. The Status dictates whether or not the Cost Reimbursable option can be selected.

I
Origination_Date
Origination date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010) If blank then defaults to AR Current processing date. ** See Assumptions and Dependencies.

J
Approved_Date
Approved date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010). Must be within current AP processing dates.

K
Fee_Percent
Fee %
Numeric
7
Allows negative numbers. Format = -3.2 * See Assumptions and Dependencies.

L
Fee_Amount
Fee Amount
Numeric
12
Allows negative numbers. Format = -8.2 * See Assumptions and Dependencies.

M
CR_Phase_Code
Phase
Text
20
No dashes. Must exist on the Job. Required if the valid Subcontractor details are defined in this record. * See Assumptions and Dependencies.
Phases

N
CR_Cost_Type
Cost type
Text
3
Must exist on the Job. Required if Phase_Code is defined. * See Assumptions and Dependencies.
Cost Type

O
Change_Request_Quantity
Cost Quantity
Numeric
11
Allows negative numbers and can be blank. Format = -7.2

P
Change_Request_Hours
Cost hours
YES
Numeric
10
Allows negative numbers and can be blank. Format = -6.2

Q
Change_Request_Amount
Cost Est Amount
YES
Numeric
14
Allows negative numbers and can be blank. Format = -10.2

R
Subcontractor_Code
Subcontractor (Vendor code)
YES
Text
10
Must be a valid combination of Subcontractor_Code and Subcontract_Number.
Vendor

S
Subcontract_Number
Subcontract #
Text
10
Must be a valid combination of Subcontractor_Code and Subcontract_Number.
Subcontract

T
Sub_Amount
Sub CO Amount
Numeric
14
If blank then defaults from Subcontract. Format = -10.2

U
Sub_Bid_Group_Item_Code
Sub group (billing item)
Text
2
Define the Sub_Bid_Group_Item_Code and Sub_Bid_Item_Code for Unit Price jobs. * See Assumptions and Dependencies.
Subcontract Phase Details

V
Sub_Bid_Item_Code
Sub item (billing item)
Text
11
For Fixed Price Jobs define the Sub item (billing item) and leave the Sub_Bid_Group_Item_Code blank. * See Assumptions and Dependencies.
Subcontract Phase Details

W
Sub_Status
Sub Status
Text
1
(P)roposed, (E )xeuted or (R )ejected only. Required if Subcontractor_Code defined.

X
Sub_Change_Order_Number
Sub CO#
Text
8
Must exist for the Job. Required if status is Executed.
Subcontract Change Order

Y
Sub_Change_Order_Date
Sub CO date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010) If left blank then defaults to the Origination_Date.
Must be within the A/R processing date range.

Z
Sub_Signed_Date
Sub signed date
Date
10
Update when Sub_Status = Executed only. Enter as: MM/DD/CCYY (for example, 01/05/2010)

AA
Sub_Description
Sub CR Description
Text
30

AB
Sub_Type
Sub CR Type
Text
15

AC
Sub_Proposal_Date
Sub proposal date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)

AD
Sub_Sent_Date
Sub sent date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)

AE
Sub_Due_Date
Sub due date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)

AF
Sub_Comments
Sub Comments
Text
250

AG
Markup_Cost_Type
Markup Cost type
Text
3
*See Assumptions and Dependencies.
Cost Type

AH
Markup_Percent
Markup %
Numeric
6
If defined then Markup_Amount must be blank. Positive numbers only. Format = 3.2 * See Assumptions and Dependencies.

AI
Markup_Amount
Markup Amount
Numeric
14
If defined then Markup_Percent must be blank. Allows negative numbers. Format = -10.2 * See Assumptions and Dependencies.

AJ
Pricing_Addon_Code
Pricing Addon
Text
10
* See Assumptions and Dependencies.
Pricing Add-ons

AK
Pricing_Addon_MU_Percent
Pricing Addon Percent
Numeric
6
* See Assumptions and Dependencies.

AL
Pricing_Addon_MU_Amount
Pricing Addon Amount
Numeric
14
For Fixed Price Addon only. Allows negative numbers. Format = -10.2

AM
Pricing_Addon_Phase
Pricing Addon Phase
Text
20
No dashes. Must exist on the Job. Required if the status action type = 3. * See Assumptions and Dependencies.
Phases

AN
Pricing_Addon_Cost_Type
Pricing Addon Cost Type
Text
3
Must exist on the Job. Required if Phase_Code is defined. * See Assumptions and Dependencies.
Cost Type

AO
CR_Billing_Group_Code
Billing Group
Text
2
Define the CR_Billing_Group_Code and CR_Billing_Item_Code for Unit Price jobs. * See Assumptions and Dependencies.
Contract Schedule of Value

AP
CR_Billing_Item_Code
Billing Item
Text
11
For Fixed Price Jobs define the Billing Item and leave the CR_Billing_Group_Code blank. *See Assumptions and Dependencies.
Contract Schedule of Value

AQ
CR_Billing_Item_Description
Billing Item Description
Text
30
Defaults from Billing_Item_Code if left blank. Otherwise overwrite.

AR
CR_Additional_Description
Additional Description
Text
40
Defaults from Billing_Item_Code if left blank. Otherwise overwrite.

AS
CR_Unit_Price
Unit Price
Numeric
11
Required for Unit Price Jobs only. Allows negative numbers and can be blank. Format = -5.4 * See Assumptions and Dependencies.

AT
CR_Quantity
Quantity
Numeric
11
Required for Unit Price Jobs only. Allows negative numbers and can be blank. Format = -7.2 * See Assumptions and Dependencies.

AU
CR_Revenue
Billing Amount
Numeric
14
Calculated for Unit Price Jobs and rounds to 2 decimal places. Allows Negative numbers. Format = -10.2 * See Assumptions and Dependencies.

AV
Proceed_Submitted_Date
Notice to Proceed Submitted date
Date
10

AW
Proceed_Received_Date
Notice to Proceed Received date
Date
10

AX
Rough_Estimate
Notice to Proceed Rough Estimate
Numeric
12
Allows negative numbers and can be blank. Format = -8.2

AY
Quotation_Submitted_Date
Quotation Submitted date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010). ** See Assumptions and Dependencies.

AZ
Quotation_Due_Date
Quotation Due date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010).

BA
Requested_Days
Quotation Requested days
Numeric
4
Whole numbers only. Allows negative numbers and can be blank. Format = -3

BB
Approved_Days
Approval Approved Days
Numeric
4
Whole numbers only. Allows negative numbers and can be blank. Format = -3

BC
Default_Billing_Total
Default Billing Total
Text
1
(Y)es or (N)o only
