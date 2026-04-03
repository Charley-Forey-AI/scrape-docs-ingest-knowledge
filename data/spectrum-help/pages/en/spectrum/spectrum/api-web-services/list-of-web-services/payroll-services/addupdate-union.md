---
title: "Add/Update Union | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/addupdate-union"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/addupdate-union"
---

# Add/Update Union

Use this service to add or update existing Union
 information.

## Connection Information

URL = https://<SPECTRUM-SERVER>:8482/payroll/union
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "unions": [
 {
 "Company_Code": "ABC",
 "Union_Code": "DF001",
 "Union_Name": "Test Union",
 "Craft_Description": "",
 "Certified_Craft_Code": "",
 "Status": "A",
 "Auto_Overtime": "",
 "Override_Overtime_Rules": "Y",
 "Daily_Overtime_Start_Hours": 10,
 "Weekly_Overtime_Start_Hours" : 50,
 "Saturday_Rules": "",
 "Sunday_Rules": ""
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

Use the table below for reference when using this service.
Excel
 Element NameDescriptionReqTypeMaxFormatValidation
B
Company_CodeYESText3Valid Company in Spectrum
C
Union_CodeYESText10Union
D
Union_NameDescriptionText30
E
Craft_DescriptionCraftText20
F
Certified_Craft_CodeCertified craft codeText20
G
StatusStatusText1(A)ctive or (I)nactive. Defaults to
 Active if blank.
H
Auto_OvertimeAuto-OvertimeText1"Y" or "N".
I
Override_Overtime_RulesOverrides job rulesText1"Y" or "N". If blank, and
 Auto_Overtime = "Y", defaults to "Y".
J
Daily_Overtime_Start_HoursDaily overtime start at how many
 hoursNumeric7Positive numbers only. Format =
 4.224 hours max
K
Weekly_Overtime_Start_HoursWeekly overtime starts at how many
 hoursNumeric8Positive numbers only. Format =
 5.2168 hours max
L
Saturday_RulesSaturday rulesText1Set all hours to (O)vertime, Set all
 hours to (D)oubletime, defaults to "Same rules as weekday" if blank.
M
Sunday_RulesSunday rulesText1Set all hours to (O)vertime, Set all
 hours to (D)oubletime, defaults to "Same rules as weekday" if blank.
