---
title: "Employee Training Certification | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/human-resources-services/employee-training-certification"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/human-resources-services/employee-training-certification"
---

# Employee Training Certification

Use this service to import HR Employee Training
 Certification information.

## Connection Information for POST

URL = https://<SPECTRUM-SERVER>:8482/employee/trainingCertification
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body for POST

```
`{
 "trainingCertifications":[
 {
 "Company_Code": "ABC",
 "Employee_Code": "MQT",
 "Training_Code": "aa",
 "Employee_Train_Level": "",
 "Employee_Train_Start_Date": "",
 "Employee_Train_End_Date": "02/03/19",
 "Employee_Train_Req_Date": "02/03/19",
 "Employee_Train_Exp_Date": "",
 "Employee_Train_Note": "071519TestingVersion"
 },
 {
 "Company_Code": "ABC",
 "Employee_Code": "MQT",
 "Training_Code": "FIRST_AID",
 "Employee_Train_Level": "1",
 "Employee_Train_Start_Date": "03/01/19",
 "Employee_Train_End_Date": "02/03/19",
 "Employee_Train_Req_Date": "02/03/19",
 "Employee_Train_Exp_Date": "03/06/19",
 "Employee_Train_Note": "071519TestingVersion"
 }
 ]
}`
```

## Connection Information for GET

URL =
 https://<SPECTRUM-SERVER>:/employee/trainingCertification/{companyCode}/{employeeCode}?code={trainingCode}&level={trainingLevel}
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: GET
Supported formats: JSON

## Sample JSON Body for GET

```
`[
 {
 "Company_Code": "ABC",
 "Employee_Code": " RYAN",
 "Training_Code": "KR",
 "Employee_Train_Level": 1,
 "Employee_Train_Start_Date": "12/31/2018",
 "Employee_Train_End_Date": "12/31/2019",
 "Employee_Train_Req_Date": "12/31/2018",
 "Employee_Train_Exp_Date": "12/31/2020",
 "Employee_Train_Note": "TestingVersion3",
 "Training_Key": "20190617141200"
 },
 {
 "Company_Code": "ABC",
 "Employee_Code": " RYAN",
 "Training_Code": "KR",
 "Employee_Train_Level": 1,
 "Employee_Train_Start_Date": "12/31/2018",
 "Employee_Train_End_Date": "12/31/2019",
 "Employee_Train_Req_Date": "12/31/2018",
 "Employee_Train_Exp_Date": "12/31/2020",
 "Employee_Train_Note": "TestingVersion4",
 "Training_Key": "20190624115100"
 },
 {
 "Company_Code": "ABC",
 "Employee_Code": " RYAN",
 "Training_Code": "KR",
 "Employee_Train_Level": 1,
 "Employee_Train_Start_Date": "12/31/2018",
 "Employee_Train_End_Date": "12/31/2019",
 "Employee_Train_Req_Date": "12/31/2018",
 "Employee_Train_Exp_Date": "12/31/2020",
 "Employee_Train_Note": "TestingVersion4",
 "Training_Key": "20190626092300"
 }
]`
```

## Underlying File Maintenance

Prior to importing HR Employee Training Certification information, the following file
 maintenance areas must be completed:

- System Administration > Installation > Human Resources

- System Administration > Installation > Payroll > Employees

- System Administration > Installation > Human Resources > Training Certification Codes

## Assumptions and Dependencies

- The Company Code and Employee Code will be validated to the Employee Master table.

- The Company Code and Training Code will be validated to the Training table.

- The following fields are controlled by the Training Code due to the setup of the code:

- Employee Train Level

- Employee Train Start Date

- Employee Train End Date

- Employee Train Req Date

- Employee Train Exp Date

- Validation of the following field as below:

- Company Code – Must a be a valid Company Code

- Employee Code – Must be a valid Employee code

- Training Code – Must be a valid Training Code

- Employee Train Level – Must be a numeric value that is less than 1000. If training code setup is required, then this value cannot be blank. If it is validated, then training level must be validated to the training level table.

- Employee Train Start Date – If training code start date is required then value cannot be blank, otherwise it is optional.

- Employee Train End Date – If training code end date is required then value cannot be blank, otherwise it is optional.

- Employee Train Req Date – If training code Required date is required then value cannot be blank, otherwise it is optional.

- Employee Train Exp Date– If training code expired date is required then value cannot be blank, otherwise it is optional.

- Employee Train Note– This field is optional.

- The web service has the ability to add new records using posts. An employee can have the same Training Code defined multiple times with different details. A training key will be created for every line of records being passed in.

- The web service will not account for reimbursement section. It will behave just the Reimburse/Deduct training amount on employee's next paycheck being cleared.

- The web service will return the Training Key for the use with the HR Training Certification Image web service.

- GET request will return records in the HR_EMPLOYEE_TRAINING_MC table.

- Parameter for GET services will be Company Code, Employee Code, Training Code and Training Level.

- GET services will return records along with training key if it exits in the HR_EMPLOYEE_TRAINING_MC Table.

- Company Code, Employee Code, Training Code and Training Level will be validated.

- Training Code and Training Level are optional parameters.

## Field Descriptions

Use the table below for reference when using this service:
Element NameDescriptionReq?TypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation screen
GUIDUnique reference number created by programmingText36** See GUID definition
Company_CodeCompany CodeYESText3Valid company in Spectrum
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

Employee_Train_Level
Employee Training Level
Numeric
3

Employee_Train_Start_Date
Employee Training Start Date
Date
10
Enter as MM/DD/CCYY (for example, 01/05/1982)

Employee_Train_End_Date
Employee Training End Date
Date
10
Enter as MM/DD/CCYY (for example, 01/05/1982)

Employee_Train_Req_Date
Employee Training Required Date
Date
10
Enter as MM/DD/CCYY (for example, 01/05/1982)

Employee_Train_Exp_Date
Employee Training Expired Date
Date
10
Enter as MM/DD/CCYY (for example, 01/05/1982)

Employee_Train_Note
Employee Training Note
Text
250
