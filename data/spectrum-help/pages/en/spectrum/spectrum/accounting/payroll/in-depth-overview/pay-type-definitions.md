---
title: "Pay Type Definitions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/pay-type-definitions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/pay-type-definitions"
---

# Pay Type Definitions

Use these predefined pay types when entering employee time cards.
In Pre-Time Card Entry, Layoff Check Entry, and Time Card Entry, the pay type helps determine at what rate the employee is to be paid.
Use the pay types shown below when entering employee time cards, and the application will use them during processing. When adding a new entry, the default pay type is Regular.
While most employees are hourly or salaried, pay types such as Overtime and Commission make it possible to tailor the payroll as you need.
All of these pay types are supported during the Pre-Time Card Import Update.

- Note that salaried employees may not receive overtime or double time pay unless the employee's pay type is Overtime salaried.

- If the pay type is an Incentive pay type, the special character designated in the Payroll Installation screen Incentive pay code field must appear before the Regular, Overtime, or Double time character.

 Pay Type Definition
R Regular
O Overtime
D Double time
V Vacation
H Holiday
S Sick
C Commission
M This is a flat amount to be paid to the employee. It can be used to record per diem. The G/L number can be defined separately in the Payroll > Department Expense File Maintenance > Miscellaneous field.
ER Equipment Regular Hours This pay type prompts you to enter an Employee code, Equipment code, Job, Phase, and Cost type. Use this pay type to pay an employee for the number of hours he/she used this equipment on the job, while also charging equipment hours to the same job. The rate paid to the employee will be different from the rate to charge equipment hours to the job.
EO Equipment Overtime Hours This pay type prompts you to enter an Employee code, Equipment code, Job, Phase, and Cost type. This is very similar to pay type ER used to record regular hours. The only difference is these are overtime hours at an overtime rate versus regular hours.
ED Equipment Double Time Hours This pay type prompts you for an Employee code, Equipment code, Job, Phase, and Cost type. This is very similar to pay type ER, which is used to record regular hours. The only difference is ED contains double time hours at a double time rate versus regular hours.
EU Equipment Usage This pay type is used to enter hours for Equipment Usage on jobs. Enter the Job, Phase, Cost type, and Equipment code. The hours entered appear on the Equipment Usage Report in Equipment Control. They will also be charged to the specified job, phase, and cost type. These hours are not paid to an employee.
SR Special Rate This pay type may have a special rate that must be set up in Employees first. This is the amount per hour to be paid to the employee for services performed outside of the normal pay rate. You may override the special rate, if necessary. Therefore, it is not mandatory to assign a special rate in Employees before using this pay type.
SA Special Amount This pay type may have a special amount that must be set up in Employees first. This is not an amount per hour but a flat amount to be paid to the employee. You may override the special amount, if necessary. Therefore, it is not mandatory to set up a special dollar amount in Employees before using this pay type.
RP Retro PayUse this pay type in cases when the union contract was signed and the rates are retroactive. The rate entered is equal to the difference between the hourly rate paid and the rate that should have been paid. The hours entered are strictly for computational purposes and will not update; they will not duplicate the hours already entered and updated. Only the additional amount paid will appear on Payroll and Job Cost reports.
You can choose to enter retro pay manually, or you can select the Automatic retro pay option. If you choose Automatic retro pay, an additional window opens, which allows you to choose which union or pay group and work dates to apply the retro pay and which date to use to post the retro pay in Time Card Entry.

JX Job Only Adjustment Hours This pay type prompts you to enter a Job, Phase, and Cost type, but is not actually paid to an employee. They are charged to the job only at the rate that would have been paid to the employee. An example of using this pay type is charging hours to a job for a non-employee. This non-employee may have been hired through an outside, temporary employment service. This pay type will not produce a check for the non-employee.
These hours are not reflected on any Payroll reports, such as Certified, Union, or Tax Reports. It is necessary to complete a Job Cost Transaction Update after updating Payroll because updating payroll creates Job Cost transactions waiting to be updated.

Pay type 1, 2, or 3 Other pay types 1, 2, or 3 are given default descriptions (for example: Bonus, Truck, Other, and so forth) in the Payroll Installation screen and require entry of a flat amount to be paid to this employee. The G/L account numbers can be defined separately in the PR Department Expense File Maintenance screen's Other earnings 1, 2, or 3 fields.
I (for example) Incentive PayIt is necessary to set up a special code in the [Payroll Installation - Properties](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---properties) screen that will designate Incentive Pay when used during Time Card Entry , Layoff Check Entry, and Pre-Time Card Entry (for example, the code I).
Make sure you do not choose a code that will duplicate a deduction or add-on code when used with R, O, or D  (for example, you might want to use an asterisk).
This code is entered along with the Regular, Overtime, and Double time pay types during Time Card Entry, Layoff Check Entry, and Pre-Time Card Entry. This pay type opens the Quick Hours Entry window; you may enter employee hours for each day and the amount of incentive pay.
Incentive pay can be entered as a total or the units times the incentive rate. Spectrum selects the higher of the Incentive Pay rate or the Standard pay rate for these time card lines.

U Unpaid TimeUse this pay type to identify and process unpaid time. This pay type is strictly for record keeping purposes, allowing you to track unpaid time (such as unpaid medical absence, comp time, and so forth).
These hours will not be included as part of paid hours to employees and will not affect the General Ledger. They cannot be charged to jobs. This pay type will not appear on any Payroll reports or inquiries, other than the Edit Listing and Time Card History Report.
