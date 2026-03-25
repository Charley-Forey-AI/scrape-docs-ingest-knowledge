---
title: "Field Definitions: IN Material Order Confirm Init Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-confirm-init-form/field-definitions-in-material-order-confirm-init-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-confirm-init-form/field-definitions-in-material-order-confirm-init-form"
---

# Field Definitions: IN Material Order Confirm Init Form

The following is a list of field descriptions for the IN
 Material Order Confirm Init form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Date

 Enter the confirmation date for this material order.

##  Material Order

 Enter the material order to confirm.

##  Confirm the Remaining Units for all Items

 Check this box to confirm the 'remaining' units for all items on the material order. The 'Confirmed This Time' column (in grid) will default the 'remaining' units for each item on the material order (less any changes to remaining units already in the current batch).
 Do not check this box if you want to manually enter the 'confirmed' units for each item on the material order.

## Include Items Where Confirm This Time Equals Zero

 Select this checkbox to include items in the
 confirmation where the Confirm this Time field value is
 zero.

## Confirm This Time

If you are confirming all remaining units (you
 checked the Confirm
 the 'Remaining Units' for all items box), this field defaults the item's
 current remaining units (Ordered — Confirmed To Date); the Remaining units
 column is set to 0.00.
If not confirming remaining units, enter the number of units of this material being confirmed at this time.
Note: If you enter a negative value, units will be 'returned' to stock.

##  Remaining

 If remaining units were initialized, this field defaults 0.00.
 If remaining units were not initialized, this field defaults the current remaining units (Ordered — Confirmed To Date — Confirmed This Time).
Note: You may override this value if desired; however, the system will not recalculate the confirmed units. In addition, it may cause negative remaining units, which can result in understated committed costs and units.
