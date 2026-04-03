---
title: "Add Equipment Billing Rates | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/time--materials-services/add-equipment-billing-rates"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/time--materials-services/add-equipment-billing-rates"
---

# Add Equipment Billing Rates

Use this service to add or edit equipment billing rates.

## Connection Information

URL = https://<SPECTRUM-SERVER>:8482/TimeMaterial/AddEquipmentTM

Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication)[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST

Supported formats: JSON

## Sample JSON Body

```
`{
 "timeMaterialEquipments": [{
 "Company_Code": "2nd",
 "Billing_Code": "Test123",
 "Description": "testGEquip",
 "Reg_Bill_1":"10",
 "Reg_Bill_2":"10",
 "Reg_Bill_3":"10",
 "Reg_Bill_4":"10",
 "Reg_Bill_5":"10",
 "OT_Bill_1":"200",
 "OT_Bill_2":"20",
 "OT_Bill_3":"20",
 "OT_Bill_4":"20",
 "OT_Bill_5":"20",
 "DT_Bill_1":"300",
 "DT_Bill_2":"30",
 "DT_Bill_3":"30",
 "DT_Bill_4":"30",
 "DT_Bill_5":"30",
 "Standby_Hourly":"5",
 "Standby_Daily":"10",
 "Standby_Weekly":"20",
 "Standby_Monthly":"30"
 }]
}
`
```

## Underlying File Maintenance

- Time + Material > Equipment Billing Rates

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
EReg_Bill_1Regular Billing Rate 1 Numeric8.3
 FReg_Bill_2Regular Billing Rate 2Numeric8.3
GReg_Bill_3Regular Billing Rate 3Numeric8.3
HReg_Bill_4Regular Billing Rate 4Numeric8.3
IReg_Bill_5Regular Billing Rate 5Numeric8.3
J
 OT_Bill_1Overtime Billing Rate 1 Numeric8.3
KOT_Bill_2Overtime Billing Rate 2 Numeric8.3
LOT_Bill_3Overtime Billing Rate 3 Numeric8.3
MOT_Bill_4Overtime Billing Rate 4 Numeric8.3
NOT_Bill_5Overtime Billing Rate 5 Numeric8.3
O
 DT_Bill_1Double Time Billing Rate 1 Numeric8.3
PDT_Bill_2Double Time Billing Rate 2Numeric8.3
QDT_Bill_3Double Time Billing Rate 3Numeric8.3
RDT_Bill_4Double Time Billing Rate 4Numeric8.3
SDT_Bill_5Double Time Billing Rate 5Numeric8.3
T
 Standby_HourlyMarkup 1 Numeric8.3
U
 Standby_DailyMarkup 2Numeric8.3
V
 Standby_WeeklyMarkup 3Numeric8.3
W
 Standby_MonthlyMarkup 4 Numeric8.3
