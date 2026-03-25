---
title: "Field Definitions: HR Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-codes-form/field-definitions-hr-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-codes-form/field-definitions-hr-codes-form"
---

# Field Definitions: HR Codes Form

The following is a list of field descriptions for the HR Codes
 form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Code Type

The Code Type field on the HR Codes form.
 Enter the 1-character code type to indicate what type of code this is.

- A = Accident Type – Use for codes that identify different types of accidents. Codes of this type are used in the HR Resource Accident program.

- B = Body Part – Use for codes that identify a body part. You can be as explicit or generic as desired. For example, Eye or Left Eye/Right Eye, Leg or Left/Right Knee, etc.). Codes of this type are used in the HR Resource Accident program.

- C = Schedule – Use for codes that identify the different work schedules (for example, Days, Swing, Graveyard). Codes of this type are used in the HR Resource Schedule program.

- D = Drug Testing – Use for codes that identify a type of drug test or reasons for drug testing (Alcohol, Narcotics, Pre-employment, Random Testing, etc.). Codes of this type are used in HR Resource Drug Testing.

- H = History – Use for codes that identify a phase or event in an employee’s history (for example, Hire Date, Accident, Grievance, etc.). Codes of this type are used in the HR Company Parameters and HR Employment Status programs.

- I = Injury Type – Use for codes that identify an injury (for example, fracture, abrasion, burn, etc.). Codes of this type are used in the HR Resource Accident program.

- N = Reason – Use for codes that identify an explanation for termination or salary adjustment (for example, Cost of Living, Discipline Problem). Codes of this type are used in the HR Resources and HR Resource Salary History programs.

- R = Rating Code – Use for codes that identify items to be evaluated during an employee’s performance evaluation (for example, Attendance, Attitude, Job Performance, etc). Codes of this type are used when setting up rating groups in HR Performance Rating Groups and when logging entries in HR Resource Review (Performance Ratings tab).

- S = Skill – Use for codes that identify an employee/applicant skill (for example, CPR, First Aid, etc.). Codes of this type are used in the HR Skills program.

- T = Train – Use for codes that identify different training acquired by an employee (for example, Accounting 1, First Aid, Computer, etc.). Codes of this type are used in the HR Resource Train program.

- U = Drug Test Status – Use for codes that identify the different statuses for drug tests (for example, Awaiting Results, Negative, Employee Refused, etc.). The system uses this code type in HR Resource Drug Testing.

- W = Reward – Use for codes that identify types of rewards given to employees for performance or contribution (for example, Bonus, Plaque, Certificate, etc.). Codes of this type are used in the HR Resource Rewards program.

## Code

Enter a unique code for the specified code type, up
 to 10 characters. The following pre-defined drug testing codes are available:

- Alcohol = Drug Test - Alcohol

- Follow-up = Drug Test - Follow-up


- Pre-employ = Drug Test -
 Pre-employment

- Post-Accid = Drug Test -
 Post-Accident

- Random = Drug Test - Random

- Ret-work = Drug Test -
 Return-to-work

##  Description

 Enter a description of this code, up to 30 characters.

##  Cert Period

Specify the period (in months) that identifies how long this skill's certification period lasts. The certification period will be used in conjunction with the class completion date to send notification (via Notifier) when a resource's skill certification expires.

##  Safety Related

 Check this box if this is a safety-related code.

##  Leave Type

 The system enables this field when you select ‘C’ in the Code Type field.
 Select this checkbox if this code is associated with a leave type. When you select this checkbox, this code is available for selection in the Leave Code fields on the HR Leave Request and HR Multi-Day Leave Request forms. For more information on leave requests, refer to Leave Requests in Related Topics below.

[](/en/vista/vista/hr-and-payroll/human-resources/leave/about-leave-requests)Leave Requests

##  PR Leave Code

 The system enables this field when you select the Leave Type checkbox.
 Enter the PR leave code to associate with this HR leave code. When you enter a leave code here, leave total information for the resource displays on the HR Leave Request (Leave Totals by Code section) and HR Leave Approval (Leave Totals by Resource and Code) forms. If you do not specify a PR leave code, leave total information does not display in HR.
Note: If you have not updated leave information in PR, the totals that display in HR may not be accurate. Furthermore, HR does not update PR; changes to leave totals in HR will not reflect in PR.
 For more information on leave requests, refer to Leave Requests in Related Topics below.

[](/en/vista/vista/hr-and-payroll/human-resources/leave/about-leave-requests)Leave Requests
