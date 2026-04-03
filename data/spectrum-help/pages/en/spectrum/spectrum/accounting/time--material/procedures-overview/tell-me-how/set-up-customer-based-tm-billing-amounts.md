---
title: "Set Up Customer-based T+M Billing Amounts | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/procedures-overview/tell-me-how/set-up-customer-based-tm-billing-amounts"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/procedures-overview/tell-me-how/set-up-customer-based-tm-billing-amounts"
---

# Set Up Customer-based T+M Billing Amounts

The Time + Material module permits the setting up and use of customer-based T+M billing amounts. These customer-based rates include customer-based labor billing rates, equipment billing rates, markups, add-ons, and fees. Using the Master (job) field allows all jobs for a specified customer to use rates that were set up for this customer.
The bulleted list outlines the setup for customer-based pricing.

## Setup for the first job for a customer

- Accounts Receivable > Customer File Maintenance

- Time + Material Installation screens

- Job Cost > Job File Maintenance

- Payroll > Employee File Maintenance

- Time + Material > Job Billing Rates Maintenance

- Time + Material > T+M Job Labor Billing Rates

- Time + Material > T+M Job Equipment Billing Rates

- Equipment Control > Equipment Type

- Equipment Control > Equipment File Maintenance

## Setup for the second, and all subsequent jobs for a customer

- Job Cost > Job File Maintenance - add the new job

- In the Master (job) field type in the first job for this customer.

After the setup is complete, the customer-based Time + Material billing amounts can be used during processing.
For example, in Payroll > Time Card Entry by Employee, say the employee's time card lines are filled out using both the first
 job and the second job created in the setup described above. The billing rate for any
 Regular, Overtime, or Double time hours would come from the Master job billing code.
 Likewise, any equipment hours would come from Job Equipment Billing Rates
 Maintenance for the Master (first) job. When the time card lines are
 transferred to the Time + Material module, the customer-based billing rates will be
 applied as follows:

- The Markups, Add-ons, and Fees for the second job (and all subsequent jobs) will be retrieved from the setup for the first job for this customer.

- The Labor Billing Rates and Equipment Billing Rates will be retrieved from the first job for this customer.

Lastly, the Time + Material > Pre-Billing Report is used to select and print transactions for billing.Note: The selected transactions can be modified if
 necessary.

Related information

- [Set Up Example: Customer-based T+M Billing Amounts](/en/spectrum/spectrum/accounting/time--material/procedures-overview/tell-me-how/set-up-customer-based-tm-billing-amounts/set-up-example-customer-based-tm-billing-amounts)
