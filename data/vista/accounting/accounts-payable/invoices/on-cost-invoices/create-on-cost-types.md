---
title: "Create On-Cost Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/create-on-cost-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/create-on-cost-types"
---

# Create On-Cost Types

You must set up on-cost types to represent vendors to which you will send on-cost payments.
On-cost types identify a specific vendor (typically the corresponding federal agency) for sending on-cost payments, as well as the percentage rate or flat amount that they should receive based on the original invoice that you sent to the subcontractor. An on-cost type also determines the pay type and job expense options for the payment (if necessary). Users in Australia can also specify an ATO category.

1. From the main menu, select Accounts Payable > Programs > On-Cost Types.

1. In the

 On-Cost ID field, enter a number or press

 F4 to select from a list of previously created on-cost IDs.

1. In the

 Description field, enter a description for the on-cost type.

1. In the

 On-Cost Vendor field, specify the vendor for this on-cost type or press

 F4 to select from a list of vendors.

1. From the

 Calculation Method drop-down, select the calculation method for the on-cost type:

- A-Amount - Selecting this option enables the Amount field.

- R-Rate - Selecting this option enables the Rate field.

1. If using the amount calculation method, enter a value in the

 Amount field. If using the rate calculation method, enter a percentage in the

 Rate field.

1. In the

 Pay Type field, enter the payable type for the on-cost type or press

 F4 to select from a list of payable types.

1. Specify a job expense option:

- Use Original Invoice Expense Account - Select to use the expense information that you specify on the original invoice that you create for the subcontractor/vendor.

- Use On-Cost Cost Type - Select to use the job and phase from the original invoice, but specify a different cost type to determine the job expense. Then, in the Cost Type field, enter the on-cost cost type or press F4 to select from a list of cost types.

- Use On-Cost Job Expense Account - Select to create an expense line for the on-cost invoice using a specified GL expense account. Then in the Job Expense Acct field, enter the GL expense account or press F4 to select from a list of GL expense accounts.

1. Specify a non-job expense option:

- Use Original Invoice Expense Account - Select to use the GL account number that you specified on the original invoice that you created for the subcontractor/vendor.

- Use On-Cost Expense Account - Select if you want to specify a cost expense account for this on-cost type. Then, in the Non-Job Expense Acct field, enter the GL account for non-job expenses or press F4 to select from a list of GL expense accounts.

1. For Australian users, if applicable, select a category from the ATO Category drop-down. Options include Superannuation and Superannuation-Extra.Note: For more information on setting up liability codes for superannuation, see [Setting Up Deduction and Liability Codes for Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation/setting-up-liability-codes-for-superannuation).


1. Save the record.

Once you have created on-cost types, you can then associate them with an on-cost group or assign them directly to a subcontractor. For more information, see [AP On-Cost Groups](/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/ap-on-cost-invoice-forms/ap-on-cost-groups-form) and [Associating On-Cost Types with a Subcontractor](/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/associate-on-cost-types-with-a-subcontractor-au-and-ca).
