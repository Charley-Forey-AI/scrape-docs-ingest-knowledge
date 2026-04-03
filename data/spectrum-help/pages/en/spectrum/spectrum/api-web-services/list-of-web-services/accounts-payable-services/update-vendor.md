---
title: "Update Vendor | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/update-vendor"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/update-vendor"
---

# Update Vendor

Use this service to update an existing Vendor's information for the defined fields only.
WSDL: UpdateVendor.jws
Method: UpdateVendor
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

 Prior to importing Vendor information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Payable

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Accounts Payable > Vendor

- System Administration > Installation > Accounts Payable > Use Tax Codes

- System Administration > Installation > Accounts Payable > Invoice Approval Routing Maintenance

- System Administration > Installation > Multi-Currency > Currency Code

- System Administration > Installation > Cash Management > Accounts

## Assumptions and Dependencies.

In the table below, cells with ** are meant to refer you to this section.

- The Vendor code must exist in the defined Company code.

- The Vendor-Update Web Service updates an existing Vendor's information for the defined fields only.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- The System Administration > Installation > Payroll > Properties Tab Payroll reporting field controls the fields displayed on the Year End Reporting Page for the Vendor Master.

- The Web Service contains fields for both the US 1099 and the Canadian T5018.

- If data is defined in a field that is not supported based on the Payroll reporting option, then it will be ignored.

- United States 1099 fields

- The Fed_1099_Indicator will defaults to 7 if the field is blank and the Send_1099_Flag is set to Y.

- If the Send_1099_Flag is blank or N and the Fed_1099_Indicator, Social_Sec_Number and/or the Fed_Id_Number are defined they will be added to the Vendor.

- The Social_Sec_Number and Fed_Id_Number cannot be populated at the same time. Each Vendor can only contain one of those two fields.

- If the Send_1099_Flag is set to Y, it is highly recommended that you include either the social security number or the Federal Tax ID number, along with the 1099 indicator (7 is non-employee compensation).

- Canadian T5018 fields

- The Social_Insurance_Number and Recipient_Account_Number cannot be populated at the same time. Each Vendor can only contain one of those two fields and are available to each Recipient Type defined.

- The Recipient_Type_Code defined controls specific fields that are available and may be required.

- Type = 1 (Individual)

- Individual_First_Name and Individual_Last_Name are required.

- Partnership_Filer_ID_Number and Alternate_T5018_Name are not available.

- Type = 3 (Corporation)

- Partnership_Filer_ID_Number , Individual_First_Name, Individual_Middle_initial and Individual_Last_Name are not available.

- Type = 4 (Partnership)

- Partnership_Filer_ID_Number is required.

- Individual_First_Name, Individual_Middle_initial, and Individual_Last_Name are not available.

- Define the Payment Method (Vendor_Status) on the Payment Setup page of the Vendor Master.

- If the payment option is any of (P)rint Check, (S)end electronic pre-note, or (E)lectronic payment options, the Payment Setup page also requires entries in these fields:

- Checking Account Code

- Account Type

- ABA Number

- If the payment option is (V)ePayments, the Vendor Main Properties page requires entries in these fields:

- Address 1

- City

- State/Province

- Postal Code

- Account reference

- The combined value of the Distribution % fields must equal 100%. For each G/L Account defined, a corresponding Distribution % must exist.

- This Web Service will ignore the defined Workflow process in Spectrum.

- The Authorized ID must have the user-defined fields defined, or mapped for this Web Service.

## Field Descriptions

 Use the table below for reference when using this service. Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
ExcelElement NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36See GUID definition
BCompany_CodeCompany CodeText3Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
CVendor_CodeVendor CodeYESText10Vendor
DVendor_NameVendor NameText30No commas
EAlpha_SortVendor Alpha RefText6No commas
FTypeVendor TypeText6
GOur_Account_NumberAccount referenceText25
HAddress_1Address 1Text30
IAddress_2Address 2Text30
JCityCityText25
KStateState/provinceText22 character postal abbreviation
LZip_CodePostal codeText10
MAddr_CountryCountryAlpha25
NPhonePhone NumberText14Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.Remove the dashes from format when sending to Spectrum.
OFax_PhoneFax #Text14Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.Remove the dashes from format when sending to Spectrum.
PVendor_EmailVendor EmailText80Example: Jon@xxx.comMust be the basic layout for an email address.
QWeb_SiteWebsiteAlpha80Example: xxx.com
RDisadv_Business_FlagDBEText1(Y)es or(N)o only
SDisadv_Business_TypeDBE TypeText10
TSmall_BusinessSmall business enterprise (SBE)?Text1(Y)es or(N)o only
UMinority_BusinessMinority-owned business enterprise (MBE)?Text1(Y)es or(N)o only
VWoman_BusinessWoman-owned business enterprise (WBE)?Text1(Y)es or(N)o only
WVeteran_BusinessVeteran-owned business enterprise (VBE)?Text1(Y)es or(N)o only
XStatusStatusAlpha1(A)ctive, (I)nactive or (N)ot used
YRouting_Code1Routing Code for Invoice ApprovalText10Routing Code Maintenance
ZRouting_LimitRouting Limit Invoice ApprovalNumeric13Positive numbers only.
AARouting_Code2Routing Code for Over Limit Invoice ApprovalText10Routing Code Maintenance
ABUse_Tax_CodeSales/Use Tax CodeText15Use Tax Code Maintenance
ACDefault_GL_AccountDefault G/L CodeNumeric12Code must have an Active status.G/L Master File Maintenance
ADHold_FlagOn Hold?Text1(Y)es or(N)o only
AEGL_Distribution_Acct_List1Multiple G/L Code (1)Numeric12Must be a Non-Direct G/L code with an Active status.G/L Master File Maintenance
AFGL_Distribution_Acct_List2Multiple G/L Code (2)Numeric12Must be a Non-Direct G/L code with an Active status.G/L Master File Maintenance
AGGL_Distribution_Acct_List3Multiple G/L Code (3)Numeric12Must be a Non-Direct G/L code with an Active status.G/L Master File Maintenance
AHGL_Distribution_Acct_List4Multiple G/L Code (4)Numeric12Must be a Non-Direct G/L code with an Active status.G/L Master File Maintenance
AIGL_Distribution_Acct_List5Multiple G/L Code (5)Numeric12Must be a Non-Direct G/L code with an Active status.G/L Master File Maintenance
AJGL_Distribution_Acct_List6Multiple G/L Code (6)Numeric12Must be a Non-Direct G/L code with an Active status.G/L Master File Maintenance
AKGL_Distribution_Acct_List7Multiple G/L Code (7)Numeric12Must be a Non-Direct G/L code with an Active status.G/L Master File Maintenance
ALGL_Distribution_Acct_List8Multiple G/L Code (8)Numeric12Must be a Non-Direct G/L code with an Active status.G/L Master File Maintenance
AMGL_Distribution_Acct_List9Multiple G/L Code (9)Numeric12Must be a Non-Direct G/L code with an Active status.G/L Master File Maintenance
ANGL_Distribution_Acct_List10Multiple G/L Codes (10)Numeric12Must be a Non-Direct G/L code with an Active status.G/L Master File Maintenance
AOGL_Distrib_Percent_List1Distribution % (1)Numeric5Enter 10.5% as 10.5. Positive number only.The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.
APGL_Distrib_Percent_List2Distribution % (2)Numeric5Enter 10.5% as 10.5. Positive number only.The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.
AQGL_Distrib_Percent_List3Distribution % (3)Numeric5Enter 10.5% as 10.5. Positive number only.The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.
ARGL_Distrib_Percent_List4Distribution % (4)Numeric5Enter 10.5% as 10.5. Positive number only.The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.
ASGL_Distrib_Percent_List5Distribution % (5)Numeric5Enter 10.5% as 10.5. Positive number only.The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.
ATGL_Distrib_Percent_List6Distribution % (6)Numeric5Enter 10.5% as 10.5. Positive number only.The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.
AUGL_Distrib_Percent_List7Distribution % (7)Numeric5Enter 10.5% as 10.5. Positive number only.The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.
AVGL_Distrib_Percent_List8Distribution % (8)Numeric5Enter 10.5% as 10.5. Positive number only.The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.
AWGL_Distrib_Percent_List9Distribution % (9)Numeric5Enter 10.5% as 10.5. Positive number only.The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.
AXGL_Distrib_Percent_List10Distribution % (10)Numeric5Enter 10.5% as 10.5. Positive number only.The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.
AYTerms_CodePayment due terms (A or B only)Text1Enter 'A' if based on invoice date. Enter 'B' if based on 1st of next month.
AZTerms_DaysDays Payment DueNumeric3Positive numbers only.
BATerms_Disc_CodeDiscount Due (A or B only)Text1Enter 'A' if based on invoice date. Enter 'B' if based on 1st of next month.
BBTerms_Disc_DaysDays Discount DueNumeric3Positive numbers only.
BCTerms_Disc_PercentDiscount %Numeric6Enter 10.25% as 10.25. Positive numbers only.
BDInsurance_Cert_FlagIns CertText1(Y)es or(N)o only
BEInsurance_Exp_DateIns Expiration DateDate10Enter as: MM/DD/CCYY (for example, 01/05/2027)
BFPO_MethodPurchase Order Default?Text11 = One Step Receiving, 2 = Two Step Receiving
BGVendor_StatusPayment methodText1(P)rint Check, (S)end electronic pre-note, (E)lectronic payment, (C )omdata, or (V) ePayments**
BHChecking_Account_CodeElectronic payment account codeText17**
BIAccount_TypeElectronic payment account typeText1(C )hecking or (S)aving**
BJABA_NumberElectronic payment ABA routing #Numeric9**
BKBank_Account_CodeCredit Card account codeText15Cash Management Credit Card account code
BLSend_1099_Flag1099-Misc applicable?Text1(Y)es or(N)o onlyUsed for United States 1099.**
BMAlt_1099_NameAlternate NameText30No commas.Used for United States 1099.**
BNFed_1099_Indicator1099 Pmt IndicatorText11; 2; 3; 4; 5; 6; 7; 8; 9 or A only (7 for non-employee compensation box)Used for United States 1099. Defaults to 7 if blank and the Send_1099_Flag = Y
BOSocial_Sec_NumberSocial Security #Text9Format = 123-45-6789 or 123456789. If defined then Fed_Id_Number must be blank.Used for United States 1099.**
BPFed_Id_NumberFederal ID #Text12If defined then Social_Soc_Number must be blank.Used for United States 1099.**
BQRecipient_Type_CodeRecipient typeText1(1) - Individual, (3) - Corporation or (4) - Partnership onlyUsed for Canadian T5018.**
BRSocial_Insurance_NumberSocial insurance #Numeric9If defined then Recipient_Account_Number must be blank. No dashes. Must be 9 characters.Used for Canadian T5018.**
BSRecipient_Account_NumberRecipient account #Text15If defined then Social_Insurance_Number must be blank. No dashes. Must be 15 characters.Used for Canadian T5018.**
BTPartnership_Filer_ID_NumberPartnership filer #Text9Required when Recipient type = 4Used for Canadian T5018.**
BUAlternate_T5018_NameAlternate NameText30Not available when Recipient type = 1Used for Canadian T5018.**
BVIndividual_First_NameFirst nameText12Required when Recipient type = 1Used for Canadian T5018.**
BWIndividual_Middle_InitialMiddle initialText1Available when Recipient type = 1Used for Canadian T5018.**
BXIndividual_Last_NameLast nameText20Required when Recipient type = 1Used for Canadian T5018.**
BYOverride_Currency_CodeOverride Currency CodeText3Multi-Currency module must be activeCurrency Code
