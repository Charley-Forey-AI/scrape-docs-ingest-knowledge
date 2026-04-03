---
title: "Import Validations and Defaults | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/import-validations-and-defaults"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/import-validations-and-defaults"
---

# Import Validations and Defaults

Use the table below for reference on import
 items.
Import items
Additional info

Pay rates
During the import, the rate is determined by the
 wage/union code combined together with the rate level. The rate level
 defaults from the phase file, the job file or the employee file, unless the
 Default pay
 rate prompt is set to Employee pay rate or
 Higher of the two rates
 (and the employee rate is higher) in the Payroll
 Installation screen.
The pay rate will be assigned based on the work date. If
 the imported time card record does not have a work date, the pay rate will
 be based on the current Payroll processing date. Pre-time cards originating
 from Work Order > Labor Entry will use the same method to determine the pay rate when labor
 hours are updated.
For prevailing wage jobs with non-stated fringe, the
 standard pay rate will include the non-stated fringe and the employee rate
 will be adjusted automatically.
To view the wage/union codes default hierarchy, click
 [Wage/Union Code Hierarchy](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/wageunion-code-hierarchy). If you import a pay rate level, wage code, or
 union code, they will not be overwritten by the hierarchy.
If you are using pay groups, the employee pay rate will
 be assigned from the Phase Rate Override window of the Non-Union
 Pay Group File Maintenance screen. To see the Pay Group Rate
 Default Hierarchy, click [Pay Group Rate Default Hierarchy](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/pay-group-rate-default-hierarchy).

Salaried employees
 Salaried employees may be included in the import file,
 depending on the pay types used. During the import of salaried employees,
 the software will automatically distribute the salary amount among hours
 included in the text file. Inactive employees may be reactivated in order to
 process a time card.

Quantities
When importing quantities a separate line is used with a
 pay type of Q. There are no hours associated with this pay type but there is
 a cost type. Quantities will be updated (a time card edit list can be run
 just for quantities) to the cost type specified because the software will
 allow multiple cost types for quantity entered. It will not duplicate hours
 posted to the job as no hours are entered on this time card line.
'Quantity complete' records in the import file (Pay type
 = Q) will conditionally generate quantity pre-time cards for additional cost
 types of the phase referenced on the import line. The update will create a
 pre-time card line for the Phase and Cost type specified on that line of the
 import file, and conditionally create entries for other cost types set up
 for that phase.

Direct cost work order department
If the import line is a 'Direct work order cost'
 department, the import will validate four additional fields: Work
 order, Site equipment,
 Component and Contract.
Note: Entry of work orders with a status of
 'proposed' will be disallowed.

Direct equipment cost department
If the import line is a 'Direct equipment cost'
 department, Spectrum will verify the G/L account code associated with the
 designated pay type is not restricted. If the G/L account is not allowed for
 the cost category, the time card will be sent to error correction.

Worker's compensation
If the Always use this worker's comp code on time card checkbox is
 selected in Employees, the worker's compensation code
 for that employee will automatically be assigned, regardless of the code
 specified in the import file. After the worker's compensation code is
 assigned, the software will ensure the assigned code and work state/worker's
 comp combination is valid.

Deductions and add-ons
The import supports all valid deduction entries, valid
 add-on entries, and all of the [standard Spectrum pay
 types](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/pay-type-definitions). When importing deductions, be sure to set the pay rate to a
 positive number when the amount should be deducted from the employee's pay
 check. For add-ons, a positive pay rate value needs to be recorded when the
 amount should be added to the check. (Likewise, for add-ons not paid to the
 employee on the check, a positive pay rate is recorded to generate a
 positive employee benefit).If the pay type of the time card entry is ER, EO,
 ED, or EU and there are Active attachments for the equipment codes specified, the
 software will automatically generate additional EU time card records (unlike
 entries that are manually added into Time Card Entry, the software will not
 conditionally open a confirmation window). Equipment codes with an
 Inactive status
 will not automatically generate time card records.

Company code
If the Company code is different from the current company, the
 imported fields will validate against setup in the current company. When not
 specified in the import file, the fields will be set based on the same
 default hierarchy as in the entry screen.
If the reporting currency of the current (payroll)
 company is different than the reporting currency of the destination company
 and the Multi-Currency module is present, validation will be provided to
 ensure that a valid currency code is assigned to the specified account and
 is the same as the reporting currency of the current company.

Billing codes and rates
The system will validate whether a time card entry is
 applicable for billing.

- For an entry with a 'Direct job cost' payroll
 department, billing is only applicable if:

- The Time + Material module is present

- The specified job has been set up in Job
 Billing Setup

- The specified phase is applicable for
 billing

- For a 'Direct work order cost' payroll department,
 billing is applicable if the Work Order module is present.

- For 'Non-direct' and 'Direct equipment cost'
 payroll departments, billing is not applicable.

The system will read the validated text file to see if a
 billing code and billing rate have been assigned.

- If the billing code and billing rate are assigned,
 these values will be assigned to the pre-time card entry.

- If the billing code is assigned but the billing
 rate is blank, the billing code will be assigned to pre-time card
 entry but the rate will be left blank.

- If the billing code is blank but the billing rate
 is assigned, the billing code will be left blank and the rate will
 assigned to pre-time card entry.

- If the billing code and billing rate are blank,
 these values will be assigned from the pre-time card entry from setup
 in the Time + Material or Work Order modules.

- If the billing code is invalid, the time card
 record will be sent to the [Pre-Time Card Import Errors](/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/pre-time-card-import-errors)
 screen.

Related codesThe system will validate that related codes entered are not already entered
 as State, County or Local tax codes.

- Invalid codes will generate an error and move the
 pre-time card to the Pre-Time Card Import Errors
 screen.

- For records that are validated, all related tax codes will automatically
 be attached to the pre-time card.

Note: This validation only applies
 to pre-time card import, as related codes cannot be entered directly on to
 the pre-time card or time card records.
