---
title: "Change Employee - Required Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/change-employee---required-update"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/change-employee---required-update"
---

# Change Employee - Required Update

Use this service to update an existing employee's information for the defined fields only.
Note: In order to use the new service, add UpdateEmployeeRequiredFields to your Authentication ID.

## Connection Info for POST

URL = https://<SPECTRUM-SERVER>:8482/employee/updateRequiredFields
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "employeeRequiredImports": [{
 "Company_Code": "2nd",
 "Employee_Code": "JWALTER",
 "Alpha_Sort":"JW",
 "First_Name":"James",
 "Middle_Name":"W",
 "Last_Name":"Walter",
 "Employee_Suffix":"DDS",
 "Worker_Comp_Code":"0101",
 "Department_Code":"DA",
 "Employment_Status":"a",
 "Termination_Date_List3":"",
 "Pay_Type":"h",
 "Pay_Frequency_Flag":"W",
 "Hourly_Rate":100.00,
 "Salary_Amount":"",
 "Standard_Work_Hours":"40",
 "Emp_Foreign":"N",
 "Fed_Tax_Code":"US",
 "Subject_to_Fed_Tax":"T",
 "Subject_to_FICA_Fed":"T",
 "Subject_to_FUTA_Fed":"T",
 "Fed_Filing_Status":"SINGLE ",
 "Fed_Exemptions":"99",
 "Fed_Tax_Override":"666.66",
 "Fed_Tax_Override_Cont":"F",
 "State_Tax_Code":"AZ",
 "Subject_to_State_Tax":"T",
 "Subject_to_SDI_State":"E",
 "Subject_to_SUTA_State":"T",
 "State_Filing_Status":"Married",
 "State_Exemptions":"98",
 "State_Tax_Override":"2.5",
 "State_Tax_Override_Cont":"p",
 "Cost_Center":"101",
 "Employee_Termination_Reason":"",
 "Employee_Rehire_Rating":"10",
 "Occupation":"",
 "Trade":"",
 "Perm_Work_Comp":"Y",
 "Pref_Status":"",
 "Employee_Telephone_Memo":"Cell phone",
 "Employee_Driver_License_State":"AZ",
 "Employee_Driver_License_Class":"",
 "Employee_Citizenship":"US",
 "Employee_Security_Stat":"Secure employee",
 "Employee_Veteran_Stat":"",
 "Employee_New_Vet":"Y",
 "Employee_Disabled":"",
 "Employee_Disabled_Note":"PTSD",
 "Employee_Place_Birth":"Hospital",
 "Effective_Date":"01/01/2026",
 "Comments":"",
 "Last_Job_Company":"ABC",
 "Last_Job_Number":"1D",
 "Last_Equipment_Company":"ABC",
 "Last_Equipment_Code":"",
 "Hire_Date_List1":"12/31/2019",
 "Rehire_Date_List2":"",
 "Legal_First_Name":"JAMES II",
 "Legal_Middle_Name":"W",
 "Legal_Last_Name":"Walter",
 "Legal_Suffix":"DDS"
 }]
}`
```

## Underlying File Maintenance

Prior to importing Employee-Required Update information, the following file maintenance areas must be completed:

- System Administration > Installation > Payroll

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Payroll > Employee Maintenance

- System Administration > Installation > Payroll > Tax Table Maintenance

- System Administration > Installation > Payroll > Department Expense Maintenance

- System Administration > Installation > Payroll > Employee Status Code Maintenance

- System Administration > Installation > Payroll > Supervisor Code Maintenance

- System Administration > Installation > Payroll > Worker's Compensation Code Maintenance

- System Administration > Installation > Payroll > Hours Bank Code Maintenance

- System Administration > Installation > Payroll > Union File Maintenance

- System Administration > Installation > Payroll > Wage Code File Maintenance

- System Administration > Installation > Payroll > EEO Classification Maintenance

- System Administration > Installation > Payroll > Occupation Maintenance

- System Administration > Installation > Payroll > Trade Maintenance

- System Administration > Installation > Payroll > Employee User-Defined Fields Maintenance

- System Administration > Installation > Time + Material > Labor Billing Rates Maintenance

- System Administration > Installation > Human Resources > Locations Maintenance

- System Administration > Installation > Human Resources > License Class Maintenance

- System Administration > Installation > Job Cost > Job Maintenance

- System Administration > Installation > Equipment Control > Equipment Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The Payroll module must be set up.

- The Employee code must exist in the defined Company code.

- To change an Employee's pay rate the following fields are dependent on each other.

- These fields are required

- Pay_Type

- Pay_Frequency_Flag

- Standard_Work_Hours

- Effective_Date

- These two fields are required also but are subject to the defined Pay_Type. Therefore based on the defined Pay_Type, it will then make one of these fields required

- Hourly_RateImportant: If the employee's Pay Type is set to Hourly, and if the Hourly Rate field is blank, the API will return an error. Rather than leave the field blank, enter 0.00.

- Salary_Amount

- If the Fed_Tax_Code field is defined, these fields are required.

- Subject_to_Fed_Tax

- Subject_to_FICA_Fed

- Subject_to_FUTA_Fed

- Fed_Filling_Status

- If the State_Tax_Code field is defined, these fields are required.

- Subject_to_State_Tax

- Subject_to_SID_State

- Subject_to_SUTA_State

- State _Filling_Status

- The Employee status can be modified using this web service therefore we recommend the user defines the appropriate hire, rehire, and termination dates.

- The Employee-Required Update Web Service updates an existing employee's information for the defined fields only.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- The Employee contact is updated based on the fields associated with the Employee Contact record.

- Cost center information will only be allowed if the Company is set to a Pending or Yes status.

## Field Descriptions

Use this table as a reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
ExcelElement NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
BCompany_CodeCompany CodeText3Valid Company in Spectrum
CEmployee_CodeEmployee CodeYESText11Unique Identifier / No commasUPPERCASE FORMAT-NO SYMBOLS
DAlpha_SortAlpha ReferenceText8
EFirst_NameEmployee First NameText20No commas
FMiddle_NameEmployee Middle NameText20No commas
GLast_NameEmployee Last NameText30No commas
HEmployee_SuffixEmployee name SuffixText3No commas
IWorker_Comp_CodeWorker's Comp CodeText6Worker's Compensation Code Maintenance
JDepartment_CodeDepartment CodeText6Department Expense Maintenance
KEmployment_StatusEmployee StatusText1Employee Status Code Maintenance
LTermination_Date_List3Latest Termination DateDate10Enter as: MM/DD/CCYY (for example, 01/05/1982)Required if Employee Status = 'T' or 'D'
MPay_TypePay TypeText1(C)ommission; (H)ourly; (O)vertime or (S)alary onlyIf (H)ourly is selected, Hourly_Rate is required and Salary_Amount is ignored.Important: Rather than leave the field blank, enter 0.00.

If (S)alary is selected, Salary_Amount is required and Hourly_ Rate is ignored.

NPay_Frequency_FlagPay FrequencyText1(D)aily; (W)eekly; (B)I-weekly; (M)onthly; (S)emi-monthly; (Q)uarterly or (A)nnual only
OHourly_RateHourly RateNumeric6Positive number only. Format = 3.4Required if Pay_Type = HImportant: Rather than leave the field blank, enter 0.00.

PSalary_AmountSalary Amount for ONE PAY PERIOD ONLYNumeric13Enter Amount for ONE PAY PERIOD ONLY!
Required if Pay_Type = S, O or C

QStandard_Work_HoursStandard Hours per Pay PeriodNumeric8Positive number only. Format = 4.2Required if Pay_Frequency_Flag = D; if blank, calculated by Spectrum.
REmp_ForeignForeign Employee?Text1(Y)es or (N)o onlyIf Payroll Installation option is selected to allow non-US payroll processing then ignore this field which is hidden.
SFed_Tax_CodeFederal Tax Table CodeText10Default to US if Payroll Installation option is not selected. Use default if defined and valid. Can be overridden. If Emp_Foriegn = N then Spectrum defaults this field to US.Payroll Tax Table Maintenance
TSubject_to_Fed_TaxSubject to Federal Income TaxText1(E)xempt or (T)axable only. If Emp_Foriegn = N then Spectrum defaults this field to T(axable).
USubject_to_FICA_FedSubject to FICAText1(E)xempt or (T)axable only. If Emp_Foriegn = N then Spectrum default this field to T(axable).
VSubject_to_FUTA_FedSubject to Federal UnemploymentText1(E)xempt or (T)axable only. If Emp_Foriegn = N then Spectrum default this field to T(axable).
WFed_Filing_StatusFederal Filing StatusText20If Subject_to_Fed_Tax = T then this field is required.Payroll Tax Table Maintenance
XFed_Exemptions# Exemptions for Federal Income TaxNumeric5
YFed_Tax_OverrideAmount of Federal Income Tax OverrideNumeric7Positive number only.
ZFed_Tax_Override_ContFederal Income Tax Override ControlText1(F)ixed; (P)ercent; (A)dd-on only
AAState_Tax_CodeResident State Tax Table CodeText10The Tax code must be unique between the Federal, Resident State, Perm Work State, Resident County and Resident Local.Payroll Tax Table Maintenance
ABSubject_to_State_TaxSubject to State Income TaxText1(E)xempt or (T)axable only. Required if field name State_Tax_Code is not blank.
ACSubject_to_SDI_StateSubject to State SDIText1(E)xempt or (T)axable only. Required if field name State_Tax_Code is not blank.
ADSubject_to_SUTA_StateSubject to State UnemploymentText1(E)xempt or (T)axable only. Required if field name State_Tax_Code is not blank.
AEState_Filing_StatusState Filing StatusText20If Subject_to_State_Tax = T then this field is required.Payroll Tax Table Maintenance
AFState_Exemptions# Exemptions for State Income TaxNumeric5
AGState_Tax_OverrideAmount of State Income Tax OverrideNumeric7Positive number only.
AHState_Tax_Override_ContState Income Tax OverrideText1(F)ixed; (P)ercent; (A)dd-on only
AICost_CenterEmployee Cost CenterText10Cost Center Maintenance
AJEmployee_Termination_ReasonTermination ReasonText30
AKEmployee_Rehire_RatingRehire rating (0-10)Numeric2
ALOccupationOccupationText50Occupation File Maintenance
AMTradeTradeText50Trade File Maintenance
ANPerm_Work_CompAlways use this worker's compensation code on time card?Text1(Y)es or (N)o only
AOPref_StatusHealth Coverage statusText3(HCF)=Full Time, (HCP)=Part time or (VAR)=Variable Hours. Defaults to Unassigned if left blank.
APEmployee_Telephone_MemoTelephone MemoText30
AQEmployee_Driver_License_StateDriver's License StateText22 character postal abbreviation
AREmployee_Driver_License_ClassDriver's License ClassText9Data entry field if HR module not installed.Human Resources License Class if HR Module installed.
ASEmployee_CitizenshipCitizenshipText30
ATEmployee_Security_StatSecurity StatusText30
AUEmployee_Veteran_StatVeteran StatusText1(D)=Disabled Veteran
(A)=Armed Forces Service Medal Veteran
(M)= Disabled Armed Forces
(O)=Other Protected Veteran
(P)=Disabled Other Protected Veteran
(N)=Non-Veteran

AVEmployee_New_VetRecently Separated Veteran?Text1(Y)es or (N)o only
AWEmployee_DisabledDisabled?Text1(Y)es or (N)o only
AXEmployee_Disabled_NoteDisabled DescriptionText30Available when Disabled? Is yes. Otherwise ignore.
AYEmployee_Place_BirthPlace of BirthText30
AZEffective_DatePay Effective DateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010). No duplicate dates may exist. Required if Hourly_Rate or Salary_Amount is defined.Used to define the effective date for a Pay Rate change on the Employee Master. **See Assumption and Dependency's for Rules.
BACommentsPay Rate Revision CommentText40For Pay Rate Changes only. Ignore date if Effective_Date is not defined.
BBLast_Job_CompanyCompany code for Last Job worked onText3If left blank and Last_Job_Number is defined then use Company_Code.Valid Company in Spectrum
BCLast_Job_NumberLast Job worked onText10Valid Job in Company defined
BDLast_Equipment_CompanyCompany code for Last Equipment worked onText3If left blank and Last_Equipment_Code is defined then use Company_Code.Valid Company in Spectrum
BELast_Equipment_CodeLast Equipment worked onText10Valid Equipment code in Company defined
BFHire_Date_List1Original hire dateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
BGRehire_Date_List2Latest rehire dateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
BHLegal_First_NameEmployee's Legal First NameText50No commas
BILegal_Middle_NameEmployee's Legal Middle NameText50No commas
BJLegal_Last_NameEmployee's Legal Last NameText50No commas
BKLegal_SuffixEmployee's Legal SuffixText3
