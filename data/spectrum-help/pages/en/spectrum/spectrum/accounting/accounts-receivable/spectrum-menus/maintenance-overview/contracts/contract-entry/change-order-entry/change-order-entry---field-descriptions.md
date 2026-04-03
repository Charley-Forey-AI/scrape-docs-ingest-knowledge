---
title: "Change Order Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-entry/change-order-entry/change-order-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-entry/change-order-entry/change-order-entry---field-descriptions"
---

# Change Order Entry - Field Descriptions

Use this table for reference when completing the fields on
 this screen.
Field/Button
Description

Job
Enter the job number for a new change order. The
 description will display to the right of this field.

Customer
The customer code will default from the job file. If no
 customer code defaults, or if there is more than one customer for the same
 job, enter a valid customer code.

Change order
Enter a new or existing change order number for the
 specified job and contract, or press Enter for the next
 sequential number.
If the Job+Customer+Change order combination exists, and
 the change order isn't already associated with a draw request or change
 request, the Operator can edit the change order.
If the job status is 'Completed' and the 'Disallow
 revenue entry' checkbox is selected in Job Main Properties, you will not be
 able to add a new change order for the selected job.

Description
Enter a description for the change order in this
 field.

Current status
Enter a change order status code in this field. Change
 order status codes are assigned in the [Change Order Status File Maintenance](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/change-order-status-file-maintenance) screen.

Origination date
Specify the change order origination date in this field.
 The current A/R processing date will default in this field.

Approved date
Specify the approved date for this change order in this
 field.

Approved days
Enter the number of days the contract will change due to
 this change order.

Cost breakdown

Take off total
The total of the Amount column on the Costs tab displays
 in this field. The percentage of the Change order total will display to the
 right of all amounts in this section.

Markups
The total of the Markup amounts column on the Markups tab
 displays in this field.

Subtotal
The sum of the Take off total plus Markups displays in
 this field.

Add-ons
The total of the Total column on the Add-ons tab displays
 in this field.

Job total
The sum of the Subtotal plus Add-ons displays in this
 field.

Fee at
The Fee percentage defaults from the Pricing Defaults for Contract
 Changes screen. The Fee percentage is multiplied by the Job
 total amount and is added to the price of the change request. You are
 allowed to override the percentage or dollar amount, and when one of these
 fields is changed the other will be recalculated immediately.

Billing adjustment
The Change order total minus the Job total minus the Fee
 at amount displays in this field.

Change order total
The total of the Amount column on the Billing tab
 displays in this field.

Grid

CR's
This tab will display all the [Change Order Entry - Change Requests](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-order-entry/change-order-entry---change-requests) attached to this
 change order. Changes made on this worksheet will not be committed until the
 change order is saved.

Costs
Use this tab to view all [Change Order Entry - Costs](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-order-entry/change-order-entry---costs) made to phases from
 the selected change request added on the cost worksheet.

Markups
This tab will display all [Change Order Entry - Markups](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-order-entry/change-order-entry---markups) from the selected
 change requests added to this change order. Change orders inherit the markup
 amounts from the attached change requests.

Add-ons
Use this tab to view all [Change Order Entry - Add-ons](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-order-entry/change-order-entry---add-ons) to the change
 order. Change orders inherit the add-on codes (and their detail) from the
 attached change requests.

Billing
Use this tab to add [Change Order Entry - Billing](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-order-entry/change-order-entry---billing) for the change order, and add undistributed
 amounts to the billing adjustment value.

Notes
Use this tab to enter unlimited [Change Order Entry - Notes](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-order-entry/change-order-entry---notes) for the change
 order.
