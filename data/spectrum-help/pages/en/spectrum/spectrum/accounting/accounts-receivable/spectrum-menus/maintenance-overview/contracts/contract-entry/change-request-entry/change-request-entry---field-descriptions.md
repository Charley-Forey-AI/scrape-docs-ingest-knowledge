---
title: "Change Request Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-entry/change-request-entry/change-request-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-entry/change-request-entry/change-request-entry---field-descriptions"
---

# Change Request Entry - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field/Button
Description

Job
Enter the job number for a new change request. The description will display to the right of this field.

Customer
The customer code will default from the job file. If no customer code defaults, or if there is more than one customer for the same job, enter a valid customer code.

Change request
Enter a new or existing change request number for the specified job and contract, or press Enter for the next sequential number.
If the Job+Customer+Change request combination exists, and the change request isn't already associated with a draw request or change order, the Operator can edit the change request.

- When editing an existing change request that has not been associated with a
 change order, the New
 CO button will display to the right of this field.
 Click this button to create a change order.
Note: If a blank billing item record was found when
 creating a change order, an error message will prompt the user to
 assign a billing item.

- If the change request is already associated with a change order, click the
 change order hyperlink to open the [Change Order Entry](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-entry/change-order-entry)
 screen.

- If the job status is 'Completed' and the Disallow revenue
 entry checkbox is selected in Job Main
 Properties, you will not be able to add a new change
 request for the selected job.

Description
Enter a description for the change request in this field.

Current status
Enter a change request status code in this field. Change request status codes are assigned in the [Change Request Status File Maintenance](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/change-request-status-file-maintenance) screen.
If the status code is changed to an action type not equal to 4-No recognition of revenue or cost, no billing, all revenue must be assigned to billing items, all costs must be assigned to phases, and undistributed amounts on the Billing Setup tab must be deleted before you can designate a new status.
If the status code is changed to 3-Recognize cost revisions, no billing and the quotation submitted date (the date that is used as the transaction date in Projected Cost History Detail) is blank, it will default to the current origination date.

Cost reimbursable?
Select this checkbox to make this change request cost-reimbursable. This checkbox can be set at any time.
When this checkbox is selected, you will have access to the Markups, Add-ons and Billing Setup tabs. Clearing this checkbox will clear markup, add-on and fee information. And if items exist in billing setup, you must delete all billing items before you can change to non-cost reimbursable.
If the status code is set to action type 1 or 2 (executed or approved), the change request cannot be set to non-reimbursable.

Origination date
Specify the change request origination date in this field. The current A/R processing date will default in this field.

Approved date
Specify the change request approved date in this field. The status code must be set to action type 1 or 2 (executed or approved) to enter a date in this field.
A message will display to the right of this field indicating any specific worksheets that have not been completed:

- If there are blank phases, Complete the cost worksheet.

- If there are blank bill items and/or undistributed amounts on the Billing tab, Complete the billing worksheet.

- If there are blank phases and blank bill items and/or undistributed amounts in billing, Complete the cost and billing worksheets.

- If there are no blank bill items or blank phases or no undistributed amounts exist, no message will be displayed.

Cost breakdown

T+M billing details
If there are time + material billings for the current change request, click
 this link to open the [T+M Job Billing History](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/inquiries-overview/tm-job-billing-history) screen. If there are no T+M billings, or the
 Operator does not have authorization to the T+M billing History
 Inquiry screen, this field will be hidden.

Take off total
The total of the Amount column on the
 Costs tab displays in this field. The percentage of the
 Change request total will display to the right of all amounts in this
 section.

Markups
The total of the Markup amounts column on the
 Markups tab
 displays in this field.

Subtotal
The sum of the Take off total plus Markups displays in this field.

Add-ons
The total of the Total column on the Add-ons tab displays in this field.

Job total
The sum of the Subtotal plus Add-ons displays in this field.

Fee at
The Fee percentage defaults from the Pricing Defaults for Contract Changes screen. The Fee percentage is multiplied by the Job total amount and is added to the price of the change request. You are allowed to override the percentage or dollar amount, and when one of these fields is changed the other will be recalculated immediately.

Billing adjustment
The billing adjustment total will be calculated as the Change request total minus the Job total minus the Fee at amount. Changes to billing lines on the Billing tab will change this total.

Change request total
The total of the Amount column on the Billing tab displays in this field.

Grid

Related
Use this tab to view and add [Change Request Entry - Projects Tab](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-request-entry/change-request-entry---projects-tab) to the change request.

Costs
Use this tab to enter contractor and subcontractor [Change Request Entry - Costs](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-request-entry/change-request-entry---costs). The sum of these cost changes will display on the Take off total in the header.

Markups
Use this tab to add cost [Change Request Entry - Markups](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-request-entry/change-request-entry---markups) to the change request.

Add-ons
Use this tab to add pricing [Change Request Entry - Add-ons](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-request-entry/change-request-entry---add-ons) to the change request.

Billing
Use this tab to add [Change Request Entry - Billing](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-request-entry/change-request-entry---billing) for the change request.

Notes
Use this tab to enter unlimited [Change Request Entry - Notes](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-request-entry/change-request-entry---notes) for the change request.

Dates
Use this tab to specify [Change Request Entry - Dates](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-request-entry/change-request-entry---dates). Changes on this tab will be saved when the change request is saved.
