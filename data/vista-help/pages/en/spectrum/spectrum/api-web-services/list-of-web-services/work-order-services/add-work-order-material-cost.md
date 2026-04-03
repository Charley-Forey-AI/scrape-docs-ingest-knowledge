---
title: "Add Work Order Material Cost | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-material-cost"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-material-cost"
---

# Add Work Order Material Cost

Use this service to add material costs to work orders.
WSDL: AddWOMaterialCost.jws
Method: AddWOMaterialCost
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Work Order Material Cost information, the following file maintenance areas must be completed:

- System Administration > Installation > Work Order

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phase

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Inventory Control > Inventory Items Maintenance

- System Administration > Installation > Inventory Control > Warehouse

- System Administration > Installation > Service Contract > Service Contract

- System Administration > Installation > Work Order > Work Order

- System Administration > Installation > Work Order > G/L Department

- System Administration > Installation > Work Order > Site File Maintenance

- System Administration > Installation > Work Order > Site Equipment

- System Administration > Installation > Work Order > Site Equipment Component

- System Administration > Installation > Work Order > Task

- System Administration > Installation > Work Order > Manufacturer

## Assumptions and Dependencies

- The WO Material Cost service adds Work Order Material Cost transaction.

- If the Company_Code is blank then use the Authorization ID default value.

- The Web Service will not create new Item, Phase or Site Equipment/Components automatically; therefore the codes defined in the web services must exist to add the transaction.

- To add multiple transactions to a Work Order the Company Code, Work Order and Item Code must be defined for each record along with the new data.

- The defined Work Order will dictate what fields will be used based on the type of the Work Order (Site or Job).

- Warranty Manufacturer fields

- The Component field must be defined in order to allow access to the Warranty information for a Site Work Order.

- If the Bill_Manufacturer field is N then ignore all other Warranty Manufacturer data defined.

- If Spectrum Tasks are used then their defined logic will be applied.

- A non-stock item can be created using the standard Spectrum logic; type an
 exclamation point (!) before entering an item code. See the standard Spectrum Help files
 for assistance.

- The Job_Number, Phase and Cost_Type combination must exist and not have a completed status for a Job Work Order.

- If the Extension field is defined, then the Unit_Price value will be recalculated and ignores any value defined for the Unit_Price field.

- The SC_Contract field will default if defined on the Work Order. If no Service Contract is defined on the Site Work Order then a valid Contract defined on the Site will be allowed.

- The Web Service follows standard Cost Center logic. See the standard Spectrum Help files for logic.

- This Web Service will ignore the defined Workflow process in Spectrum.

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
Valid Company in Spectrum

C
WO_Number
Work Order
YES
Text
10
Work Order Entry

D
Item_Code
Item Code
YES
Text
15
**See Assumptions and Dependencies for Non-Stock Items
Item Maintenance

E
Item_Description
Item Description
Text
35
Used for non-stock items. Defaults from Item_Code if valid. Can overwrite on Job Work Order.

F
Warehouse_Code
Warehouse
Text
10
Ignore if non-stock item.
Warehouse File Maintenance

G
Quantity_Used
Quantity
Numeric
11
Negative numbers allowed. Format = -7.2

H
Unit_Of_Measure
Unit of Measure
Text
2
Defaults from Item_Code if valid. **See Assumptions and Dependencies.

I
GL_Department
G/L department
Text
5
Defaults from Work Order Header.
Work Order G/L Department File Maintenance

J
Work_Task
Task
Text
15
Work Order Task

K
Task_Complete
Task completed?
Text
1
Y(es) or N(o). If blank then defaults to N.

L
WO_Site_Equipment
Work Order Site Equipment
Text
8
Required if Work Order Installation option is selected for Site WO.
Work Order Site Equipment

M
Component_Number
Work Order Site Equipment Component
Text
2
Required if Work Order Installation option is selected for Site WO. **See Assumptions and Dependencies.
Work Order Site Equipment Component

N
SC_Contract
Contract
Text
10
If defined on the Work Order then only allows the defined SC_Contract. Otherwise is valid if defined on the Site.
Service Contract File Maintenance

O
Bill_Customer
Bill customer for this material?
Text
1
Y(es) or N(o). Defined Work_Task impacts this option. If Y then Extension field is created.

P
Tax_Flag
Taxable on customer invoice? / Taxable?
Text
1
Y(es) or N(o). If blank then defaults to N. Ignore if Bill_Customer = N on Site WO.

Q
Show_Invoice_Detail
Show this item on A/R invoice in detail?
Text
1
Y(es) or N(o). If blank then defaults to N. Ignore if Bill_Customer = N on Site WO.

R
Unit_Cost
Standard Cost/Unit Cost
Numeric
12
Negative numbers allowed. Format = -8.2 Used for non-stock items only. **See Assumptions and Dependencies.

S
Unit_Price
Unit Price/Price
Numeric
13
Negative numbers allowed. Format = -9.2 Field defaults for Site type WO within Spectrum with the best price but can be overwritten.

T
Extension
Invoice extension
Numeric
13
Negative numbers allowed. Format = -9.2 If defined then Unit_Price will be recalculated. If left blank then will be calculated.

U
Bill_Manufacturer
Warranty: bill manufacturer for this material?
Text
1
Y(es) or N(o). If blank then defaults to N. **See Assumption and Dependencies.

V
Mfg_Tax_Flag
Warranty: taxable on manufacturer invoice?
Text
1
Y(es) or N(o). If blank then defaults to N. **See Assumption and Dependencies.

W
Mfg_Code
Warranty Manufacturer
Text
10
**See Assumption and Dependencies.
Work Order Manufacturer

X
Mfg_Unit_Price
Warranty Billing rate
Numeric
13
Negative numbers allowed. Format = -9.2 **See Assumption and Dependencies.

Y
Phase_Code
Phase
Text
20
Required for Job Work Order. Must exist on the Job.
Phase

Z
Cost_Type
Cost type
Text
3
Required for Job Work Order. Phase/Cost type combination must exist on the Job.
Cost Type
