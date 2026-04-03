---
title: "Update Job | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/update-job"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/update-job"
---

# Update Job

Use this service to update any existing data for the defined job.
WSDL: UpdateJob.jws
Method: UpdateJob

## Underlying File Maintenance

Prior to importing Job-Update information, these maintenance areas in System Administration > Installation must be completed.

- Job Cost

- General Ledger > G/L Master File Maintenance

- General Ledger > Departments

- Accounts Payable > Routing Code Maintenance

- Accounts Receivable > Customers

- Accounts Receivable > Sales Tax Code Maintenance

- Accounts Receivable > Unit of Measure File Maintenance

- Job Cost > Job Maintenance

- Job Cost > Phase Maintenance

- Job Cost > Cost Type Maintenance

- Job Cost > Tax Classification File Maintenance

- Job Cost > Phase Categories Maintenance

- Job Cost > Job User-Defined Fields Maintenance

- Payroll > Employee Maintenance

- Payroll > Tax Table Maintenance

- Payroll > Worker's Compensation Code Maintenance

- Work Order > Site File Maintenance

- Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The Job Master Update web service will update any existing data for the defined Job.

- The Job Master cost center flag is validated against the customer cost center.

- The Job Master Update does not modify existing AR Contracts for the Job.

- It creates new AR Contract for the Job if the Customer_Code is defined. It will use the Original_Amount field as well if defined but it is not required to create the AR Contract.

- If the AR Contract exists then a message is provided that it cannot be changed. The user will have to manually change the information on the Contract itself via Accounts Receivable.

- A new Contract is set up when a NEW Customer code and Original_Contract is defined in the layout.

- An existing Contract will not be update if the Customer code and Original_Contract is defined. This is an Accounts Receivable function not a Job function.

- The T+M Billing setup occurs when the Price_Method_Code is defined as Cost Plus or Time+Material and the Customer code is defined.

- The Report_Calc_Override field controls the 'Override Calculation for the contract status and profitability reports?' option. If defined as Y then one of the following fields needs to be defined

- Entered_Perecent_Complete

- Entered_Projected_Complete

- The Override Payroll work tax codes must be unique for each of the three defined.

- The earned calculation logic is based on the Price type defined on the Job.

- Phase mask, start/end major group and start/end minor group default from the Job Installation screen if fields are blank.

- Master Job logic

- The Master Job tied to the Sub Job must be valid and not have a complete status.

- The Master Job and Sub Job must have the same Phase length.

- The Sub Job will be created with the same Phase setup as the Master Job.

- The Sub Job will default the Master Job's Customer and Tax classification if left blank.

- The T+M billing submitted by each Sub Job option is selected on the Master Job and defaults to unselected unless a Sub Job defines the Bill_From_Master field option. The last created Sub Job controls this feature on the Master Job.

- The Job Setup page has an option to setup the Default Job Address used on the Purchase Orders. The 'Ship-to name' must be defined in order to modify the other fields such as address information and/or comments as needed.

- The Job cannot have both the Davis-Bacon and Prevailing wage options selected.

- The Estimated and Actual complete dates must be greater than or equal to the Estimated and Actual start dates.

- The Key personnel display as Job contacts if the Job Cost Installation option validates to the Employee code.

- The PR_OH_Type_Code field

- The following fields are not dependent on the PR_OH_Type Code field being defined -

- Payroll_OH_Percent

- PR_OH_Amount

- OH_Phase

- OH_Cost_Type

- If any of the above fields are populated they will be updated if they meet the PR_OH_Type_Code current setting.

- If the PR_OH_Type_Code field is defined as (N)one then it will ignore the above four fields.

- Cost center information will only be allowed in if the Company is set to a Pending or Yes status.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

## Field Descriptions

 Use the table below for reference when using this service. Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
ExcelElement NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
BCompany_CodeCompany CodeYESText3Valid Company in Spectrum. If blank, defaults from Authorization ID.
CJob_NumberJob NumberYESText10No duplicates
DJob_DescriptionJob Name25
EDivisionDivision NumberNumeric5Required if Job Cost installation option is selected.
FAddress_1Address Line 1Text30
GAddress_2Address Line 230
HCityCity25
IStateState22-digit postal abbreviation
JZip_CodeZip Code10
KPhonePhone number14One of these formats:

- (123) 456-7890

- 123-456-8970

- 456-7890

- 1234567890

LFax_PhoneFax Number
MJob_Site_PhoneJob Site Phone Number
NSuperintendentSuperintendentText15Employee Code if installation screen selected.
OEstimatorEstimator
PProject_ManagerProject Manager
QCustomer_CodeCustomer CodeText10**See Assumptions and Dependencies.Customer Maintenance File
RContract_NumberContract Number30
SJob_TypeContract Type10
TTax_Class_CodeTax classification -Use Tax Code or A/R Sales Tax Code.Text15Required based on the Job Cost installation settings.JC Tax Classification Maintenance file. If JC install screen is set to 'Y' for Use Tax Classification. Or to A/R Sales Tax Maintenance File if Use Tax Classification flag is 'N'.
UTaxable_FlagTaxable Flag1Y(es) or N(o) only.
VTotal_UnitsJob UnitsNumeric9Positive numbers only.
WUnit_of_MeasureUnit of MeasureText5Units of Measure Maintenance File
XCertified_FlagCertified FlagText1Y(es) or N(o) only.
YWork_Comp_CodeWorker's Compensation CodeText6Workers' Compensation Code Maintenance File
ZWage_Rate_LevelWage Rate LevelNumeric1Numbers 1-9 only
AAPrice_Method_CodePrice Type CodeText1(F)ixed Price, (T)ime & Material, (C)ost Plus, or (U)nit Price
ABEst_Start_DateEstimated Start DateDate10Text format for import MM/DD/CCYY
ACEst_Complete_DateEstimated Complete Date
ADStart_DateActual Start Date
AEComplete_DateActual Complete DateIf Status_Code is Completed and this field is blank, the default value is the Job Cost processing date.
AFWork_State_Tax_CodeWork State Tax CodeText10The Work Tax codes must be unique.Tax Table Maintenance
AGWork_County_Tax_CodeWork County Tax Code
AHWork_Local_Tax_CodeWork Local Tax Code
AIOriginal_ContractOriginal Contract AmountNumeric14No change to Schedule of Values. **See Assumptions and Dependencies.
AJWO_SiteWork Order SiteText10Work Order Site Maintenance File
AKLatitudeLatitudeNumeric11Format for import - XXX.XXXXXX.
ALLongitudeLongitude
AMTrack_Davis_BaconDavis-Bacon JobText1Y(es) or N(o) only.
ANTrack_Prevailing_WagePrevailing Wage Job and optionY=Prevailing Wage, F=Regular wages include non-stated Fringes OR N=Not Prevailing Wage only
AOCreate_DateJob Create DateDate10Text format for import MM/DD/CCYY. If left blank it will use the date it was imported.
APCost_CenterJob Cost CenterText10Cost Center Maintenance and Customer Code Cost Center
AQMaster_JobMaster JobText10Valid Job that does not have a complete status. Master Job must have the same Phase length as Job.
ARBill_From_MasterSubmit sub-job billings from the Master Job?Text1Y(es) or N(o) only. Defined on the Master Job only.Used in the Time+Material Module. Ignore if module is not active.
ASStandard_Phase_CategoryPhase setup categoryText10If defined, displays the Phase information as setup for each field. **See Assumptions and Dependencies.Validates to the Phase Category
ATPhase_Display_CodePhase setup mask20If blank, defaults from Job Installation. If Sub-Job, defaults from Master Job. **See Assumptions and Dependencies..
AUMajor_Group_StartPhase Major group start positionNumeric2
AVMajor_Group_EndPhase Major group end position
AWMinor_Group_StartPhase Minor group start position
AXMinor_Group_EndPhase Minor group end position
AYStatus_CodeStatusText1(A)ctive, (I)nactive or (C)omplete. Default is A.
AZOwner_NameOwner nameText50
BACommentCommentText125
BBReports_Calc_OverrideOverride calculation for contract status and profitability reports?Text1Y(es) or N(o) only.
BCEntered_Percent_Complete% complete - OverrideNumeric5Format xxx.x Positive only. Field works with the Projected Cost Amount Override. **See Assumptions and Dependencies.
BDEntered_Projected_CostProjected Cost - OverrideNumeric14Format -10.2 Field works with the Percent Complete Override. **See Assumptions and Dependencies.
BELegal_DescLegal descriptionText350
BFJob_Oh_Batch_CodeJob overhead batchText10
BGRouting_Code1A/P invoice approval default routing codeText10Routing Code
BHRouting_LimitA/P invoice approval invoice dollar limitNumeric13Positive numbers only.
BIRouting_Code2A/P invoice approval routing code if overlimitText10Routing Code
BJPO_Ship_NameOverride job address on PO- Ship-to nameText30If defined, creates a new Job PO Ship-to address for the Job if it doesn't exist. If the Job has a defined PO Ship-to address, it modifies the information. Required if a PO_Ship_Name does not exist in Spectrum.
BKPO_Ship_Address1Override job address on PO- Ship-to address 1**See Assumptions and Dependencies.
BLPO_Ship_Address2Override job address on PO- Ship-to address 2
BMPO_Ship_CityOverride job address on PO- Ship-to city25
BNPO_Ship_StateOverride job address on PO- Ship-to state22 digit postal abbreviation. **See Assumptions and Dependencies.
BOPO_Ship_Zip_CodeOverride job address on PO- Ship-to zip code10**See Assumptions and Dependencies.
BPPO_Ship_CountryOverride job address on PO- Ship-to country25
BQPO_Ship_CommentOverride job address on PO- Ship-to address comment250
BREarned_Calc_TypeEarned revenue calculationText1(P)ercent, (B)illed, (C)ost, or (M)aster job calculation.
BSUnder_BilledUnbilled AmountNumeric12Used with the 'Billed' Earned_Calc_Type only. Otherwise ignore. Negative numbers allowed. Format = -xxxxxxxx.xx
BTCost_Markup_PercentCost %Numeric5Used with the 'Cost' Earned_Calc_Type only. Otherwise ignore. Positive number only and format = xxx.x
BUJob_Pay_When_PaidPay A/P invoice on this Job based on customer payment?Text1Y(es) or N(o) only.
BVJob_Auto_Release_PercentPercentage of non-retention portion of customer billing is paid for auto-releaseNumeric5Cannot be zero. Positive number only and format = xxx.x or xx.xx
BWJob_Review_PercentPercentage of non-retention portion of customer billing is paid to flag for review
BXAuto_Ot_FlagApply Federal rules for auto-overtime?Text1Y(es) or N(o) only.
BYCertified_Project_IDCertified Payroll IDText50
BZBurden_FlagPost actual burden to job?Text1Y(es) or N(o) only.
CAPre_TC_Burden_PercentPayroll burden percentageNumeric5Cannot be zero. Positive number only and format = xxx.x or xx.xx
CBBurden_PhasePayroll burden phaseText20Phase
CCBurden_Cost_TypePayroll burden cost typeText3Cost type
CDPR_OH_Type_CodePayroll overhead typeText1(N)one, (P)ercent or (A)mount/Hour **See Assumptions and Dependencies.
CEPayroll_OH_PercentPayroll overhead percentNumeric5Cannot be zero. Positive number only and format = xxx.x **See Assumptions and Dependencies.
CFPR_OH_AmountPayroll overhead rate
CGOH_PhasePayroll overhead phaseText20**See Assumptions and Dependencies.
CHOH_Cost_TypePayroll overhead cost typeText3Cost type
CILock_Revenue_EntryDisallow revenue entry?Text1Y(es) or N(o) only. Only used for Jobs with a complete job status.
CJCertified_Week_TypeCertified Week numberingText1(F)-From first time card date, (W)=work weeks only, or (C) =calender year (starting 01/01).
CKOverride_By_JobAuto-overtime for this Job?Text1Y(es) or N(o) only.Must be Y to set Auto-overtime rules.
CLDaily_OT_StartDaily overtime starts at ?Numeric5Positive numbers only. Format = 2.2 Cannot exceed 24 hours.If Override_By_Job is Y and field is blank, defaults to 8.
CMWeekly_OT_StartWeekly overtime starts at ?Numeric6Positive numbers only. Format = 3.2 Cannot exceed 168 hours.If Override_By_Job is Y and field is blank, defaults to 40.
CNSaturday_OTSaturday overtimeText1(S)ame rules as weekday, set all hours to (O)vertime, or set all hours to (D)oubletime.If Override_By_Job is Y and field is blank, defaults to S.
COSunday_OTSunday overtimeIf Override_By_Job is Y and field is blank, defaults to S.
