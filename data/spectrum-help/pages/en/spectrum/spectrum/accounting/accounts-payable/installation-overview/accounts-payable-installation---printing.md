---
title: "Accounts Payable Installation - Printing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/installation-overview/accounts-payable-installation---printing"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/installation-overview/accounts-payable-installation---printing"
---

# Accounts Payable Installation - Printing

Use this screen to select default printing settings for the Accounts Payable module. These settings can be changed as needed at any time.
In order to allow users to print a separate check to the vendor for each subcontract so that it can be paired with the Lien Release Form with each payment, [A/P Payment Processing](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing) allows you to separate job payments onto separate check sequences whenever a lien release is applicable, based on Document Tracking setup at the subcontract or vendor level.
Payments not set up for 'Lien release' document tracking will not be split out onto separate checks.
Field/ButtonDescriptions
Use separate sequence for manual check?If you use different check stock for hand-written and computer-generated checks, and you have separate manual check stock, select this checkbox so the last manual check number will be stored.
If this checkbox is left clear, then during Manual Check Entry and pre-paid check entry in A/P Invoice/Create Memo Entry, the default check number will be provided based on the shown check number for both computer-generated and manual checks.
Leave this checkbox clear if you will use the same A/P check stock regardless of whether it is hand-written or printed by the computer during payment processing.

Post 'H' for manual checks?Select this checkbox to update payment records with a preceding 'H' designation (for handwritten) as part of the check number.
For example, if this checkbox is selected, the manual check number will be recorded throughout Spectrum files as "H12345". If this checkbox is left clear, the same check would have been stored as "12345". The 'H' is system-generated during posting; if you enter "12345" in either scenario, selection of this checkbox will determine whether the 'H' is included when updated.
You may prefer to include the 'H' in the check number in order to identify manual checks at a glance. In reviewing payment records, system-generated checks can be easily distinguished from hand-written checks, and there is a possibility the stored information for the manual check may differ from the actual document. Or you may prefer to omit the 'H' for consistency of check numbering; when the 'H' is eliminated, all checks sort sequentially rather than with manual checks at the end.
Important: If the Cash Management module is present, the software will determine whether to include the 'H' designation in the check number based on settings in the Cash Management Bank Account File Maintenance; this setting will override whatever is set in Accounts Payable Installation.

Print instant manual check?Typically, this feature is used only if the computer system includes a dedicated A/P check printer. With check stock always loaded in a designated printer, it is often more convenient to generate "manual" checks using Spectrum.
Select this checkbox to provide the flexibility to print an instant check during Vendor Invoices Entry. The system provides a prompt for Prepaid during invoice entry for use in recording expenses already paid; if this checkbox is selected, an additional prompt will appear asking whether to print an instant manual check.

Use secure download page for electronic files?Select this checkbox if your company requires secure download of ACH files. When selected, only users with a security level of 9 will be able to access the download page.
 Note: If the ePayments Setup button says Complete, Spectrum submits the file directly and does not provide a file for you to download. See [Generate ePayments Export File](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/generate-epayments-export-file).

Last check numberThe most recently used check number is displayed, and can be changed. The number is updated automatically as part of payment processing, and will then be used to offer the next higher number as a default the next time you issue checks.

- If you are installing the Accounts Payable module, enter check number 1. The first time you issue checks, the software will default from this field during payment processing, but you will override it with the correct next check number to be issued. From then on, this field will reflect your actual last check number.

- If the Cash Management module is present, the software will determine the next check number based on settings in the Cash Management Bank Account File Maintenance screen.

Next electronic check numberAn "E" (Electronic) displays to the left of the field and you may enter a 5-digit number. This number will be bumped incrementally by 00001.
This number is used during the 'File Compilation for United Stated (ACH)' and the 'File Compilation for Canada (AFT)'.

Spectrum ePayments
Next ePayments check numberA "V" (Vendor) displays to the left of the field, and you may enter a 5-digit number. This number will be bumped incrementally by 00001.
This number is used during processing of electronic vendor payments.

Enable direct connection to ePayments?
ePayments Setup (button)
Select to open the ePayments Direct Connection Setup window. Enter the required information as you received it from Corpay, then select Connection Test to test that the entries are valid.
These screens indicate whether or not the direct connection to ePayments has been established:

- Generate ePayments Export File

- Import ePayments Return File

If the connection is established at the moment you generate the ePayments export file, Spectrum submits the file directly instead of providing a file for download.

Related information

- [Generate ePayments Export File](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/generate-epayments-export-file)
