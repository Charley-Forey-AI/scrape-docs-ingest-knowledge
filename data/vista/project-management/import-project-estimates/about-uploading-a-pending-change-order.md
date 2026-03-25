---
title: "About Uploading a Pending Change Order | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-uploading-a-pending-change-order"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-uploading-a-pending-change-order"
---

# About Uploading a Pending Change Order

This option is used when the import data will be uploaded
 into PM as a change order.
Once checked, fields in the lower section of the form are enabled. Specify the change order type (defined in PM Document Types) and enter the change order number.
If you are uploading to a new project, enter a new change order. However, if you are uploading to an existing project, you can specify either a new change order or an existing change order.
Once you have identified the pending change order, the change order items are assigned as follows:
If a single contract item exists in the work file and . . .

- you are uploading contract items
 as change order items (option in PM Import Templates), the PCO Item input is
 disabled, and the contract item becomes the change order item. If the contract item
 cannot be formatted as a change order item, the system assigns a sequential
 number.

- you are not uploading contract items as change order items, the PCO Item input is enabled, and you must specify the change order item.

Note: Both of the conditions specified above also apply if you are uploading data to an existing project and PCO.If multiple contract items exist in the work file and . . .

- you are uploading contract
 items as change order items (option in PM Import Templates), the Starting PCO Item
 and Increment By inputs are disabled, and contract items become change order
 items. If contract items cannot be formatted as change order items, the system
 assigns sequential numbers.

- you are not uploading contract items as change order items, the Starting PCO Item and Increment By inputs are enabled and you must specify the number with
 which to begin numbering CO items, as well as the number by which to increment the items. For example, if you set the starting number at 200 and increment by 5, your change order items will be uploaded as
 200, 205, 210, etc.

If you are uploading to an existing project and PCO, the Starting PCO Item and Increment By options are used regardless of whether you have specified to upload contract items as change order items.
