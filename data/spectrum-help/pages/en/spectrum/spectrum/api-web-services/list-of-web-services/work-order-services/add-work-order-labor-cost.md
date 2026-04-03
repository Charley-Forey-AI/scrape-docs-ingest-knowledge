---
title: "Add Work Order Labor Cost | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-labor-cost"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-labor-cost"
---

# Add Work Order Labor Cost

Use this service to add labor costs to work orders.
WSDL: AddWOLaborCost.jws
Method: AddWOLaborCost
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Work Order Labor Cost information, the following file maintenance areas must be completed:

- System Administration > Installation > Work Order

- System Administration > Installation > Payroll

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phase

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Payroll > Employee Maintenance

- System Administration > Installation > Payroll > Union File Maintenance

- System Administration > Installation > Payroll > Wage Code File Maintenance

- System Administration > Installation > Payroll > Worker's Compensation Code Maintenance

- System Administration > Installation > Payroll > Tax Table Maintenance

- System Administration > Installation > Equipment Control > Equipment Maintenance

- System Administration > Installation > Service Contract > Service Contract

- System Administration > Installation > Work Order > Work Order

- System Administration > Installation > Work Order > G/L Department

- System Administration > Installation > Work Order > Site File Maintenance

- System Administration > Installation > Work Order > Site Equipment

- System Administration > Installation > Work Order > Site Equipment Component

- System Administration > Installation > Work Order > Tasks

- System Administration > Installation > Work Order > Technicians

- System Administration > Installation > Work Order > Manufacturer

## Assumptions and Dependencies

- The WO Labor Cost service adds Work Order Labor Cost transaction.

- If the Company_Code is blank then use the Authorization ID default value.

- The Web Service will not create new Phase or Site Equipment/Components automatically; therefore the codes defined in the web services must exist to add the transaction.

- To add multiple transactions to a Work Order the Company Code, Work Order and Technician must be defined for each record along with the new data.

- The defined Work Order will dictate what fields will be used based on the type of the Work Order (Site or Job).

- The Pay type used allows access to the various fields. Equipment pay types allow access to the Equipment fields for both Site and Job Work Orders.

- The EU (Equipment Usage) pay type makes the following fields unavailable for a Site Work Order:

- Bill_Rate

- Bill_Manufacturer

- Mfg_Code

- Mfg_Hours_Billed

- The Job_Number, Phase and Cost_Type combination must exist and not have a completed status for a Job Work Order.

- The Technician field validates to an existing Employee setup in the Payroll module or as a Work Order Technician in the Work Order module.

- The Payroll fields will follow standard Spectrum default logic based on type of Work Order. See standard Spectrum Help files for logic.

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
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
WO_Number
Work Order
YES
Text
10
Work Order Entry

D
Employee_Code
Technician
YES
Text
11
Active status only
Technician Maintenance or Employee Maintenance

E
Pay_Type
Pay Type
YES
Text
2
(R)egular; (O)vertime; (D)ouble time;(SR)-Special rate; (ER)-Equipment-Regular; (EO)-Equipment-Overtime; (ED)-Equipment-Double time and (EU)-Equipment usage.

F
Time_Card_Date
Work date
YES
Date
10
Enter as: MM/DD/CCYY (that is, 01/05/2010).
Within P/R processing date range

G
Time_In
Time in
Text
5
Military time. Format = HHMM or HH:MM Example = 1602 or 16:02

H
Time_Out
Time out
Text
5
Military time. Format = HHMM or HH:MM Example = 1602 or 16:02

I
Hours
Hours
Numeric
8
Calculated if Time_In and Time_Out is defined and required if are blank. Allows negatives. Format = -4.2

J
GL_Department
G/L department
Text
5
Defaults from Work Order Header.
Work Order G/L Department File Maintenance

K
Work_Task
Task
Text
15
Work Order Task

L
Task_Complete
Task completed?
Text
1
Y(es) or N(o). If blank then defaults to N.

M
WO_Site_Equipment
Work Order Site Equipment
Text
8
Required if Work Order Installation option is selected for Site WO.
Work Order Site Equipment

N
Component_Number
Work Order Site Equipment Component
Text
2
Required if Work Order Installation option is selected for Site WO.
Work Order Site Equipment Component

O
Contract_Number
Contract
Text
10
Service Contract File Maintenance

P
Bill_Customer
Bill customer for this entry?
Text
1
Y(es) or N(o). If blank then defaults to N.
For EU transactions on a Site WO defaults to Y and cannot be changed.

Q
Tax_Flag
Taxable on customer invoice? / Taxable?
Text
1
Y(es) or N(o). If blank then defaults to N. Ignore if Bill_Customer = N on Site WO.

R
Hours_Billed
Customer Billing hours hours / Bill hours
Numeric
8
Negative numbers allowed. Format = -4.2

S
Labor_Billing_Code
Bill code
Text
10
Labor Billing Code

T
Bill_Rate
Customer Billing rate
Numeric
9
Positive numbers only. Format = 4.3 Ignore if Pay_Type = EU on Site WO.

U
Bill_Manufacturer
Warranty: bill manufacturer for this labor?
Text
1
Y(es) or N(o). If blank then defaults to N. **See Assumption and Dependencies.

V
Mfg_Tax_Flag
Warranty: taxable on manufacturer invoice?
Text
1
Y(es) or N(o). If blank then defaults to N.

W
Mfg_Code
Warranty Manufacturer
Text
10
Required when Bill_Manufacturer is Y(es).
Work Order Manufacturer

X
Mfg_Hours_Billed
Warranty Billing hours
Numeric
8
Negative numbers allowed. Format = -4.2

Y
Mfg_Bill_Rate
Warranty Billing rate
Numeric
8
Positive numbers only. Format = 4.3

Z
Work_State
State / Province
Text
10
Required for a Job Work Order. **See Assumptions and Dependencies
Tax Table Maintenance

AA
Work_County
County
Text
10
**See Assumptions and Dependencies
Tax Table Maintenance

AB
Work_Locality
Local
Text
10
**See Assumptions and Dependencies
Tax Table Maintenance

AC
Worker_Comp_Code
Worker's comp
Text
6
**See Assumptions and Dependencies
Worker's Compensation Code Maintenance File

AD
Pay_Group_Code
Pay group
Text
6
**See Assumptions and Dependencies
Pay Groups

AE
Wage_Code
Wage Code
Text
10
**See Assumptions and Dependencies
Union / Wage code combination

AF
Union_Code
Union
Text
10
**See Assumptions and Dependencies
Union Code

AG
Pay_Rate_Code
Level
Text
1
1 - 9 only.

AH
Phase_Code
Phase
Text
20
Required for Job Work Order. Must exist on the Job.
Phase

AI
Cost_Type
Cost type
Text
3
Required for Job Work Order. Phase/Cost type combination must exist on the Job.
Cost Type

AJ
Equipment_Code
Co. Equipment / Equipment
Text
10
Required for Equipment Pay types. **See Assumptions and Dependencies
Equipment Maintenance

AK
Equipment_Rate_Type
Equipment rate type
Text
1
(H)ourly, (D)aily, (W)eekly, or (M)onthly **See Assumptions and Dependencies

AL
Equipment_Hours
Equipment hours
Numeric
8
Negative numbers allowed. Format = -4.2 **See Assumptions and Dependencies

AM
Equipment_Bill_Hours
Equipment Bill hours
Numeric
8
Negative numbers allowed. Format = -4.2 **See Assumptions and Dependencies

AN
Equipment_Bill_Rate
Equipment Bill rate
Numeric
8
Positive numbers only. Format = 4.3 **See Assumptions and Dependencies
