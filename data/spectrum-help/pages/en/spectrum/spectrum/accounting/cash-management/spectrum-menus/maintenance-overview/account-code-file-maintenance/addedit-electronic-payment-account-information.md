---
title: "Add/Edit Electronic Payment Account Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/account-code-file-maintenance/addedit-electronic-payment-account-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/account-code-file-maintenance/addedit-electronic-payment-account-information"
---

# Add/Edit Electronic Payment Account Information

Add or edit electronic payment account information in the Account Code File Maintenance screen with the Electronic Payment tab.
Note: The Electronic Payment tab is disabled if a credit card account is selected.
The Account Code File Maintenance screen stores electronic payment processing information that is required by banks and varies by bank account. While the ACH file specifications allow for funds to be withdrawn from the vendor's account (in the CCD record), it is up to you to obtain proper authorization when setting up ACH to perform such a withdrawal. Negative payments will always be processed when using the ACH file format.
Select an Electronic payment format:

- Not defined

- United States (ACH)

- Canada (AFT)

If you select 'United States (ACH)' or 'Canada (AFT)' additional fields display.
Electronic Payments allow you to include header information in the auto deposit file. You can include a company-specific text file (where the first three characters of the file name matches the current company code followed by NACHA.TXT, for example, XYZNACHA.TXT), or a general header (NACHAHDR.TXT). Be sure to save the .txt file to your Spectrum data directory. If you press Enter to accept the default file name and the software finds that the file already exists, the following error message displays: "This file already exists. OK to continue."
The software will first look for a company-specific text file, and if this file is found, the text contained in it will be copied automatically into the beginning of the NACHA file. If the company-specific file is not present, the software will look for and copy the NACHAHDR.TXT file text into the beginning of the NACHA file. These files can be edited using any text editor, such as Notepad. If no header information is required by the company's bank, these files should not be present in the Spectrum data directory.
