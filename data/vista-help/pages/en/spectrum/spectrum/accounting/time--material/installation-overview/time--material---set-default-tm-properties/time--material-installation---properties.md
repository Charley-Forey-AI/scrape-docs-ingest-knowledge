---
title: "Time + Material Installation - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/installation-overview/time--material---set-default-tm-properties/time--material-installation---properties"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/installation-overview/time--material---set-default-tm-properties/time--material-installation---properties"
---

# Time + Material Installation - Properties

Use this tab to set default properties for the Time +
 Material module. You can change these settings as needed.
Fields
Descriptions

Post billings to Accounts Receivable?
Select this checkbox if you want invoices created in Accounts Receivable. An invoice will be created using the invoice number from the Accounts Receivable Installation screen. This invoice will be a summary invoice with totals for each Cost type.
Leave this checkbox blank if you do not want invoices created in Accounts Receivable. You may choose this option if you want to create your summary invoices manually and then enter them in Accounts Receivable.

Post Accounts Receivable invoices as printed?
This field is only used if you selected the Post invoices to Accounts Receivable checkbox. If you are not posting invoices to A/R then this field is not used.
Select this checkbox if you want the invoices posted with the printed flag equal to Yes if you are sending a separate summary Time + Material invoice or no summary invoice for your Time + Material bills. Many contractors send a separate invoice that meets the specific requirements for that customer; if this is the case then you do not have to print the summary invoice out of Spectrum® Accounts Receivable.
Do not select this checkbox if you want to print the summary Time + Material invoice out of Spectrum Accounts Receivable. Accounts Receivable will only post invoices that have the printed flag as Yes on the Sales Journal and Update.
When a job is set up in the Job File Maintenance screen and the price method is Time + Material, then the job is automatically set up in the Time + Material module. If the job being set up is not associated with a master job, then it will be set up with markups, add-ons, and fees that are set up on this screen. If none are entered here, then the job will be set up without any markups, add-ons, or fees on the line items being posted.

Include burden when adding Payroll cost-plus billings?
Select this checkbox if you wish to include burden when creating labor billing transactions for cost-plus jobs. By default, this checkbox will be selected.

- If this checkbox is selected, transactions for cost-plus jobs will be updated with burden included in the labor amount (the burden and the time card extension are bundled, regardless of whether or not the burden was combined in Job Cost history records).

- If this checkbox is clear, then the time card extension is updated to the Time + Material module but burden costs are NOT added to this amount. This allows you to track actual labor costs before burden for billing processes and to calculate markups on these pre-tax, non-burden labor totals. For example, some cost-plus contracts may specify a different markup percent for regular Payroll hours versus overtime hours.

Default sales G/L account code
Enter the default General Ledger code for Time + Material contract sales.
This account is used only if there is no sales account set up in the contract file. If there is an account in Contract File Maintenance then that account is used when bills are created in Accounts Receivable.

Next non-Accounts Receivable invoice number
If you did not select the Post invoices to Accounts Receivable checkbox, then this field will be used to indicate an invoice number on the posted Time + Material bill. This invoice number will print on the billing history reports and inquiry screens. It is not used in Accounts Receivable at all.
If you selected the Post invoices to Accounts Receivable checkbox, then this field is not used at all. The default invoice number from the Accounts Receivable Installation screen is used during the posting.

Description from Payroll

- Employee name

- Employee title

- Union craft

- Union level description

- Wage code description

- Billing code description

The system is prompting for one of the fields below to be used as the
 description when Payroll > Time Card Entry records are posted to the Time + Material billing file. The
 Employee name
 will default if a selection is not made.

Description from Accounts Payable

- Vendor name

- Item code

When a Purchase Order is received and then the A/P invoice is posted for a Time + Material job, the vendor name and item description is recorded in the Time + Material module. This installation option identifies what information will post to Time + Material.
Select Vendor name so the vendor's name posts to the Time + Material detail billing description. Select Item code so the item code from the A/P invoice (which comes from the P/O) posts to the Time + Material detail billing description.
This option is particularly desirable for companies not wishing to include vendor information as part of the Time + Material billing.
