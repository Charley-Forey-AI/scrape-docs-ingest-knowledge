---
title: "Generate ePayments Export File | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/generate-epayments-export-file"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/generate-epayments-export-file"
---

# Generate ePayments Export File

If you have selected ePayments for electronic vendor payments, use this screen to generate the export file to send to Corpay for processing.

## Export File: Download vs Direct submission

The output method of this file depends on your settings in the Printing tab of the Accounts Payable Installation screen; if the entries on that screen are valid, a note displays on this screen indicating that the direct connection to ePayments has been established.

- If the Enable direct connection to ePayments checkbox is selected and if the ePayments Setup button says Complete, Spectrum

- Submits the file directly to Corpay and does not provide a file for you to download.

- Ignores your selection in the Use secure download page for electronic files checkbox and does not provide the option to download the file.

- If that checkbox is not selected, Spectrum uses your setting in the Use secure download page for electronic files checkbox:

- If selected - once the export file is generated it becomes available on the [Secure Electronic File Downloads](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/secure-electronic-file-downloads) screen.

- If not selected - the export file is saved locally.

You can re-generate the export file as needed, and Spectrum will assign a new check number automatically.

Table 1. Field DescriptionsFieldDescription
Bank accountThe bank account code for ePayments transactions displays in this field.
Export file nameEnter an export file name in the form Company Code+EPAY+MMDDYY.
Check dateSpecify a check date for the export file. This date must be within the A/P minimum/maximum processing dates, and will default to the current A/P processing date.
