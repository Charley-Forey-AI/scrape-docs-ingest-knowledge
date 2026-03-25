---
title: "Accounts Payable Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/accounting/accounts-payable-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/accounting/accounts-payable-features"
---

# Accounts Payable Features

Vista 2024 R1 delivers on user-requested Accounts Payable enhancements, fixes, and other improvements.

## Add PO and SL to Unapproved Invoice Header

When entering unapproved invoices (in AP Unapproved Invoice Entry), you now have the option to specify purchase order and subcontract numbers in the invoice header. These values are then used as defaults when entering invoice lines, enabling quicker entry.
To enable this functionality, new PO and SL fields were added to the invoice header. In addition, the following changes were made:

- If you enter only a PO number in the invoice header, new lines automatically default a Line Type of 6-PO and the PO field automatically defaults the PO number you specified in the header.

- If you enter only an SL number in the invoice header, new lines automatically default a Line Type of 7-SL and the SL field automatically defaults the SL number you specified in the header.

- If you enter both a PO and SL number in the invoice header, new lines automatically default a Line Type of 6-PO and the PO number from the header. If you change the line type to 7-SL, the SL field defaults the SL number from the header.

## Initialize POs from Unapproved Invoice Header

You now have the ability to initialize a purchase order to an unapproved invoice (in AP Unapproved Invoice Entry) via the invoice header.
With focus in the header of the desired invoice, select File > Initialize from PO. The AP Purchase Order Initialize form opens, displaying all POs for the vendor on the Purchase Order tab or all POs for the vendor that have been received in PO Receipts Entry on the Receiver # tab. If you entered a purchase order in the PO field of the invoice header, the PO field on the Purchase Order tab automatically defaults that PO number and filters the grid accordingly. You can select that PO to initialize or use the filter to select a different PO.
Note: If you initialize a PO at the invoice line level, the Purchase Order tab does not automatically filter by the PO specified in the invoice header. You must manually enter the PO number in the PO field and select Apply Filter.

For more information, see [Initialize Purchase Orders to AP Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/enter-unapproved-invoices/initialize-purchase-orders-to-ap-invoices).

## Update AP Invoices / AP Unapproved Invoices for SM Tax Handling

 In conjunction with the changes made in Service Management for Tax Handling, the AP Transaction Entry and AP Unapproved Invoice Entry forms will now default tax information (Tax Type and Tax Code) for SM-related lines (type 8-SM Work Order) based on the taxability of the work order scope. Taxability is determined by the SM Cost Type entered on the invoice line, and the Material Tax Override and Tax Option Override specified for the work order scope. For detailed information, see the F1 Help.
For more information about the tax changes made in SM, see the [SM Tax Handling](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/service-management/service-management-features#concept-k1quaafr1002--en__SMTaxHandlingRN) feature in the Service Management release notes.

## AP Invoices Now Track Originating User

When you enter invoices, whether manually, via import, or via auto invoicing, the system now records who entered the invoice. To view this information, a new Entered By field was added to the following forms:

- AP Transaction Entry, header Info tab

- AP Unapproved Invoice Entry, header Info tab

- AP Unapproved Invoice Review, invoice header Grid tab

This display-only field shows the login name of the person who entered the invoice.
 For unapproved invoices, when the invoice is approved and added to an AP Transaction Entry batch, the Entered By field reflects the name of the user who entered the invoice, not the person who added the invoice to the AP batch.

## Updates to Split Released Retainage Put Back on
 Hold

Note: Use of the word retainage refers
 to retainage, retention, and holdback.

If you release retainage and split it for payment, but you put the retainage back on hold without paying any of the split, the batch posting action to put the retainage back on hold will automatically remove the split.

## Updates to Making Partial Payments of Released Retention /
 Holdback with Tax (Australia and Canada)

Note: The following applies to Australian and Canadian companies only, as Australia and Canada allow tax on
 retainage. Use of the word retainage refers to retention
 and holdback.

If you release retainage and split it for payment, but you only want to make a partial payment, you should pay the portion of the split with the retainage tax *first*. This is because if the taxed remainder of the retainage is put back on hold, you will most likely see an incorrect tax amount when you release the retainage in the future. For more information, see [About Partial Payments for Split Released Retention / Holdback with
 Tax (AU and CA)](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-partial-payments/about-partial-payments-for-split-released-retention--holdback-with-tax-au-and-ca).

## AP EFT Downloads Now Process in the Background

When you download EFT files on the AP EFT Download form, the
 process now runs in the background, enabling you to continue using Vista for other work. You will receive a
 notification when the download finishes.
For more details, see [AP EFT Download Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-eft-download-form).
Similar background processing was previously implemented in
 Payroll on the following forms: PR Check Print, PR Direct Deposit Print, and PR EFT
 Payments.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
