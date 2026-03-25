---
title: "Field Definitions: IN Material Order Confirmation Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-confirmation-form/field-definitions-in-material-order-confirmation-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-confirmation-form/field-definitions-in-material-order-confirmation-form"
---

# Field Definitions: IN Material Order Confirmation Form

The following is a list of field descriptions for the IN
 Material Order Confirmation form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq#

 Enter NEW to create a new entry or enter the
 batch sequence number of an existing entry to display.

##  Matl Order

 Enter the material order to confirm. Press F4 for a list of valid material orders.

##  Item

 Enter the material order item to confirm. Press F4 for a list of valid items for this material order.

##  Date

 Specify the date for this confirmation entry. Initially defaults the current date.

##  Confirmed

 Specify the number of units of this material that are being confirming at this time. Initially defaults the “remaining” units.
Note: If you enter a negative value, units will be returned to stock.

##  Change to Remaining

 This field defaults the change to the item's remaining units; typically the opposite of the confirmed amount. For example, if you confirmed 100.000 units, this field will default as -100.000.
Note: You may override this value if necessary; however, the system will not recalculate the confirmed units. In addition, it may cause negative remaining units, which can result in understated committed costs and units.

## Memo

Enter miscellaneous notes about this confirmation entry, if applicable, up to 60 characters. Initially defaults the material's description from the material order item (if one exists).
Note: The entry here is updated to JCCD (Cost Detail). If you override the default description, the override description (or memo) will be updated to JCCD, not the material description. However, if this field is blank, JCCD will be updated with the material description from HQMT (HQ Materials).
