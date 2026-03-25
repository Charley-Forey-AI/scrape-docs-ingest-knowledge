---
title: "Purchase Order Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r1/costs-and-contracts/purchase-order-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r1/costs-and-contracts/purchase-order-features"
---

# Purchase Order Features

Vista 2022 R1 delivers on user-requested Purchase Order enhancements, fixes, and other improvements

## Added Validation of Tax Type to Purchase Order Entry Batch Validation

When you post a purchase order batch, the system now validates that if a tax code exists, there is a valid tax type associated with the tax code. This validation now ensures that transactions added to a purchase order batch from a third-party app or via the Imports module have a valid tax type/tax code combination. The validation will throw an error if:

- a tax code exists, but no tax type

- both a tax type and tax code exist, but the tax code is invalid for the tax type

If this occurs, you must correct the transaction(s) before you can post the batch.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
