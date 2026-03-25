---
title: "Delete an SM Cost Type | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-sm-cost-types/delete-an-sm-cost-type"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-sm-cost-types/delete-an-sm-cost-type"
---

# Delete an SM Cost Type

You can delete an SM cost type as long as there are no costs
 posted to it.
If there are costs associated with a cost type, you must remove the costs before you can delete the cost type. Therefore, you will typically only use this function for cost types that you have yet used on a work order or for those you have only used on a few work orders.

To delete a cost type with no associated costs:

1. In SM Cost Types, select
 the cost type to delete.

1. Click Delete.To delete a cost type with
 associated costs:

1. If you have billed a
 work order and processed the invoice (sent it to AR), [void the invoice](/en/vista/vista/service-management/sm-invoices/about-voiding-invoices/void-an-sm-invoice) to release the work completed
 lines.

1. If you have billed a
 work completed line, but have not processed the invoice, delete the work
 completed lines from the invoice (in SM Invoice Review).

1. In SM Work Orders,
 delete all work order completed lines referencing the cost type from all work
 orders.

1. In SM Cost Types, select
 the cost type to delete and click Delete.
