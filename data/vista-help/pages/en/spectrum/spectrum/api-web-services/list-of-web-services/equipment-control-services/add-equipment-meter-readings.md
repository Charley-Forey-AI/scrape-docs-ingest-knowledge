---
title: "Add Equipment Meter Readings | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/add-equipment-meter-readings"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/add-equipment-meter-readings"
---

# Add Equipment Meter Readings

Use this service to import Equipment Meter Reading
 information.
 WSDL: AddEquipMeterReading.jws Method:
 AddEquipMeterReading
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Equipment Meter Reading information, the following file maintenance screens must be completed:

- System Administration > Installation > Equipment Control

- System Administration > Installation > Equipment Control > Equipment

- System Administration > Installation > Equipment Control > Equipment Meters

- System Administration > Installation > Equipment Control > Equipment Status File Maintenance

## Assumptions and Dependencies

- The Add Meter Readings Web Service adds historical meter information for defined fields only

- The Web Service will not support the following logic:

- Equipment with a 'Not Used' status type

- Multi-company readings

- Meter replacement

- New base readings

- The Web Service follows the majority of the same logic as manually entering meter reading in Meter Reading Transaction Entry, with the exceptions of the data defined here. The Spectrum Help Files can be used for troubleshooting errors along with the details defined here.

- If Meter_Reading is defined in the import (that is, a non-zero value), then use that number. Otherwise, if left blank (or zero), the use the Meter_Change value.

- When Meter_Reading is used, save new reading using same rules as in Meter Reading Transaction Entry.

- Example: Current Spectrum meter reading is 1500.and imported meter reading is 1550. Web Service stores 1550 as the new Meter Reading.

- When Meter_Change is used, compute the new meter reading.

- Determine the most recent prior meter reading (using the Transaction Date). If there is already a reading in Spectrum exactly matching the defined Transaction Date, use that meter reading value, if not found, look back day-by-day to find the 'most recent prior' date.

- Add the defined incremental change-in-meter to the Meter Reading on the date determined above. Use this amount as the new Meter Reading, and save it using same rules as in Meter Reading Transaction Entry.

- Example: Current Spectrum meter reading is 1500.and imported change-in-meter reading is 50. Web Service stores 1550 as the new Meter Reading.

- It is possible there will be meter reading(s) for dates later than this Meter_Change: Add the Meter_Change value to all subsequent (later) meter readings

- The Web Service will automatically record Meter Type, Fiscal Year and Period (based on defined Transaction Date), Operator ID (from Authorization ID), system Date/Time of the import, and internal Transaction ID in the new Meter History record. It will also store the 'Last Meter' and 'Last Meter Date' in the Equipment Master, like during the Equipment Meter Reading Update.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReq?TypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeYESText3Valid company in Spectrum
C
Equipment_CodeEquipment CodeYESTextValid equipment code must exist in the defined company
Status Type = Active or Inactive
D
Meter_NumberMeter #Text1Format = 1, 2, 3 or 4. If left blank, auto-assign meter #1Meter# must exist for defined equipment code
E
Batch_IDBatch CodeText10
F
Transaction_DateDateDateFormat = MM/DD/CCYY
If left blank, assign current E/C processing dateMust be within E/C minimum/maximum processing date range
G
Meter_ReadingNew Meter ReadingNum9*** See Assumptions and Dependencies
Use this value if non-zeroNegative number not allowed
H
Meter_ChangeIncremental Meter ChangeNum9*** See Assumptions and Dependencies
Use this value only when Meter_Reading is blank (or zero)Must be non-zero, if Meter_Reading is blank (or zero)
Must not result in a negative Meter Reading
I
Meter_RemarksRemarksText50
