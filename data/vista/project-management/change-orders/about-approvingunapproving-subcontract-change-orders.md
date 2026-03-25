---
title: "About Approving/Unapproving Subcontract Change Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-approvingunapproving-subcontract-change-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-approvingunapproving-subcontract-change-orders"
---

# About Approving/Unapproving Subcontract Change Orders

The Approve / Unapprove Button in PM Subcontract Change Orders allows you to approve or unapprove subcontract change orders.
 You can only interface approved subcontract change orders.The Approve button at the bottom of the form allows you to automatically approve a subcontract change order and its items, which you can then interface with the accounting modules using PM Interface.
 You can also manually select which subcontract change order items should be interfaced by selecting the Interface checkbox on the Info tab in the lower portion of the form. Then select the Ready For Accounting checkbox on the Info tab in the upper portion of the form. Only items with this checkbox selected are included during the interface process.
When you select the Approve button, the system:


- Selects the Interface checkbox for every subcontract change order item.

- Selects the Ready to Interface checkbox in the subcontract header (upper section of form).

- Sets the Status field in the subcontract change order header to the default final status (defined in PM Company Parameters).

-  Populates the Approved field in the header with the current date.

- Changes the system status of the subcontract change order (displayed to the right of the Project field) to Approved.

-  Disables the subcontract item section of the form to prevent modifying existing items or creating new ones.

- Changes the Approve button to an Unapprove button.
 Note: If you try to approve a change order on a subcontract item that is being corrected, the system displays a message indicating that "SL Item(s) have been marked for correction", and you will be unable to approve the subcontract change order

When you select the Unapprove button, the system:


- Clears the Interface checkbox for every subcontract change order item.

- Clears the Ready for Accounting checkbox in the subcontract header.

-  Clears the Status field in the subcontract change order header.

-  Clears the date from the Approved field.

-  Changes the system status of the SubCO to Unapproved.
