---
title: "About Subcontract Status | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-status"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-status"
---

# About Subcontract Status

When setting up new subcontracts in SL Subcontract Entry, the
 status is set to “Open” and cannot be changed.
If you are changing an existing subcontract, the
 following rules apply to changing the Status field:

- If the subcontract is “Open,” the status may be changed to “Complete,”
 even if the current amount on one or more of the items is not equal to the invoiced
 amount.

- If the subcontract is “Complete,” the status can be changed to
 “Open.”

- If the subcontract is “Closed,” the status can be changed to either
 “Open” or “Complete.” When the batch is posted, the system records the closing month
 as null (to prevent purging), and the status updates in SL Compliance.

- The status cannot be changed to “Closed” for any subcontract. This is
 done internally by the system when the subcontract is closed in SL Close.

Note: You cannot change a subcontract with a “Closed”
 status. This includes change orders, backcharges, or posting payables against the
 subcontract.
