---
title: "Work Order Image | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/document-imaging-services/work-order-image"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/document-imaging-services/work-order-image"
---

# Work Order Image

Use this service to add an image to the applicable Spectrum DI cabinet / drawer / folder and records Image Transaction information tied to the defined work order.

## Connection Info

URL: https://<SPECTRUM-SERVER>:8482/workOrders/images
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication),
 [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{"workOrderImages":[
 {
 "Company_Code": "SP1",
 "WO_Number": "536",
 "Image_Type": "TXT",
 "Image_Description": "WORK ORDER FORM",
 "Document_ID": "",
 "Image_File": "JVBERi0xLjMNJf////8NMSAw...w0lJUVPRg0="
 },
 {
 "Company_Code": "SP1",
 "WO_Number": "536",
 "Image_Type": "TXT",
 "Image_Description": "WORK ORDER FORM",
 "Document_ID": "",
 "Image_File": "JVBERi0xLjMNJf////8NMSAw...w0lJUVPRg0="
 }
]}`
```

## Underlying File Maintenance

Prior to importing an IMAGE for a particular work order, the following file maintenance
 areas must be completed:

- System Administration > Installation > Document Imaging

- System Administration > Installation > Document Imaging > Cabinet Maintenance

- System Administration > Installation > Work Order

- System Administration > Installation > Work Order > Work Order Main Properties

- System Administration > Installation > Work Order > Site Main Properties

- System Administration > Installation > Job Cost > Job Main Properties

## Assumptions and Dependencies

- The Add Work Order Image Web Service adds an image to the applicable Spectrum DI cabinet / drawer / folder and records Image Transaction information tied to the defined work order. The Web Service also stores the Image File using the applicable Path defined in Spectrum for that work order.

- The Web Service will determine the applicable Cabinet and Drawer, as follows:

- Read the WO_HEADER_MC Table for the defined work order to determine whether it references a Site or a Job (column = WO_Reference_Code)

- When the work order references a Site: Cabinet = WO and Drawer = SITE WO

- When the work order references a Job: Cabinet = WO and Drawer = JOB WO

- The Web Service will determine the applicable DI Folder for the incoming Image File, by reading WO_HEADER_MC Table for the Job code or Site code (WO_Job_Number)

- Folder = <Job/Site Code>

- The Web Service will determine the applicable Path for the Image File by reading for the company-wide default "Path" variable specified in Document Imaging Installation Note to Reader: Document Imaging offers an option to store images by Year and Period. The Web Service will automatically store imported work order images as if the DIPathByYearAndPeriod value variable is <blank>.

- Work Order Image Header Information:

- The Web Service will need the Transaction_ID assigned to the defined work order in DI_MASTER_MC in order to associate the incoming Image with that same work order in Spectrum.

- HEADER EXISTS: Find Transaction_ID in DI_MASTER_MC in the record with the following KEYS:

- Company_Code = defined Company_Code (from WS import)

- Cabinet = WO

- Drawer = JOB WO or SITE WO, determined above

- Folder = <Job/Site Code> determined above (left-justified)

- Reference = defined WO_Number (from WS import, not left-justified) Note to Reader: The Image Header record is automatically created when a new work order is added within Spectrum, but may not exist yet if the work order was initially created using the Work Order Web Service.

- HEADER NOT FOUND: The Web Service will need to insert a new DI header record into DI_MASTER_MC if it does not already exist, using above KEY information, plus the following:

- Transaction_Description =

- For Site = Site Work Order <1234567890> (WO# not left justified)

- For Job = Job Work Order <1234567890> (WO# not left justified)

- Keywords =

- For Site = 'S' + <wo#> + ' ' + <site name> + ' WORK ORDER'

- For Job = 'J' + <wo#> + ' ' + <job name> + ' WORK ORDER'

- Transaction_ID = assign unique ID (programmer's discretion)

- Work Order Image-Specific Detail Information:

- The Web Service will insert a record for the incoming work order image into DI_IMAGE_MASTER, as follows:

- Document_ID = Use text string from Import File, if specified

- However, if no Document ID is imported, the Web Service will generate unique Document ID.

- In the case where the Web Service generates the Document ID, the value will be returned to a 3rd party calling the web service.

- Image_Path = Path determined above

-  Image_Filename = Unique file name devised by Web Service

- Create_Operator = Set to 3-character Spectrum Operator Code associated with the Authorization ID in Data Exchange Installation

- Create_Date = Set to current system date

- Create_Time = Set to current system time

- Change_Operator = <leave blank>

- Change_Date = <leave blank>

- Change_Time = <leave blank>

- Image_Description = Use text string from Import File, if specified

- However, if no descriptive text imported, assign same text stored in Transaction_Description column of the Work Order Image Header record (DI_MASTER_MC - detailed above)

- Image Cross-Reference Table:

- The Web Service will insert a record into the DI_IMAGE_XREF Table, linking the Work Order Image-Specific Detail with the detail and the Work Order Image Header record, as follows:

- Transaction_ID = same as field in DI_MASTER_MC

- Document_ID = same as KEY field in DI_IMAGE_MASTER

- The Web Service follows the majority of the same logic as manually attaching an image to the work order, with the exceptions of the data defined here. The Spectrum Help Files can be used for troubleshooting errors along with the details defined here.

- The Web Service does not change or delete values that exist in Spectrum.

- The Web Service will not support the following (and will need to return an error to Field Connect):

- Invalid work order # in the defined company

- Document_ID specified in the imported file:

- Blank to add a new document to the work order;

- Pass an existing document_id to replace the image (the document_id must also be valid for that work order)

## Field Descriptions

Use the table below for reference when using this service.
Element NameDescriptionReq?TypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation screen
GUIDUnique reference number created by programmingText36** See GUID definition
Company_CodeCompany CodeYESText3Valid company in Spectrum
WO_NumberWork Order NumberYESText10Valid WO# must exist in defined company
Image_FileImage FileYESBase64
Image_TypeFile ExtensionYESText
Document_IDDocument IDText19*** See Assumptions and DependenciesMust be unique in Spectrum
Image DescriptionImage DescriptionText40*** See Assumptions and DependenciesUpdate if modifying an existing record, unless blank passed in
