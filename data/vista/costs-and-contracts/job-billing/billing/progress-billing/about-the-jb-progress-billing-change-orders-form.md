---
title: "About the JB Progress Billing Change Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-progress-billing-change-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-progress-billing-change-orders-form"
---

# About the JB Progress Billing Change Orders Form

Use this form to edit, add, and remove change orders.
Access this form by clicking the Change Orders button on the JB Progress Billing form. The system automatically adds any change orders entered (in JC Change Orders) since the last billing to the current progress billing as follows:

- When a billing is created automatically by JB Progress Bill Initialize, change orders with approval dates through the specified Change Orders Thru date are added to the current billing.

- When a new billing is added manually in JB Progress Billing, all approved External change orders not already on another billing are added to the current billing.

Once a change order is added to the current billing,
 its information can be viewed and/or edited in this form. Additionally, the change
 order amount is reflected in the current Contract and Item amounts in the Bill Items
 Info section of JB Progress Billing. For more information, see [About Updating Previous Billed Amounts on
 Future Bills](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-updating-previous-billed-amounts-on-future-bills).

## About Adding Change Orders

Add change orders manually to this form
 when:

- The system did not automatically
 add the change orders due to the billing date range set for the billing

- The change order was entered in
 JC Change Orders after the billing was created and you want the change order
 included on the billing.

Note: Change orders MUST exist in JC Change Orders
 before they can be added to a billing. Additionally, if you try to add a change
 order/item to a current billing, and the change order item is for a contract item
 that does not exist on the billing (JB Progress Billing), a warning displays. At
 this point, you can select to have the system automatically add the contract item to
 the billing.

## About Changing Change Orders

You are responsible for the timing of changes to change orders (in JC Change Orders)
 and including those changes on a billing invoice.
JB has no way of knowing if a change
 order from a previous invoice has been changed or not. Because you are allowed to
 make changes to change orders in JC as long as the month is open, it is possible for
 you to print an invoice, and then revise a change order. In which case, JB contract
 amounts would no longer match Job Cost. JB derives the current contract amount based
 on previous billings. The change in the change order would be reflected in JC but
 not in JB. If you have the ability to delete and re-pull the billing, the changes
 made in Job Cost would then be reflected on the new bill.
Note: You can use the JB Change Order Billing report
 to review change order amounts vs. previously billed amounts for a change order.


## About Deleting Change Orders

You can delete (remove) a change order from a billing as long as the GL month is
 open.
Because change orders affect current contract amounts and not
 billed amounts, removing them from a billing will have no affect on the billing.


## Deleting a Billing

You can delete a billing (using the Delete button), as long as the billing has not
 been interfaced.
If the billing has been interfaced, you
 must flag the billing for deletion by setting the Status to Delete. Once set, the
 system will perform a check for change orders. If change orders exist, a message
 displays informing you that you cannot delete a bill until the change orders have
 been removed. When you click OK, the JB Progress Bill Change Orders form displays so
 that you can remove the change orders from the billing. Once they have been removed,
 the JB Progress Billing form displays, where you must reflag the billing for
 deletion. The bill must then be re-interfaced to complete the deletion process.
Note: If you have checked the Automatic Update of Prev
 Billed and ChgOrder Amounts on Future Bills option in JB Company Parameters, the
 system will automatically update the previous billed amounts, current
 contract/contract units, and ACO additions/deductions by excluding the value of the
 billing you deleted from the previous amount of all subsequent billings. If the
 Automatic Update of Prev Billed and ChgOrder Amounts on Future Bills option in JB
 Company Parameters is not checked, you will need to perform the update manually. See
 Related Topics below for more information on updating previous billed
 amounts.
