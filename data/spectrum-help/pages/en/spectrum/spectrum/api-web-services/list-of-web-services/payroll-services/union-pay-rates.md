---
title: "Union Pay Rates | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/union-pay-rates"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/union-pay-rates"
---

# Union Pay Rates

Use this service to change pay rates defined on the union.
 This is useful when not using wage codes.

## Connection Information

URL = https://<SPECTRUM-SERVER>:8482/payroll/unionrates
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
 "Effective_Date": "12/29/2019",
 "Rate_Level_Description_1": "1",
 "Rate_Level_Description_2": "22",
 "Rate_Level_Description_3": "333",
 "Rate_Level_Description_4": "4444",
 "Rate_Level_Description_5": "55555",
 "Rate_Level_Description_6": "666666",
 "Rate_Level_Description_7": "7777777",
 "Rate_Level_Description_8": "88888888",
 "Rate_Level_Description_9": "999999999",
 "Total_Regular_Rate_Level_1": 1.123,
 "Total_Regular_Rate_Level_2": 2.34,
 "Total_Regular_Rate_Level_3": 3.4,
 "Total_Regular_Rate_Level_4": 4,
 "Total_Regular_Rate_Level_5": 5.6,
 "Total_Regular_Rate_Level_6": 6.78,
 "Total_Regular_Rate_Level_7": 7.890,
 "Total_Regular_Rate_Level_8": 8.90,
 "Total_Regular_Rate_Level_9": 9.0,
 "Regular_Base_Rate_Level_1": 1.123,
 "Regular_Base_Rate_Level_2": 2.34,
 "Regular_Base_Rate_Level_3": 3.4,
 "Regular_Base_Rate_Level_4": 4,
 "Regular_Base_Rate_Level_5": 5.6,
 "Regular_Base_Rate_Level_6": 6.78,
 "Regular_Base_Rate_Level_7": 7.890,
 "Regular_Base_Rate_Level_8": 8.90,
 "Regular_Base_Rate_Level_9": 9.0,
 "Total_Overtime_Rate_Level_1": 1.123,
 "Total_Overtime_Rate_Level_2": 2.34,
 "Total_Overtime_Rate_Level_3": 3.4,
 "Total_Overtime_Rate_Level_4": 4,
 "Total_Overtime_Rate_Level_5": 5.6,
 "Total_Overtime_Rate_Level_6": 6.78,
 "Total_Overtime_Rate_Level_7": 7.890,
 "Total_Overtime_Rate_Level_8": 8.90,
 "Total_Overtime_Rate_Level_9": 9.0,
 "Total_Double_Time_Rate_Level_1": 1.123,
 "Total_Double_Time_Rate_Level_2": 2.34,
 "Total_Double_Time_Rate_Level_3": 3.4,
 "Total_Double_Time_Rate_Level_4": 4,
 "Total_Double_Time_Rate_Level_5": 5.6,
 "Total_Double_Time_Rate_Level_6": 6.78,
 "Total_Double_Time_Rate_Level_7": 7.890,
 "Total_Double_Time_Rate_Level_8": 8.90,
 "Total_Double_Time_Rate_Level_9": 9.0,
 "Bill_Code_Level_1": "L1",
 "Bill_Code_Level_2": "LF",
 "Bill_Code_Level_3": "O1",
 "Bill_Code_Level_5": "",
 "Bill_Code_Level_6": "T1",
 "Bill_Code_Level_7": "T1",
 "Bill_Code_Level_8": "TO",
 "Bill_Code_Level_9": " "
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
Company_CodeCompany Code
YESText3Valid Company in Spectrum
C
Union_CodeUnion Code
YESText10Union File Maintenance
D
Effective_Date
Effective Date
Date
10
Enter MM/DD/CCYY
Defaults to current payroll data

E
Rate_Level_Description_1
First level Wage Title/Description
Text
 20

F
Rate_Level_Description_2
Second level Wage Title/Description
Text
 20

G
Rate_Level_Description_3
Third level Wage Title/Description
Text
 20

H
Rate_Level_Description_4
Fourth level Wage Title/Description
Text
 20

I
Rate_Level_Description_5
Fifth level Wage Title/Description
Text
 20

J
Rate_Level_Description_6
Sixth level Wage Title/Description
Text
 20

K
Rate_Level_Description_7
Seventh level Wage Title/Description
Text
 20

L
Rate_Level_Description_8
Eighth level Wage Title/Description
Text
 20

M
Rate_Level_Description_9
Ninth level Wage Title/Description
Text
 20

N
Total_Regular_Rate_Level_1
Total regular rate level 1
Numeric
9
Total rate is used for payroll tax purposes. Format =
 -5.3

O
Total_Regular_Rate_Level_2
Total regular rate level 2
Numeric
9
Format = -5.3

P
Total_Regular_Rate_Level_3
Total regular rate level 3
Numeric
9
Format = -5.3

Q
Total_Regular_Rate_Level_4
Total regular rate level 4
Numeric
9
Format = -5.3

R
Total_Regular_Rate_Level_5
Total regular rate level 5
Numeric
9
Format = -5.3

S
Total_Regular_Rate_Level_6
Total regular rate level 6
Numeric
9
Format = -5.3

T
Total_Regular_Rate_Level_7
Total regular rate level 7
Numeric
9
Format = -5.3

U
Total_Regular_Rate_Level_8
Total regular rate level 8
Numeric
9
Format = -5.3

V
Total_Regular_Rate_Level_9
Total regular rate level 9
Numeric
9
Format = -5.3

W
Regular_Base_Rate_Level_1
Base regular rate level 1
Numeric
9
Base figure is used when calculating percent of base
 add-ons and deductions. Format = -5.3

X
Regular_Base_Rate_Level_2
Base regular rate level 2
Numeric
9
Format = -5.3

Y
Regular_Base_Rate_Level_3
Base regular rate level 3
Numeric
9
Format = -5.3

Z
Regular_Base_Rate_Level_4
Base regular rate level 4
Numeric
9
Format = -5.3

AA
Regular_Base_Rate_Level_5
Base regular rate level 5
Numeric
9
Format = -5.3

AB
Regular_Base_Rate_Level_6
Base regular rate level 6
Numeric
9
Format = -5.3

AC
Regular_Base_Rate_Level_7
Base regular rate level 7
Numeric
9
Format = -5.3

AD
Regular_Base_Rate_Level_8
Base regular rate level 8
Numeric
9
Format = -5.3

AE
Regular_Base_Rate_Level_9
Base regular rate level 9
Numeric
9
Format = -5.3

AF
Total_Overtime_Rate_Level_1
Numeric
9
Format = -5.3

AG
Total_Overtime_Rate_Level_2
Numeric
9
Format = -5.3

AH
Total_Overtime_Rate_Level_3
Numeric
9
Format = -5.3

AI
Total_Overtime_Rate_Level_4
Numeric
9
Format = -5.3

AJ
Total_Overtime_Rate_Level_5
Numeric
9
Format = -5.3

AK
Total_Overtime_Rate_Level_6
Numeric
9
Format = -5.3

AL
Total_Overtime_Rate_Level_7
Numeric
9
Format = -5.3

AM
Total_Overtime_Rate_Level_8
Numeric
9
Format = -5.3

AN
Total_Overtime_Rate_Level_9
Numeric
9
Format = -5.3

AO
Overtime_Base_Rate_Level_1
 Numeric
 9
Calculates from base rate if blank. Format = -5.3

AP
Overtime_Base_Rate_Level_2
 Numeric
 9
Format = -5.3

AQ
Overtime_Base_Rate_Level_3
 Numeric
 9
Format = -5.3

AR
Overtime_Base_Rate_Level_4
 Numeric
 9
Format = -5.3

AS
Overtime_Base_Rate_Level_5
 Numeric
 9
Format = -5.3

AT
Overtime_Base_Rate_Level_6
 Numeric
 9
Format = -5.3

AU
Overtime_Base_Rate_Level_7
 Numeric
 9
Format = -5.3

AV
Overtime_Base_Rate_Level_8
 Numeric
 9
Format = -5.3

AW
Overtime_Base_Rate_Level_9
 Numeric
 9
Format = -5.3

AX
Total_Double_Time_Rate_Level_1
 Numeric
9
 Format = -5.3

AY
Total_Double_Time_Rate_Level_2
 Numeric
9
 Format = -5.3

AZ
Total_Double_Time_Rate_Level_3
 Numeric
9
 Format = -5.3

BA
Total_Double_Time_Rate_Level_4
 Numeric
9
 Format = -5.3

BB
Total_Double_Time_Rate_Level_5
 Numeric
9
 Format = -5.3

BC
Total_Double_Time_Rate_Level_6
 Numeric
9
 Format = -5.3

BD
Total_Double_Time_Rate_Level_7
 Numeric
9
 Format = -5.3

BE
Total_Double_Time_Rate_Level_8
 Numeric
9
 Format = -5.3

BF
Total_Double_Time_Rate_Level_9
 Numeric
9
 Format = -5.3

BG
Double_Time_Base_Rate_Level_ 1
 Numeric
1
Calculates from base rate if blank. Format = -5.3

BH
Double_Time_Base_Rate_Level_ 2
 Numeric
1
Format = -5.3

BI
Double_Time_Base_Rate_Level_ 3
 Numeric
1
Format = -5.3

BJ
Double_Time_Base_Rate_Level_4
 Numeric
1
Format = -5.3

BK
Double_Time_Base_Rate_Level_5
 Numeric
1
Format = -5.3

BL
Double_Time_Base_Rate_Level_ 6
 Numeric
1
Format = -5.3

BM
Double_Time_Base_Rate_Level_7
 Numeric
1
Format = -5.3

BN
Double_Time_Base_Rate_Level_8
 Numeric
1
Format = -5.3

BO
Double_Time_Base_Rate_Level_ 9
 Numeric
1
Format = -5.3

BP
Bill_Code_Level_1
 Text
10
T&M Billing Code Maintenance

BQ
Bill_Code_Level_2
 Text
10
T&M Billing Code Maintenance

BR
Bill_Code_Level_3
 Text
10
T&M Billing Code Maintenance

BS
Bill_Code_Level_4
 Text
10
T&M Billing Code Maintenance

BT
Bill_Code_Level_5
 Text
10
T&M Billing Code Maintenance

BU
Bill_Code_Level_6
 Text
10
T&M Billing Code Maintenance

BV
Bill_Code_Level_7
 Text
10
T&M Billing Code Maintenance

BW
Bill_Code_Level_8
 Text
10
T&M Billing Code Maintenance

BX
Bill_Code_Level_9
 Text
10
T&M Billing Code Maintenance
