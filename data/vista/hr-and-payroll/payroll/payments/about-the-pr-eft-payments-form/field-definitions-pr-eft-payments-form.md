---
title: "Field Definitions: PR EFT Payments Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-eft-payments-form/field-definitions-pr-eft-payments-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-eft-payments-form/field-definitions-pr-eft-payments-form"
---

# Field Definitions: PR EFT Payments Form

The following is a list of field descriptions for the PR EFT
 Payments Form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Assign: PR Group

 Enter the PR group to process.

##  Assign: Pay Period Ending Date

 Enter the pay period ending date that, when combined with the PR group, will identify an open pay period. Initially defaults the last accessed pay period for the current user.

##  Assign: Payment Seq#

 Enter a valid payment sequence number to identify the sequence for which you want payments downloaded in this pay period.

## Assign: Restrict by Employee SortName?

The Restrict by Employee SortName? checkbox on the PR EFT Payments form, Assign tab.
Select this checkbox to restrict assigning EFT payment information to single employee or a selected range of employees in the specified payroll group and pay period.
Leave this checkbox unselected to include all employees within the specified payroll group and pay period.

## Assign: Beginning Employee Sort Name

The Beginning Employee Sort Name field on the PR EFT Payments form, Assign tab.
Enabled only if you selected the Restrict by Employee SortName? checkbox.
Entry in this field is required.
Enter the employee sort name with which to begin assigning EFT information.

## Assign: Ending Employee Sort Name

The Ending Employee Sort Name field on the PR EFT Payments form, Assign tab.
Enabled only if you selected the Restrict by Employee SortName? checkbox.
Entry in this field is required.
Enter the employee sort name with which to end assigning EFT information. Defaults the employee sort name specified in the Beginning Employee Sort Name field.

##  Assign: Effective Date

 Enter the date when these payments should be made effective. This entry is used as the paid date when updating CM.

##  Assign: Paid Month

 Enter the paid month, which will be used when updating CM, GL (credit to Cash), and Employee Accumulations. Must be either the first or second month assigned to this pay period.

## Assign: CM Reference#

Enter the CM Reference #, up to 10 digits, that will be used for all payments within this EFT.
Note: The ACH format used to transmit data is limited to eight digits. Only the first eight digits are transmitted, but the system uses all 10 digits for internal tracking.

##  Assign: PR Group

 Enter the PR group to process.

##  Clear: PR Group

 Specify the PR group for which to clear EFT entries.

##  Clear: Pay Period Ending Date

 Enter the pay period ending date for which to clear EFT entries. This date, when combined with the PR group, will identify an open pay period. Initially defaults the last accessed pay period for the current user.

## Clear: CM Reference#

Enter the CM reference of EFT entries you want to clear, or leave blank to include all EFT entries for this payroll group/pay period. Press F4 for a list of existing CM reference numbers for this payroll group/pay period. Click the Refresh button to populate the grid with all entries meeting the criteria, then click Clear to remove existing payment information from all employees displayed in the grid. Once cleared, you may return to the first tab and assign new EFT payment information.

##  Download: PR Group

 Specify the PR group to process; defaults from Assigned tab.

## Download: Export File Type

The Export File Type field on the PR EFT Payments form, Download tab.
This field is enabled for U.S. companies only (that is, companies with a Default Country of US in HQ Company Setup).
Select the type of EFT that you are downloading.

- Active – Pulls direct deposit distributions from employee earnings already assigned a CM Reference #. Use this option to create a text file with 'live' payroll information for export to your bank.

- Prenote – Creates a text file using EFT information from all active employees within the PR Group that have a 'prenote' designation. Use this option as needed to confirm Bank Account and Routing information. The "Pay Period Ending Date" and "CM Reference #" inputs are disabled.

- Test – Creates a text file with a single 'dummy' entry, allowing you to check its format. All inputs are disabled.

##  Download: Pay Period Ending Date

 Disabled if using the Prenote or Test export file type options.
 Enter the open pay period ending date for which to download EFT payments or the closed pay period ending date for which to re-download EFT payments. Defaults the pay period ending date specified on the Assign tab.

## Download: CM Reference#

Disabled if using the Prenote or Test export file type options.
Specify the CM reference number assigned to the payments you want to download. Only EFT payments with this reference number are included in the download. Defaults the CM Reference # entered on the Assign tab.

## Download: File Creation Number

This field displays for Canadian companies only (HQ Company Setup).
Enter a number that uniquely identifies this download file for the bank. You can enter any number up to 9999. The download uses this number in the A, C, and Z records in position 21-24.
Note: If you leave this field blank, the system defaults 0001 in the download.

## Download: Description

Enter a description, up to 10 characters. The default description is “EFT.”
Note: This field populates positions 54-63 in the EFT file, Batch Header Record.

##  Download: Effective Date

 Disabled if using the Active or Test export file type options.
 Specify the effective date for this prenote file.
 If downloading an Active export file, this field displays the effective date specified on the Assign tab, but cannot be edited.

## Download: Download Filename

Download Filename field in the PR EFT Payments form, Download tab
If
 you are using the Secure File Path feature, a Save As dialog box does not appear when you
 click Download. This field provides your only opportunity to name your EFT data
 file.
Enter a file name (cannot contain * \ | : " < > ? characters) or accept the default file name provided.
Help Keyword 350038047

Related information

- [Secure EFT Data Files](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information/secure-eft-data-files)
