---
title: "Prepare and Process 1099s | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/prepare-and-process-1099s"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/prepare-and-process-1099s"
---

# Prepare and Process 1099s

Instructions for preparing and processing 1099s.
Before you can process 1099s, you must have done the following:

- Set up valid 1099 types (in the AP 1099 Types form).

- [Set applicable vendors as subject to 1099 reporting](/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-reporting/set-vendors-subject-to-1099-reporting-united-states) in AP Vendors

- Made sure the appropriate 1099 information is applied to each invoice in AP Transaction Entry (Payment Overrides tab).

You can use use Aatrix to print and/or eFile 1099s. If you do not already have Aatrix installed, do the following:

- Download and install the application to your local workstation. For instructions, see [Enabling Aatrix on a workstation](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aatrix-reporting/enable-aatrix-on-a-workstation).

- [Enroll with Aatrix](https://partner.aatrix.com/vista). This is required in order to submit your electronic files.

- Enter your [DUNS #](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form/field-definitions-hq-company-setup-form#ID-0000ebcc--en) in the HQ Company Setup form.

Accounts Payable provides options to accumulate data for e-filing and printing 1099s. Although there are multiple types of 1099 forms, Vista only provides the ability to print or generate e-files for Form 1099-NEC. You can, however, use Aatrix to e-file or print the 1099 Miscellaneous Income, Dividend & Distributions, NEC, and Interest Income forms.
Complete the following steps for vendor payments that are to be reported on 1099 forms:

1. At calendar year-end, print the AP 1099 Report (summarized or detailed) to obtain a list of each vendor's YTD 1099 amount, and verify the following:

1. The YTD 1099 amounts are accurate (if you printed the summarized version of this report, you may find it necessary to print this report in detail to see if specific transactions are included/excluded).

1. The vendor's address is present and correct.

1. The vendor's Tax ID#, 1099 Type, and 1099 Box are present and correct. Remember, if you are accumulating amounts for filing purposes, Vista only includes totals accumulated under 1099 type NEC. However, Aatrix includes totals accumulated under 1099 types MISC, INT, NEC, or DIV.

Note: This report only shows vendors with 1099 amounts equal to or greater than the specified Minimum Payment Amount, or vendors with 1099 amounts less than the minimum amount where the Include in 1099 Processing (Ignore Minimum) checkbox is selected in the AP Vendors form. (The 'minimum amount' restriction does not apply to dividend amounts because dividends do not have a minimum amount and are always included in this report.) You can review all vendors with totals less than the minimum amount, regardless of the Include in 1099 Processing (Ignore Minimum) setting, using the "AP 1099 Vendors Less Than Minimum" report.

1. If necessary, for any paid or partially paid transaction, change the 1099 box in the AP 1099 Edit Transactions form so the amount is either included or excluded from the vendor's YTD 1099 amount.Note: It is possible to change a vendor's 1099 YTD amount in the AP 1099 Processing form. However, changing the amount there means you will not have an accurate audit trail to support the YTD 1099 amount.

1. If you need to report in more than one box on the 1099, make those entries in the AP 1099 Processing form. For example, California requires withholding to be reported in Box 16.

1. If needed, add or update vendor information (such as payment address information or Tax ID#) in the AP Vendors form.

1. If you made changes to 1099 amounts, box numbers, or other values, then you may want to run the AP 1099 Report again to double-check information and have a final copy of the vendor information that will print on the 1099 forms.

1. For each Vendor and 1099 Type combination in the reporting year, review the 1099 Email Consent setting in AP 1099 Processing and update if necessary. For more information about this field, see the [F1](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-1099-processing-form/field-definitions-ap-1099-processing-form#concept-19230--en) help.

1. When you are ready to generate the e-file, select Tasks > Download.The AP 1099 Download form displays.

1. Enter the required information as applicable. Refer to the F1 help for each field for more information.

1. Depending on how you are submitting 1099s, do one of the following:

- If using Aatrix to e-file or print 1099s, select Launch Aatrix, and then follow the prompts in the Aatrix wizard to complete processing.

- If using Vista to generate an e-file (1099-NEC only), select Download, and then save the e-file(s) locally for submission to the IRS. If you want to print 1099-NECs, you can do so using the AP 1099 NEC Recipient Copies report (available in the AP Reports menu or from the AP 1099 Processing form by selecting Options > Reports > AP 1099 NEC Recipient Copies.

Note: Aatrix does not send data back to Vista . If you need to make corrections after you submit your 1099s to the taxing authority, you must do so directly in Aatrix. For more information, see [Make Corrections to Regulatory Filings via Aatrix](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/make-corrections-to-regulatory-filings-via-aatrix).If you used Vista to generate and save your 1099-NECs, and have already submitted them to the IRS, corrections must be made via Aatrix; you cannot use Vista. For more information, see [Correct 1099-NECs Generated in Vista](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/correct-1099-necs-generated-in-vista).

 Once you have completed printing and eFiling 1099s and you no longer need the year's 1099 amounts, use the Annual 1099 Totals option in the AP Purge form to purge these YTD totals.

Related information

- [DUNS Number](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form/field-definitions-hq-company-setup-form#ID-0000ebcc--en)
