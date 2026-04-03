---
title: "T+M Job Billing Setup - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/spectrum-menus/maintenance-overview/tm-job-billing-setup/tm-job-billing-setup---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/spectrum-menus/maintenance-overview/tm-job-billing-setup/tm-job-billing-setup---field-descriptions"
---

# T+M Job Billing Setup - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Job
Enter or search for the number of a Time + Material job which has already been set up in the Job Cost module. The description will display, as well as all fields linked to the job.

Customer
The customer code and name displays from the Job Main
 Properties screen.
Note: The Job Billing record can still be created even if there is
 no assigned primary customer in Job Cost.

Master job

- If the specified job above is a master job, a checkbox will be provided in this field to submit sub-job billings from the master job.

- If the specified job is a sub-job, the assigned master job and billing method will display in this field.

- If the specified job is neither a master or sub-job, this field will be blank.

Properties

Contract #
The contract number displays from the Job Main
 Properties screen.

Contract type
The contract type displays from the Job Main Properties
 screen.

Not to exceed
Enter the dollar amount that the billings for this job is not to exceed. When billings are selected, if the job amount exceeds this amount, then the system will beep a warning and the Not to Exceed Billing Exception Report prints automatically.

Price
The cost method displays: Time + Material or CostPlus.

Billing method
Select whether the job will generate an A/R Invoice or Change request.

Taxable?
Press Enter to accept the default from the
 Job File Maintenance, or select the checkbox if
 this job is taxable, or leave clear if the job is not taxable.

Sales tax
Press Enter to accept the default Sales tax code (as
 defined in the Job File Maintenance screen) or enter
 the desired tax code. Entries of up to 15 characters are allowed.

Retention
Enter the retention percentage for this billing.

Buttons

Markups
Click to view the [Job-Specific Markups](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/maintenance-overview/cost-type-markup-file-maintenance/job-specific-markups) window.

Add-ons
Click to view the [Job-Specific Add-ons](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/maintenance-overview/tm-job-billing-setup/job-specific-add-ons) window.

Fees
Click to view the [Job-Specific Fees](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/job-overview/job-specific-fees) window.

Billing details

Next billing # Next transaction #
This job's next billing and transaction numbers display. If the billing number exceeds 999, the billing number will automatically be converted to the alpha equivalent (Example: A00 = 1000).

Equipment level
Enter the level 1–5 at which equipment for this job should be billed. Rates
 corresponding to this level will default from the price table in
 Equipment Billing Rates Maintenance or
 T+M Job Equipment Billing Rates. This level
 defaults from the labor level designated in the Customer File
 Maintenance screen.
Note: If a level is not specified for a Time + Material job in
 this field, no rates will transfer to Time + Material.

Material level
Enter the level 1–5 (or leave blank for 0 for cost) at which material for this
 job should be billed. For materials taken out of inventory, rates
 corresponding to this level will default from the selected Price level or
 Standard cost in Inventory Control. This level
 defaults from the material level in the Customer File
 Maintenance screen.
When stock items are updated to the job from Job Requisition Entry during the Inventory Transaction Update or from Purchase Order Entry during the A/P Transaction Update, the price per unit will be determined based on price level 1-5, if indicated here, or on cost, if this field is blank.
Any associated Markup charges will be calculated based on the same price. Cost plus jobs always use cost as the basis, regardless of the level specified here.
Note: If a material level is entered in this field and a stock
 item is used during entry that does not have a price in the corresponding
 level, a markup will not occur, even on a manually entered cost.

Labor level
Enter the level 1–5 at which labor for this job should be billed. Rates
 corresponding to this level will default from the price table in
 Labor Billing Rates Maintenance or T+M
 Job Labor Billing Rates. This level defaults from the labor
 level designated in the Customer File Maintenance
 screen.
Note: If a level is not specified for a Time + Material job in
 this field, no rates will transfer to Time + Material.

Billing address

Print to alternate address on T+M billing/invoice?
Select to print the customer's alternate bill-to address on the contract's T+M
 billings and invoices. By selecting this checkbox, entry is required in the
 Bill-to code field.
Customer alternate bill-to addresses are set up in Accounts Receivable > Alternate Bill-To Address Maintenance.

Bill-to code
If you selected the checkbox above, entry in this field is required. Enter or
 search for the alternate address bill-to code in the Alternate
 Bill-to Addresses window. Alternate bill-to codes can also be
 added or edited from this window.

Name Address
The addressee name and address display. If you selected Print
 alternate address on T+M billing/invoice checkbox, then the
 alternate billing addressee name will display based on the code entered in
 the Bill-to code field. Otherwise, the billing
 addressee name will default from Customer File
 Maintenance.
