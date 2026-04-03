---
title: "Employee Image | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/document-imaging-services/employee-image"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/document-imaging-services/employee-image"
---

# Employee Image

Use this service to import Employee Image information.

## Connection Information

URL: https://<SPECTRUM-SERVER>:8482/employee/images
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication),
 [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{"employeeImages":[
 {
 "company_Code": "SP1",
 "employee_Code": "536",
 "drawer": "Resume",
 "image_Type": "PDF",
 "image_Description": "John Smith Resume",
 "document_ID": "",
 "image_File": "JVBERi0...NDY2NjQKJSVFT0YK"
 },
 {
 "company_Code": "SP1",
 "employee_Code": "536",
 "drawer": "I9",
 "image_Type": "PDF",
 "image_Description": "I-9 Documentation",
 "document_ID": "",
 "image_File": "JVBERi0xLjMNJf////8NMSAw...w0lJUVPRg0="
 }
]}`
```

## Assumptions and Dependencies

- The company_Code and employee_Code will be a valid record in employee master table.

- The drawer passed in must be non-blank and a valid drawer for the EMPLOYEE cabinet in that company.

- The document_ID can be blank, which will indicate that a new document is being added. If not blank, it must be a valid document_ID, and have a transactionID matching the company_Code, employee_Code, and drawer values.

- The Web Service will determine the applicable Path for the Image File by reading for the company-wide default "Path" variable specified in Document Imaging Installation

- Document Imaging offers an option to store images by Year and Period. The Web Service will automatically store imported work order images as if the DIPathByYearAndPeriod value variable is <blank>.

- The Web Service will generate a new Transaction_ID as a GUID.

- If document_ID is passed in, then the existing Transaction_ID will be used.

- The Web Service will insert a record for the incoming employee DI transaction into DI_MASTER_MC, as follows, if no document_ID is passed in:

- Company_Code = passed in

- Cabinet = "EMPLOYEE"

- Drawer = passed in

- Folder = employee_Code (with any leading blanks removed)

- Reference = new unique GUID

- Transaction_Description = image_Description passed in (if blank, use the drawer name and current date as 'mm/dd/yyyy')

- Keywords = tbd

- Transaction_ID = new unique GUID

- The Web Service will insert a record for the incoming employee image into DI_IMAGE_MASTER, as follows:

- Document_ID = Use text string from Import File, if specified

- However, if no Document ID is imported, the Web Service will generate unique Document ID.

- In the case where the Web Service generates the Document ID, the value will be returned to a 3rd party calling the web service.

- Image_Path = Path determined above

- Image_Filename = Unique file name devised by Web Service

- Create_Operator = Set to 3-character Spectrum Operator Code associated with the Authorization ID in Data Exchange Installation

- Create_Date = Set to current system date

- Create_Time = Set to current system time

- Change_Operator = <leave blank>

- Change_Date = <leave blank>

- Change_Time = <leave blank>

- Image_Description = Use text string from Import File. If blank, use transaction Description from above.

- Image Cross-Reference Table:

- The Web Service will insert a record into the DI_IMAGE_XREF Table:

- Transaction_ID = same as field in DI_MASTER_MC

- Document_ID = Same value as above for DI_IMAGE_MASTER

## Field Descriptions

Element NameDescriptionReq?TypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation screen
GUIDUnique reference number created by programmingText36** See GUID definition
Company_CodeCompany CodeYESText3Valid company in Spectrum
Employee_CodeEmployee CodeYESText11Valid employee must exist in the specified company
DrawerDI DrawerYESText20Must be a valid Drawer in the EMPLOYEE cabinet for the specified company
Image_TypeFile ExtensionYESText
Image_DescriptionImage DescriptionText40*** See Assumptions and DependenciesUpdate if modifying an existing record, unless blank passed in
Document_IDDocument IDText19*** See Assumptions and DependenciesMust be unique in Spectrum
Image_FileImage FileYESBase64
