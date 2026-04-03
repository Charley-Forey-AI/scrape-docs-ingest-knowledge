---
title: "Add Labor Billing Rates | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/time--materials-services/add-labor-billing-rates"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/time--materials-services/add-labor-billing-rates"
---

# Add Labor Billing Rates

Use this service to add or update labor billing rates.

## Connection Information

URL = https://<SPECTRUM-SERVER>:8482/TimeMaterial/AddLaborTM

Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication),
 [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST

Supported formats: JSON

## Sample JSON Body

```
`{
 "timeMaterialLabors": [{
 "Company_Code": "2nd",
 "Billing_Code": "VS1",
 "Description": "",
 "Markup_Type":"N",
 "Reg_Bill_1":"1",
 "Reg_Bill_2":"10",
 "Reg_Bill_3":"100",
 "Reg_Bill_4":"1000",
 "Reg_Bill_5":"100000",
 "OT_Bill_1":"20",
 "OT_Bill_2":"20",
 "OT_Bill_3":"20",
 "OT_Bill_4":"20",
 "OT_Bill_5":"20",
 "DT_Bill_1":"30",
 "DT_Bill_2":"30",
 "DT_Bill_3":"30",
 "DT_Bill_4":"30",
 "DT_Bill_5":"30",
 "Markup_1":"5",
 "Markup_2":"10",
 "Markup_3":"25",
 "Markup_4":"29",
 "Markup_5":"35"
 }]
}
`
```

## Underlying File Maintenance

- System Administration > Installation > Time + Material > Labor Billing Rates

## Field Descriptions

ExcelElement NameDescriptionReqTypeMaxFormatValidation
Authorization_ID Authorization ID to
 access the serverYESText20Data Exchange
 Installation Screen
GUID Unique reference number created
 by programmingText36** See GUID definition
B
Company_CodeCompany CodeYESText3KeyValid Company in Spectrum
C
 Billing_CodeBilling CodeYESText10Key
D
 DescriptionBill Code DescriptionText25
EMarkup_Type Markup TypeText1'N'one, 'P'ercentage or 'R'ate per hour
FReg_Bill_1Regular Billing Rate 1 Numeric8.3
 GReg_Bill_2Regular Billing Rate 2Numeric8.3
HReg_Bill_3Regular Billing Rate 3Numeric8.3
IReg_Bill_4Regular Billing Rate 4Numeric8.3
JReg_Bill_5Regular Billing Rate 5Numeric8.3
K
 OT_Bill_1Overtime Billing Rate 1 Numeric8.3
LOT_Bill_2Overtime Billing Rate 2 Numeric8.3
MOT_Bill_3Overtime Billing Rate 3 Numeric8.3
NOT_Bill_4Overtime Billing Rate 4 Numeric8.3
OOT_Bill_5Overtime Billing Rate 5 Numeric8.3
P
 DT_Bill_1Double Time Billing Rate 1 Numeric8.3
QDT_Bill_2Double Time Billing Rate 2Numeric8.3
RDT_Bill_3Double Time Billing Rate 3Numeric8.3
SDT_Bill_4Double Time Billing Rate 4Numeric8.3
TDT_Bill_5Double Time Billing Rate 5Numeric8.3
UMarkup_1 Markup 1Numeric5.23.2/5.2Percentage is 3.2, Rate/Hr is 5.2
VMarkup_2
Markup 2Numeric5.23.2/5.2Percentage is 3.2, Rate/Hr is 5.2
WMarkup_3 Markup 3Numeric5.23.2/5.2Percentage is 3.2, Rate/Hr is 5.2
XMarkup_4
Markup 4Numeric5.23.2/5.2Percentage is 3.2, Rate/Hr is 5.2
YMarkup_5
Markup 5Numeric5.23.2/5.2Percentage is 3.2, Rate/Hr is 5.2
