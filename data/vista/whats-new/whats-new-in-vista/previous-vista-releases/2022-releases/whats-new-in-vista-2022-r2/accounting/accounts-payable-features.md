---
title: "Accounts Payable Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r2/accounting/accounts-payable-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r2/accounting/accounts-payable-features"
---

# Accounts Payable Features

Vista 2022 R2 delivers on user-requested Accounts Payable enhancements, fixes, and other improvements.

## Easier Workflow for Selecting and Paying Released Retainage

You can now easily identify and select released/open retainage for payment when creating a payment workfile in AP Payment Workfile.
The AP Payment Workfile form now includes a new Open Retainage only checkbox in the Selection Criteria. When you select this option, payments added to the grid will include only those transactions with open, released retainage that meet any other selection criteria you entered. If a transaction includes both retainage and non-retainage lines, only the retainage lines will show, as long as they have been released.
Once transactions are added to the workfile, you can modify the list as needed (that is, add or remove transactions, if applicable) and then create the payment batch.
Note: You can only use the Open Retainage only option for retainage that was released using the AP Release Retainage form.

 For more information about adding open released retainage to a workfile, see [Create a Released Retainage Payment Workfile](/en/vista/vista/accounting/accounts-payable/payments/retainage/create-a-released-retainage-payment-workfile).

## Electronic Delivery Consent for Vendor 1099s (US only)

In support of the IRS allowed consent for electronic delivery of year-end filing information, you can designate whether a vendor has consented to receive 1099s via email. Aatrix supports both direct mail and email of 1099s, allowing you to save on mailing costs by having 1099s sent via email to those who have consented.
To implement this feature, the following changes were made:
In AP Vendors:Added a new 1099 Email Consent checkbox to the Add'l Info tab, 1099 Info section. This checkbox is only enabled if you have selected the Subject to 1099 reporting checkbox for the vendor.Selecting the 1099 Email Consent checkbox indicates the vendor has consented to receive 1099s via email, and requires that an email address be specified for the vendor. If this checkbox is left unselected, the vendor will receive printed 1099s.
The setting designated here defaults when processing 1099s via AP 1099 Processing, but may be overridden.
In AP 1099 Processing:Added a new 1099 Email Consent checkbox to the Info tab. This checkbox is always enabled and defaults based on how you set the corresponding checkbox in AP Vendors. You can override the setting for the vendor and reporting year by 1099 Type. However, if you change the checkbox to selected for a reporting year/vendor/1099 Type, the vendor must have an email address specified in AP Vendors.When you launch Aatrix (via the AP 1099 Processing form), the setting defined here is sent to Aatrix and determines how Aatrix will handle delivery of 1099s for the vendor.

## Access to Automatic Invoicing from Vista

If you are a Trimble Construction One user with SSO enabled, you can now access Automatic Invoicing from within Vista.
To enable access to Automatic Invoicing:

- A new AP Automatic Invoice Entry link was added to the Programs menu of the Accounts Payable module.

- A new Automatic Invoice Entry button was added to the [AP Unapproved Invoice Entry](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form#ID-000071df--en__APUnapprInvEntry_AutoInvoicing) form (just below the form's toolbar).

Once you click either of these links, if you are already logged into Trimble Construction One (with your Trimble ID login/password), you are taken to the Automatic Invoicing screen. If you are not logged onto Trimble Construction One, you are presented with the Trimble Construction One login screen. Once you login, you can then access Automatic Invoicing.
Note: If you do not have Trimble Construction One with SSO enabled, clicking either of the links indicated above will launch a Trimble Viewpoint Automatic Invoicing product page.

For more information about Automatic Invoicing, see [Automatic Invoicing (for Trimble Construction One Users)](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/automatic-invoicing-for-trimble-construction-one-users).

## Approval/Rejection Time for AP Unapproved Invoices

When you approve or reject an unapproved invoice in AP Unapproved Invoice Review, the system now includes the time in the DateApproved and RejectDate columns in the AP Unapproved Reviewers (APUR) table. These columns are not currently visible in AP Unapproved Invoice Review.
Note: In a future release, these fields will also be populated when approving/rejecting unapproved invoices in Viewpoint Financial Controls.

## Financial Controls Access from AP Unapproved Invoice Review

The AP Unapproved Invoice Review form now provides quick access to AP Invoice Review in Financial Controls.
A Review Invoices on the Web link was added to the AP Unapproved Invoice Review form header. If you have Financial Controls and have integrated your Vista Web account (that is, you have designated the appropriate Vista Web URL in VA Site Settings), clicking this link takes you to AP Invoice Review in Financial Controls.
If you do not have Financial Controls, clicking the Review Invoices on the Web link takes you the [Trimble Viewpoint website](https://www.viewpoint.com/products/vista/vista-web) for information about AP Invoice Review.

## Add Filtering by CM Reference for Void Payments

You can now filter payments for voiding by CM Reference number, making it easier find the payment transactions you want to void.
To enable this functionality, a CM Reference field was added to the Filter Payments section in AP Void Payments. If filtering by CM Reference number, only payment transactions with the specified CM reference number will be added to the Eligible to Void grid.
In addition, the Record CM Reference as Void - number cannot be reused field was replaced by a new Action field containing Void and Clear options. These options work in the same manner as selecting or deselecting the Record CM Reference as Void - number cannot be reused field; however, the new option allows you to specify how to treat CM reference numbers individually for each transaction you select to void.
Once you have populated the Eligible to Void grid with applicable payment transactions, you can select the payment transactions to void, indicate whether to Void or Clear CM reference numbers, and then click Update Batch. The transactions are added to the Payment Batch grid and flagged based on the option you selected.
For example, you can select one group of payments, flag them as Void, and add them to the batch, and then select another group of payments, flag them as Clear, and add them to the batch. When you process the batch, the system clears the CM reference numbers from CM and AP Payment History for the transactions flagged as Clear so they can be reused, and then marks the CM reference numbers for the remaining transactions as Void in CM and AP Payment History so that the numbers cannot be reused.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
