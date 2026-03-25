---
title: "Field Definitions: PR Automatic Earnings Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-automatic-earnings-form/field-definitions-pr-automatic-earnings-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-automatic-earnings-form/field-definitions-pr-automatic-earnings-form"
---

# Field Definitions: PR Automatic Earnings Form

The following is a list of field descriptions for the PR
 Automatic Earnings form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Employee

 Enter a valid employee number for which automatic earnings are to be calculated.

## Earnings Code

Enter a valid earnings code. These might be salary or salary reduction codes such as 401k etc.

##  Seq#

 Enter a sequence number to keep entries unique within employee and earnings codes to allow for multiple distributions per earnings code.

## Payment Seq#

Enter a payment sequence number if you want these earnings posted only to a specific payment sequence in each pay period. A value entered here overrides the pay sequence number entered when a batch of Automatic Earnings are processed. Leave this field blank if all pay sequence numbers are eligible to have these earnings calculated (i.e., 401k earnings to be added to all subject earnings regardless of Pay Seq#). A value here can be used to direct salary to Pay Seq#1, or to direct auto allowance to a second Pay Seq# that will be paid on a separate check.

##  Department

 If you want to override the employee’s standard Payroll department, then enter a valid department.

##  Ins Code

 Enter a valid insurance code if you want an insurance code posted with these earnings. The Insurance State is controlled by the employee and PR Company Parameters options.
Note: If you selected
 the Use Override
 Code When Pay Rate Exceeds Threshold Rate checkbox in PR State Insurance
 Codes for this insurance code and the employee's combined pay rate and applicable add-on
 earnings are equal to or greater than the specified threshold rate, the system will use the
 override insurance code. Applicable earnings are those where the earnings code is included
 in the liability's basis codes, and where the calculation method is F-Factored Rate per
 Hour, H-Rate per Hour, or V-Variable Factored Rate.
Note: For more information, see [About Override Insurance Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-california-override-insurance-codes).

##  Craft

 If you want these earnings posted to a Craft, then enter a valid Craft Code.

##  Class

 If you want these earnings posted to a craft class, then enter a valid craft class combination. This field is required if a craft is entered in the previous field and is disabled if the craft is blank.

##  JC Co#

 Enter a JC Company number if you want these earnings posted to a job.

## Job

Enter a job that has been set up in the JC
 Jobs to which these earnings will be posted. This field may be blank if not posted to a
 job. This field will be validated.
Note: If you enter a soft- or hard-closed job, the status displays in red in the header. The system will only save the record if you allow posting to soft or hard-closed jobs (flags in JC Company Parameters).

##  Phase

 If posted to a job, then enter a phase to which these earnings will be posted in Job Cost. Standard phase validation applies and the phase group is based on the JC Company number.

##  GL Co#

If posted to a job, the GL company is based on the JC company, and this field is disabled.
 If the earnings are not posted to a job, then enter the GL company to be expensed when initializing automatic earnings. If left blank, when initializing auto earnings, the GL company specified for the employee in PR Employees is used. If no GL company specified for the employee, the GL company specified in PR Company Parameters is used.

##  Override Pay Period's Standard Hours

 Check this box if you want to enter the hours here.
 Do not check this box if you want to use the standard hours specified in the PR Pay Period Control form for the group and pay period.

##  Hours

 Enter the number of hours to post; enter zero to have the system default the number of hours posted this pay period to Earnings that are Subject to Automatic Earnings. If you enter zero, the system treats the timecard as an add-on, posting zero hours and multiplying the rate by the posted hours in this pay period

## Use Regular Hourly Rate

Check this box to use the employee's rate
 (from PR Employees, Hourly Rate field) or the employee's rate based on the craft/class/template
 hierarchy for this automatic earnings. The system uses the higher of the two rates.
Note: This functionality is meant to be used in conjunction with [tracking Australian RDO accruals](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/track-rostered-days-off-accruals-australia). However, users in other countries may find additional uses for this functionality.

## Rate/Amount

Enter a rate or an amount that is interpreted based on the earnings method. Negative values are valid.
Note: The rate or amount entered here must be of the same sign as the standard limit. For example, if the standard limit is a negative value, the rate/amount must also be a negative value. If they do not match, you will receive a message stating that the Rate/Amount and Standard Limit must both be of the same sign. You will need to correct the value before you can save the record.

 If you enter a salaried employee, this field defaults the salary amount from the Salary field in PR Employees. If you enter one or more additional sequences for the same earnings code, the amount specified here should represent the portion of the total salary applicable to the sequence. The sum of all sequences for the employee/earnings code should equal the total Salary amount. For example, if you enter one sequence for Earnings Code 1, Job 100 and one sequence for Earnings Code 1, Job 200, and each represent 50% of the total salary ($1,000), you would enter $500 in this field for each sequence.
Note: If you selected the Update Auto Earnings checkbox for an employee/earnings code in PR
 Employees that is also set up in PR Automatic Earnings, changes to the employee's
 salary will update this field for the specified employee/earnings code. For more
 information, see [About Updating Salary Changes to Auto Earnings](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-updating-salary-changes-to-auto-earnings)..

##  Override Standard Limit

 Check this box to override the standard limit specified for this earnings code in PR Earnings Codes for this employee. (The Standard Limit and Limit Type for this earnings code is shown in the informational display above.)
 Do not check this box if you do not want to override the standard limit specified for this earnings code in PR Earning Codes.

## Override Limit Amount

Enabled only if the Override Standard Limit option is checked.
Enter the limit amount (to override the standard limit defined in PR Earnings Codes) for these earnings, or enter 0.00 if no limit applies. Negative values are valid.
Note: The amount entered here must be of the same sign as the rate/amount. For example, if the rate/amount is a negative value, the override limit amount must also be a negative value. If they do not match, you will receive a message stating that the Rate/Amount and Standard Limit must both be of the same sign. You will need to correct the value before you can save the record.

##  Frequency

 Enter a valid frequency code to indicate which automatic earnings will be active in the pay period.

## Equipment Usage/Mechanic's Time

Indicate whether these earnings include equipment usage, mechanic's time, or neither.

- None – Select if earnings do not include equipment usage or mechanic’s time.

- Equipment Usage – Select this option if these earnings include equipment usage and are posted to a job. When selected, the Revenue Code and Usage Units inputs are enabled.

Note: This option can only be selected if the "Enter Equipment Usage with Time Cards" option is checked in PR Company Parameters. Also, if using this option, you must specify a JC Co#, Job, and Phase above.

- Mechanic's Time – Select this option if these earnings include mechanics' time. You will typically select this option when you want to charge the employee's time to the equipment. When selected, the Cost Code input is enabled.

##  EM Co#

 If these earnings include equipment usage or mechanics' time, enter a valid EM Company number to qualify the equipment.

##  Equipment

 Enter a valid equipment code that has been
 set up in the EM Equipments form to which usage revenue or mechanics' time will be
 recorded.

##  Revenue Code

 Enabled only if 'Equipment Usage' option is selected above.
 Enter a valid equipment revenue code to identify the type and rate charged to use this equipment.

##  Usage Units

 Enabled only if 'Equipment Usage' option is selected above.
 Enter the number of time units to post for equipment usage. Typically hours, but can also be days, weeks, and months, to name a few.

##  Cost Code

 Enabled only if the 'Mechanic's Time' option is selected above.
 Specify the cost code that will receive this mechanic's labor costs.
