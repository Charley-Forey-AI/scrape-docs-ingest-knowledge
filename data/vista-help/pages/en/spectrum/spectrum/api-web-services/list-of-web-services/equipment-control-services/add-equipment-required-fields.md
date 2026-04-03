---
title: "Add Equipment (Required Fields) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/add-equipment-required-fields"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/add-equipment-required-fields"
---

# Add Equipment (Required Fields)

Use this service to import Equipment information.
WSDL: AddEquip_Req.jws Method: AddEquip_Req
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Equipment information, the following file maintenance screens must be completed:

- System Administration > Installation > Equipment Control

- System Administration > Installation > Equipment Control > Cost Category File Maintenance

- System Administration > Installation > Equipment Control > Equipment Status File Maintenance

- System Administration > Installation > Equipment Control > Equipment Type File Maintenance

- System Administration > Installation > Equipment Control > Fuel / Oil File Maintenance

- System Administration > Installation > Equipment Control > Equipment Location File Maintenance

- System Administration > Installation > Equipment Control > Yard File Maintenance

- System Administration > Installation > Equipment Control > Tire File Maintenance

- System Administration > Installation > Equipment Control > Warranty Type File Maintenance

- System Administration > Installation > Equipment Control > Warrantor File Maintenance

- System Administration > Installation > Equipment Control > Equipment User-Defined Fields

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > General Ledger > G/L Department File Maintenance

- System Administration > Installation > Payroll > Wage Code Maintenance

- System Administration > Installation > Payroll > Union Maintenance

- System Administration > Installation > Time & Material > Job Equipment Billing Code Maintenance

- System Administration > Installation > Time & Material > Equipment Billing Code Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- Depends on flag for "validate equipment division with G/L department" in the Equipment Control installation screen.

- If selected, then field entry is mandatory.

- The users will press F4 to select from the G/L Department File Maintenance.

- If not selected, this field is not mandatory and can be used to enter other information in alphanumeric format, up to 5 characters.

- If a Meter type is populated then the Meter description is required.

- The cost accruals method defaults to Year when the item is created.

- The Make and Model fields validate based on the Equipment Control Installation screen validation option for make and model.

- If the Equipment_Retired field is defined then the Equipment_Status field must have a status type of Retired.

- If the Equipment_Sold field is defined as Y(es) then the Sell Price, Sold Date, and Sold To fields are required.

- Cost center information will only be allowed if the Company is set to a Pending or Yes status.

- Cost centers will validate against the Cost Center Maintenance Table.

## Field Descriptions

Use the table below for reference when using this service. The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.ExcelElement NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
BCompany_CodeCompany CodeYESText3Valid Company in Spectrum
CEquipment_CodeEquipment CodeYESText10Unique identifier-No commasUPPERCASE FORMAT- NO SYMBOLS
DDivision_CodeDivisionText5Depends on flag for Validate equipment division with G/L department? in the Equipment Control installation screen. If selected, this field entry is mandatory.
EEquipment_TypeEquipment TypeYESText4Equipment Type Maintenance
FDescriptionDescriptionYESText30
GYearYearNumeric2
HEquipment_MakeMakeText20Validated if Equipment installation option selected.
IEquipment_ModelModelText20Validated if Equipment installation option selected.
JSerial_NumberSerial No.Text50
KOn_Road_CodeRoad UsageText1(1) for on-road or (2) for off road. If blank then defaults to 1.
LMeter_TypePrimary Meter TypeText1(M)iles, (H)ours, (K)ilometers, or (U)sage
MFuel_Oil_CodeFuel CodeText2Must have a fuel type of Gas or Diesel only.Fuel/Oil Maintenance
NCapacityCapacity Wt.Numeric6Positive numbers only.
OGross_WeightVehicle Gross Wt.Numeric6Positive numbers only.
PScale_WeightVehicle Scale Wt.Numeric6Positive numbers only.
QOwned_FlagAcquisition TypeText1(O)wned, (R)ent, or (L)ease
RCondition_CodeCondition: New or Used?Text1(N)ew or (U)sed
SBilling_Rate_CodeBilling CodeText10T&M billing code file in EQ Billing Rates
TLast_JobLast Job No.Text10Valid Job number or data entry field.Jobs Maintenance (if applicable)
UWage_CodeWage CodeText10Payroll Wage Code file in combination with Union Code
VUnion_CodeUnion CodeText10Payroll Wage Code file in combination with Union Code
WEquipment_StatusEquipment statusYESText4Equipment Status Code Maintenance
XPurchase_DatePurchase DateDate10Enter as MM/DD/CCYY (06/15/2026)
YPurchased_FromPurchased FromText15
ZPurchase_CostOriginal CostNumeric14Enter decimals but no $ or commas.
AALast_MeterPrimary Last Meter ReadingNumeric10No entry allowed in start screen field. If field is defined then Meter_Type must be defined.
ABLast_Meter_DatePrimary Last Meter Read DateDate8Enter as MM/DD/CCYY (06/15/2026)No entry allowed in start screen field. If field is defined then Meter_Type must be defined.
ACEngine_MakeEngine MakeText20Validated if Equipment installation option selected.
ADEngine_ModelEngine ModelText20Validated if Equipment installation option selected.
AETransmission_MakeTransmission MakeText20Validated if Equipment installation option selected.
AFTransmission_ModelTransmission ModelText20Validated if Equipment installation option selected.
AGPower_Axle_MakePower Axle Make #1Text20Validated if Equipment installation option selected.
AHPower_Axle_ModelPower Axle Model #1Text20Validated if Equipment installation option selected.
AITire_Code_1Tire Code 1Text14Equipment Tire Maintenance
AJTire_Code_2Tire Code 2Text14Equipment Tire Maintenance
AKYard_CodeYard No.Text5Yard Maintenance
ALLocationYard LocationText8Equipment Location Maintenance
AMEquipment_RFIDEquipment RFIDText30
ANEquipment_GPSEquipment GPSText30
AOEquipment_Meter_Type2Equipment MeterÂ #2 TypeText1(M)iles; (H)ours; (K)ilometers or (U)sage
APEquipment_Meter_Type3Equipment Meter #3 TypeText1(M)iles; (H)ours; (K)ilometers or (U)sage
AQEquipment_Meter_Type4Equipment Meter #4TypeText1(M)iles; (H)ours; (K)ilometers or (U)sage
AREquipment_Meter_Desc1Equipment Meter #1 DescriptionText20Meter type must be defined in order to have a Meter description defined.
ASEquipment_Meter_Desc2Equipment Meter #2 DescriptionText20Meter type must be defined in order to have a Meter description defined.
ATEquipment_Meter_Desc3Equipment Meter #3 DescriptionText20Meter type must be defined in order to have a Meter description defined.
AUEquipment_Meter_Desc4Equipment Meter #4 DescriptionText20Meter type must be defined in order to have a Meter description defined.
AVEquipment_Engine_YrEngine YearNumeric4Enter the year
AWEquipment_Trans_YrTransmission YearNumeric4Enter the year
AXEquipment_Power_Axle1_YrPower Axle #1 YearNumeric4Enter the year
AYEquipment_Power_Axle2_YrPower Axle #2 YearNumeric4Enter the year
AZEquipment_Power_Axle2_MakePower Axle #2 MakeText20Validated if Equipment installation option selected.
BAEquipment_Power_Axle2_ModelPower Axle #2 ModelText20Validated if Equipment installation option selected.
BBEquipment_Power_Axle3_YrPower Axle #3 YearNumeric4Enter the year
BCEquipment_Power_Axle3_MakePower Axle #3 MakeText20Validated if Equipment installation option selected.
BDEquipment_Power_Axle3_ModelPower Axle #3 ModelText20Validated if Equipment installation option selected.
BEEquipment_HeightTransportation HeightNumeric10Positive numbers only. Decimal ok
BFEquipment_WidthTransportation WidthNumeric10Positive numbers only. Decimal ok
BGEquipment_LengthTransportation LengthNumeric10Positive numbers only. Decimal ok
BHEquipment_Dim_UOMTransportation Unit of MeasureText2Unit of Measure File
BIEquipment_Weight_UOMWeight Unit of MeasureText2Unit of Measure File
BJEquipment_Weight_ClassWeight ClassText10Weight Class Code
BKEquipment_RetiredRetired DateDate8Enter as MM/DD/CCYY (06/15/2026). If defined then Equipment_Status field must have a Status Type of Retired.
BLEquipment_SoldEquipment Sold?Text1(Y)es or (N)o.If yes then the Equipment_Sell_Price; Equipment_Sell_Date and Equipment_Sell_To fields are required.
BMEquipment_Sell_PriceEquipment Sold PriceNumeric11Decimal okRequired if Equipment_Sold = Y
BNEquipment_Sell_DateEquipment Sold DateDate8Enter as MM/DD/CCYY (06/15/2026)Required if Equipment_Sold = Y
BOEquipment_Sell_ToEquipment Sold ToText15Required if Equipment_Sold = Y
BPMarket_ValueCurrent Market ValueNumeric9Positive numbers only.
BQEntry_DateEntry DateDate8Enter as MM/DD/CCYY (06/15/2026) If left blank then defaults to the system date.
BRCost_CenterEquipment Cost CenterText10Cost Center Maintenance
