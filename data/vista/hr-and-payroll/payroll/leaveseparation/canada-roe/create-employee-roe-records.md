---
title: "Create Employee ROE Records | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/canada-roe/create-employee-roe-records"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/canada-roe/create-employee-roe-records"
---

# Create Employee ROE Records

Before you can generate your Record of Employment (ROE) reports, you must first create an ROE record for each employee for which you will be submitting the report.
Use the PR Employee ROE Workfile form to:

- select employee records

- add specific details to each record

- have the system create an ROE record for each employee.

 The system will then use these records when you generate the ROE reports.
To create employee ROE records:

1. From the Main Menu, open the PR Record of Employment form.

1. Select ROE Employee Workfile.The system displays the PR Employee ROE Workfile form.

1. In the Begin and End fields of the Employee Selection Criteria section, enter a separation date range.The system brings in employees who have a separation date that falls within this range (Separation Date field, PR Employees form, Add'l Info tab).

1.  In the Default ROE Date field, enter the date that will be assigned to each ROE record.

1. (Optional) Use the Optional Default Values section of the form to enter information that will default to all records that are added to the grid. This is useful when all records have data in common. You can later override the information in the grid.For more information, see the F1 help for each field.

1. Select Fill Grid.Note: The records that display in the workfile are associated with your login (as displayed in the VPUserID field at the top of the form). This allows you to view only records in the workfile that you have specifically added and not see records that another user may have added.

The system adds employee records to the grid that meet the specified date range criteria. Additionally, the system adds the date from the Default ROE Date field and any information from the fields in the Optional Default Values section of the form.

1. Review the records in the grid and edit the fields as necessary. You can also manually add employee records to the grid as needed.

1. Select the Process ROE checkbox for each employee in the grid that you want to process or select the Process all ROE Records checkbox (above the grid) to process all employees in the grid.

1. Select Initialize ROE.The system creates an ROE record for each employee in the grid and then displays a confirmation dialog.Note: The system will not create employee ROE records that have missing or incorrect data, or if a duplicate record exists in PR Record of Employment. If this occurs, the system will display a message after you select Initialize ROE. Close the message and review the Error Message field in the workfile grid for the exact reason why the record could not be created. The information in this field will provide information on how to fix the situation, after which you can reattempt to create the ROE record.

1. Select Close.The system closes the PR Employee ROE Workfile form and returns to the PR Record of Employment form where all new employee ROE records now appear in the grid.Note: In some cases, you will be given the opportunity to overwrite an existing record. If an overwrite message displays, you will be given the following options:

- Select Yes to overwrite the existing record in PR Record of Employment.

- Select No to return to the workfile; the system will display a message in the Error Message field.

- Select Cancel to take no action and to return to the PR Employee ROE Workfile form.

Each ROE record contains hours and amounts data compiled from the employee's payroll history and which is required for reporting on the ROE.

Related information

- [About the PR Record of Employment Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/canada-roe/about-the-pr-record-of-employment-form)

- [About the PR Employee ROE Workfile Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/canada-roe/about-the-pr-employee-roe-workfile-form)

- [About Record of Employment Reporting](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/canada-roe/about-record-of-employment-reporting)
