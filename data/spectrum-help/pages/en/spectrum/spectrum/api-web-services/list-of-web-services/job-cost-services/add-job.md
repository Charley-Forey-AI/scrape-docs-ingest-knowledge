---
title: "Add Job | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/add-job"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/add-job"
---

# Add Job

Use this service to add Job information.
WSDL: AddJob.jws
Method: AddJob
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Job information, these maintenance areas in System Administration > Installation must be completed.

- Accounts ReceivableJob Cost

- Accounts Receivable > Sales Tax Code Maintenance

- Accounts Receivable > Unit of Measure File Maintenance

- Customers

- Enterprise Management > Cost Center Maintenance

- General Ledger > G/L Department File Maintenance

- General Ledger > G/L Master File Maintenance

- Job Cost > Job User-Defined Fields Maintenance

- Job Cost > Tax Classification File Maintenance

- Payroll > Tax Table Maintenance

- Payroll > Worker's Compensation Code Maintenance

- Work Order > Site File Maintenance

## Assumptions and Dependencies

- The Job Master cost center flag is validated against the customer cost center.

- The following sections in the Job Master are defined by the Job Cost Installation options:

- Payroll burden

- Payroll overhead

- Phase setup

- Tax_Class_Code field logic

- Key personnel validation logic

- The contract is set up when the Customer code is defined in the layout.

- The T+M Billing setup occurs when the Price_Method_Code is defined as Cost Plus or Time+Material and the Customer code is defined.

- The Payroll work tax codes must be unique for each of the three defined.

- The earned calculation logic is based on the Price type defined on the Job.

- Phase mask, start/end major group and start/end minor group default from the Job Installation screen if fields are blank.

- If the Phase Categories is defined then define the correct Phase mask and major/minor group positions for the Job.

- Master Job logic:

- The Master Job tied to the Sub Job must be valid and not have a complete status.

- The Master Job and Sub Job must have the same Phase length.

- The Sub Job will be created with the same Phase setup as the Master Job.

- The Sub Job will default the Master Job's Customer and Tax classification if left blank.

- The T+M billing submitted by each Sub Job option is selected on the Master Job and defaults to unselected unless a Sub Job defines the Bill_From_Master field option. The last created Sub Job controls this feature on the Master Job.

- The Job cannot have both the Davis-Bacon and Prevailing wage options selected.

- The Estimated and Actual complete dates must be greater than or equal to the Estimated and Actual start dates.

- The Key personnel display as Job contacts if the Job Cost Installation option validates to the Employee code.

- Cost center information will only be allowed in if the Company is set to a Pending or Yes status.

- This Web Service will work with the defined Workflow process in Spectrum.

- The Authorized ID must have the user-defined fields defined, or mapped for this Web Service.

## Field Descriptions

Use the table below for reference when using this service.Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.

ExcelElement NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
BCompany_CodeCompany CodeYESText3Valid Company in Spectrum
CJob_NumberJob NumberYESText10No duplicates
DJob_DescriptionJob NameText25
EDivisionDivision NumberNumeric5Required if Job Cost installation option is selected.
F Address_1Address LineText30
GAddress_2Address Line 2Text30
HCityCityText25
IStateStateText22-digit postal abbreviation
JZip_CodeZip CodeText10ZIP or ZIP + 4 (for example, 98012-1234)
KPhonePhone numberText14Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.Remove the dashes from format when sending to Spectrum.
LFax_PhoneFax NumberText14Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.Remove the dashes from format when sending to Spectrum.
MJob_Site_PhoneJob Site Phone NumberText14Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.Remove the dashes from format when sending to Spectrum.
NSuperintendentSuperintendentText15Employee Code if installation screen selected
OEstimatorEstimatorText15Employee Code if installation screen selected
PProject_ManagerProject ManagerText15Employee Code if installation screen selected
QCustomer_CodeCustomer CodeText10Customer Maintenance File
RContract_NumberContract NumberText30
SJob_TypeContract TypeText10
TTax_Class_CodeTax classification -Use Tax Code or A/R Sales Tax Code.Text15Required based on the Job Cost installation settings. Defaults from Customer if blank and Job Cost Installation is not utilizing job classification validation option.JC Tax Classification Maintenance file. If JC install screen is set to "Y" for Use Tax Classification. Or to A/R Sales Tax Maintenance File if Use Tax Classification flag is "N".
UTaxable_FlagTaxable FlagYESText1"Y" or "N" only
VTotal_UnitsJob UnitsNumeric9Positive numbers only.
WUnit_of_MeasureUnit of MeasureText5Units of Measure Maintenance File
XCertified_FlagCertified FlagText1'Y' or 'N' only
YWork_Comp_CodeWorker's Compensation CodeText6Worker's Compensation Code Maintenance File
ZWage_Rate_LevelWage Rate LevelNumeric1Numbers 1-9 only
AAPrice_Method_CodePrice Type CodeYESText1(F)ixed Price; (T)ime & Material; (C)ost Plus or (U)nit Price
ABEst_Start_DateEstimated Start DateDate10Text format for import MM/DD/CCYY
ACEst_Complete_DateEstimated Complete DateDate10Text format for import MM/DD/CCYY
ADStart_DateActual Start DateDate10Text format for import MM/DD/CCYY
AEComplete_DateActual Complete DateDate 10Text format for import MM/DD/CCYY
AFWork_State_Tax_CodeWork State Tax CodeText10The Work Tax codes must be unique.Tax Table Maintenance
AGWork_County_Tax_CodeWork County Tax CodeText10The Work Tax codes must be unique.Tax Table Maintenance
AHWork_Local_Tax_CodWork Local Tax CodeText10The Work Tax codes must be unique.Tax Table Maintenance
AIOriginal_ContractOriginal Contract AmountNumeric14Not validated. DOES NOT include change order amounts. Change Orders are entered manually into Spectrum.
AJWO_SiteWork Order SiteText10Work Order Site Maintenance File
AKLatitudeLatitudeNumeric11Format for import -XXX.XXXXXX.
ALLongitudeLongitudeNumeric11Format for import -XXX.XXXXXX.
AMTrack_Davis_BaconDavis-Bacon JobText1'Y'or 'N' only
ANTrack_Prevailing_WagePrevailing Wage Job and optionText1'Y' or 'N' onlyY=Prevailing Wage, F=Regular wages include non-stated Fringes OR N=Not Prevailing Wage only
AOCreate_DateCreate DateDate10Text format for import MM/DD/CCYY. If left blank it will use the date it was imported.
APUDF1User Defined Alpha/Numeric/Date 1+20Web Service Authorization ID Service UDF defined.
AQUDF2User Defined Alpha/Numeric/Date 2+20Web Service Authorization ID Service UDF defined.
ARUDF3User Defined Alpha/Numeric/Date 3+20Web Service Authorization ID Service UDF defined.
ASUDF4User Defined Alpha/Numeric/Date 4+20Web Service Authorization ID Service UDF defined.
ATUDF5User Defined Alpha/Numeric/Date 5+20Web Service Authorization ID Service UDF defined.
AUUDF6User Defined Alpha/Numeric/Date 6+20Web Service Authorization ID Service UDF defined.
AVUDF7User Defined Alpha/Numeric/Date 7+20Web Service Authorization ID Service UDF defined.
AWUDF8User Defined Alpha/Numeric/Date 8+20Web Service Authorization ID Service UDF defined.
AXUDF9User Defined Alpha/Numeric/Date 9+20Web Service Authorization ID Service UDF defined.
AYUDF10User Defined Alpha/Numeric/Date 10+20Web Service Authorization ID Service UDF defined.
AZUDF11User Defined Alpha/Numeric/Date 11+20Web Service Authorization ID Service UDF defined.
BAUDF12User Defined Alpha/Numeric/Date 12+20Web Service Authorization ID Service UDF defined.
BBUDF13User Defined Alpha/Numeric/Date 13+20Web Service Authorization ID Service UDF defined.
BCUDF14User Defined Alpha/Numeric/Date 14+20Web Service Authorization ID Service UDF defined.
BDUDF15User Defined Alpha/Numeric/Date 15+20Web Service Authorization ID Service UDF defined.
BEUDF16User Defined Alpha/Numeric/Date 16+20Web Service Authorization ID Service UDF defined.
BFUDF17User Defined Alpha/Numeric/Date 17+20Web Service Authorization ID Service UDF defined.
BGUDF18User Defined Alpha/Numeric/Date 18+20Web Service Authorization ID Service UDF defined.
BHUDF19User Defined Alpha/Numeric/Date 19+20Web Service Authorization ID Service UDF defined.
BIUDF20User Defined Alpha/Numeric/Date 20+20Web Service Authorization ID Service UDF defined.
BJCost_CenterJob Cost CenterText10Cost Center Maintenance and Customer Code Cost Center
BKMaster_JobMaster JobText10Valid Job that does not have a complete status and phase length must match Job.
BLBill_From_MasterSubmit sub-job billings from the Master Job?Text1Y(es) or N(o) only. Defined on the Master Job only.Used in the Time+Material Module. Ignore if module is not active.
BMStandard_Phase_CategoryPhase setup categoryText10If defined then display the Phase information as setup for each field. **See Assumptions and Dependencies.Validates to the Phase Category
BNPhase_Display_CodePhase setup maskText20If blank defaults from Job Installation. If Sub-Job then defaults from Master Job. **See Assumptions and Dependencies.
BOMajor_Group_StartPhase Major group start positionNumeric2If blank defaults from Job Installation. If Sub-Job then defaults from Master Job. **See Assumptions and Dependencies.
BPMajor_Group_EndPhase Major group end positionNumeric2If blank defaults from Job Installation. If Sub-Job then defaults from Master Job. **See Assumptions and Dependencies.
BQMinor_Group_StartPhase Minor group start positionNumeric2If blank defaults from Job Installation. If Sub-Job then defaults from Master Job. **See Assumptions and Dependencies.
BRMinor_Group_EndPhase Minor group end positionNumeric2If blank defaults from Job Installation. If Sub-Job then defaults from Master Job. **See Assumptions and Dependencies.
BSStatus_CodeStatusText1(A)ctive, (I)nactive or (C)omplete. Defaults to Active if blank.

+ NOTE = the UDF (1-20) elements can be Numeric, Date or Text depending on how they are created within Spectrum.
