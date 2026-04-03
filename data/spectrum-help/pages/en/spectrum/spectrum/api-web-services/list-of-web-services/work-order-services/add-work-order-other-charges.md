---
title: "Add Work Order Other Charges | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-other-charges"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-other-charges"
---

# Add Work Order Other Charges

Use this service to add Work Order Other Charges Cost transactions.
WSDL: AddWOOtherCharges.jws
Method: AddWOOtherCharges
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Work Order Other Charges information, the following file maintenance areas must be completed:

- System Administration > Installation > Work Order

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phase

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Service Contract > Service Contract

- System Administration > Installation > Work Order > Work Order

- System Administration > Installation > Work Order > Other Charges

- System Administration > Installation > Work Order > G/L Department

- System Administration > Installation > Work Order > Site File Maintenance

- System Administration > Installation > Work Order > Site Equipment

- System Administration > Installation > Work Order > Site Equipment Component

- System Administration > Installation > Work Order > Task

## Assumptions and Dependencies

- The WO Other Charges Cost service adds Work Order Other Charges Cost transaction.

- If the Company_Code is blank then use the Authorization ID default value.

- The Web Service will not create new phase or Site Equipment/Components automatically; therefore the codes defined in the web services must exist to add the transaction.

- To add multiple transactions to a Work Order the Company Code, Work Order and Other Charge Item must be defined for each record along with the new data.

- The defined Work Order will dictate what fields will be used based on the type of the Work Order (Site or Job).

- The Other_Cost_Item field

- The Taxable flag defaults from the Other Charge Item setup if left blank.

- The rate type controls what fields are allowed to be updated or allowed access to.

- The rate type 'Percent of Cost' uses the labor hours defined for the Work Order to do it's calculations. Therefore a 'locking' error will appear if someone is reviewing or is sitting in the screen that could prevent the creation of the current record.

- The rate type defined on the Other Charges Item controls if the Cost_Of_Sales_Amount and Sell_Price fields are defined or calculated. The web service allows these fields to be defined.

- The Work Order's defined Price Method (Flat Rate or TM) impacts what information is allowed based on the Other Item code.

- Impacts the default logic.

- Impacts what fields can be modified

- The Contract_Number will default from the Work Order Header if defined. However the standard Spectrum logic for the defined Equipment will control it if the field will be used.

- If Spectrum Tasks are used then their defined logic will be applied and included in the Cost_Of_Sales_Amount and Sell_Price fields.

- The Job_Number, Phase and Cost_Type combination must exist and not have a completed status for a Job Work Order.

- The Web Service follows standard Cost Center logic. See the standard Spectrum Help files for logic.

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
Field Information
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
If blank defaults from Authorization ID.
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
WO_Number
Work Order
YES
Text
10
Work Order Entry

D
Other_Cost_Item
Item Code/Other Charge Code
YES
Text
15
**See Assumptions and Dependencies.
Work Order Other Charges Maintenance

E
Description
Description
Text
35

F
GL_Department
G/L department
Text
5
Defaults from Work Order Header if defined.
Work Order G/L Department File Maintenance

G
Work_Task
Task
Text
15
Work Order Task

H
Task_Complete
Task completed?
Text
1
Y(es) or N(o). If blank then defaults to N.

I
WO_Site_Equipment
Work Order Site Equipment
Text
10
Required if Work Order Installation option is selected for Site WO.
Work Order Site Equipment

J
Component_Number
Work Order Site Equipment Component
Text
2
Required if Work Order Installation option is selected for Site WO.
Work Order Site Equipment Component

K
Contract_Number
Contract
Text
10
Defaults from Work Order Header if defined. **See Assumptions and Dependencies.
Service Contract File Maintenance

L
Taxable_Flag
Taxable on customer invoice? / Taxable?
Text
1
Y(es) or N(o). Defaults based on the Other_Cost_Item setup.

M
Cost_Of_Sales_Amount
Cost Amount/Sell Price
Numeric
13
Negative numbers allowed. Format = -9.2 **See Assumptions and Dependencies.

N
Sell_Price
Invoice extension/ Sell price
Numeric
13
Negative numbers allowed. Format = -9.2 **See Assumptions and Dependencies.

O
Phase_Code
Phase
Text
20
Required for Job Work Order. Must exist on the Job.
Phase

P
Cost_Type
Cost type
Text
3
Required for Job Work Order. Phase/Cost type combination must exist on the Job.
Cost Type
