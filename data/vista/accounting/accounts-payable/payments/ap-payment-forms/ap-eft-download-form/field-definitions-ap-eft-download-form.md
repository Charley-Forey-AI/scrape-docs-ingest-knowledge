---
title: "Field Definitions: AP EFT Download Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-eft-download-form/field-definitions-ap-eft-download-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-eft-download-form/field-definitions-ap-eft-download-form"
---

# Field Definitions: AP EFT Download Form

The following is a list of field descriptions for the AP EFT Download form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## CM Account

The CM Account field on the AP EFT Download form.
Enter the bank account from which this payment will be made. Only payable transactions in this payment batch that have been assigned this CM account will be included in this download file.

## Overwrite Existing CM Reference# and
 Seq#

The Overwrite Existing CM Reference# and Seq# checkbox on the AP EFT Download
 form.
Applies only to instances where you are rerunning a batch of EFTs.
Select this checkbox to assign new CM
 Reference and Sequence numbers when you rerun the batch.
Do not select this box if you want to skip any
 payments already assigned a CM Reference # when you rerun the batch.

## CM Reference#

The CM Reference # field on the AP EFT Download form.
This number is used for all payments within this EFT and must be unique within the CM Account. This field is alphanumeric and allows up to 10 characters.

## Description

The Description field in the AP EFT Download form.
When you post this batch, if this particular payment includes more than one vendor, the description you enter appears in various reports and forms in the CM module. If you leave this field blank, the system uses EFT Payment as the description.
If this payment includes only one single vendor, the system inserts the vendor name in those same places in the CM module and any entry in this field is ignored.
This field accepts up to 10 characters.
Note: For US companies, this field populates positions 54-63 of the EFT file's
 Batch Header Record.

## Created Date

The Created Date field on the AP EFT Download form.
Accept the default value (today's date) or modify the creation date for this EFT batch.

## Created Time

The Created Time field on the AP EFT Download form.
Accept the default value or modify the creation time for this EFT batch, in 24-hour format. For example, enter 3:00 p.m. as 15:00.

## File Creation #

The File Creation # field on the AP EFT Download form.
This field displays for Canadian companies only (HQ Company Setup).
Enter a number that uniquely identifies this download file for the bank. You can enter any number up to 9999. The download uses this number in the A, C, and Z records in position 21-24.
Note: If you leave this field blank, the system defaults
 0001 in the download.

## Effective Date

The Effective Date field on the AP EFT Download form.
Accept the default value (today's date), or enter the date all payments in this batch should be made effective by the receiving bank. This date becomes the Paid Date when data is updated to AP Payment History and to the CM module.
Note: If the effective date falls outside the payment/batch month and/or year, the system displays a warning, but allows the date.

## Download Filename

The Download Filename field in the AP EFT Download form.
If
 you are using the Secure File Path feature, a Save As dialog box does not appear when you
 click Download and this field provides your only opportunity to name your EFT
 data file.
Enter a file name or accept the default file name provided.

Related information

- [Secure EFT Data Files](/en/vista/vista/accounting/accounts-payable/payments/electronic-funds-transfers-efts/set-up-the-eft-process/secure-eft-data-files)
