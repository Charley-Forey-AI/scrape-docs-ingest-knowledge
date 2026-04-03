---
title: "Equipment Cost Categories (Get) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/equipment-cost-categories-get"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/equipment-cost-categories-get"
---

# Equipment Cost Categories (Get)

Use this service to import Equipment Cost Categories
 information.
 WSDL: GetEqCostCategory.jws Method:
 GetEqCostCategory
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank in the parameter fields.

- All parameter fields have SuperSelect logic except the following-

- pStatus

- pCost_Center

- pSort_By

## Parameter Fields

Use the table below for reference when using this service.Element NameDescriptionReqTypeMaxField Information
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen.
GUIDUnique reference number created by programmingText36** See GUID definition
pCompany_CodeCompany CodeYESText3Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
pCost_Category_TypeCost Category TypeText1Equipment Cost Category File Maintenance
pStatusStatusText1Define one specific Status or leave blank to see Active and Inactive only
pCost_CenterCost Category Cost CenterText10Define one specific Cost Center or leave blank to see all based on Authorization ID
pSort_BySort By OptionsText1Blank = Cost Category Code or T= Cost Category Type

## Return Fields

Use the table below for reference when using this service.Element NameDescriptionTypeMaxField Information
Company_CodeCompany CodeText3Valid Spectrum Company
Cost_Category_CodeCost Category CodeText4Equipment Cost Category File Maintenance
Cost_Category_DescriptionCost Category DescriptionText30
Cost_Category_TypeCost Category TypeText1
StatusStatusText1
Cost_CenterCost Category Cost CenterText10
Error_CodeError CodeText1Used for Error information if needed
Error_DescriptionError DescriptionText250Used for Error information if needed
Error_ColumnError ColumnText100Used for Error information if needed
