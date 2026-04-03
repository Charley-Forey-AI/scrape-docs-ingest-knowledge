---
title: "Write Automatic Deposits | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits"
---

# Write Automatic Deposits

Spectrum provides the option of depositing an employee's
 paycheck directly into up to five different bank accounts.
For the automatic deposit feature to work, the Payroll
 Installation screen must be set appropriately, and bank account information
 must be completed in the Auto Deposit dialog box in
 Employees for all employees desiring direct deposit.
The Write Auto Deposits
 Update allows you to include header information in the auto deposit file.
 You can include a company-specific text file. Be sure to save the .txt file to your
 Spectrum data directory. If you press Enter the export file name defaults to the name from the previous export.
 If the software finds that the file already exists, the browser tacks on numbers to the
 file name, so if the first export is to myfile.txt then the second will be to myfile-1.txt
 in Firefox or myfile(1).text in Chrome. If Cash Management is installed, then the header
 text and default export file name come from Account Code File Maintenance > Electronic Payment tab. There's also an electronic payment format option that if set to Canada
 (AFT) will present a slightly different auto deposit start screen. If Cash Management is
 NOT installed, then the header text comes from HHCNACHA.TXT or if that file doesn't exist
 then NACHAHDR.TXT.
The software will first look for a company-specific text file, and if this file is found, the text contained in it will be copied automatically into the beginning of the NACHA file. If the company-specific file is not present, the software will look for and copy the NACHAHDR.TXT file text into the beginning of the NACHA file. These files can be edited using any text editor, such as Notepad. If no header information is required by the company's bank, these files should not be present in the Spectrum data directory.
If the Cash Management module is installed and a bank account has been
 designated for the pay cycle, the Payroll update will transfer transaction data to the
 Cash Management > Bank Reconciliation table. At most, a single record is added across all Auto Deposits for all
 employees processed during the Payroll Update, and if no auto deposit check were paid, then
 no record is added for the auto deposit total.
Based on the 'Electronic payment format' assigned to the bank account, this starting screen will offer input fields for 'United States (ACH)' or 'Canada (AFT)'. The Canadian AFT file layout is based on the Standard 005 for the Exchange of Financial Data on AFT Files.
Also, if a Cash Management bank account was specified in Set Payroll
 Cycle AND that bank account is configured for 'Electronic Payment' using the 'ACH file
 format, the screen will automatically default in the appropriate ACH/direct deposit bank
 information over into the Auto Deposit screen. In this manner, you
 can have multiple NACHA/ACH files within your company.

Related information

- [Save Auto Deposit Files](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/save-auto-deposit-files)

- [Direct Deposit Guidelines](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines)

- [Write Automatic Deposits Update](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits-update)
