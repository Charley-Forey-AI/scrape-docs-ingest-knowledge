---
title: "Set Up Example: Customer-based T+M Billing Amounts | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/procedures-overview/tell-me-how/set-up-customer-based-tm-billing-amounts/set-up-example-customer-based-tm-billing-amounts"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/procedures-overview/tell-me-how/set-up-customer-based-tm-billing-amounts/set-up-example-customer-based-tm-billing-amounts"
---

# Set Up Example: Customer-based T+M Billing Amounts

You can use the following to demonstrate how to set up T +
 M Billing accounts.

## Part A: Accounts Receivable – Customer File Maintenance

1. On the Site Map screen, click Accounts Receivable  >  Customers.

1. Add new customer DYNTMC.

1. In the Price levels section, enter Materials level 2
 and Labor level 1.

1. Save the entry and return to the main menu.

## Part B: Time + Material - Installation

1. On the Site Map screen, click Admin  >  Installation  >  Time + Material.

1. Click the Markups tab. Delete all the default markups
 and save your changes.

1. Next, click the Add-ons tab. Delete all the default
 add-ons and click OK to save your changes.

1. Next, click the Fees tab. Delete all the default fees
 and save your changes. All the system defaults for markups, add-ons, and fees
 should now be removed, and all future markups, add-ons and fees will be based on
 the customer.

1. Click Save again to return to the main menu.

## Part C: Job Cost – Job File Maintenance

1. On the Site Map screen, click Job Cost  >  Jobs.

1. Add the first job for customer DYNTMC (for example, DYNTMC – JI).

1. In the Address section, leave the
 Master field blank.

1. Make sure the Taxable field is set to
 No.

1. In the Price section, select Time +
 Material. The Earned Calc dialog box
 displays automatically; select Master job calc and click
 OK.

1. Set the Job status option to
 Active.

1. Using the buttons on the right of the screen, set up and add appropriate
 phases and cost types. Click OK three times to save your
 changes and return to the main menu.

## Part D: Payroll – Employee File Maintenance

1. On the Site Map screen, click Payroll  >  Employees.

1. Enter an employee code and click the Financials link.

1. In the Billing code field, enter an existing billing
 code from T+M, for example, L1.
Note: The billing code may also be determined from the
 appropriate wage code or union code.

1. Save your changes and return to the main menu.

## Part E: Time + Material – T+M Job Billing Setup

1. On the Site Map screen, click Time + Material  >  Maintenance  >  Job Billing. Use this screen to set up customer-based markups, add-ons, and
 fees.

1. Enter the Job code DYNTMC-J1.

1. Use the Markups, Add-ons, and
 Fees buttons to enter your customer-based information.

1. Save your changes and return to the main menu.

## Part F: Time + Material – Labor Billing Rates Maintenance

1. On the Site Map screen, click Time + Material  >  Maintenance  >  Labor Billing.

1. At the Billing code field, enter L1 (remember: L1 was
 taken from the Payroll section of this example).

1. In the Rates section, enter the
 Regular, Overtime,
 Double time, and Markup amounts
 to be used on this job and all future jobs for this customer.

1. Save your changes and return to the main menu.

## Part G: Time + Material – T+M Job Equipment Billing Rates

1. On the Site Map , click Time + Material  >  Maintenance  >  T+M Job Equipment Billing
 Rates.

1. At the Job field, enter DYNTMC-J1.

1. At the Billing code field, enter E1 for this example.

1. In the Rates section of the screen, complete 2 Levels.
 will bill the same rate for Regular,
 Overtime, and Double time hours
 worked by an employee. Billing Equipment at Level 2 will bill the customer
 increasing rates for Regular,
 Overtime, and Double time hours
 worked by an employee.

1. Save your changes and return to the main menu.

## Part H: Equipment Control – Equipment Type File Maintenance

1. On the Site Map screen, click Equipment Control  >  Maintenance  >  Equipment Type. Use this screen to modify a piece of equipment to use the E1
 equipment billing code.

1. Enter Equipment type PU (for Pick Up truck).

1. Click the Properties button. In the
 Defaults section, at the Billing
 code field, enter E1.

1. Save your changes and return to the main menu.

## Part I: Job Cost – Job File Maintenance

1. On the Site Map screen, click Job Cost  >  Jobs. Use this screen to add a second job for this customer.

1. Add the second job for customer DYNTMC (for example, DYNTMC – J2).

1. In the Address section, at the
 Master field enter the first job, DYNTMC-J1.

1. Save your changes and return to the main menu. Now the first job number added
 for this customer is referenced in the Master job field of
 the second job for this customer and all subsequent jobs for this customer.
Setup of the second job is complete. Now customer-based Time + Material
 billing amounts can be used during processing.
For example, in Payroll Time Card Entry by Employee, say the employee's time card lines are filled out using both the first job and the second job created in the setup described above. The billing rate for any Regular, Overtime, or Double time hours would come from the Master job billing code. Likewise, any equipment hours would come from Job Equipment Billing Rates Maintenance for the Master (first) job. When the time card lines are transferred to the Time + Material module, the customer-based billing rates will be applied as follows:

- The markups, add-ons, and fees for the second job (and all subsequent jobs) will be retrieved from the setup for the first job for this customer.

- The labor billing rates and equipment billing rates will be retrieved from the first job for this customer.
Lastly, the T+M Pre-Billing Report is used to select and print transactions for billing.
Note: The selected transactions can be modified if
 necessary.
