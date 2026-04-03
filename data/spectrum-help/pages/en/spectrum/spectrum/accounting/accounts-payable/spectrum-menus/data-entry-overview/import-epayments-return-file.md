---
title: "Import ePayments Return File | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/import-epayments-return-file"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/import-epayments-return-file"
---

# Import ePayments Return File

Use this screen to import the ePayments return file from Corpay.
Files you import will update the ePayments fields on the Vendor Payment History and Subcontract Payment History screens.
Once the return file has been imported and the data mapped, the Return File Import Report runs automatically. This report provides totals on Invoice/Credit Memo Amount, Discount Amount, Total Payment, and Retention Paid.
If there are issues with the API credentials, a note displays on the screen.
ButtonDescription
ContinueIf your API connection is set up, select this button to download all return files available for your Company ID. This eliminates the need to have to download the CSV file from the AP Gateway and manually import it into Spectrum.Important: This process downloads and imports ALL return files that have not already been imported. This is so that the system continues to update Spectrum with the latest new information, even if payments have been released at different times on the AP Gateway.
If your API connection isn't set up, select this button to upload the file you've downloaded from the gateway.
CancelStops the process.
ErrorsOpens the [ePayments Import Errors](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/import-epayments-return-file/epayments-import-errors) screen to view any transactions that could not be imported.
ManualFor use when you want to control which return files are imported. Download a specific return file from the AP Gateway and use this button to upload it manually. This option also provides backward compatibility.
