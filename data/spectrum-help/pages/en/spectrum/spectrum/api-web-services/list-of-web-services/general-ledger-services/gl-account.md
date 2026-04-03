---
title: "G/L Account | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/general-ledger-services/gl-account"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/general-ledger-services/gl-account"
---

# G/L Account

Use this service to import G/L Account
 information.
 WSDL: AddGLAccount.jws Method: AddGLAccount
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing G/L Account information, the following file maintenance areas must be completed:

- System
 AdministrationInstallationGeneral
 Ledger

- System
 AdministrationInstallationGeneral
 LedgerG/L Department File Maintenance

- System
 AdministrationInstallationGeneral
 LedgerG/L User-Defined Fields
 Maintenance

- System
 AdministrationInstallationJob
 CostCost Type File Maintenance

## Assumptions and Dependencies

- The GL Account Master cost center flag is shared. The GL Account import will validate that the company has the cost center option set to Pending or Yes and will set the default for the new G/L Account to Shared.

- If the Direct_Cost_Flag field is defined with a Y then the Cost_Type field is required.

- All General Ledger accounts will post in detail.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeYESText3Valid company in Spectrum
C
GL_AccountG/L AccountYESNumeric12Verifies the GL mask and department prefix for the account code from install screen. Positive numbers only. No dashes.
D
DescriptionDescriptionText30
E
Short_DescriptionAbbreviated DescriptionText18
F
Account_Type_CodeAccount TypeYESText1(A)ssets; (L)iabilities; (C)apital; (I)ncome; (E)xpense; or (S)tatistic only
G
Direct_Cost_FlagDirect CostYESText1(Y) - Direct Job; (E) - Direct Equipment; or (N) - Non-Direct only; (W) - Work Order
H
Cost_TypeCost TypeText3Required if Direct_Cost_Flag = YCost Type Master
I
StatusStatusYESText1(A)ctive; (I)nactive; or (N)ot Used only
