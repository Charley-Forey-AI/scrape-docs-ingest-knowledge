---
title: "Change Equipment Charges | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/change-equipment-charges"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/change-equipment-charges"
---

# Change Equipment Charges

Use this service to import Equipment Charges change
 information.
 WSDL: UpdateEquip_Charges.jws Method:
 UpdateEquip_Charges
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Equipment module must be set up.

- The Equipment code must exist in the defined Company code.

- The Equipment Items - Charges Information Web Service updates existing Equipment's information for the defined fields only.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes the data with the defined data in the field name.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access
 the serverYESText20Data Exchange Installation
 Screen
GUIDUnique reference number
 created by programmingText36** See GUID
 definition
B
Company_CodeCompany CodeYESText3Valid Company in
 Spectrum
C
Equipment_CodeEquipment CodeYESText10Valid Equipment Code in
 Spectrum
D
Insurance_Cost_Per_YearInsurance Cost/Yr.Numeric10Enter decimals but no $ or
 commas.
E
License_Per_YearLicense Cost/Yr.Numeric10Enter decimals but no $ or
 commas.
F
Depreciation_CostDepreciation Cost/Yr.Numeric10Enter decimals but no $ or
 commas.
G
Depreciation_MethodDepreciation MethodText1(Y)ear, (M)eter, or
 (H)ours
H
Rate_Per_HourJob Rate/Full
 Charge/HourlyNumeric8Enter decimals but no $ or
 commas. Positive number only.
I
Rate_Per_DayJob Rate/Full
 Charge/DailyNumeric8Enter decimals but no $ or
 commas. Positive number only.
J
Rate_Per_WeekJob Rate//Full
 Charge/WeeklyNumeric8Enter decimals but no $ or
 commas. Positive number only.
K
Rate_Per_MonthJob Rate/Full
 Charge/MonthlyNumeric8Enter decimals but no $ or
 commas. Positive number only.
L
Job_Operating_Rate_HourJob Rate/
 Operating//HourlyNumeric8Enter decimals but no $ or
 commas. Positive number only.
M
Job_Operating_Rate_DayJob Rate/
 Operating/DailyNumeric8Enter decimals but no $ or
 commas. Positive number only.
N
Job_Operating_Rate_WeekJob Rate/
 Operating/WeeklyNumeric8Enter decimals but no $ or
 commas. Positive number only.
O
Job_Operating_Rate_MonthJob Rate/
 Operating/MonthlyNumeric8Enter decimals but no $ or
 commas. Positive number only.
P
Stand_By_Rate_HourJob Stand By
 Rate/HourlyNumeric8Enter decimals but no $ or
 commas. Positive number only.
Q
Stand_By_Rate_DayJob Stand By
 Rate/DailyNumeric8Enter decimals but no $ or
 commas. Positive number only.
R
Stand_By_Rate_WeekJob Stand By
 Rate/WeeklyNumeric8Enter decimals but no $ or
 commas. Positive number only.
S
Stand_By_Rate_MonthJob Stand By
 Rate/MonthlyNumeric8Enter decimals but no $ or
 commas. Positive number only.
T
Hourly_Rental_RateRental Rate/Full
 Charge/HourlyNumeric8Enter decimals but no $ or
 commas. Positive number only.
U
Daily_Rental_RateRental Rate/Full
 Charge/DailyNumeric8Enter decimals but no $ or
 commas. Positive number only.
V
Weekly_Rental_RateRental Rate/Full
 Charge/WeeklyNumeric8Enter decimals but no $ or
 commas. Positive number only.
W
Monthly_Rental_RateRental Rate/Full
 Charge/MonthlyNumeric8Enter decimals but no $ or
 commas. Positive number only.
X
Rent_Operating_Rate_HourRental Rate/
 Operating/HourlyNumeric8Enter decimals but no $ or
 commas. Positive number only.
Y
Rent_Operating_Rate_DayRental Rate/
 Operating/DailyNumeric8Enter decimals but no $ or
 commas. Positive number only.
Z
Rent_Operating_Rate_WeekRental Rate/
 Operating/WeeklyNumeric8Enter decimals but no $ or
 commas. Positive number only.
AA
Rent_Operating_Rate_MonthRental Rate/
 Operating/MonthlyNumeric8Enter decimals but no $ or
 commas. Positive number only.
AB
Rental_Stand_By_HourRental Rate/ Stand
 By/HourlyNumeric8Enter decimals but no $ or
 commas. Positive number only.
AC
Rental_Stand_By_DayRental Rate/ Stand
 By/DailyNumeric8Enter decimals but no $ or
 commas. Positive number only.
AD
Rental_Stand_By_WeekRental Rate/ Stand
 By/WeeklyNumeric8Enter decimals but no $ or
 commas. Positive number only.
AE
Rental_Stand_By_MonthRental Rate/ Stand
 By/MonthlyNumeric8Enter decimals but no $ or
 commas. Positive number only.
