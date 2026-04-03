---
title: "Union Benefit Tiers | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/union-benefit-tiers"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/union-benefit-tiers"
---

# Union Benefit Tiers

Use this service to import union benefit tiers.

## Connection Information

URL = https://<SPECTRUM-SERVER>:8482/payroll/unionbenefittier
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "unionBenefitTiers": [
 {
 "Company_Code": "ABC",
 "Union_Code": "DF001",
 "Benefit_Tier_Code": "T4",
 "Benefit_Tier_Description": "Tier 4"
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

Excel
Element NameDescriptionReqTypeMaxFormatValidation
B
Company_CodeCompany Code
YESText3Valid Company in Spectrum
C
Union_CodeUnion Code
YESText10Union File Maintenance
D
Benefit_Tier_CodeBenefit Tier CodeYESText10Unique Identifier
E
Benefit_Tier_DescriptionDescriptionText50
