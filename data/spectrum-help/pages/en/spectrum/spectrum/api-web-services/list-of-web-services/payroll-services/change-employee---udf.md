---
title: "Change Employee - UDF | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/change-employee---udf"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/change-employee---udf"
---

# Change Employee - UDF

Use this service to import Employee User-Defined Fields information.

## Connection Information

WSDL: UpdateEmp_UDF.jws
Method: UpdateEmp_UDF
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Sample XML Body

```
`<UDF>
 <UDF_EL></UDF_EL>
 <UDF_EL></UDF_EL>
</UDF>`
```

## Assumptions and Dependencies

- The Payroll module must be set up.

- The Employee code must exist in the defined Company code.

- The Employee User-Defined Field Information Web Service updates an existing employee's information for the defined fields only.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- The Employee user-defined fields need to be defined in Spectrum.

- The Authorized ID must have the user-defined fields defined, or mapped, for this Web Service.

## Field Descriptions

 Use the table below for reference when using this service. Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
ExcelElement NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
BCompany_CodeCompany CodeYESText3Valid Company in Spectrum
CEmployee_CodeEmployee CodeYESText11Unique Identifier / No commasEmployee Code must exist for the defined Company Code.
DUDF1User Defined Alpha/Numeric/Date 1+20Web Service Authorization ID Service UDF defined.
EUDF2User Defined Alpha/Numeric/Date 2+20Web Service Authorization ID Service UDF defined.
FUDF3User Defined Alpha/Numeric/Date 3+20Web Service Authorization ID Service UDF defined.
GUDF4User Defined Alpha/Numeric/Date 4+20Web Service Authorization ID Service UDF defined.
HUDF5User Defined Alpha/Numeric/Date 5+20Web Service Authorization ID Service UDF defined.
JUDF6User Defined Alpha/Numeric/Date 6+20Web Service Authorization ID Service UDF defined.
IUDF7User Defined Alpha/Numeric/Date 7+20Web Service Authorization ID Service UDF defined.
KUDF8User Defined Alpha/Numeric/Date 8+20Web Service Authorization ID Service UDF defined.
LUDF9User Defined Alpha/Numeric/Date 9+20Web Service Authorization ID Service UDF defined.
MUDF10User Defined Alpha/Numeric/Date 10+20Web Service Authorization ID Service UDF defined.
NUDF11User Defined Alpha/Numeric/Date 11+20Web Service Authorization ID Service UDF defined.
OUDF12User Defined Alpha/Numeric/Date 12+20Web Service Authorization ID Service UDF defined.
PUDF13User Defined Alpha/Numeric/Date 13+20Web Service Authorization ID Service UDF defined.
QUDF14User Defined Alpha/Numeric/Date 14+20Web Service Authorization ID Service UDF defined.
RUDF15User Defined Alpha/Numeric/Date 15+20Web Service Authorization ID Service UDF defined.
SUDF16User Defined Alpha/Numeric/Date 16+20Web Service Authorization ID Service UDF defined.
TUDF17User Defined Alpha/Numeric/Date 17+20Web Service Authorization ID Service UDF defined.
UUDF18User Defined Alpha/Numeric/Date 18+20Web Service Authorization ID Service UDF defined.
VUDF19User Defined Alpha/Numeric/Date 19+20Web Service Authorization ID Service UDF defined.
WUDF20User Defined Alpha/Numeric/Date 20+20Web Service Authorization ID Service UDF defined.
