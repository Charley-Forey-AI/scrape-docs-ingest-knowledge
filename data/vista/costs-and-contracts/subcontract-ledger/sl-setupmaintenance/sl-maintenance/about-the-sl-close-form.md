---
title: "About the SL Close Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-maintenance/about-the-sl-close-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-maintenance/about-the-sl-close-form"
---

# About the SL Close Form

Use this form to close completed subcontracts.
Closing a subcontract means the following:

- The subcontract is complete and accurate

- Change orders, backcharges, or AP invoices can no longer be posted to it.

- The subcontract can be purged using [SL Purge](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-maintenance/about-the-sl-purge-form).

When this form is run, the system closes any
 subcontracts with a status of complete, and any open subcontracts that have been fully
 invoiced (current = invoiced, and remaining committed costs in Job Cost are zero). Open
 subcontracts with remaining committed costs may be closed if the Include ‘Open’
 Subcontracts with Remaining Units and Costs box is checked.
To close a subcontract, enter the required information and click Close SLs. The SL Close form closes and the SL Batch Process form displays. Validate and post the batch to implement the close.
The close process sets the Current Units and Costs equal to the Invoiced Units and Costs on all regular, change order, and add-on items. Any changes will be recorded as new entries in SL Change Detail. Total and Remaining Committed Units and Costs in JC will be adjusted. After all items have been processed, the subcontract’s status is set to Closed, and the Month Closed record is updated in the system.

- Completing Subcontracts with Committed Costs - If you manually changed the status of any subcontracts in SL Subcontract Entry to “Complete” before they were fully invoiced in AP, this program will zero out any remaining committed costs in JC.

- Printing Reports - SL reports can still be printed after closing subcontracts. The details remain online until the subcontract is deleted in SL Purge.

- Reopening Subcontracts - You can use the SL Subcontract Entry process to reopen a subcontract that has been closed using this form. Click [here](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/reopen-a-closed-subcontract) for more information.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-maintenance/about-the-sl-purge-form)SL Purge
