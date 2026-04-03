---
title: "Change Employee - Payroll Tax | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/change-employee---payroll-tax"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/change-employee---payroll-tax"
---

# Change Employee - Payroll Tax

Use this service to import Employee Payroll Tax information.
Note: In order to use this service, add EmployeePayrollTax to your Authentication ID.
The prior SOAP service (UpdateEmp_PR_Tax) is still available on the template titled Import Employee Payroll Tax – Old. While the service will remain available in the short term, we recommend that you migrate all usage to the new service.

## Connection Info for POST

URL = https://<SPECTRUM-SERVER>:8482/employee/payrolltaximports
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "employeePayrollTaxImports": [{
 "Company_Code": "2ND",
 "Employee_Code": "VS123",
 "Auto_Deposit_Allocation":"",
 "Bank_Account_Number":"",
 "Bank_Account_Type":"",
 "ABA_Number":"",
 "Auto_Deposit_Flag":"",
 "Auto_Deposit_Rate1":"",
 "Bank_Account_Number_2":"",
 "Bank_Account_Type_2":"",
 "ABA_Number_2":"",
 "Auto_Deposit_Flag_2":"",
 "Auto_Deposit_Rate2":"",
 "Bank_Account_Number_3":"",
 "Bank_Account_Type_3":"",
 "ABA_Number_3":"",
 "Auto_Deposit_Flag_3":"",
 "Auto_Deposit_Rate3":"",
 "Bank_Account_Number_4":"",
 "Bank_Account_Type_4":"",
 "ABA_Number_4":"",
 "Auto_Deposit_Flag_4":"",
 "Auto_Deposit_Rate4":"",
 "Bank_Account_Number_5":"",
 "Bank_Account_Type_5":"",
 "ABA_Number_5":"",
 "Auto_Deposit_Flag_5":"",
 "Auto_Deposit_Rate5":"",
 "Part_time_Casual_Flag":"",
 "Billing_Code":"A",
 "Special_Pay_Rate":"",
 "Special_Pay_Amount":"",
 "Misc_Allowance_Rate":"",
 "Prevail_Wage_Fringe_Rate":"",
 "Perm_wk_State_Tax_Code":"",
 "Subject_to_Perm_wk_State_Tax":"",
 "Subject_to_SDI_Perm_wk":"",
 "Subject_to_SUTA_Perm_wk":"",
 "Perm_wk_State_Filing_Status":"",
 "Perm_wk_State_Exemptions":"",
 "Perm_wk_State_Tax_Override":"10",
 "Perm_wk_State_Tax_Override_Cont":"P",
 "Res_County_Tax_Code":"BO",
 "Subject_to_Res_County_Tax":"",
 "Subject_to_FICA_Res_County":"",
 "Subject_to_FUTA_Res_County":"",
 "Res_County_Filing_Status":"",
 "Res_County_Exemptions":"",
 "Res_County_Tax_Override":"",
 "Res_County_Tax_Override_Cont":"",
 "Res_Local_Tax_Code":"WA",
 "Subject_to_Res_Local_Tax":"E",
 "Subject_to_FICA_Res_Local":"E",
 "Subject_to_FUTA_Res_Local":"E",
 "Res_Local_Filing_Status":"SINGLE",
 "Res_Local_Exemptions":"",
 "Res_Local_Tax_Override":"",
 "Res_Local_Tax_Override_Cont":"",
 "Permanent_Unemployment_State":"",
 "Permanent_SDI_State":"",
 "Apprentice_ID":"225",
 "Apprentice_Wage_Percent":"",
 "Summary_Post_Flag":"Y",
 "Suppress_Post_Flag":"Y",
 "Fed_Two_Jobs_Total": "Y",
 "Fed_Dep_Claimed_Annually": "",
 "Fed_Other_Annual_Income": "",
 "Fed_Other_Annual_Deductions": "",
 "Fed_Income_Tax_Override": "",
 "Fed_Income_Tax_Override_Cont": ""
 }]
}`
```

## Assumptions and Dependencies

- The Payroll module must be set up.

- The Employee code must exist in the defined Company code.

- The Change Employee - Payroll Tax Web Service updates an existing employee's information for the defined fields only.

- Any field that is left blank will not be updated in Spectrum.

- The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- The Auto deposit rates must equal 100% if the Auto Deposit Allocation Method is defined as Percent. Therefore if any changes are made, all accounts must be defined in the Employee-Payroll Tax Information Web Service.

- The Primary Account must be active (Y) if any other accounts have an active status. Therefore the Auto_Deposit_Flag field must be defined as Y in order for the other accounts to be updated.

- The Tax code must be unique between the Resident state, Perm work state, Resident county, and Resident local.

- The Permanent_Unemployment_State defined tax code is the permanent override for the Resident and Work State unemployment calculation.

- The defined tax code can be the same as the Resident state, Perm work state, Resident county, or Resident local.

- If it is defined, then the Permanently override resident and work state unemployment checkbox will be selected.

- The Permanent_SDI_State defined tax code is the permanent override for the Resident and Work State disability calculation.

- If it is defined, then the Permanently override resident and work state disability insurance (SDI) checkbox will be selected.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
ExcelElement NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
BCompany_CodeCompany CodeYESText3Valid Company in Spectrum
CEmployee_CodeEmployee CodeYESText11Unique Identifier / No commas.Employee Code must exist in the defined Company Code
DAuto_Deposit_AllocationAuto-Deposit Allocation MethodText1(P)ercent or (F)ixed amount onlyIf Percent is defined then all Account Rates must total 100%.
EBank_Account_NumberPrimary Auto-Deposit Acct #Text17
FBank_Account_TypePrimary Auto-Deposit Acct TypeText1(C)hecking or (S)avings only
GABA_NumberPrimary Auto-Deposit Acct ABA #Text9
HAuto_Deposit_FlagPrimary Auto-Deposit Acct StatusText1(Y)es; (N)o or (P)re-notification onlyThe Primary Account must be active if any other accounts have an active status.
IAuto_Deposit_Rate1Primary Auto-Deposit Acct RateNumeric8If multiple Accounts exist then all Accounts must be defined to make changes.If Percent is defined in field name Auto_Deposit_Allocation then all Account Rates must total 100%.
JBank_Account_Number_2Second Auto-Deposit AcctText17
KBank_Account_Type_2Second Auto-Deposit Acct TypeText1(C)hecking or (S)avings only
LABA_Number_2Second Auto-Deposit Acct ABA #Text9
MAuto_Deposit_Flag_2Second Auto-Deposit Acct StatusText1(Y)es; (N)o or (P)re-notification onlyThe Primary Account must be active if any other accounts have an active status.
NAuto_Deposit_Rate2Second Auto-Deposit Acct RateNumeric8If multiple Accounts exist then all Accounts must be defined to make changes.If Percent is defined in field name Auto_Deposit_Allocation then all Account Rates must total 100%.
OBank_Account_Number_3Third Auto-Deposit AcctText17
PBank_Account_Type_3Third Auto-Deposit Acct TypeText1(C)hecking or (S)avings only
QABA_Number_3Third Auto-Deposit Acct ABA #Text9
RAuto_Deposit_Flag_3Third Auto-Deposit Acct StatusText1(Y)es; (N)o or (P)re-notification onlyThe Primary Account must be active if any other accounts have an active status.
SAuto_Deposit_Rate3Third Auto-Deposit Acct RateNumeric8If multiple Accounts exist then all Accounts must be defined to make changes.If Percent is defined in field name Auto_Deposit_Allocation then all Account Rates must total 100%.
TBank_Account_Number_4Fourth Auto-Deposit AcctText17
UBank_Account_Type_4Fourth Auto-Deposit Acct TypeText1(C)hecking or (S)avings only
VABA_Number_4Fourth Auto-Deposit Acct ABA #Text9
WAuto_Deposit_Flag_4Fourth Auto-Deposit Acct StatusText1(Y)es; (N)o or (P)re-notification onlyThe Primary Account must be active if any other accounts have an active status.
XAuto_Deposit_Rate4Fourth Auto-Deposit Acct RateNumeric8If multiple Accounts exist then all Accounts must be defined to make changes.If Percent is defined in field name Auto_Deposit_Allocation then all Account Rates must total 100%.
YBank_Account_Number_5Fifth Auto-Deposit AcctText17
ZBank_Account_Type_5Fifth Auto-Deposit Acct TypeText1(C)hecking or (S)avings only
AAABA_Number_5Fifth Auto-Deposit Acct ABA #Text9
ABAuto_Deposit_Flag_5Fifth Auto-Deposit Acct StatusText1(Y)es; (N)o or (P)re-notification onlyThe Primary Account must be active if any other accounts have an active status.
ACAuto_Deposit_Rate5Fifth Auto-Deposit Acct RateNumeric8If multiple Accounts exist then all Accounts must be defined to make changes.If Percent is defined in field name Auto_Deposit_Allocation then all Account Rates must total 100%.
ADPart_time_Casual_FlagPart-Time?Text1(Y)es or (N)o only (if left blank; this flag will default to 'no' in Spectrum). This is an option to exclude the Employee from Automatic Pay Cycle.
AEBilling_CodeT&M Billing CodeText10T&M Billing Code Maintenance
AFSpecial_Pay_RateSpecial Pay RateNumeric7Positive number only.
AGSpecial_Pay_AmountSpecial Pay AmountNumeric7Positive number only.
AHMisc_Allowance_RateMisc Allow AmountNumeric7Positive number only.
AIPrevail_Wage_Fringe_RatePrevailing Wage Fringe Employer BenefitNumeric7Positive number only.
AJPerm_wk_State_Tax_CodePerm Work State Tax Table CodeText10The Tax code must be unique between the Resident State, Perm Work State, Resident County and Resident Local.Payroll Tax Table Maintenance
AKSubject_to_Perm_wk_State_TaxSubject to Perm Work State Income TaxText1(E)xempt or (T)axable only. Required if field name Perm_wk_State_Tax_Code is not blank.
ALSubject_to_SDI_Perm_wkSubject to Perm Work State SDIText1(E)xempt or (T)axable only. Required if field name Perm_wk_State_Tax_Code is not blank.
AMSubject_to_SUTA_Perm_wkSubject to Perm Work State UnemploymentText1(E)xempt or (T)axable only. Required if field name Perm_wk_State_Tax_Code is not blank.
ANPerm_wk_State_Filing_StatusPerm Work State Filing StatusText20If Subject_to_Perm_wk_State_Tax = T then this field is required.Payroll Tax Table Maintenance
AOPerm_wk_State_Exemptions# Exemptions for Perm Work State Income TaxNumeric5
APPerm_wk_State_Tax_OverrideAmount of Perm Work State Income Tax OverrideNumeric7
AQPerm_wk_State_Tax_Override_ContPerm Work State Income Tax OverrideText1(F)ixed; (P)ercent; (A)dd-on only
ARRes_County_Tax_CodeResident County Tax Table CodeText10The Tax code must be unique between the Resident State, Perm Work State, Resident County and Resident Local.Payroll Tax Table Maintenance
ASSubject_to_Res_County_TaxSubject to Resident County Income TaxText1(E)xempt or (T)axable only. Required if field name Res_County_Tax_Code is not blank.
ATSubject_to_FICA_Res_CountySubject to Resident County FICAText1(E)xempt or (T)axable only. Required if field name Res_County_Tax_Code is not blank.
AUSubject_to_FUTA_Res_CountySubject to Resident County UnemploymentText1(E)xempt or (T)axable only. Required if field name Res_County_Tax_Code is not blank.
AVRes_County_Filing_StatusResident County Filing StatusText20If Subject_to_Res_County_Tax = T then this field is required.Payroll Tax Table Maintenance
AWRes_County_Exemptions# Exemptions for Resident County Income TaxNumeric5
AXRes_County_Tax_OverrideAmount of Resident County Income Tax OverrideNumeric7
AYRes_County_Tax_Override_ContResident County Income Tax Override ControlText1(F)ixed; (P)ercent; (A)dd-on only
AZRes_Local_Tax_CodeResident Local Tax Table CodeText10The Tax code must be unique between the Resident State, Perm Work State, Resident County and Resident Local.Payroll Tax Table Maintenance
BASubject_to_Res_Local_TaxSubject to Resident Local Income TaxText1(E)xempt or (T)axable only. Required if field name Res_Local_Tax_Code is not blank.
BBSubject_to_FICA_Res_LocalSubject to Resident Local FICAText1(E)xempt or (T)axable only. Required if field name Res_Local_Tax_Code is not blank.
BCSubject_to_FUTA_Res_LocalSubject to Resident Local UnemploymentText1(E)xempt or (T)axable only. Required if field name Res_Local_Tax_Code is not blank.
BDRes_Local_Filing_StatusResident Local Filing StatusText20If Subject_to_Res_Local_Tax = T then this field is required Payroll Tax Table Maintenance
BERes_Local_Exemptions# Exemptions for Resident Local Income TaxNumeric5
BFRes_Local_Tax_OverrideAmount of Resident Local Income Tax OverrideNumeric7
BGRes_Local_Tax_Override_ContResident Local Income Tax Override ControlText1(F)ixed; (P)ercent; or (A)dd-on only
BHPermanent_Unemployment_StateUnemployment state (Permanent Override for resident and work state)Text10This Tax code can be the same as a Resident State, Perm Work State, Resident County or the Resident Local.Payroll Tax Table Maintenance
BIPermanent_SDI_StateDisability insurance state (Permanent Override for resident and work state)Text10Payroll Tax Table Maintenance
BJApprentice_IDApprentice program ID #Text20
BKApprentice_Wage_PercentWage %Numeric6Format = xxx.xx Positive numbers only and cannot exceed 100. If defined then Apprenctice_ID is required.
BLSummary_Post_FlagPost in summary to job and equipment history (confidential employee)?Text1(Y)es or (N)o only. If left blank then defaults to N. Field is not available in a Confidential Payroll Company.
BMSuppress_Post_FlagAlso suppress employee's hours in job and equipment history Text1Summary_Post_Flag must = Y in order to define. (Y)es or (N)o only. If left blank then defaults to N. Field is not available in a Confidential Payroll Company.
BNFed_Two_Jobs_TotalTwo jobs in total?Text1(Y)es = Selected, Blank or (N)o = Not selected
BOFed_Dep_Claimed_AnnuallyDependents claimed annuallyNumeric6.2
BPFed_Other_Annual_IncomeOther annual incomeNumeric6.2
BQFed_Other_Annual_DeductionsOther annual deductionsNumeric6.2
BRFed_Income_Tax_OverrideFederal income tax overrideNumeric4.2
BSFed_Income_Tax_Override_ContFederal income tax override controlText1(F)ixed, (P)ercent, (A)dd-on only
