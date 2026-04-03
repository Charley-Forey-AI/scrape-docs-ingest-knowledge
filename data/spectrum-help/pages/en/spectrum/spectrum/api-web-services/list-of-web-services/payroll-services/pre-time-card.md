---
title: "Pre-Time Card | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/pre-time-card"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/pre-time-card"
---

# Pre-Time Card

Use this service to import Pre-Time Card Transaction information.
WSDL: PreTimeCard.jws
Method: PreTimeCard
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Pre-Time Card Transaction information, the following file maintenance screens must be completed:

- System Administration > Installation > Payroll

- System Administration > Installation > Payroll > Tax Table Maintenance

- System Administration > Installation > Payroll > Deduction/Add-on Code Maintenance

- System Administration > Installation > Payroll > Department Expense Maintenance

- System Administration > Installation > Payroll > Worker's Comp Base Code

- System Administration > Installation > Payroll > Worker's Compensation Code Maintenance

- System Administration > Installation > Payroll > Union File Maintenance

- System Administration > Installation > Payroll > Non-Union Pay Group Maintenance

- System Administration > Installation > Payroll > Wage Code File Maintenance

- System Administration > Installation > Payroll > Crew Maintenance

- System Administration > Installation > Payroll > Employee Status Code Maintenance

- System Administration > Installation > Payroll > Employees Maintenance

- System Administration > Installation > General Ledger

- System Administration > Installation > General Ledger > G/L Department File Maintenance

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Human Resources

- System Administration > Installation > Human Resources > Triggers Maintenance

- System Administration > Installation > Job Cost

- System Administration > Installation > Job Cost > Jobs Maintenance

- System Administration > Installation > Job Cost > Cost Type Maintenance

- System Administration > Installation > Job Cost > Phases Maintenance

- System Administration > Installation > Equipment Control

- System Administration > Installation > Equipment Control > Equipment Status File Maintenance

- System Administration > Installation > Equipment Control > Equipment Maintenance

- System Administration > Installation > Equipment Control > Equipment Components File Maintenance

- System Administration > Installation > Equipment Control > Cost Category Maintenance

- System Administration > Installation > Equipment Control > Job Specific Equipment Charge Rates

- System Administration > Installation > Preventive Maintenance

- System Administration > Installation > Preventive Maintenance > Equipment Work Order Entry

- System Administration > Installation > Work Order

- System Administration > Installation > Work Order > Site File Maintenance

- System Administration > Installation > Work Order > G/L Department File Maintenance

- System Administration > Installation > Work Order > Work Order Type File Maintenance

- System Administration > Installation > Work Order > Labor Category File Maintenance

- System Administration > Installation > Work Order > Labor Billing Rates Maintenance

- System Administration > Installation > Work Order > Work Order Standard Phase

- System Administration > Installation > Work Order > Work Order Entry

- System Administration > Installation > Service Contract

- System Administration > Installation > Service Contract > Contract Type File Maintenance

- System Administration > Installation > Service Contract > Service Contract File Maintenance

- System Administration > Installation > Time & Material

- System Administration > Installation > Time & Material > Job Billing Maintenance

- System Administration > Installation > Time & Material > Labor Billing Rates

- System Administration > Installation > Time & Material > Job Labor Billing Rates Maintenance

- System Administration > Installation > Time & Material > Equipment Billing Rates

- System Administration > Installation > Time & Material > Job Equipment Billing Rates Maintenance

- System Administration > Installation > Enterprise > Cost Center Maintenance

## Assumptions and Dependencies

General Guidelines

- The transaction data being submitted using this web service are stored within the Payroll Approve Pre-Time Import screen by Employee or by Quantity and requires the data to be manually approved within Spectrum using the Approval buttons on the screen.

- The Pre-time card Web Service submits one record at a time and creates 'R'egular Check types for the next available sequence number. If a 'R'egular Check types exist then it adds the details to the first existing sequence number.

- The Pre-time card Web Service does not support the Salary redistribution logic used in standard Pre-time card entry.

- To maintain Spectrum's flexibility, the Data Exchange logic will validate the web service authorization, required fields, numeric, date and generic validations only.

- The Payroll and General Ledger Modules must be set up.

- The flexibility within the Pre-Time Card web service creates new employee and quantity records. The SDX manual defines the specific guidelines for each type of record.

- Validation will be performed on the Company_Code, Work_Date and Pay_Type.

- Cost center information will only be allowed if the Company is set to a Yes status.

- This Web Service is not impacted by the Workflow process in Spectrum.

Employee Record Guidelines

- Any Pay_Type other than Q(uantity) will be sent to the Pre-Time Card Import Errors screen located within the Pre-Time Card Import logic.

- The Department_Code defined controls what information appears in the record.

- If excess data is sent within the record, the Department_Code will control what data remains in the record for review.

- Non-direct departments should not have any Job, Equipment or Work Order details defined.

- All standard Spectrum Pay Types and Add-on / Deduction codes are supported and validated to the Company_Code. See the Pay Types options defined in layout.

Quantity Record Guidelines

- The Quantity pay type 'Q' is used to designate that a quantity record is to be created and submitted to the Pre-time Card Quantity Import Errors screen within the Pre-Time Card Import logic.

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
Data Exchange Installation Screen.

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
Company where the records will be created.
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Batch_Code
Batch Code
YES
Text
8
New or existing batch code

D
Employee_Code
Employee
Text
11
Must exist in company per the Company_Code entry. Not required for quantity records.

E
Department_Code
Department
Text
6
Not required for quantity records. ** See Assumptions and Dependencies.

F
Pay_Type
Pay type
YES
Text
10
(R)egular; (O)vertime; (D)ouble time; (H)oliday; (V)acation; (S)ick;
 (M)iscellaneous; (SA)-Special amount; (ER)-Equipment-Regular;
 (EO)-Equipment-Overtime; (ED)-Equipment-Double time; (EU)-Equipment usage;
 (RP)-Retro-pay; (JX)-Job only adjustment hours; (1,2 or 3)-Description set in
 Payroll Installation screen; (Q)uantity entries only;
 (I)ncentive pay or (U)npaid time and Add-on or Deduction codes.
Validates to the defined Company_Code field name. All pay types supported
 including Incentive pay types when specified on the Payroll
 Installation screen (for example, IR, IO, ID when "I" is specified),
 Add-on and Deduction codes.

G
Hours_Employee
Employee Hours
Numeric
8
Enter decimals but no $ signs or commas. Can be positive or negative; Not required for quantity records.

H
Job_Number
Job
Text
10
Required for Quantity records.

I
Phase_Code
Phase
Text
20
No dashes. Required for Quantity records.

J
Cost_Type
Cost type
Text
3
Required for Quantity records.

K
Work_Date
Date
YES
Text
8
Enter as: MM/DD/CCYY (that is, 01/05/2010).
Within P/R processing date range

L
Message
Message
Text
30
Cannot contain Super select characters.

M
Pay_Rate_Code
Rate level
Text
1
1 thru 9 only

N
Wage_Code
Wage code
Text
10

O
Union_Code
Union code OR Pay group
Text
10

P
Worker_Comp_Code
Work Comp
Text
6

Q
State
Work state
Text
10

R
Work_County
Work county
Text
10

S
Work_Locality
Work local
Text
10

T
Equipment_Code
Equipment
Text
10

U
Equipment_Hours
Equipment Hours
Numeric
8
Enter decimals but no $ signs or commas. Can be positive or negative

V
Additional_JTD_Quantity
Add'l JTD Qty
Numeric
14
Enter decimals but no $ signs or commas. Can be positive or negative

W
Inter_Company_Code
Inter-Company code
Text
3
For Employee records- the data will be shown for this company code. For Quantity records the data will need to be reviewed and the company code changed on the error screen.
Define the valid Company code here if the Job, Work Order or Equipment is from a different company.

X
Pay_Rate
Pay Rate
Numeric
12
Enter decimals but no $ signs or commas. Can be positive or negative

Y
Cost_Category_Code
Cost Category
Text
4

Z
Crew_Number
Crew
Text
10

AA
WO_Number
Work Order
Text
10

AB
WO_Equipment
WO Site Equipment
Text
8

AC
WO_Component
WO Component
Text
2

AD
SC_Contract
WO Contract
Text
10

AE
PM_Work_Order
Equipment Work Order
Text
10

AF
Cost_Center
Cost Center
Text
10
Cost Center Maintenance; G/L Account Cost Center; Job Cost Center; Phase Cost Center; Equipment Cost Center; Equipment Type Cost Center and Work Order Cost Center
