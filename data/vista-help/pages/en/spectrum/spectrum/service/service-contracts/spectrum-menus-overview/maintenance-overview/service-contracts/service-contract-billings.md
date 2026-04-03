---
title: "Service Contract Billings | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/maintenance-overview/service-contracts/service-contract-billings"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/maintenance-overview/service-contracts/service-contract-billings"
---

# Service Contract Billings

Use this tab to enter customer billing information for the
 service contract.
The upper portion of this tab will contain sections for billing details and alternate
 bill-to address (if available). The lower portion of this tab displays scheduled billings.
 Billing may or may not happen in concurrence with work. For example, work may be performed
 once a week, but billing happens once a month. You can bill in advance or in arrears, based
 on the billing start date.
In order to save a billing, the sum of the scheduled billing amounts
 cannot exceed Total contract
 amount, and the number of scheduled billings cannot exceed Total contract billings. The system warns
 you if either of these situations is true and choose whether to proceed or edit billing
 values. If you accept revised values, the system notes the revision in the applicable
 headers in the Service Contract
 Billings.
If the deferred revenue schedule is used, the software ensures that the sum of the scheduled transactions is equal to the total revenue that will have been earned over the life of the contract before you save a billing. If the Earned revenue basis is set to 'As billed', this validation does not occur.
Fields / Buttons
Descriptions

Customer
Enter a customer code in this field, or
 press F4 to search
 for customers.
Total contract amount
Enter a total dollar amount for the
 service contract in this field. To cancel a service
 contract, change the contract amount and number of visits based on the work
 performed, and review the earning table for the contract. Changes to the
 earned revenue table will take effect when the earned revenue update is
 run.
For contracts billed from a work order, this
 field will display entries from the Service Contract Visits page. The
 Billing start date, Total
 contract billings, Unscheduled balance, and Earned revenue basis
 fields will also be disabled.

Sales tax code
Enter a sales tax code in this field to
 override the customer's default tax code.
Billing start date
Enter the earliest scheduled billing
 date included in the current contract in this field. Every billing on or after
 this date is considered to be part of the current contract.
Total contract billings
Enter the number of scheduled billings
 for the service contract in this field. If there are no
 previously scheduled billing records for this contract, a dialog box will
 open prompting whether to create billing records. If you choose to generate
 scheduled billings, the software will divide the total contract amount by
 the number of scheduled billings.

Unscheduled balance
The difference between the Total contract amount and sum
 of the scheduled billings between the billing start date and end date displays
 in this view-only field. This amount will appear as a positive value until
 scheduled billings equal the contract total.If the sum of
 the scheduled billings exceed the total contract amount, the unscheduled
 balance will appear as a negative value and a warning message will display
 to the right of this total.

Earned revenue basis
The earned revenue basis will be
 validated to ensure that the selected basis is authorized for the current
 contract type. If the selected basis is not allowed, a warning message
 displays. In the 'New Contract' window this field will default from the
 'Default earned revenue basis' specified in Contract Type File
 Maintenance. Click the associated View
 History link to open the Service Contract Earned Revenue screen in a new
 Spectrum tab.
In the 'Edit Contract' window, if you
 change the basis from 'As billed' to any other basis code, the Build Schedule window
 automatically opens. The software will determine whether there are any
 earned revenue G/L distribution records already present for this contract,
 and if so, will require the Operator to build the schedule in order to reset
 the earned revenue basis. After the build is complete, the software will
 open the Contract Earned
 Revenue Schedule window.
When the
 earned revenue basis is set to 'As billed', the lookup button to the right
 of this field will open the Earned Revenue G/L History Inquiry window. When the earned
 revenue basis is set to any other setting, the 'Schedule' button will appear
 to the right of this field and will open the Contract Earned Revenue
 Schedule window.

Alternate bill-to-address

Print alternate address on work order and invoice?
If the customer has more than one
 address defined, select this checkbox to print an alternate address on the
 work order and invoice.
Bill-to code
Enter the alternate bill-to code that
 you want to apply to the selected manufacturer invoice or double-click on this
 field to select from a list of available bill-to codes. This field must be
 completed if the Print alternate
 address on invoice checkbox is selected.
Schedule billings

Edit/New/Delete
Use these action buttons to add, edit,
 or review a scheduled billing in the [New/Edit Scheduled Billing](/en/spectrum/spectrum/service/service-contracts/service-contracts---getting-started/create-service-contracts/newedit-scheduled-billing).
A/R Invoice
Click this button to open the global
 Accounts Receivable Invoice Inquiry window. This button will not open the
 global window if the Invoice # column is blank or non-valid in the Contract
 Billing Table.
