---
title: "Copy a Material Order | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-copy-form/copy-a-material-order"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-copy-form/copy-a-material-order"
---

# Copy a Material Order

Follow the steps below to create a new material order using the information already entered on an existing material orders.
Copying material orders can save you time if you have commonly used standard material orders.

1. Select File > Copy Material Order from the IM Material Order Entry form.The IN Material Order Copy form displays.

1. In the Source section, press F4 in the Material Order field to select the material order that you want to copy.

1. In the Destination section, enter the material order number that you want to create in the Material field. If you use auto-numbering, enter "new" and the system will automatically assign the material order the next available number.Auto-numbering is set up using the Auto Generate MO#s box in IN Company Parameters. The system will automatically generate the material order number based on the Last Used MO# in IN Company Parameters.
Note: Manually entered numbers will not update the Last Used MO# field in IN Company Parameters.

1. Enter a description of the material order in the Description field, up to 60 characters.

1. Enter the JC company where the materials are being allocated to in the JC CO# field.

1. Enter the job being charged for the materials in the Job field or press F4 to select one from a list. You can only select a job that is associated with the JC company selected in the JC CO# field.

1. Complete the Order Date and Ordered By fields.

1. Select what should be copied.

- Quantities - Select this checkbox to copy units from the source material order to the new material order. If not selected, the units and total values will default to 0.00 for each item.

- Unit Prices - Select this checkbox to copy unit prices from the source material order to the new material order. If not selected, the unit price for each material will default based on the pricing option for jobs in IN Company Parameters and the current unit price/unit cost values in IN Location Materials.

- Notes - Select this checkbox to copy header and item notes from the source material order to the new material order.

1. Click the Copy button when complete.

Related information

- [About the IN Material Order Entry Form](/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-entry-form)

- [About the IN Material Order Confirmation Form](/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-confirmation-form)
