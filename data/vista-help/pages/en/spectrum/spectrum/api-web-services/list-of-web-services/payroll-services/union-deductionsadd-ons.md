---
title: "Union Deductions/Add-ons | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/union-deductionsadd-ons"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/union-deductionsadd-ons"
---

# Union Deductions/Add-ons

Use this service to import Union Deductions and Add-on
 codes information.

## Connection Information

URL = https://<SPECTRUM-SERVER>:8482/payroll/uniondedaddon
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "unionDedAddOns": [
 {
 "Company_Code": "ABC",
 "Union_Code": "DF001",
 "Ded_Add_On_Code": "23",
 "Record_Type": "R",
 "Ded_Add_On_Description": "Description",
 "Method": "H",
 "Formula_Code": "",
 "Rate": 10,
 "Formula_Variable_1": 0,
 "Formula_Variable_2": 0,
 "Formula_Variable_3": 0,
 "Gross_Pay_Flag": "Y",
 "Override_GL_Account": "",
 "Status": "A",
 "Effective_Date": ""
 }
 ]
}`
```

## Underlying File Maintenance

System Administration > Installation > Payroll > Deduction/Add-on Code Maintenance
System Administration > Installation > Payroll > Worker's Compensation Code Maintenance
System Administration > Installation > Payroll > Tax Table Maintenance
System Administration > Installation > Time + Material > Labor Billing Rates

## Field Descriptions

Use the table below for reference when using this service.
Excel
Element NameDescriptionReqTypeMax
FormatValidation
B
Company_CodeCompany Code
YESText3
Valid Company in Spectrum
C
Union_CodeUnion Code
YESText10
Union File Maintenance
D
Ded_Add_On_CodeDeduction or Add-On CodeYESText10
Deduction/Add-on Maintenance Table
 (PR_VOL_DEDUCT_MASTER_MC)
E
Record_Type (if updating)
When updating this indicates whether the change is to
 rate or status, when adding a new deduction this field is ignored
YES (if updating)
Text
1
R = Rate change S = Status change

F
Ded_Add_On_Description
Description
Text
 15

G
MethodMethodYESText1
G = % of gross B = % of base S = %
 of straight line R = Regular O = Overtime D = Double time A = All hours F =
 Fixed amount U = User-defined C = Prevailing wage adj H = Health and welfare
 N= Non-stated fringe
H
Formula_CodeFormula CodeText5
If Method = (U)ser-defined, this
 field is requiried, otherwise not available
I
RateRateNumeric7
If NOT using Formula_Code Format =
 3.3
J
Formula_Variable_1Formula Variable 1 (V1)
 RateNumeric7
If using Formula_Code Format =
 3.3
K
Formula_Variable_2Formula Variable 2 (V2)
 RateNumeric7
If using Formula_Code Format =
 3.3
L
Formula_Variable_3Formula Variable 3 (V3)
 RateNumeric7
If using Formula_Code Format =
 3.3
M
Gross_Pay_FlagInclude in Gross Pay FlagText1
"Y" or "N"Include deduction in gross
 pay?
N
Override_GL_AccountGL Account OverrideNumeric12
Code must have an Active
 statusG/L Master File Maintenance
O
StatusText1
(A)ctive or (Inactive). Defaults to
 Active if blank
P
Effective_DateEffective DateDate10
Enter MM/DD/CCYYDefaults to current payroll
 data
