---
title: "Add Employee (Required Fields) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/add-employee-required-fields"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/add-employee-required-fields"
---

# Add Employee (Required Fields)

Use this service to add employee required
 fields.
Note: In order to use the
 new service, add AddEmployeeRequiredFields to your Authentication ID.
The prior
 SOAP service (AddEmp_Req) is still available on the template titled Employee Required
 Import – Old. While the service will remain available in the short term, we recommend that
 you migrate all usage to the new service.

## Connection Info

URL = https://<SPECTRUM-SERVER>:8482/employee/addRequiredFields
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication),
 [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "employeeRequiredImports": [{
 "Company_Code": "2nd",
 "Employee_Code": "JWALTER",
 "Alpha_Sort":"JW",
 "First_Name":"James",
 "Middle_Name":"W",
 "Last_Name":"Walter",
 "Employee_Suffix":"DDS",
 "Worker_Comp_Code":"0101",
 "Department_Code":"DA",
 "Employment_Status":"a",
 "Termination_Date_List3":"",
 "Pay_Type":"h",
 "Pay_Frequency_Flag":"W",
 "Hourly_Rate":100.00,
 "Salary_Amount":"",
 "Standard_Work_Hours":"40",
 "Emp_Foreign":"N",
 "Fed_Tax_Code":"US",
 "Subject_to_Fed_Tax":"T",
 "Subject_to_FICA_Fed":"T",
 "Subject_to_FUTA_Fed":"T",
 "Fed_Filing_Status":"SINGLE ",
 "Fed_Exemptions":"99",
 "Fed_Tax_Override":"666.66",
 "Fed_Tax_Override_Cont":"F",
 "State_Tax_Code":"AZ",
 "Subject_to_State_Tax":"T",
 "Subject_to_SDI_State":"E",
 "Subject_to_SUTA_State":"T",
 "State_Filing_Status":"Married",
 "State_Exemptions":"98",
 "State_Tax_Override":"2.5",
 "State_Tax_Override_Cont":"p",
 "Cost_Center":"101",
 "Employee_Termination_Reason":"",
 "Employee_Rehire_Rating":"10",
 "Occupation":"",
 "Trade":"",
 "Perm_Work_Comp":"Y",
 "Pref_Status":"",
 "Employee_Telephone_Memo":"Cell phone",
 "Employee_Driver_License_State":"AZ",
 "Employee_Driver_License_Class":"",
 "Employee_Citizenship":"US",
 "Employee_Security_Stat":"Secure employee",
 "Employee_Veteran_Stat":"",
 "Employee_New_Vet":"Y",
 "Employee_Disabled":"",
 "Employee_Disabled_Note":"PTSD",
 "Employee_Place_Birth":"Hospital",
 "Effective_Date":"01/01/2026",
 "Comments":"",
 "Last_Job_Company":"ABC",
 "Last_Job_Number":"1D",
 "Last_Equipment_Company":"ABC",
 "Last_Equipment_Code":"",
 "Hire_Date_List1":"12/31/2019",
 "Rehire_Date_List2":"",
 "Legal_First_Name":"JAMES II",
 "Legal_Middle_Name":"W",
 "Legal_Last_Name":"Walter",
 "Legal_Suffix":"DDS"
 }]
}`
```

## Underlying File Maintenance

Prior to importing Employee information, the following file maintenance areas must be completed:

- System Administration > Installation > Payroll

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Payroll > Tax Table Maintenance

- System Administration > Installation > Payroll > Department Expense Maintenance

- System Administration > Installation > Payroll > Employee Status Code Maintenance

- System Administration > Installation > Payroll > Supervisor Code Maintenance

- System Administration > Installation > Payroll > Worker's Compensation Code Maintenance

- System Administration > Installation > Payroll > Hours Bank Code Maintenance

- System Administration > Installation > Payroll > Union File Maintenance

- System Administration > Installation > Payroll > Wage Code File Maintenance

- System Administration > Installation > Payroll > EEO Classification Maintenance

- System Administration > Installation > Payroll > Employee User-Defined Fields Maintenance

- System Administration > Installation > Time + Material > Labor Billing Rates Maintenance

- System Administration > Installation > Human Resources > Locations Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The Payroll module must be set up.

- The combination of the First_Name, Middle_Name and Last_Name is used to create the displayed name within Spectrum which cannot exceed 30 characters including spaces. An error will occur if the combined value of these three individual fields exceeds the 30 character limit.

- Non-US Payroll Processing

- Payroll Installation option on the Default Tab.

- If selected then the Federal Tax code on the Employee master can be defined as any Tax code.

- The option allows for a Federal tax code can be defined on the Payroll Installation and used as a default when adding new Employees.

- Field can be defined in the service and must be unique for each tax code on the Employee master.

- Cost center information will only be allowed if the Company is set to a Pending or Yes status.

- The Employee-required Web Service creates new records only.

- The Employee contact is created.

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
Valid Company in Spectrum

C
Employee_Code
Employee Code
YES
Text
11
Unique Identifier / No commas
UPPERCASE FORMAT-NO SYMBOLS

D
Alpha_Sort
Alpha Reference
YES
Text
8

E
First_Name
Employee First Name
YES
Text
20
No commas

F
Middle_Name
Employee Middle Name
Text
20
No commas

G
Last_Name
Employee Last Name
YES
Text
30
No commas

H
Employee_Suffix
Employee name Suffix
Text
3
No commas

I
Worker_Comp_Code
Worker's Comp Code
YES
Text
6
Worker's Compensation Code Maintenance

J
Department_Code
Department Code
YES
Text
6
Department Expense Maintenance

K
Employment_Status
Employee Status
YES
Text
1
Employee Status Code Maintenance

L
Termination_Date_List3
Latest Termination Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/1982)
Required if Employee Status = 'T' or 'D'

M
Pay_Type
Pay Type
YES
Text
1
(C)ommission; (H)ourly; (O)vertime or (S)alary only
If (H)ourly selected then Salary_Amount is ignored and Hourly_Rate is required.
If (S)alary is selected then Salary_Amount is required and Hourly_ Rate is ignored.

N
Pay_Frequency_Flag
Pay Frequency
YES
Text
1
(D)aily; (W)eekly; (B)I-weekly; (M)onthly; (S)emi-monthly; (Q)uarterly or (A)nnual only

O
Hourly_Rate
Hourly Rate
Numeric
8
Positive number only. Format = 3.4
Required if Pay_Type = H

P
Salary_Amount
Salary Amount for ONE PAY PERIOD ONLY
Numeric
13
Enter Amount for ONE PAY PERIOD ONLY!
Required if Pay_Type = S , O or C

Q
Standard_Work_Hours
Standard Hours per Pay Period
Numeric
8
Positive number only. Format = 4.2
Required if Pay_Frequency_Flag = D, otherwise calculated by Spectrum if blank.

R
Emp_Foreign
Foreign Employee?
Text
1
(Y)es or (N)o only
If Payroll Installation option is selected to allow non-US payroll processing then ignore this field which is hidden.

S
Fed_Tax_Code
Federal Tax Table Code
YES
Text
10
Default to US if Payroll Installation option is not selected. Use default if defined and valid. Can be overriden. If Emp_Foreign = N then Spectrum defaults this field to US.
Payroll Tax Table Maintenance

T
Subject_to_Fed_Tax
Subject to Federal Income Tax
YES
Text
1
(E)xempt or (T)axable only. If Emp_Foreign = N then Spectrum default this field to T(axable).

U
Subject_to_FICA_Fed
Subject to FICA
YES
Text
1
(E)xempt or (T)axable only. If Emp_Foreign = N then Spectrum default this field to T(axable).

V
Subject_to_FUTA_Fed
Subject to Federal Unemployment
YES
Text
1
(E)xempt or (T)axable only. If Emp_Foreign = N then Spectrum default this field to T(axable).

W
Fed_Filing_Status
Federal Filing Status
Text
20
If Subject_to_Fed_Tax = T then this field is required.
Payroll Tax Table Maintenance

X
Fed_Exemptions
# Exemptions for Federal Income Tax
Numeric
5
Number is required based on conditional settings.

Y
Fed_Tax_Override
Amount of Federal Income Tax Override
Numeric
7
Positive number only.

Z
Fed_Tax_Override_Cont
Federal Income Tax Override Control
Text
1
(F)ixed; (P)ercent; (A)dd-on only

AA
State_Tax_Code
Resident State Tax Table Code
YES
Text
10
The Tax code must be unique between the Federal, Resident State, Perm Work State, Resident County and Resident Local.
Payroll Tax Table Maintenance

AB
Subject_to_State_Tax
Subject to State Income Tax
YES
Text
1
(E)xempt or (T)axable only. Required if field name State_Tax_Code is not blank.

AC
Subject_to_SDI_State
Subject to State SDI
YES
Text
1
(E)xempt or (T)axable only. Required if field name State_Tax_Code is not blank.

AD
Subject_to_SUTA_State
Subject to State Unemployment
YES
Text
1
(E)xempt or (T)axable only. Required if field name State_Tax_Code is not blank.

AE
State_Filing_Status
State Filing Status
Text
20
If Subject_to_State_Tax = T then this field is required.
Payroll Tax Table Maintenance

AF
State_Exemptions
# Exemptions for State Income Tax
Numeric
5
Number is required based on conditional settings.

AG
State_Tax_Override
Amount of State Income Tax Override
Numeric
7
Positive number only.

AH
State_Tax_Override_Cont
State Income Tax Override
Text
1
(F)ixed; (P)ercent; (A)dd-on only

AI
Cost_Center
Employee Cost Center
Text
10
Cost Center Maintenance

AJ
Employee_Termination_Reason
Termination Reason
Text
30

AK
Employee_Rehire_Rating
Rehire rating (0-10)
Numeric
2
0-10 only. Required if Employee has an Employment status of Terminated.

AL
Occupation
Occupation
Text
50
Occupation File Maintenance

AM
Trade
Trade
Text
50
Trade File Maintenance

AN
Perm_Work_Comp
Always use this worker's compensation code on time card?
Text
1
(Y)es or (N)o only

AO
Pref_Status
Health Coverage status
Text
3
(HCF)=Full Time, (HCP)=Part time or (VAR)=Variable Hours. Defaults to Unassigned if left blank.

AP
Employee_Telephone_Memo
Telephone Memo
Text
30

AQ
Employee_Driver_License_State
Driver's License State
Text
2
2 character postal abbreviation

AR
Employee_Driver_License_Class
Driver's License Class
Text
9
Data entry field if HR module not installed.
Human Resources License Class if HR Module installed.

AS
Employee_Citizenship
Citizenship
Text
30

AT
Employee_Security_Stat
Security Status
Text
30

AU
Employee_Veteran_Stat
Veteran Status
Text
1
(D)=Disabled Veteran
(A)=Armed Forces Service Medal Veteran
(M)= Disabled Armed Forces
(O)=Other Protected Veteran
(P)=Disabled Other Protected Veteran
(N)=Non-Veteran

AV
Employee_New_Vet
Recently Separated Veteran?
Text
1
(Y)es or (N)o only

AW
Employee_Disabled
Disabled?
Text
1
(Y)es or (N)o only

AX
Employee_Disabled_Note
Disabled Description
Text
30
Available when Disabled? Is yes. Otherwise ignore.

AY
Employee_Place_Birth
Place of Birth
Text
30

AZ
Effective_Date
Pay Effective Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010). No duplicate dates may exist. Required if Hourly_Rate or Salary_Amount is defined.
Used to define the effective date for a Pay Rate change on the Employee Master. **See Assumption and Dependency's for Rules.

BA
Comments
Pay Rate Revision Comment
Text
40
For Pay Rate Changes only. Ignore date if Effective_Date is not defined.

BB
Last_Job_Company
Company code for Last Job worked on
Text
3
If left blank and Last_Job_Number is defined then use Company_Code.
Valid Company in Spectrum

BC
Last_Job_Number
Last Job worked on
Text
10
Valid Job in Company defined

BD
Last_Equipment_Company
Company code for Last Equipment worked on
Text
3
If left blank and Last_Equipment_Code is defined then use Company_Code.
Valid Company in Spectrum

BE
Last_Equipment_Code
Last Equipment worked on
Text
10
Valid Equipment code in Company defined

BF
Hire_Date_List1
Original hire date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)

BG
Rehire_Date_List2
Latest rehire date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)

BH
Legal_First_Name
Employee's Legal First Name
Text
50
No commas

BI
Legal_Middle_Name
Employee's Legal Middle Name
Text
50
No commas

BJ
Legal_Last_Name
Employee's Legal Last Name
Text
50
No commas

BK
Legal_Suffix
Employee's Legal Suffix
Text
3
