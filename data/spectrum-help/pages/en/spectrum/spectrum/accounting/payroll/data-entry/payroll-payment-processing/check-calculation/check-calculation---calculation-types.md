---
title: "Check Calculation - Calculation Types | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/check-calculation/check-calculation---calculation-types"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/check-calculation/check-calculation---calculation-types"
---

# Check Calculation - Calculation Types

Use the following information for check calculation
 types.

## Pre-Time Card Import Errors

If any records are being held in the Pre-Time Card Import Errors screen a warning will display before you are allowed to proceed, telling you that these records will not be updated to Time Card Entry. [Warning - Errors still exist](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/warning---errors-still-exist)
If replacement checks are already in progress, a warning message displays to let you know that the checks have not yet been transferred. Following this warning, a Replacement Check window displays a list of the replacement checks still in progress. You can click the OK button to proceed with to Check Calculation or you can click Cancel to exit Check Calculation while you transfer the replacement checks to Time Card Entry.
After the update is performed, the Payroll Wage and Tax Listing and the Pre-Check Register should be printed and reviewed for accuracy. Note that the burden % specified in the Phase Rate Override window will be used if the rate is a non-zero figure. The software also first searches the check file for duplicate check numbers before updating. If a check number has been used more than once during this check cycle, an on-screen report with the check number and both employee names will display. If there are no duplicate check numbers, the update will continue as usual.

## Pay Groups and Unions

When a pay group or union is specified on a time card line, the specified deductions and add-ons for this pay group/union will be calculated for the employee and included on the check. The computation for the check will be based on either the time card line or the pay group/union total depending on the formula file setup. If the pay group/union contains prevailing wage information, Health & Welfare and Prevailing Wage Adjustment paid on the employee check will be computed and applied to the check. Any non-cash Prevailing Wage Adjustment will also be computed and applied on the employee's behalf. If the rate for a deduction or add-on is left blank in the pay group or union file, then the computation will be based on the rate specified in the Employee Deduction / Add-on Code Maintenance screen.
If the wage code has been assigned a benefit tier, Spectrum will use the override settings to apply a tier-specific rate. If there is no override setting assigned to that benefit tier, the standard union rate will be applied instead.
If the union add-on has been assigned the non-standard fringe calculation method, the standard pay rate will include the non-stated fringe and the employee rate will be adjusted automatically.

## Worker's Compensation Rate per $100

Check Calculation also computes the worker's compensation rate per $100 amounts up to the limit (if any) specified in the [New/Edit Tax Table - Other Taxes](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---other-taxes)
For Pay per cycle limits, the computation applies the tax rate across check sequences for an employee up to the specified limit. Then the next pay cycle will start over and apply the tax rate across sequences again. For Annual limits, the computation applies the tax rate across check sequences on a year-to-date basis for an employee up to the specified limit. The 'subject to' earnings used to calculate worker's compensation is the extension of the time card line (unless it is an exempt pay type), adjusted for straight-time equivalent if applicable for the code, then subject to the limit, if any. 'Subject to' earnings for add-ons in the time card file are computed if the state specified on the time card line is set up to 'Y' (taxable) in the Tax Effects window of Deduction / Add-on Code Maintenance. In this case, the add-on amount will be included in 'Covered Earnings' up to the limit.
The software maintains employee year-to-date totals 'subject to' worker's compensation by state and Check Calculation determines at each time card line whether the state total has exceeded the specified limit. The update calculates the worker's compensation based on the time card line order and will first process the worker's compensation for the pay type lines across sequences. The software will determine if each line is included in the 'covered earnings' and if so, it will then determine if the limit has been reached. If the limit has NOT been reached, the worker's compensation tax amount is computed and rounded to the nearest penny. After all the pay type lines have been processed, and any union fringe add-ons are added to the time card file, the software will compute the worker's compensation on the add-ons. Calculations for worker's compensation code computed using the rate/hour method are not applicable here. Limits and add-on adjustments do NOT affect the calculation of these codes because they are calculated only based on hours (for pay types R, O, D, SR, ER, EO, ED, V, H, and S, unless exempted in Tax Table Maintenance).
A special exception report will also display during this update to list time card lines with no work state entered. The report also shows employees with time card lines which have a work state, but contain a workers' compensation code which is not valid for that state. The check calculation update must be performed again after those time card lines have been corrected. This error check is primarily designed to detect problems which may have originated at Job Sites.
A second exception report may also display on the screen showing deductions or add-ons not taken during the cycle due to various constraints. These deductions or add-ons will not be included on the employee's check unless the constraints are resolved and the Check Calculation Update is performed again.

## Unemployment Multi-State Excess Calculations

The year-to-date limit for Unemployment calculations for jurisdictions with a 'Limit basis' set to 'All States' in [New/Edit Tax Table - Other Taxes](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---other-taxes) calculates the SUTA limit based on 'subject-to' earnings where tax was assessed (instead of using total YTD 'subject-to' earnings, including excess). In other words, the system calculates the sum of 'total subject-to' earnings minus any excess of each state in which the employee worked during the current year to determine whether the employee is over the limit for SUTA.
In addition to state unemployment, the software permits the Payroll Manager to set up unemployment tax for County and Local jurisdictions. Like for states, the software provides the SUTA calculation when figuring whether the employee is over-limit for Counties and Locals.

## Income Tax Deductions and Tax Adjustments

If tax adjustments are being used, as the income tax of each code is being calculated the system will read for adjustment codes assigned to the tax codes and increase or decrease withholding based on the adjustment type. This calculation is performed before dividing the annualized income tax deduction amount back to the current period.
If multiple adjustment codes are assigned to the Tax Table Code, the system calculates each adjustment separately in the sequence order (in order to sum up all tax adjustments, then add that total to the income tax amount).
This functionality is provided because Ontario's 'Tax Reduction' calculation include the adjustment amount computed for Ontario Surtax.

## Entity-Specific Override

The Check Calculation (and Layoff Check Calculation) look for entity-specific override tax rates for SUTA, Employee SDI, Employer SDI and Worker's Compensation when 'Entity tracking' is enabled in Enterprise Installation and the current pay cycle is for an entity other than the 'main company entity'--meaning that an override rate exists for the SUTA, SDI, and/or Worker's Compensation rates for the entity code assigned.

## Non-Standard Calendar Year

If the Extra pay period this year checkbox is selected in [New/Edit Tax Table - Income Tax tab](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---income-tax-tab), check calculations will be adjusted to include an extra pay period for the current year to annualize wages for weekly and bi-weekly employees when calculating all taxes (federal, state, county, local).
