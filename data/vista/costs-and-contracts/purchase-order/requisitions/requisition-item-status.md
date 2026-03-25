---
title: "Requisition Item Status | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/requisitions/requisition-item-status"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/requisitions/requisition-item-status"
---

# Requisition Item Status

The status of a requisition item indicates where the requisition is during its processing.
Initially, each requisition line is assigned a status of 'Open'. Then as the requisition is approved, added to a quote or purchase order, etc., the system automatically updates the status accordingly. There are seven statuses that can be assigned to a requisition:

- 0-Open – Default status for all newly created requisition lines.

- 1-Approved for Quote – This status is only used for requisitions that are routed to quote. If you require approval of requisitions before they are added to a quote (flag in PO Company Parameters), this status will be assigned once all reviewers assigned to the line have approved it. If you do not require approval and have not assigned a reviewer to the requisition line, this status is assigned automatically once the line is entered and saved.

- 2-On Quote – This status is assigned to a requisition line once it is initialized or added to a quote. Lines with this status are disabled.

- 3- Quoted –This status is assigned to a requisition line once the quote line it is associated with has been flagged as Quoted. This only applies when approval is required on quotes before they can be initialized to a purchase order and the quote has not yet been approved.If approval is not required and the quote line is flagged as Quoted, once saved the status is automatically updated to 'Approved for Purchase'. Lines with this status are disabled.

- 4-Approved for Purchase – This status is assigned to all requisition lines that are ready to be added to a purchase order. Requisition lines meet this criteria when:

- they are routed directly to a purchase order and no approval is required or,

- they are on a quote that has been flagged as 'Quoted' and no approval is required or,

- they are on a quote that has been flagged as 'Quoted', approval is required, and all assigned reviewers have approved the line.

- 5-Completed –This status is applied to all requisition lines once they have been added to a purchase order. Lines with this status are disabled.

- 6-Denied –This status applies only to requisitions that require approval before they are added to a quote or purchase order. If the reviewer flags the requisition line or quote line as rejected in PO Requisition Reviewer, the line's status is set to 'Denied'.
