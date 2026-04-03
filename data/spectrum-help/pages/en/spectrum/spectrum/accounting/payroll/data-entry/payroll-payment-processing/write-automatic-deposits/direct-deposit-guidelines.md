---
title: "Direct Deposit Guidelines | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines"
---

# Direct Deposit Guidelines

When starting a direct deposit option for your company,
 Viewpoint recommends that you contact your bank and notify it of your intentions.
Some banks require a summary record in the NACHA format, others do not. Determine needs at
 your bank then record preferences in the Payroll Installation screen. Your bank may also
 require a "prenotification" (zero-dollar) file, usually 10 days prior to your first
 automatic deposit transaction, in order to check the accuracy of account numbers and file
 format. You will need to leave a sufficient amount of time for testing and making the
 necessary adjustments.
The Automated Clearing House (ACH) is a nationwide electronic payments system used by thousands of participating financial institutions, corporations, and consumers. The concept of a nationwide electronic payments network began in the late 1960s by a group of imaginative bankers who recognized the need for an electronic alternative to check processing. In 1974, the National Automated Clearing House Association (NACHA) was formed as the regulatory body for the ACH network. NACHA annually publishes "The ACH Rules: The Complete Guide to Rules & Regulations Governing the ACH Network". The user may find it helpful to obtain this book for specific questions on the mechanics of ACH processing.
The transaction which will be created through the auto-deposit feature in Spectrum will create a Prearranged Payment or Deposit (PPD) file. PPD is defined by NACHA to be an "automated consumer payment application allowing a consumer to authorize the debiting or crediting of his/her account by a company or financial institution in connection with a standing obligation." Five types of records will be created in building the PPD file: the File Header Record, the Company/Batch Header Record, the Entry Detail Records, the Company/Batch Control record, and the File Control Record. The records in PPD files will be in the following sequence:
Note: This topic is intended only to be an overview of the
 guidelines from NACHA; your bank will provide for specifications on handling, testing, and
 processing transactions and input in each individual field.

Related information

- [File Header Record (Record Type 1)](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/file-header-record-record-type-1)

- [Company / Batch Header Record (Record Type 5)](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/company--batch-header-record-record-type-5)

- [Entry Detail Records (Record Type 6)](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/entry-detail-records-record-type-6)

- [Company / Batch Control Record (Record Type 8)](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/company--batch-control-record-record-type-8)

- [File Control Record (Record Type 9)](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/file-control-record-record-type-9)

- [Field Inclusion Requirements](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/field-inclusion-requirements)
