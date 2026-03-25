---
title: "PM PO Change Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/pm-po-change-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/pm-po-change-orders-form"
---

# PM PO Change Orders Form

Use this form to record the change in scope to an existing purchase order (for example additions or subtractions to existing items, or the creation of new scope items).
From this form you can create and maintain PO change orders (POCOs), generate and send PO change order documents using the Create and Send feature, and then approve the PO change orders.
You cannot use this form to create new purchase orders, but you can create new PO items using the PO Item field in the lower portion of the form.
You can also create a PO change order using the PO Change Order Entry form in the PO module; however, the purchase order information will not be available in the PM module. By entering the POCO in the PM module and then interfacing it with the PO module, the PO information is available in both the PM and PO modules.

## Totals

The Totals tab displays the totals associated with the original purchase order and any related PO change orders. All of the totals on this tab include taxes. The totals are derived as follows:

- Original Purchase Order

- Current Purchase Order — Original PO + Prior Approved PO Change Orders

- Pending Purchase Order CO — This amount includes all PO change orders on the purchase order that have not been interfaced with the accounting modules, and it also includes the amounts associated with the items in the lower portion of the form.

- Pending Purchase Order — Current Purchase Order + Pending PO Change Orders

- Other Pending COs — In order to be included in this amount, PO change order items must meet the following criteria:

- The change order item's Interface checkbox is selected in the Items grid

- The change order item is included on a PO change order that has not been approved or has been approved, but does not have a final status (Status field in header of the PM PO Change Orders form)

- The change order item is not included on the current PO change order

## Approve / Unapprove

The Approve button is used to automatically approve all of the items on a PO change order. Once you approve a PO change order, you can then interface it to the accounting modules using PM Interface (accessed by selecting Tasks > Open PM Interface).
You can also manually approve individual PO change order items using the Interface checkbox, which allows you to select which items on a POCO will be interfaced with the accounting modules.
When you select the Approve button:

- The Interface checkbox is selected for every PO change order item.

- The Ready for Accounting checkbox is selected on the Info tab in the upper portion of the form.

- The status of the PO change order is changed to the default final status (using the Default Final Status field on the Info tab of PM Company Parameters).

- The Approved field is populated with the current date; however, this only applies if a date has not already been entered in this field.

- The system status of the PO change order is changed to Approved. This status displays at the top of the form next to the Project field.

- All PO change order items on the POCO are locked down so that they cannot be changed.

- The Approve button changes to an Unapprove button.

When you select the Unapprove button:

- The Interface checkbox is cleared for every PO change order item.

- The Ready for Accounting checkbox is cleared.

- The PO change order status is deleted.

- The Approved field is cleared.

- The system status changes to Unapproved

- The PO change order are enabled so that they can be edited.

## Available Estimate / Non-Interfaced / Remaining Estimate

These display-only fields are visible in the Item section, above the Grid/Info/Notes tabs, and show estimate information for the selected sequence. These values are calculated as follows:
FieldCalculation
Available EstimateCurrent Estimated Cost - Actual Cost - Remaining Committed Cost + Non-Interfaced Estimated Cost
Non-InterfacedThis is a more complex calculation that takes a number of factors into consideration. However, in general, this calculation is the sum of the amount and taxes from PM Material Detail and based on certain factors, the subtraction of some PO Item and PO Change Order detail costs (which can include taxes), plus Non-Interfaced Estimated.
Remaining EstimateAvailable Estimate - Non-Interfaced

Related concepts

- [PO Change Orders Overview](/en/vista/vista/project-management/materials/po-change-orders-overview)

- [Material Buyout Overview](/en/vista/vista/project-management/materials/material-buyout-overview)

- [About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)

- [About Distribution Groups/Default Distribution](/en/vista/vista/project-management/create-and-send/about-distribution-groupsdefault-distribution)

- [About Related Items](/en/vista/vista/project-management/about-related-items)

Related tasks

- [Correct an Interfaced PO Change Order Item](/en/vista/vista/project-management/materials/correct-an-interfaced-po-change-order-item)

- [Add Contacts to a Distribution List](/en/vista/vista/project-management/create-and-send/add-contacts-to-a-distribution-list)
