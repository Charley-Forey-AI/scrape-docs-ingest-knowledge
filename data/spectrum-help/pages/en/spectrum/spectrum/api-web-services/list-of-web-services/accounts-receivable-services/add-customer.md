---
title: "Add Customer | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-customer"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-customer"
---

# Add Customer

Use this service to import Customer information.
WSDL: AddCustomer.jws
Method: AddCustomer
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Customer information, the following file maintenance areas under System Administration > Installation must be completed:

- Accounts Receivable

- General Ledger > G/L Master File Maintenance

- Accounts Receivable > Sales Tax Code Maintenance

- Accounts Receivable > Transaction Code File Maintenance

- Accounts Receivable > Salesperson Code Maintenance

- Accounts Receivable > Terms Code File Maintenance

- Accounts Receivable > Customer User-Defined Fields Maintenance

## Assumptions and Dependencies

- The Customer Master cost center flag is shared. The Customer import will validate that the company has the cost center option set to Pending or Yes and will set the default for the new Customer to Shared.

- The new customer's status will default to (A)ctive.

- The Contact_1 field will be defined as the Primary Contact.

- The Contact_2 and Contact_3 fields will be additional contacts.

- If left blank, these field's values are defined by the Accounts Receivable Installation screen:

- Standard_Retention_Percent

- Statement_Flag

- Finance_Charge_Tran_Code

- Finance_Charge

- This Web Service will work with the defined Workflow process in Spectrum.

- The Authorized ID must have the user-defined fields defined, or mapped, for this Web Service.

## Field Descriptions

Use the table below for reference when using this service. Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
ExcelElement NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
BCompany_CodeCompany CodeYESText3Valid Company in Spectrum
CCustomer_CodeCustomer CodeYESText10Unique identifier / No commasUPPERCASE FORMAT-NO SYMBOLS
DNameCustomer NameYESText30No commas
EAlpha_SortCustomer Alpha RefText8No commas, created if blank
FTypeCustomer TypeText10
GAddress_1Address 1Text30
HAddress_2Address 2Text30
ICityCityText25
JStateStateText22 character postal abbreviation
KZip_CodeZip CodeText10
LPhonePhone NumberText14Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.Remove the dashes from format when sending to Spectrum.
MFax_PhoneFax #Text14Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.Remove the dashes from format when sending to Spectrum.
NContact_1Contact 1Text20No commas
OContact_2Contact 2Text20No commas
PContact_3Contact 3Text20No commas
QSalespersonSalesman CodeText3Salesperson Code Maintenance
RTerms_CodeTerms CodeYESText1Terms Code File Maintenance
SStandard_Retention_PercentDefault Retention (Holdback) %Numeric7Enter 10.5% as 10.5. Positive numbers only.Defaults from AR Installation screen if left blank.
TTaxable_FlagTaxableText1(Y)es or(N)o only
USales_Tax_CodeSales (Providence) Tax CodeYESText15Sales Tax Code Maintenance
VResale_NumberResale Cert. #Text15
WResale_Exp_DateResale Exp. DateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
XStatement_FlagSend Statement?Text1(Y)es or(N)o only. Defaults to Y if left blank.
YFinance_Charge_Tran_CodeFinance Charge CodeText10Transaction Code File Maintenance. Defaults from AR Installation screen if left blank.
ZFinance_ChargeFinance Charge %Numeric6Enter 10.5% as 10.5. Positive numbers only.If Finance_Charge_Tran_Code is blank then defaults from AR Installation screen if left blank.
AAPrice_Level_MaterialWork Order Material LevelNumeric11-5 onlyRecommend input for clients with the WO, TM, OP, or SI modules
ABPrice_Level_LaborWork Order Labor LevelNumeric11-5 onlyRecommend input for clients with the WO, TM, OP, or SI modules
ACCredit_LimitCredit LimitNumeric14
ADDate_CreatedDate EstablishedDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)If left blank then it will use the current date in the system
AECustomer_EmailCustomer EmailText70Example: John@xxx.comMust be the basic layout for an email address.
AFMarkup_CodeNon-stock MarkupText10Non-Stock Markup Codes
AGUDF1User Defined Alpha/Numeric/Date 1+20Web Service Authorization ID Service UDF defined.
AHUDF2User Defined Alpha/Numeric/Date 2+20Web Service Authorization ID Service UDF defined.
AIUDF3User Defined Alpha/Numeric/Date 3+20Web Service Authorization ID Service UDF defined.
AJUDF4User Defined Alpha/Numeric/Date 4+20Web Service Authorization ID Service UDF defined.
AKUDF5User Defined Alpha/Numeric/Date 5+20Web Service Authorization ID Service UDF defined.
ALUDF6User Defined Alpha/Numeric/Date 6+20Web Service Authorization ID Service UDF defined.
AMUDF7User Defined Alpha/Numeric/Date 7+20Web Service Authorization ID Service UDF defined.
ANUDF8User Defined Alpha/Numeric/Date 8+20Web Service Authorization ID Service UDF defined.
AOUDF9User Defined Alpha/Numeric/Date 9+20Web Service Authorization ID Service UDF defined.
APUDF10User Defined Alpha/Numeric/Date 10+20Web Service Authorization ID Service UDF defined.
AQUDF11User Defined Alpha/Numeric/Date 11+20Web Service Authorization ID Service UDF defined.
ARUDF12User Defined Alpha/Numeric/Date 12+20Web Service Authorization ID Service UDF defined.
ASUDF13User Defined Alpha/Numeric/Date 13+20Web Service Authorization ID Service UDF defined.
ATUDF14User Defined Alpha/Numeric/Date 14+20Web Service Authorization ID Service UDF defined.
AUUDF15User Defined Alpha/Numeric/Date 15+20Web Service Authorization ID Service UDF defined.
AVUDF16User Defined Alpha/Numeric/Date 16+20Web Service Authorization ID Service UDF defined.
AWUDF17User Defined Alpha/Numeric/Date 17+20Web Service Authorization ID Service UDF defined.
AXUDF18User Defined Alpha/Numeric/Date 18+20Web Service Authorization ID Service UDF defined.
AYUDF19User Defined Alpha/Numeric/Date 19+20Web Service Authorization ID Service UDF defined.
AZUDF20User Defined Alpha/Numeric/Date 20+20Web Service Authorization ID Service UDF defined.

 + NOTE = the UDF (1-20) elements can be Numeric, Date, or Text depending on how they are created within the application.
