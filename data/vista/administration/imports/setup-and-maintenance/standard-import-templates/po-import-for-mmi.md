---
title: "PO Import for MMI | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/po-import-for-mmi"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/po-import-for-mmi"
---

# PO Import for MMI

 Additional Information about the PO Import for MMI template.
When importing material purchase records, you can have the records added to an existing purchase order in the Purchase Order (PO) module.
The Template Detail for the POHB record type includes an
 AllowAddItemToExistingPO identifier (#155). To allow adding
 material records to an existing purchase order, make sure the User Default
 Value field for this identifier is set to Y
 (default).
During the import process, the system adds the material records as items to an existing
 purchase order. If a material already exists on a purchase order item, a new purchase
 order item is added; the import does not update the values for the material on the
 existing purchase order item. If no purchase order is found, a new purchase order is
 created.
If you always want a new purchase order created for material records, set the
 User Default Value field to N.
Note: As with other standard Viewpoint templates, it is recommended that you copy this template and make your modifications to the copy. This prevents your modifications from being overwritten if an update is made to the template for a release.
