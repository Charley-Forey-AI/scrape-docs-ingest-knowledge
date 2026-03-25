---
title: "Accounts Payable Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.6/accounting/accounts-payable-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.6/accounting/accounts-payable-features"
---

# Accounts Payable Features

Vista 2025.6 delivers on user-requested Accounts Payable enhancements, fixes, and other improvements.

## Increased Character Allowance for EFT Seq # on Payment Reversals

The character allowance for the EFT Seq # field in AP Prior Month Check Reversal was modified to allow entering numbers larger than 255.

## Viewpoint ePayments Renamed to ePayments

The Viewpoint ePayments feature in Vista is now called ePayments. This change affects the following forms and fields. For report changes, see [Vista Reports](/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.6/system-tools/vista-reports):
Form/ReportChange
AP Company ParametersOn the Payment Services tab:

- The Viewpoint ePayments group box is now titled "ePayments".

- The Upload Invoice Attachments to Viewpoint ePayments checkbox is now titled "Upload Invoice Attachments to ePayments".

AP Initialize PaymentsIn the Payment Methods group box, the Viewpoint ePayments checkbox is now titled "ePayments".
AP Payment Preview
AP Payment Workfile
AP Payment HistoryChanges made include:

- In the Payment Method dropdown (above the tabs), the N-Viewpoint ePayments option is now titled "N-ePayments"

- On the Add'l Info tab, the Viewpoint ePayments group box is now titled "ePayments".

AP Payment PostingIn the Pay Method dropdown (header Info tab), the N-Viewpoint ePayments option is now titled "N-ePayments".
AP Prior Mth Payment ReversalIn the Payment Method dropdown (above the tabs), the N-Viewpoint ePayments option is now titled "N-ePayments"
AP Recurring InvoicesIn the Pay Method dropdown (header Info tab), the N-Viewpoint ePayments option is now titled "N-ePayments".
AP Transaction EntryIn the Pay Method dropdown (Payment Overrides tab), the N-Viewpoint ePayments option is now titled "N-ePayments".
AP Unapproved Invoice Entry
AP VendorsIn the Pay Method dropdown (Payment Method tab), the N-Viewpoint ePayments option is now titled "N-ePayments".
AP Viewpoint ePayments ExportChanges made include:

- The Form's title changed to AP ePayments Export

- In the Payment Methods group box, the Viewpoint ePayments only option is now titled "ePayments only".

- In the Download Filename field, the default filename is now "ePayments Co # (where number defaults from active company)

AP Void PaymentsIn the Payment Method dropdown (Filter Payments section) and Pay Method columns (Eligible to Void and Payment Batch grids), the N-Viewpoint ePayments option is now titled "N-ePayments".
VA Site SettingsOn the Add'l Settings tab, the Viewpoint ePayments Settings groupbox is now titled "ePayments Settings".

## Improved Error Report for Invoiced Amounts Exceeding PO Totals

The HQ Batch Control Error List now reports a single "invoiced amount exceeds PO total cost" error when posting PO invoices (in AP Transaction Entry) that exceed a purchase order's total cost.

Previously, the report would repeat the error for every PO line item without a line-level error. Additionally, the error message no longer includes the batch line number or item number, as they are not relevant at the PO total level.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
