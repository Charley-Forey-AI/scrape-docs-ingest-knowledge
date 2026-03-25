---
title: "PM Subcontract Change Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/pm-subcontract-change-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/pm-subcontract-change-orders-form"
---

# PM Subcontract Change Orders Form

Use the PM Subcontract Change Orders form to create and maintain subcontract change orders (SCOs/SubCOs).
You can also use this form to record changes in scope to an existing subcontract, such as additions or subtractions to existing items or the creation of new scope items. In addition, you can generate and send the SCO document to a list of contacts using the Create and Send feature, as well as approve the SCO.
What do you need to know?

- You cannot use this form to create new subcontracts.

- You can create new subcontract items using the SL Item field in the lower portion of the form. When you add items to subcontract change order, you are actually creating new subcontract (SL) items. Once you add a new SL item, you can view the new item in PM Subcontracts (Non-Interfaced tab).

- You cannot create a change order for back charges or add-ons. Only subcontract items with an item type of Regular or Change can be included on a subcontract change order, which means that you cannot create change orders for subcontract items that are back charges or add-ons.

- You can remove items from a subcontract change order by highlighting the item in the lower grid and then selecting the Remove Item from SCO button (bottom of form). Removing items from a subcontract change order does not remove them from the subcontract.

## Subcontract Totals

The Totals tab displays the subcontract amounts. The formulas used to calculate the totals are listed below. All of the totals on this tab include taxes.
Total TypeDescription
Original SubcontractOriginal Cost + Original TaxThis amount only includes regular and add-on subcontract item types.

Prior Approved Change OrdersA change order item must meet all of the following conditions before it will be included in this amount:

- Associated with a subcontract change order number that is less than the current subcontract change order number (Subcontract CO field in the upper portion of PM Subcontract Change Orders)

- The Interface box is checked on the Info tab in the lower portion of PM Subcontract Change Order

- Either assigned to an ACO or on a subcontract change order with a final status (Status field on the Info tab of the header of PM Subcontract Change Orders)

- Associated with a subcontract change order that has the Ready for Accounting box checked on the Info tab in the upper portion of PM Subcontract Change Order

- Not interfaced with the accounting modules using PM Interface

- OR if the item has been interfaced with the accounting modules, none of the conditions above need to be met and the subcontract change order item will be included in the total

This amount does not include back charges (subcontract items with an item type of back charge).

Current SubcontractOriginal Subcontract + Prior Approved Change Orders
Pending Sub COTotal of the current SubCO including calculated tax
Pending SubcontractCurrent Subcontract + Pending Subcontract
Other Pending Sub COsSubcontract change order items must meet all of the following requirements to be included in this amount:

- Have the Interface box checked on the Info tab in the lower portion of PM Subcontract Change Order

- Subcontract change order number that is less than the current subcontract change order (Subcontract CO field in the upper portion of PM Subcontract Change Orders)

- On a subcontract that has not been approved, or has been approved but does not have a final status (Status field on the Info tab of the header of PM Subcontract Change Orders)

This amount does not include:

- Back charges

- Subcontract items assigned to an ACO or interfaced with accounting

## Available Estimate / Non-Interfaced / Remaining Estimate

These display-only fields are only visible in the SL items section, and show estimate information for the selected Seq/SL Item. These values are calculated as follows:
FieldCalculation
Available EstimateCurrent Estimated Cost - Actual Cost - Remaining Committed Cost + Non-Interfaced Estimated Cost
Non-InterfacedThis is a more complex calculation that takes a number of factors into consideration. However, in general, this calculation is the sum of the amount and taxes from PM Subcontract Detail and based on certain factors, the subtraction of some SL Item and SL Change Order detail costs (which can include taxes), plus Non-Interfaced Estimated.
Remaining EstimateAvailable Estimate - Non-Interfaced

Related information

- [Add Contacts to a Distribution List](/en/vista/vista/project-management/create-and-send/add-contacts-to-a-distribution-list)

- [Enable/Disable the Error Correction Feature in PM](/en/vista/vista/project-management/setupmaintenance/enabledisable-the-error-correction-feature-in-pm)

- [Subcontract Change Orders - Overview](/en/vista/vista/project-management/subcontracts/subcontract-change-orders---overview)

- [About Subcontract Buyout](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)

- [About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)

- [PM Interface Form](/en/vista/vista/project-management/setupmaintenance/pm-interface-form)
