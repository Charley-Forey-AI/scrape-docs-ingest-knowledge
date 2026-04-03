---
title: "Wage Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/unions--wage-code-procedures/union--wage-codes/wage-codes"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/unions--wage-code-procedures/union--wage-codes/wage-codes"
---

# Wage Codes

The wage code system may be used to expand the power of
 union codes.
Rather than entering classes in the union rate level fields, as illustrated above for
 Laborers, classes are indicated by wage codes; levels in the union file may then be used to
 indicate pay rates for apprentices, journeymen, supervisor's, and so forth. This greatly
 expands the number of default pay rates.
Wage Code: LB
Laborer
Regular
Overtime
Double

Level #1: Apprentice 70%
$ 7.00
$10.50
$14.00

Level #2: Apprentice 80%
$ 8.00
$12.00
$16.00

Level #3: Apprentice 90%
$ 9.00
$13.50
$18.00

Level #4: Journeyman
$10.00
$15.00
$20.00

Level #5: Supervisor
$10.50
$15.25
$21.00

For those using the Job Cost module, combining wage codes with union codes has an additional advantage over the standard union code system.
Enter the wage code and union code combination in the Job Maintenance screen. You can enter only one combination for a job; during time card entry, the wage code will default from Employees (for example, laborer, operator), or from Equipment File Maintenance (if an equipment code ER, EO or ED pay type is entered). Once the wage code is defaulted and the job is entered, the software will automatically default the union code from the job file (remember, there is only wage code/union code combination per job). This combination will set the pay rate.
When using Job Maintenance to set up a job in which unions are used, enter the wage codes for all types of work which will be performed, then specify which union's rates for that wage code should be paid on this particular job. Enter the union code to use for the dues.
To set up a hypothetical job in Seattle, view the wage codes column above and specify the wage/union combinations needed (L1-242, L2-440, and so forth). This will set the defaults. By specifying a wage/union combination in the job file, all unions not specified will be excluded; the software knows which union to look at for rates.
Then, during Pre-Time Card Entry and Time Card Entry, every time an employee with "L1" wage code specified in Employees has hours on this job, the software will look at the union file for the corresponding union (242) and pay that employee the hourly rate for the level specified in the employee file (for example, a level "4" employee would receive $15 per hour in this example).
Another option available in the use of wage codes is for each type of worker to be set up in the wage code file (L7 = laborer apprentice 70%, L8 = laborer apprentice 80%, and so forth). This is of particular benefit to those performing work on a single job across multiple years. In this instance, the pay levels can be used for each contract year's rates. (This is also an option with prevailing wage jobs.)
Just as a wage code and union code is specified in Job Maintenance, the level number can also be specified. The software will then automatically determine which contract year should be paid by looking at the default level defined in Job Maintenance; if that field is blank, the level will default from the Employees screen.
You must set up a different union code for different employer fringes that must be paid. For example, if a union has different employer fringe rates that they pay for apprentice 70% versus apprentice 90% versus journeyman, then a different union code must be set up. You will not be able to use the level numbers for these different pay rates.
There is another option for paying fringes. If you must pay Davis Bacon prevailing wages to an employee with these fringes, you can set this up in the union file as another pay type. This allows the fringe to show up separately on the check stub (as "other" pay); additionally, the information will print under the "benefits paid" column on the Certified Payroll Report. The other option is to just increase the employee's pay rate by the amount of the fringe.
