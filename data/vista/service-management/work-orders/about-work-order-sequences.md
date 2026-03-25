---
title: "About Work Order Sequences | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-work-order-sequences"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-work-order-sequences"
---

# About Work Order Sequences

Work order sequences (also known as work order scopes) are entered in the lower section of the SM Work Orders form.
A work order scope is used to specify what work is to be done, when the work is due to be completed, and who will be billed for the work. Although all work order scopes require the same basic information, additional information may be required depending on the work order type (customer, job, or agreement), as well as the price method selected. For example, job work orders require entry of a phase, customer work orders require selecting a price method, and customer work orders with Flat Price scopes require that you set up split revenue entries.

## Work Scopes

If you have set up work scopes (in SM Work Scopes), you can assign them to work order sequences to identify the problems, maintenance tasks, or jobs needed to complete the work order. For job work orders, the work scope may also provide a default phase for posting costs to JC. (See the F1 help for more information.) If you do not use work scopes, you can use the Description text box to enter details about the work to be performed for each sequence.

## Call Types

You can change the call type for any work order scope (except for those generated from an agreement), regardless of whether you have entered work completed, billed the work order, and/or closed the scope. When you change the call type, the following occurs:

- All work completed lines associated with the scope will be updated with the correct GL accounts. This will only apply if you have set up overrides by call type or call type/cost type in SM Departments and the accounts differ.

- For work completed labor lines, if you have not invoiced the labor line and labor rate overrides exist for the new call type, the Bill Rate and Bill Subtotal will be recalculated for the work completed line accordingly. If no override rate exists for the call type, the Bill Rate/Bill Subtotal will be recalculated using the standard rate hierarchy.
If you have invoiced the labor line, no Bill Rate/Bill Subtotal updates will occur.

- If the call type is associated with a Flat Price scope, all revenue splits for the scope will be updated to the correct GL accounts (on the Posted Detail tab).

- If changing from a non-WIP tracking call type to a WIP-tracking call type, or vice-versa, the system will update the appropriate Cost or Cost WIP account.

- The system updates GL as applicable; costs and revenue are backed out of the current GL accounts and moved to the new GL accounts accordingly.

## Scope Status

The status of each work order sequence is shown in the Scope Status field (display only). There are currently four statuses available for scopes: Open, On Hold, Complete, and Closed.
You can change the status of a scope using the status selection button (to the left of the Scope Status field). The options available from the status selection drop-down will depend on the current status of the scope. Options are as follows:

- Complete - This option is only available when the scope status is Open, and is used complete a scope (typically when the work is complete, but you are not ready to close the scope).

- Place on Hold - This option is only available when the scope status is Open, and is used to place a scope on hold (via the SM Dispatch Scopes on Hold form). Once you place a scope on hold, a Details button appears to the left of the status selection button to allow viewing the hold reason and follow up date information.

- Close - This option is only available when the scope status is Open or Complete, and is used to close a work order scope (via the SM Work Order Close form). When a scope is closed, you cannot add new work completed or purchase orders for the scope.

For single-scope work orders, closing a scope will also close the work order, along with any open trips. Existing trips with a status other than Open will remain intact, but cannot be edited. You will also be unable to add work completed, purchase orders, or new scopes; however, you will be able bill the work order as needed.

- Reopen - This status is only available when the scope status is Complete, and sets the scope status to Open.

- Remove Hold - This status is only available when the scope status is On Hold, and sets the scope status to Open.

- Unclose - This status is only available when the scope status is Closed, and sets the scope status to Complete.

For single-scope work orders, if the work order status is closed, selecting this option will also set the work order status to Complete.

- You can complete a work order sequence at any time, regardless of whether you have open trips, work completed, POs, and/or invoices. However, if the work order is for a customer or for a job using the Markup costing method, the scope must be assigned a call type and rate template before it can be completed.

- Job work orders using a costing method of Actual Cost do not use rate templates to derive billable amounts and therefore, are not assigned rate templates. Scopes for these work orders can be completed without a rate template assigned.

## Deleting Work Order Sequences

You can delete a work order sequence using the Delete Record button in the toolbar or by selecting Records  > Delete.
However, you can only delete a sequence if the following is true:

- There are no tasks defined for the sequence (Tasks tab).

- You have not associated the sequence with a PO/PO item.

- You have not captured work completed for the sequence.

- There are no invoices associated with the sequence.
