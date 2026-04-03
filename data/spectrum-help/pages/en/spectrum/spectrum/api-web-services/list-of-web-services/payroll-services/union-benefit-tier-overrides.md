---
title: "Union Benefit Tier Overrides | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/union-benefit-tier-overrides"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/union-benefit-tier-overrides"
---

# Union Benefit Tier Overrides

Use this service to add an override to an existing benefit
 tier.

## Connection Information

URL = https://<SPECTRUM-SERVER>:8482/payroll/unionbenefittieroverride
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "unionBenefitTierOverrides": [
 {
 "Company_Code": "ABC",
 "Union_Code": "DF001",
 "Ded_Add_On_Code": "WW",
 "Benefit_Tier_Code": "T3",
 "Override_Status": "T",
 "Rate": 3.456,
 "Formula_Variable_1": 0,
 "Formula_Variable_2": 0,
 "Formula_Variable_3": 0
 }
 ]
}`
```

## Underlying File Maintenance

System Administration > Installation > Payroll > Deduction/Add-on Code Maintenance
System Administration > Installation > Payroll > Worker's Compensation Code Maintenance
System Administration > Installation > Payroll > Tax Table Maintenance
System Administration > Installation > Time & Material > Labor Billing Rates

## Field Descriptions

Excel
Element NameDescriptionReqTypeMaxFormatValidation
B
Company_CodeCompany Code
YESText3Valid Company in Spectrum
C
Union_CodeUnion Code
YESText10Union File Maintenance
D
Ded_Add_On_Code
Deduction or Add-On Code
YES
Text
10
Deduction/Add-on Maintenance Table

E
Benefit_Tier_CodeBenefit Tier CodeYESText10
F
Override_Status
Override Status
 Text
1
(N)ot applicable,(T)ier-specific rate. If left blank,
 defaults to 'No override'

G
Rate
Rate
Numeric
 If NOT using Formula_Code Format = 3.3

H
Formula_Variable_1
Formula Variable 1 (V1) Rate
Numeric
7
 If using Formula_Code Format = 3.3

I
Formula_Variable_2
Formula Variable 2 (V2) Rate
Numeric
7
If using Formula_Code Format = 3.3

J
Formula_Variable_3
Formula Variable 3 (V3) Rate
Numeric
7
 If using Formula_Code Format = 3.3
