---
title: "Project Log Image | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/document-imaging-services/project-log-image"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/document-imaging-services/project-log-image"
---

# Project Log Image

Use this service to import Project Log Image
 information.

## Connection Information

URL = https://<SPECTRUM-SERVER>:8482/projectLog/images Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication) Supported methods: POST
 Supported formats: JSON

## Sample JSON Body

```
`{
 "projectLogImages": [
 {
 "Company_Code": "SP2",
 "Job_Number": "NEWJOB",
 "ProjectLogTran_Id": "58126C5C-C5DC-456C-AEF2-FBB5312495D9",
 "Category": "CORRESPONDENCE",
 "Reference_Num": "4",
 "Drawer": "CORRESPONDENCE",
 "Image_Type": "PDF",
 "Image_Description": "PDF Document",
 "Document_ID": "",
 "Image_File": "***BASE 64ed Image***"
 },
 {
 "Company_Code": "SP2",
 "Job_Number": "NEWJOB",
 " ProjectLogTran_Id ": "58126C5C-C5DC-456C-AEF2-FBB5312495D9",
 "Category": "CORRESPONDENCE",
 "Reference_Num": "4",
 "Drawer": "CORRESPONDENCE",
 "Image_Type": "JPG",
 "Image_Description": "Pikachu",
 "Document_ID": "",
 "Image_File": ""
 }
 ]
}`
```

## Underlying File Maintenance

Prior to importing Project Log Image information, the following file maintenance areas must be completed:

- System Administration > Installation > Job Cost

- System Administration > Installation > Project Management > Project Log

## Assumptions and Dependencies

- The companyCode and jobCode will be a valid record in job master table.

- The documentID can be blank, which will indicate that a new document is being added. If not blank, it must be a valid documentID, and have a transactionID matching the companyCode, jobCode, and drawer values.

- The Web Service will determine the applicable Path for the Image File by reading for the company-wide default "Path" variable specified in Document Imaging Installation

- Document Imaging offers an option to store images by Year and Period. The Web Service will automatically store imported work order images as if the DIPathByYearAndPeriod value variable is <blank>.

- The Web Service will generate a new Transaction_ID as a GUID.

- If documentID is passed in, then the existing Transaction_ID will be used.

- The Web Service will insert a record for the incoming project log correspondence DI transaction into DI_MASTER_MC, as follows, if no documentID is passed in:

- Company_Code = passed in

- Cabinet = "Job"

- Drawer = "CORRESPONDENCE"

- Folder = jobCode (with any leading blanks removed)

- Reference = new unique GUID

- Transaction_Description = imageDescription passed in (if blank, use the drawer name and current date as 'mm/dd/yyyy')

- Keywords = tbd

- Transaction_ID = new unique GUID

- The Web Service will insert a record for the incoming project log correspondence image into DI_IMAGE_MASTER, as follows:

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

Use the table below for reference when using this service.
Element Name
Description
Req
Type
Max
Format
Validation

Authorization_ID
Authorizaton ID to access the server
Text
20
Data Exchange Installation screen

GUID
Unique reference number created by programming
Text
36
** See GUID definition

Company_Code
Company Code
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

Job_Number
Job code
Text
10
Valid Job in Spectrum

ProjectLogTran_Id
Project Log ID
Text
36
ProjectLogTran_Id is created within Spectrum when the project log is added.
Validates to the Project Log entry.

Category
Category
Text
30
Validates to the Project Management Category Maintenance.

Reference_Num
Number
Text
10
Must be a valid Project Log reference number in the Database

Drawer
DI Drawer
Text
20
Must be a valid Drawer in the JOB cabinet for the specified company.

Image_Type
File Extension
Text

Image_Desc
Image Description
Text
40
** See Assumptions and Dependencies
Update if modifying an existing record, unless blank passed in

Document_ID
** See Assumptions and Dependencies
Must be unique in Spectrum

Image_File
Image File
Base64
