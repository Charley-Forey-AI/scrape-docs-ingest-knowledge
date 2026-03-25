---
title: "Accounts Payable Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/accounting/accounts-payable-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/accounting/accounts-payable-features"
---

# Accounts Payable Features

Vista 2021 R2 delivers on user-requested Accounts Payable enhancements, fixes, and other improvements.

Important:Vista Year-End Requirements Information for 2021 Tax YearYear-end regulatory reporting for US and Canadian Vista customers, including 1099 and T5018 forms printing and eFiling for the tax year 2021, will require Aatrix. Please review the following Knowledge articles and make sure you are prepared in advance:

- [Vista Year-End 2021 Full Transition to Aatrix Reporting](http://go.viewpoint.com/NjIzLU5EQS00ODcAAAF-bjsPmJruf_aUi80Sk7avugNAaZGjDO_Ei9n9XLBgLn_kC75xcMln2CndaO-3WMKKkB2zK18=)

- [What is Aatrix](http://go.viewpoint.com/NjIzLU5EQS00ODcAAAF-bjsPmNS_gJN2H7uvJgCB8MCyOtHHByPnLmthlJRREvAiRP1eW3SlKFSPhgl_mDk6qVk3onw=)

Click [here](https://partner.aatrix.com/vista) for information about enrolling with Aatrix.

## Allow Syncing Vendors to ProjectSight

If you are using the ProjectSight web application, you can now sync vendors to ProjectSight.
To enable this functionality, the AP Vendors form now includes a new Sync to ProjectSight checkbox (on the Addl Info) tab. When you select this checkbox, the system sends the selected vendor to the ProjectSight web application, setting it up as a Company.

## Improved Payment Processing in AP

Several changes were made to improve the workflow for issuing, voiding, and/or reversing AP payments. These changes are as follows:In AP Payment Posting:

- The CM Seq# field now defaults to zero and is disabled for all payment types.

- The Pay Method field is now enabled for all payment types, as long as no CM Ref# is assigned. This means you can now change the payment method for a transaction without having to delete the payment sequence from the batch, add it to a payment workfile, and then re-add it to a payment batch.

- The CM Acct field is now only enabled when the Pay Method is C-Check and the Check Type is M-Manual.

- Validation for the Pay Method field now includes the following checks:

- If the Pay Method is S-Credit Service and the payment service is set to 1-Comdata in AP Company Parameters, the system checks to make sure a Payment Service Email is defined for the vendor (in AP Vendors).

- If the Pay Method is E-EFT or N-Viewpoint ePayments, the system checks to make sure there is Routing information set up for the vendor in AP Vendors.

In AP Prior Mth Payment Reversal:

- If you do not select the Create Open Transactions in Batch Month checkbox, clicking the Update button now displays a message indicating the reversal batch will be created without open transactions and asking if you want to continue. Select Yes to proceed; No to cancel.

- The F4 lookup in the CM Ref field now displays all payments applicable for reversal in Open and Closed months. In addition, the lookup now includes the EFTSeq, Amount, and Paid Date. For Checks and Credit Service payments, the list shows one row per CM Ref#/CM Ref Seq# for the CM Co#/CM Account/Paid Mth and for EFTs and ePayments, one row per CM Ref#/EFT Seq# for the CM Co#/CM Account/Paid Mth.

## Merge Duplicate Vendors for a Single Vendor

You can now merge duplicate vendors for a single vendor using AP Vendor Merge. This method is most useful if you already have some idea of which vendors are duplicates.
To enable this functionality, a new Limit To Vendor field was added to the AP Vendor Merge form. When you enter a vendor in this field, the duplicate identification process compares all vendors to the single vendor based on your selected Confidence Level and Identify By options, and then populates the grid with potential duplicate vendors. You can then review the list, flag the actual and duplicate vendors as needed, and process.
For more information about duplicate vendor merge, see [AP Vendor Merge Form](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendor-merge-form).

## Using a Vendor SSN instead of EIN in AP Vendors

You can now choose to use a vendor's Social Security Number or Employer Identification Number in the Tax ID # field of AP Vendors, Add'l Info tab.
To enable identifying the Tax ID value, a new EIN/SSN drop-down was added to the AP Vendors form. Just select either EIN or SSN to indicate what the Tax ID value represents.Note: When you enter the vendor's Tax ID, make sure you omit dashes and spaces.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
