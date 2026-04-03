---
title: "Write Automatic Deposits Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits-update"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits-update"
---

# Write Automatic Deposits Update

Protection is incorporated into the Write Auto Deposits
 Update to assure that an operator with insufficient security access for a Confidential Payroll
 company will not be allowed to proceed with the file creation if the Confidential Payroll
 company is included in the batch.
Important: Files are exported to the DOWNLOADS location on
 the workstation, not to a particular path.The operator must have
 Payroll category access to the confidential company, and the security level for Payroll
 in that company must be greater than or equal to the level assigned to the Write Auto
 Deposits screen.The Write Auto Deposits Update allows you to
 include header information in the auto deposit file. You can include a company-specific
 text file (where the first three characters of the file name match the current company
 code followed by NACHA.TXT, for example, XYZNACHA.TXT), or a general header
 (NACHAHDR.TXT). Be sure to save the .txt file to your Spectrum data directory. If you
 press Enter to accept the
 default file name and the software finds that the file already exists, the following
 error message displays: "This file already exists. Click OK to continue." The software will first look for a company-specific text file, and if
 this file is found, the text contained in it will be copied automatically into the
 beginning of the NACHA file. If the company-specific file is not present, the software
 will look for and copy the NACHAHDR.TXT file text into the beginning of the NACHA file.
 These files can be edited using any text editor, such as Notepad. If no header
 information is required by the company's bank, these files should not be present in the
 Spectrum data directory.
Note: Note Regarding Company Codes Containing "&": In order for the
 header record to be read from a company-specific file, manually replace the "&" with a
 zero or use the general file NACHAHDR.TXT. For example, for company code 2&D, the
 header file 2&DNACHA.TXT will be ignored, but 20DNACHA.TXT will be read.
