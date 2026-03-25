---
title: "About Posted Detail: Work Completed | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/updates-to-gl/about-posted-detail-work-completed"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/updates-to-gl/about-posted-detail-work-completed"
---

# About Posted Detail: Work
 Completed

When you process work completed lines for a work order, the system displays the
 related accounting entries on the Posted Detail tab in SM Work Orders.
For each work completed line that you post,
 the Posted Detail grid shows two transaction detail entries: the debit (cost) entry and the
 credit (revenue) entry.
Work completed lines that are not
 posted—either because the batch process was interrupted or because batch posting is handled
 at a later time—do not display in the grid regardless of whether you saved the work
 completed line. The grid only shows the accounting details once the appropriate batch
 process is completed. This allows you to see which work completed lines were posted and
 updated to GL and which were not.
Note: In order to show cost and revenue entries on the
 Posted Detail grid, you must set the GL Interface level for the related module to Summary
 or Detail. For more information, see [Updates to GL](/en/vista/vista/service-management/work-orders/updates-to-gl).

## Cost / Revenue Entries for Customer Work Orders

For Cost entries, the system handles
 updates to the Posted Detail grid depending on the work completed line type.

- Work Completed Equipment - The update
 occurs once you post the batch (automatically or manually).

- Automatically - If you selected the Auto Post New Work Completed checkbox in SM Company Parameters, the update occurs once you save the line and move off the work order.

- Manually - If you did not select the Auto Post New Work Completed checkbox, the update occurs once you post the batch via SM Work Order Cost Posting.

 For work completed
 lines generated from service timecards with equipment usage in PR Timecard Entry,
 the cost entries are updated to the Posted Detail tab once you run PR Ledger
 Update.

- Work Completed Labor - Updates occur once you process payroll and run PR Ledger
 Update. If override accounts exist for burden by liability type in SM Departments,
 the system creates a separate cost line with the appropriate GL account for each
 applicable liability type. Liability types with no override GL account defined are
 posted to the standard Cost Burden or Cost WIP Burden (if tracking WIP for the
 associated call type)

- Work Completed Miscellaneous - Update occurs once you post the
 batch (automatically or manually).

- Inventory Lines - Update occurs once you post the
 batch (automatically or manually).

- Purchase Lines - The cost (debit) entry occurs once you receive
 the purchase order item in PO Receipts Entry. When you invoice the PO in AP
 Transaction Entry, the system backs out the original cost entry and adds a new one
 based on the invoice amount. This results in a total of three cost entries for the
 purchase line. If you receive the purchase order using AP Transaction Entry, the
 system generates a single cost entry.

For Revenue entries, the system updates the
 Posted Detail grid for all line types once you bill the work completed line in SM
 Invoice Review or SM Agreement Invoice Review, and process the batch (send to AR).
If you entered Use tax with the work completed line, the system posts one debit entry for the full amount of the transaction and a separate credit entry for the use tax amount. For example, if the Cost Subtotal is $800 and the use tax amount is $100, the system adds a debit entry for the total amount ($900) and a credit entry for the tax amount ($100).

## Cost / Revenue Entries for Job Work Orders

For job work orders, the system handles updates to the Posted Detail grid a little
 differently. When you post a work completed line, the system generates both a cost and a
 revenue entry. Since job work orders are not billed in SM, this is the only revenue
 entry created for the work completed line; no additional revenue entries are added when
 you bill the work order in Job Billing or Accounts Receivable.
For purchase lines on a job work order, updates to the Posted Detail tab depend on
 whether you receive the PO in the PO Receipts Entry form or in the AP Transaction Entry
 form.

- If you receive the PO in PO Receipts Entry, the cost entry is created once you
 receive the PO and post the receipts batch. When you invoice the purchase order in
 AP Transaction Entry, the system backs out the original cost entry and adds a new
 one (resulting in three cost entries total). In addition, the system adds a
 revenue entry to the Posted Detail grid.

- If you receive the PO in AP Transaction Entry, the system generates one cost
 entry and one revenue entry once you post the invoice batch. No other cost or
 revenue entries are created

## Adjustments

If you create an adjustment to a work completed line (that is, you move the work completed line from one work order to another), the Posted Detail is updated as follows:

- Originating work order - The Posted Detail tab shows one debit line for the original transaction amount and one credit line for the transferred amount (both including tax). If you adjusted the full amount, the credit amount will be equal to the debit amount. However, if you changed the transfer amount, only the transferred portion will show. For example, if the original transaction was for $3,000, but the adjustment was for $1,500, the debit line shows as $3,000 and the credit line shows as $1,500.

- Destination work order - The Posted Detail tab shows a single debit line for the transferred amount (including tax).
