---
title: "Work Order Other Charges for Site Work Orders - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-other-charges/work-order-other-charges-for-site-work-orders/work-order-other-charges-for-site-work-orders---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-other-charges/work-order-other-charges-for-site-work-orders/work-order-other-charges-for-site-work-orders---field-descriptions"
---

# Work Order Other Charges for Site Work Orders - Field
 Descriptions

Use the table below for reference when completing the fields on this screen.
Field
Description

Item code Description Calculation method
Enter the other charge item code in
 this field. The associated Description and Calculation method will display beneath this field. Note: If this is a G/L transaction, the window
 header will display the Journal Entry # in place of the other charges item
 code.

Source
The source of the other charge
 transaction (Entry or General Ledger) displays in this view-only field.
Status
The status of the other charge
 transaction displays in this view-only field.
Details

G/L department
Enter the G/L department to be used in
 recording these costs in the general ledger. A search window is available for
 viewing Work Order G/L departments. The department entered here must have been
 previously set up in Work Order G/L Department File Maintenance. Note: The other charge for this line must have
 been designated in the Work Order G/L Department file using the Other
 button.

Task
Enter the task associated with this
 item, double-click in this field to select from a list of available tasks, or
 press Enter to leave this field blank.
Task completed?
Select this checkbox if the assigned
 task has been completed.
Customer billing

Taxable on customer invoice?
Check this box if this item is taxable;
 otherwise, leave it cleared if the item is not taxable. The default will come
 from Other Cost Item Maintenance, but can be overridden if desired.  Additional Customer billing fields will be available,
 depending on the type of transaction.

- For 'Fixed amount' transactions originating in Work
 Order (Entry source) the Cost amount and Invoice extension
 fields will be available for entry. For transactions originating in
 Journal Entry processing (G/L source) the Cost (journal debit)
 field will be view-only, and the Invoice extension field
 will be available for entry.

- For 'Hourly' transactions originating in Work Order
 (Entry source) the Calculation basis, Hourly cost rate, Hourly bill rate and
 Invoice
 extension fields will be view-only. The Invoice extension
 field is calculated based on the Calculation basis (total hours) times
 the Hourly bill rate totals.

- For 'Percent of cost' transactions originating in
 Work Order (Entry source) the Calculation basis, Cost percentage,
 Billing percentage and Invoice extension
 fields will be view-only. The Calculation basis field will be computed by
 summing the costs associated with each of the labor, material and other
 charge items in the three transaction tables. However, the bill amount
 for other charges and the basis for the bill amount does not include
 warranty billings in the computation.The Invoice extension field is
 calculated based on the Calculation basis (total cost) times the Billing
 percentage totals.

- For 'Percent of bill' transactions originating in
 Work Order (Entry source) the Calculation basis, Cost percentage,
 Billing percentage and Invoice extension
 fields will be view-only. The Calculation basis (total billing) field
 will be computed by summing the customer invoice extensions associated
 with each of the labor, material and other charge and flat-rate task
 items in the three transaction tables.
