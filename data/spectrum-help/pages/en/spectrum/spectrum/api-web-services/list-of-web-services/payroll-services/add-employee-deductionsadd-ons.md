---
title: "Add Employee Deductions/Add-ons | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/add-employee-deductionsadd-ons"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/add-employee-deductionsadd-ons"
---

# Add Employee Deductions/Add-ons

Use this service to import Employee – Deduction/Add-ons information.
WSDL: Update_Empl_Vol_Ded.jws
Method: Update_Empl_Vol_Ded
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Employee – Deduction/Add-ons information, the following file maintenance areas must be completed:

- System Administration > Installation > Payroll

- System Administration > Installation > Payroll > Employee Maintenance

- System Administration > Installation > Payroll > Deduction/Add-on Code Maintenance

- System Administration > Installation > Payroll > Formula File Maintenance

- System Administration > Installation > Accounts Payable > Vendors

- System Administration > Installation > Human Resource > Recurring Benefits Code Maintenance

## Assumptions and Dependencies

- The Payroll Module must be set up.

- The Employee code must exist in the defined Company code.

- The Employee-Deduction Add-on Web Service updates an existing employee's information for the defined fields only.

- If the Deduction/Add-on does not exist then it will be added to the Employee.

- Does not change the following fields (changes all other fields if Vol_Deduct_Code exists for the Employee)

- Company_Code

- Employee_Code

- VoL_Deduct_Code

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- If Human Resources module is active then it will update the Employees Benefits Master.

- Deduction/Add-on codes have specific rules regarding the status code option allowed and will follow the standard Spectrum rules.

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
YES
Text
3
Company where the records will be created.
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Employee_Code
Employee
YES
Text
11
Valid Employee Code in Spectrum.

D
Vol_Deduct_Code
Employee
YES
Text
10
Deduction/Add- on Maintenance Table

E
Vol_Deduct_Status
YES
Text
1
(R)ecurring, (O)ne Time, (I)nactive or (S)kip one
Required if Vol_Deduct_Code is being added to the defined Employee_Code

F
Formula_Code
Text
5
Dependent on Status & Code defined.Â If blank defaults from defined code.
Valid Formula code

G
Vol_Deduct_Amount
Numeric
9
Dependent on Status & Code defined. Format = -5.2

H
Vol_Deduct_Percent
Numeric
6
Dependent on Status & Code defined. Positive numbers only. Format = 2.3

I
Vol_Deduct_Limit
Numeric
8
Dependent on Status & Code defined. Positive numbers only. Format = 5.2

J
Monthly_Limit
Numeric
8
Dependent on Status & Code defined. Positive numbers only. Format = 5.3

K
Cycle_Amount_Limit
Numeric
8
Positive numbers only.

L
Cycle_Percent_Limit
Numeric
6
Positive numbers only. Format = 2.3

M
Formula_Value_1
Numeric
9
Format = -4.3
Defaults to zero- Tied to Formula_Code field.

N
Formula_Value_1
Numeric
9
Format = -4.3
Defaults to zero- Tied to Formula_Code field.

O
Formula_Value_1
Numeric
9
Format = -4.3
Defaults to zero- Tied to Formula_Code field.

P
Vendor_Code
Text
10
Required if Vol_Deduct_Code requires it.
Valid Vendor Code in Spectrum

Q
AP_Remark
Text
30
Required if Pay_Frequency_Flag = D, otherwise calculated by Spectrum.
