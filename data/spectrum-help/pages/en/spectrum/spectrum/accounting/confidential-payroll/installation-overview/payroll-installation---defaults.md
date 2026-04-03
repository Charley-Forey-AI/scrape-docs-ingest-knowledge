---
title: "Payroll Installation - Defaults | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/confidential-payroll/installation-overview/payroll-installation---defaults"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/confidential-payroll/installation-overview/payroll-installation---defaults"
---

# Payroll Installation - Defaults

A reference for completing the fields in the Defaults tab of the Payroll Installation screen.
Use this tab to set up or change the default settings for the Payroll module.
Fields/ButtonsDescriptions
Utilize pay cycle calendar?If you select this checkbox, the check date and period end date will default from the calendar when the Payroll cycle is set. The software warns you if a date has already been set up or used.
Number of working hours per weekEnter the standard number of hours a full-time employee works during a normal week.
The figure stored in this field will be used by the software when employees are added. The number of hours specified here will default in the Employees > Financials window but may be over-written if desired. The figure stored in the employee file is used in turn when the automatic time card feature is specified during the Set Payroll Cycle update.

Default rate table
UnionsSelect to make Union rates the default pay rate throughout the Payroll module.
Wage codes/unionsSelect to be able to set up multiple pay rates (two-digit alphanumeric) for each union code. This is especially useful if you use heavy equipment and must pay union scale wages depending on the type of equipment getting operated. In this case, there can be up to thirty different pay rates within the same union. The wage code can then be set up in the Equipment Maintenance page so that when that equipment is entered in the time card entry, the correct wage code will automatically default.
For each wage code there are also up to nine pay levels which can be used for the contractual year of the pay agreement and this pay level can be set up in the job file for automatic default. An additional feature allows you to set up the wage/union code combination in the Job Maintenance page so that the correct union code will also default from the job file during Time Card Entry.
All these default features are available when using the wage code system.

Pay groupsSelect to use the pay group file to default the pay rate in Time Card Entry.
The rate from the pay group file may be modified using a percentage stored in the Employees page. This is particularly useful for apprentices who may less than the full rate for that pay group level.
Each pay group may also be set up with a default rate by employee, or by employee and job phase code.

Post to Job Cost using standard labor rates?Note: Applicable only if the Equipment Control module is installed.
Select this checkbox to enable standard cost functionality.
For more information about standard labor rates, refer to the [Standard Costing in Payroll](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/standard-costing-in-payroll) in-depth article.

Default equipment rate
Entry in this field affects how the equipment rate defaults when entering equipment lines during time card and pre-time card entry.
If this field is changed mid-Payroll cycle, the change will take effect during the next new cycle.Note: Applicable only if the Equipment Control module is installed.

Default rates are set up in Equipment Control > Maintenance > Equipment File Maintenance or per job in Equipment Control  >  Maintenance > Job/Equipment Rates File Maintenance.

Full rateIf you select Full rate, the full charge rate for equipment will default.
Operating rateIf you select Operating rate, operating rate for that equipment will default. This flag may be overridden when actual time card lines are entered.
Hide fringe tab in Union File Maintenance?Select this checkbox if you will be tracking union fringe benefits using add-on codes, or if you do not utilize union functionality.Note: This checkbox is unavailable if the Pay groups default rate table option was selected above.

Use Nacha service class code 200 and balanced file format?Select this checkbox to use the Nacha service class code 200 and balanced file format.
The service class code identifies the general classification of dollar entries to be exchanged. The three possible entries available in PPD transactions are 200 (mixed debit and credit transactions), 220 (credit only transactions), and 225 (debit only transactions). Primarily, 200 will be used. Check with your bank to verify what it requires for input.

Calculate actual pension benefits for the D-B/Prevailing wage employer benefit credit?If you select this checkbox and the employee's pay rate is higher than the base pay rate in the non-union pay group file, the prevailing wage adjustment is reduced by the 401(k) amount and the employer benefits (Health & Welfare) are increased. Furthermore, if the Adjust prevailing wage fringe checkbox is selected, this will reduce the fringe even more.
If you select this checkbox, an additional Is this computed as part of the D-B/Prevailing wage employer benefit checkbox will display in the Deduction / Add-on Maintenance > Add-ons tab for all non-cash add-ons. This prompt is not available for Health & Welfare or Prevailing Wage Adjustment codes.
To view an example that uses this checkbox, refer to the [Example - Check Calculation for Davis-Bacon and Prevailing Wage Jobs](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/example---check-calculation-for-davis-bacon-and-prevailing-wage-jobs) page.

Trimble Construction One HR ManagementFor new hires that are onboarded from Trimble Construction One, specify the default employee status that appears on the Employee Main Properties screen.
Default pay rate
Union/pay group rateSelect to have the union rates take precedence over the rates in Employees. If the rates in the employee file are zero for all union employees, this installation option does not affect your processing. For users selecting the non-union pay group option, the software will look first to the pay group file and default this rate if non-zero. If zero, the software will then default the pay rate based on the employee master file.
Employee pay rateSelect to always have the Employee's pay rate override the union rate or pay group during Pre-Time Card Entry and Time Card Entry.
This is used for union companies that pay certain senior employees or other employees pay rates that are different from union scale. However, they are still union employees and will be listed on the union reports and then union fringes still apply. For other union employees, you would enter a pay rate in Employees, then the union rates would default in Pre-Time Card Entry and Time Card Entry.
The system would look in the employee file first and the rate would be zero, so it would then look to the wage code or union file for the rate. This sets the default only when entering time card lines or using the automatic pay cycle; the pay rate can be overwritten during entry. If you select the non-union pay group option, the software looks first to Employees and default this rate if it is non-zero. If zero, the software defaults the pay rate based on the non-union pay group.

Higher of the two ratesSelect to default the higher of the union/wage code rate and the Employees pay rate for the time card line. If you select the non-union pay group option, the software defaults the higher rate of the employee master file and the non-union pay group file.
Adjust prevailing wage fringe?Appears only if the Default employee pay rate option is set to Higher of the two rates.
If this checkbox is selected and the employee pay rate is higher than the pay group, then the prevailing wage adjustment will be adjusted downward by the difference between these two rates.
This allows employers to pay employees their regular pay rate (without adding any additional prevailing wage adjustment) when the employees are already being paid more than the prevailing wage specified for the job. It also allows the employer to pay a prevailing wage adjustment when the employee is paid more than the specified prevailing wage.Note: The prevailing wage adjustment rate is never less than zero.

Time Card Entry FieldsSelect to display the [Time Card Entry Fields Window](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/time-card-entry-fields-window) where you can designate which fields will be automatically skipped during time card entry.
Default overtime calculation method

Rate in effectSelect to have the system apply overtime costs to only the timecards which happen to have them occur.
Weighted averageSelect to have the system calculate overtime for each given seven-day working period and then apply the weighted average across all timecard lines during the same time period in both Pre-Time Card and Time Card Auto Overtime.
How Spectrum determines the weighted average

- The weighted overtime average is equal to the sum of all pay for all work, divided by the total number of straight time hours worked during the workweek.

- Straight time hours are R (regular), ER (equipment regular), and unless you exclude it, SR (special regular).

- The workweek is the existing seven-day working period.

Related information

- [Regular Pay Examples](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/regular-pay-examples)

- [Overtime / Double Time Examples](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/overtime--double-time-examples)
