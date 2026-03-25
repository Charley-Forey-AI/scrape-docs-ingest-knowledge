---
title: "PR Automatic Earnings Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-automatic-earnings-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-automatic-earnings-form"
---

# PR Automatic Earnings Form

Use the PR Automatic Earnings form to set up automatic earnings such as salary or car allowances.
Once you set up automatic earnings in this form, you can then run the PR Post Auto Earnings form to generate a batch of timecards from the entries without being required to manually enter each Employee’s earnings.
You will typically use automatic earnings for salaried earnings and any other earnings that are constant. Any recurring earnings that can be calculated as follows may be set up here.

- Rate per hour — based on either total hours already posted to the employee, hours entered here or the standard number of hours for the group pay period.

- Rate of gross — based on the total earnings (subject to automatic add-ons) already posted to this employee.

- Rate per day — based on the total number of days worked; uses the days to which earnings have been posted or the standard number of days for the group pay period.

- Flat amount — uses the amount entered here (such as salary).

The sequence number assigned to each entry is used to keep entries unique within Employee and Earnings code, allowing for multiple distributions per earnings code. This number also determines the order of automatic earnings.
If you have earnings that you want only posted to a specific payment sequence in each pay period, you can enter a payment sequence number for applicable auto entries. The payment sequence entered here overrides the Pay Seq # entered when a batch of automatic earnings is processed. If all pay sequences are eligible to have earnings calculated, then leave this field blank. The value entered here can be used to direct salary to Pay Seq #1, or to direct auto allowance to a second pay sequence # that will be paid on a separate check.

## Override Standard Limit

The Override Standard Limit option allows you to override the standard limit for an earnings code by employee. The Standard Limit and Limit Type (Annual, Monthly, or Pay Period) for the earnings code is shown in the informational display above this option; standard limits and limit types are defined for each applicable earnings code in PR Earnings Codes. When checked, the override amount is entered to the right. If the limit is changed for an earnings code, all employees are updated with the new limit. If an override limit has been defined for an employee, it will not be updated. The override amount must be changed manually as necessary. Note: If you define an annual limit for this code’s earn type in HQ Earn Types (Annual Limit field), the system uses that limit when processing multiple codes with the same earn type (PR Post Auto Earnings). For more information, see the F1 help for the [Annual Limit](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-earn-types-form/field-definitions-hq-earn-types-form#ID-0000eda9--en) field.

## Equipment Usage/Mechanic's Timecards

The Equipment Usage/Mechanic's Timecards section is used to indicate whether automatic earnings include equipment usage or mechanic's time cards.
First, you must specify the EM company and equipment. Then, indicate whether to use the Equipment Usage or Mechanic's Time option. If automatic earnings do not include equipment usage or mechanic’s time, select the None radio button.
The Equipment Usage option can only be selected if you allow entering equipment usage with payroll timecards (option in PR Company Parameters). In addition, earnings must be posted to a job; therefore, you will need to specify a JC Co#, Job, and Phase in the "Post To" section. When this option is selected, the 'Revenue Code' and 'Usage Units' inputs are enabled, allowing you to specify the revenue code and the number of units to post for equipment usage.
If you are charging an employee to a piece of equipment, select the Mechanic's Time option. Selecting this option enables the Cost Code input, allowing you to specify the cost code to which the mechanic's labor costs will be posted.

For more information about this form, click the link below.
[About Updating Salary Changes to Auto Earnings](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-updating-salary-changes-to-auto-earnings)

Related information

- [Create Allowances](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances/create-allowances)

- [About Posting Automatic Earnings](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-posting-automatic-earnings)
