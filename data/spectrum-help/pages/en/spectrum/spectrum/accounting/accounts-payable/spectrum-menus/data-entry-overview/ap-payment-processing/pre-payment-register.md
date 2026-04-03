---
title: "Pre-Payment Register | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/pre-payment-register"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/pre-payment-register"
---

# Pre-Payment Register

The Pre-Payment Register is a listing, by vendor, of invoices selected for payment. The report includes the total payment for each vendor and a grand total for the entire check run. Use this listing to review selections before printing checks. Click the Preview button and the corresponding screen will display, allowing entry of the G/L account from which cash for the check run should be taken.
[A/P Payment Selection](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/ap-payment-selection) is used to change the selected invoices which appear on the report, if necessary, before checks are run. In this case, the Pre-Payment Register must be reprinted. Be sure this report is correct before proceeding to print checks.

- If a payment location code was specified in the Vendor Location screen, any invoices with matching vendor and location codes will be grouped together.

- Credit memos applied to invoices may result in a negative amount. Checks for negative dollar amounts will not print.

- Payment Processing separates job payments onto separate check sequences whenever a lien release is applicable, based on Document Tracking setup: looking first at the subcontract level and that at the vendor level. Payments not set up for 'Lien release' document tracking are not split out onto separate checks.

- In order to process deselected items, the subcontract should be set up again in the [Subcontracts](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts) screen. If a credit memo and invoice cancel each other resulting in zero dollars being owed to a vendor, a void check for $0.00 will print.

- The [Document Tracking Item Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance) will create the possible tracking items to set up by vendor or subcontractor in the Vendor/Subcon Document Track screen.
