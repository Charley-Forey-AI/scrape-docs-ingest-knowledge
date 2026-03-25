---
title: "Accounts Payable Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/accounting/accounts-payable-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/accounting/accounts-payable-features"
---

# Accounts Payable Features

Vista 2021 R1 delivers on user-requested Accounts Payable enhancements, fixes, and other improvements.

## Updated Viewpoint ePayments to New Nvoicepay API

Viewpoint ePayments now uses the new Nvoicepay Customer API system for ePayments and ePayments response files.
As a result of this change, you must do the following once you install this release, before you generate and process ePayments.

1. Contact Nvoicepay's [Help Center](https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fnvoicepay.zendesk.com%2Fhc%2Fen-us&data=04%7C01%7Cangela.anastasakis%40nvoicepay.com%7C00987c0d5f344acc5c9108d914e7f8ec%7C8ad0e60b834b4e40bdbd2b43fea3fa1f%7C0%7C0%7C637563808852167172%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=CJJPKsrPavRrWByd%2FMG41IUhDhR9xH2D%2BMfdYP83Yy4%3D&reserved=0) or [Tech Support](https://www.nvoicepay.com/about/contact-us/) for your new configuration settings.

1. In AP Company Setup (Payment Services tab), update the following fields with the new values provided by Nvoicepay.

1. Company ID

1. Client ID

1. Client Secret

1. In VA Site Settings (Viewpoint ePayments Settings section), enter the values provided by Nvoicepay in the following fields (these are new fields added for this release):

1. Customer API URL - This is the URL for invoice attachment file uploads, payment batch uploads, and return file processing.

1. Identity URL - This is the URL for the Viewpoint ePayments identity API.

Other changes made for this update include the following:

- In AP Company Parameters, removed the API Key and Password fields from the Payment Services tab, as these fields are no longer being used.

- In VA Site Settings, removed the Viewpoint ePayments URL field, as it is no longer being used. In place of this field, added the Customer API URL and Identity URL fields (indicated above).

- In the AP Viewpoint ePayments Export form, a new Upload button replaces the Download button. When you click this button, the system automatically uploads your file to Nvoicepay and displays a confirmation message. When you click Close, you are prompted to save the file. Once you save the file, you can then process the batch.Additionally, changed the file name that defaults in the Download Filename field from " Viewpoint ePayments" to "Viewpoint ePayments CoX, where "X" is the current AP company.

- Modified the download process to use the Secure File Path defined in AP Company Parameters. If the Use Secure File Path checkbox is selected and you have specified a location in the Secure File Path field, the system automatically saves the file to the specified secure location. If you did not select the Use Secure File Path checkbox, the system allows you to save the file to any selected location.

## Added Ability to Associate Invoice Lines with Job Cost Field Tickets

 You can now assign Job Cost field tickets to AP invoice and unapproved invoice lines, enabling you to link related costs to specific work activity on a job, and facilitate owner billing.
To enable this functionality, added a Ticket field to the AP Transaction Entry and AP Unapproved Invoice Entry forms. This field displays only for invoice lines with a Type of 1-Job or 6-PO.
 For job lines, you can associate the invoice line to an open field ticket for the specified job/contract. For PO lines (initialized or manually added), this field is display only and only populates if you assigned a field ticket to the PO item (in PO Purchase Order Entry).
Once you post invoices via AP Transaction Entry or AP Unapprove Invoice Posting (unapproved invoices), the system updates the Cost Detail tab in JC Field Ticket with the transaction information, including the actual and posted dates, and showing a Source of AP Entry.
 For more information about the Field Tickets feature, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Prior Month Payment Reversals for Viewpoint ePayments / EFTs

You can now perform prior month payment reversals for Viewpoint ePayments and EFT payments. To enable this functionality, the following changes were made to the AP Prior Mth Payment Reversal form:

- Added N-Viewpoint ePayments and E-EFT options to the Payment Method drop-down.

-  Added a Reverse all Seqs checkbox to allow reversing all payment sequences on an EFT or Viewpoint ePayment transmission. This checkbox is enabled only for payment methods N-Viewpoint ePayments and E-EFT.

- Added an EFT Seq # field for entering a specific payment sequence to reverse. This field is enabled only for payment methods N-Viewpoint ePayments and E-EFT, and only if you did not select the Reverse all Seqs checkboxNote: It is important to note that if you reverse a Viewpoint ePayments payment, you must also cancel the payment on the Nvoicepay website.

## Include Attachments on Open Invoices Created for Voided Payments or Payment Reversals

When you reverse payments that include attachments (in AP Prior Mth Payment Reversal, respectively), if you select to have the system create new open invoice transactions, the system now includes those attachments on the newly created open transactions.

## Duplicate Vendor Merge

You can now merge duplicate vendor accounts and designate a single vendor to use for invoicing, payments, and consolidated reporting. This vendor is designated as the Actual (parent) vendor, while the other linked vendors are designated as duplicate vendors. Duplicate vendors are inactivated and are not eligible for invoicing or posting to other transactions (such as purchase orders); however, you can still access their historical data.
The changes made for this functionality include:

- AP Vendor Merge - This new form uses a set of criteria to identify potential duplicate vendors and groups them together by their similar data (that is, the vendor name, purchasing address, payment address, and/or phone email). You can then select the vendor to designate as the actual (or parent) vendor and specify which vendors are duplicates.Note: You can only designate one vendor as the parent vendor in a merge session. Therefore, if you have multiple parent vendors, you will need to run a separate session for each parent vendor and its duplicates.

 Once you process a session, the system sets the duplicate vendors to inactive so they are not available for transaction posting (invoices, purchase orders, etc.). In addition, they are added to the Duplicate Vendors tab for the parent vendor in AP Vendor Master.
 For more information, see [AP Vendor Merge Form](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendor-merge-form).

- AP Vendor Master - Added a new Duplicate Vendors tab to display vendors designated as duplicates of the Actual (parent) vendor. The system adds vendors to this tab automatically once you process a session in AP Vendor Merge; however, you can also add vendors to this tab manually.
Once a vendor is designated as a duplicate, the system marks the vendor inactive. When you access the vendor's record in AP Vendor Master, a message displays (in red) above the grid indicating the vendor is disabled and a duplicate of the specified Actual vendor. In addition, you can no longer post invoices or other transactions to that vendor. However, you can still access the vendor's historical data.
For more information, see [AP Vendors Form](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form).

- AP Vendor Drillldown / AP Vendor Payment History Drilldown - These reports were modified to group duplicate vendors with their Actual vendor.
 For more information, see the [Vista Reports](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/system-tools/vista-reports) release notes.

Note: You cannot designate a vendor as a duplicate if that vendor has any open invoices. You must first close all open invoices for that vendor before you can link it to a parent vendor.
Click below to see a brief video about merging duplicate vendors!

## Reset Beginning Check Number by CM Account

You can now override the beginning check number used when printing checks by CM Account.
A new Beginning Check # field was added to the CM Accounts form to allow resetting the beginning check number default for printed checks. The value entered in this field applies to both Accounts Payable and Payroll checks using the same CM account.
When printing checks in AP Check Print, the Beginning Check # field defaults the beginning check number value specified for the CM account. Once you complete the check run, the system updates the Beginning Check # field in CM Accounts based on the last check number used plus one.
If the Beginning Check # field in CM Accounts is blank, the system uses standard defaulting; that is, it defaults the beginning check number based on the highest check number in the system.
In addition to this change, the Ending Check # field in AP Check Print now defaults based on the number of checks being printed for the specified CM Account/batch. For example, if the beginning check number is 100 and you are printing 10 checks, the ending check number defaults to 110.
 For additional information, see the [Cash Management](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/accounting/cash-management-features) release notes.

## Using a Vendor SSN instead of EIN in AP Vendors

You can now choose to use a vendor's Social Security Number or Employer Identification Number in the Tax ID # field of AP Vendors, Add'l Info tab.
To enable identifying the Tax ID value, a new EIN/SSN drop-down was added to the AP Vendors form. Just select either EIN or SSN to indicate what the Tax ID value represents.Note: When you enter the vendor's Tax ID, make sure you omit dashes and spaces.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
