---
title: "Employee Training Certification Image | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/human-resources-services/employee-training-certification-image"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/human-resources-services/employee-training-certification-image"
---

# Employee Training Certification Image

Use this service to add any images to employee training
 certifications.

## Connection information

URL = https://<SPECTRUM-SERVER>:8482/employee/trainingCertification/images
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "trainingCertImages": [
 {
 "Company_Code": "SP2",
 "Employee_Code": "NEWJOB",
 "Training_Code": "NEWJOB",
 "Training_Key": "20190623103900",
 "Drawer": "TRAINING",
 "Image_Type": "PDF",
 "Image_Description": "PDF Document",
 "Document_ID": "",
 "Image_File": "***BASE64ed Image***"
 },
 {
 "Company_Code": "SP2",
 "Employee_Code": "NEWJOB",
 "Training_Code": "NEWJOB",
 "Training_Key": "20190623103901",
 "Drawer": "TRAINING",
 "Image_Type": "JPG",
 "Image_Description": "Pikachu",
 "Document_ID": "",
 "Image_File": ""***BASE64ed Image**"
 }
 ]
}`
```

## Underlying File Maintenance

Prior to importing HR Training Certification Image information, the following file maintenance areas must be completed:

- System Administration > Installation > Human Resources

- System Administration > Installation > Human Resources > Training / Certification

## Assumptions and Dependencies

- The companyCode, employeeCode ,trainingkey, trainingCode will be a valid record in HR Employee Training master table.

- The documentID can be blank, which will indicate that a new document is being added. If not blank, it must be a valid documentID, and have a transactionID matching the companyCode, jobCode, and drawer values.

- The Web Service will determine the applicable Path for the Image File by reading for the company-wide default "Path" variable specified in Document Imaging Installation

- Document Imaging offers an option to store images by Year and Period. The Web Service will automatically store imported work order images as if the DIPathByYearAndPeriod value variable is <blank>.

- The Web Service will generate a new Transaction_ID as a GUID.

- If documentID is passed in, then the existing Transaction_ID will be used.

- The Web Service will insert a record for the incoming HR_EMPLOYEE_TRAINING_MC into DI_MASTER_MC, as follows, if no documentID is passed in:

- Company_Code = passed in

- Cabinet = "Employee"

- Drawer = "TRAINING"

- Folder = employeeCode (with any leading blanks removed)

- Trainingkey = Passed in

- Reference = new unique GUID

- Transaction_Description = imageDescription passed in (if blank, use the drawer name and current date as 'mm/dd/yyyy')

- Keywords = employeeCode(with leading blanks remove) + 'Training' + Training Code + Training Description

- The Web Service will insert a record for the incoming employee training certification image into DI_IMAGE_MASTER, as follows:

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
Req?
Type
Max
Format
Validation

Authorization_ID
Authorization ID to access the server
YES
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
YES
Text
3
Valid company in Spectrum

Employee_Code
Employee Code
YES
Text
11
Valid employee must exist in the specified company

Training_Code
Training Code
YES
Text
15
Valid training code in Spectrum

Drawer
DI Drawer
Text
20
Must be a valid Drawer in the EMPLOYEE cabinet for the specified company

Image_Type
File Extension
YES
Text

Image_Description
Image Description
Text
40
*** See Assumptions and Dependencies

Document_ID
Document ID
Text
19
*** See Assumptions and Dependencies
Must be unique in Spectrum

Image_File
Image File
YES
Base64
