---
title: "Union Fringes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/union-fringes"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/union-fringes"
---

# Union Fringes

Use this service to add union fringes
 information.

## Connection Information

URL = https://<SPECTRUM-SERVER>:8482/payroll/unionfringe
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "unionFringes": [
 {
 "Company_Code": "ABC",
 "Union_Code": "DF001",
 "Fringe_Code": "F1",
 "Record_Type": "R",
 "Base_Type": "A",
 "Formula_Code": "",
 "Fringe_Rate": 2.34,
 "Formula_Variable_1": 0,
 "Formula_Variable_2": 0,
 "Formula_Variable_3": 0,
 "Fringe_Payable_GL_Acct": "0255",
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
Element NameDescriptionReqTypeMaxFormatValidation
B
Company_CodeYESText3Valid Company in Spectrum
C
Union_CodeYESText10UnionUnion File Maintenance
D
Fringe_CodeYESText20
E
Record_TypeWhen updating this indicates whether
 the change is to rate or status, when adding a new deduction this field is
 ignoredYES (if updating)Text1R = Rate change S = Status
 change
F
Base_TypeBase TypeYESText1P = % of Gross B = % of Base R =
 Regular O = Overtime D = Double time A = All hours U = User-defined
G
Formula_CodeFormula CodeText5If Method = (U)ser-defined, this
 field is requiried, otherwise not availableValid Formula Code
 (PR_FORMULA_MC)
H
Fringe_RateFringe RateNumeric7If NOT using Formula_Code Format =
 3.4
I
Formula_Variable_1Formula Variable 1 (V1) RateNumeric7If using Formula_Code Format =
 4.4
J
Formula_Variable_2Formula Variable 2 (V2) RateNumeric7If using Formula_Code Format =
 4.4
K
Formula_Variable_3Formula Variable 3 (V3) RateNumeric7If using Formula_Code Format =
 4.4
L
Fringe_Payable_GL_AcctFringe Payable GL AccountYESNumeric12Code must have an Active
 statusG/L Master File Maintenance
M
StatusStatusText1(A)ctive or (Inactive). Defaults to
 Active if blank
N
Effective_DateEffective DateDate10Enter MM/DD/CCYYDefaults to current payroll
 data
