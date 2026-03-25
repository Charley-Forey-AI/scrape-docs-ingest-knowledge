---
title: "PO Compliance Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form"
---

# PO Compliance Form

Use this form to keep track of vendor compliance requirements on purchased items.
Tracking compliance on a PO helps to determine whether a vendor is paid or payment is withheld. You can set up compliance to track the following:

- Receipt of Material Safety Data Sheets (MSDS), which are required by manufacturers of specific materials or equipment.

- Receipt of Certifications of Specifications, which certify that standard specifications required for certain types of machines or equipment have been met.


You can initialize compliance codes to a purchase order by assigning a compliance group to the purchase order in PO Purchase Order Entry. When the batch is updated, all of the compliance codes assigned to the compliance group are automatically set up on the purchase order.
If you change the compliance group for a purchase order, the system retains all original codes and adds any unique codes from the new group. If you manually deleted codes prior to changing the compliance group and they exist for the new compliance group, they will be re-added. You can manually delete them again if needed.
Compliance may also be set up by vendor in AP Vendor Compliance. This should be used if a compliance code applies to all purchase orders for the vendor. When a compliance code is added or the status of a code is changed in that form, specify if this is to be applied to all active purchase orders. If applied, the system updates the status or adds the code on all open purchase orders for the vendor.
Note: Memos added for the vendor/compliance code (in AP Vendor Compliance) will display in the Vendor Memo column. This column is display only, so any edits/additions to memos must be made via AP Vendor Compliance.

To have compliance verified before a purchase order is paid, select the Verify checkbox for each compliance code on the purchase order. Verification depends on setup options in the AP Company Parameters, Audit Options tab. If compliance is not met, then you may be warned at the time of invoice entry, invoices may not be pulled for payment, or you may just receive a warning on the AP Payment Preview With Compliance report run when payments are selected. With just the warning at the time of payment, you can decide whether to put the invoice on hold, pay the vendor, issue a two-party check, or take whatever other measures you decide are most appropriate.
When verifying compliance for flag type codes, the Complied flag status is checked and if set to N, the warning message prints.
For date type codes, the Expiration Date specified in PO Compliance Tracking is compared to the Invoice Date of the payables transaction. If the payables transaction has a more recent date than the specified Expiration Date, the warning message prints.

Related information

- [Vendor Compliance Tracking](/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking)

- [AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)

- [PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)
