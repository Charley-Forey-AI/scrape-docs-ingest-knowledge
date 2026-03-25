---
title: "Set Capped Codes and Limits | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-capped-codes-and-limits_1"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-capped-codes-and-limits_1"
---

# Set Capped Codes and Limits

When setting up crafts and classes, you can establish a
 maximum employee benefit package.
Typically, this feature is used by non-union contractors performing prevailing wage work and provides the ability to establish an hourly limit per classification when individuals have different benefits paid.
In order to accomplish this you must identify the earnings and liabilities that make up the hourly rate for each classification's benefits package. If the total amount does not reach the prevailing wage, you can create add-on earnings (capped) codes that have flexible rates that would allow an employees to reach the wage.
For example, a classification is set up that pays $15.00 straight time wages and the employer pays insurance of $1.50 to $2.50 per hour (based on dependents) and pension of $2.00 per hour; this makes a total of $18.50–$19.50 per hour. A prevailing wage job sets the rate of pay at $20.00 per hour for the class (including employer-paid benefits). In this case, an additional earnings amount is required to meet the prevailing wage/limit. You could create a fringe earnings code that would reach the limit.
The following instructions detail how to establish a maximum employee benefit limit, and create additional earnings (capped) codes to reach the limit.

1. In PR Earnings Codes,
 [create the additional (capped) earnings
 code(s)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form). The codes you set up must have a method of H-Rate per hour.


1. In PR Craft Classes,
 [add the capped earnings code(s) to the applicable
 craft/classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form). Set the rate for each capped earnings code at the
 highest amount it would pay. Using the example above, the maximum would be
 $1.50.

1. In PR Crafts, select the
 Capped Basis tab and add the employees regular earnings code(s), the capped
 earnings code you created in step 1, and all applicable employer liability codes
 (to which the earnings are subject). Liability codes added here must have a
 method of H-Rate per hour or A-Amount AND a calculation category of C-Craft,
 E-Employee, or A-Any.Note: Liabilities must also be set up on the
 Dedns/Liabs tab in PR Crafts, PR Craft Classes, PR Craft Template, PR Craft
 Class Templates, or PR Employee Dedns/Liabs to ensure they are included when
 calculating capped basis and rates. Employee-based liabilities are only
 included in the capped basis calculation if the liability's frequency
 (assigned in PR Employee Dedns/Liabs) is set up in the Active Frequency
 Codes grid in PR Pay Period Control.

1. For earnings and
 liabilities that need to be included in prevailing wage and capped calculations
 for only a particular job or jobs, use the Capped Basis tab in PR Craft
 Templates to set up the applicable earnings and/or liability codes. Liability
 codes added here must have a method of H-Rate per hour or A-Amount AND a
 calculation category of C-Craft, E-Employee, or A-Any.The earnings and liabilities
 added here will be included in prevailing wage and capped calculations for
 employees working on any job assigned this template (in JC Jobs, PR Info
 tab), in addition to the earnings and liabilities specified for the
 employee’s craft on the Capped Basis tab in PR Crafts. If you specify an
 earnings code or liability code on the Capped Basis tab in both PR Craft
 Templates and PR Crafts, the rate for that code will be used only once in
 calculations (it is not duplicated).”

1. In PR Crafts, select the
 Capped Codes tab and add the capped earnings code(s), since they have the
 adjustable rate.Note: You can designate as many
 earnings/liabilities codes as necessary that are adjustable to meet the
 limit. These codes are reduced in order by sequence number; the first
 sequence is reduced down to zero first, then the second, and so forth. These
 codes apply to all classes for the craft, and to all templates. The capped
 limit may differ by job by using Craft/Class templates.
Note: Employee-based liabilities (those with a
 calculation category of Any or Employee that are flagged as employee-based
 in PR Employee Dedns/Liabs) should not be set up in the capped codes; only
 craft-based codes are reduced based on the capped amount.

1. In PR Craft Classes,
 [set up the appropriate prevailing wage hourly,
 benefit, and total wage rates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes). The system uses the effective date
 specified in PR Crafts or PR Craft Template to determine which rates are
 used. You can also override class
 prevailing wage rates at the craft class template level in PR Craft Class
 Templates. For more information, see [Setting Up Craft Class Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-class-templates).
The system will first calculate
 the wage using all of the earnings and liabilities codes set up on the
 Capped Basis tab. Then the system subtracts from the amounts entered on the
 Capped Codes tab until it meets the limit specified for the class. Using the
 example above, the system would use a fringe earnings rate of $1.50 an
 employee who received $1.50 for insurance ($20.00 less $18.50). For an
 employee who received $2.50 for insurance, the system would use a fringe
 earnings rate of $0.50 ($20.00 less $19.50).

Related information

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)
