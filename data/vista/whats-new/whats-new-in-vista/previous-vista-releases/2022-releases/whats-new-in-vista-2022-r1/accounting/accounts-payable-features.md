---
title: "Accounts Payable Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r1/accounting/accounts-payable-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r1/accounting/accounts-payable-features"
---

# Accounts Payable Features

Vista 2022 R1 delivers on user-requested Accounts Payable enhancements, fixes, and other improvements.

## ePayment Retry Option

You can now select Retry to initiate another attempt if a timeout occur occurs when attempting to upload transactions and/or attachments to Viewpoint ePayments.

## Improved AP Vendor Merge

Several changes were made to the AP Vendor Merge feature to improve functionality. These changes are as follows: Saved Search CriteriaThe system now saves the Confidence Level and Search By settings in AP Vendor Merge. When you open the AP Vendor Merge form, the settings default from your last session. You can change the defaulted settings as needed; the system saves the changes each time and default them the next time you open the AP Vendor Merge form.
Clear GridYou now have the option to clear the Duplicate Vendors grid in AP Vendor Merge. A Clear Grid button was added below the Identify Duplicates button. When clicked, the system displays a message asking if you are sure you would like to clear all vendors from the grid and start again. If you click Yes, the system clears the grid of all vendors so that you can start with a new search.Search Completed NotificationWhen the system finishes searching for potential duplicate vendors, you will now receive a message indicating the search is complete and how many potential duplicates were found.

## Improved Void Payment Process

When voiding payments in AP Void Payments, you now have the ability to select multiple payments at a time and add them to a void payment batch.
The AP Void Payments form is now in grid format, with an upper grid titled Eligible To Void and a lower grid titled Payment Batch.
 The Eligible To Void grid is populated based on criteria entered in the Filter Payments section above the grid. You can enter any combination of criteria (Payment Method, CM Account, and/or Batch #) or leave all options blank to include all eligible payments, depending on your specific needs. Clicking the Fill Grid button populates the grid with all payments meeting the criteria that are eligible to void (that is, have already been posted to a month that is still open). You can then select individual payments in the grid to void or select all payments by clicking the Check All button.
Once you select the payments you want voided, use the Batch Control section to enter a void memo and specify whether to void CM reference numbers so they cannot be reused. If you select the Record CM Reference as Void - number cannot be reused checkbox, the system sets the CM reference for each selected payment to void in the AP payment files and in CM so the numbers cannot be reused. If you leave the checkbox unselected, the CM reference numbers are removed from the payment transactions and will be available for reuse later.
When you are ready to add the payments to a void payments batch, click the Update Batch button. All selected payments are cleared from the Eligible To Void grid and added to the Payment Batch grid. You can then review the payments and if needed, remove any payments that should not be voided.
When you are ready to post the batch, click the Post Batch button and process the void payments batch via the AP Batch Process form.
For more information about this new functionality, see the [Void Payments in an Open Month](/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/void-payments-in-an-open-month) and [AP Void Payments Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-void-payments-form) topics.

## Updated Default Behavior for Vendor 1099 Settings

When you enter a new vendor in AP Vendors, the system no longer defaults values in the 1099 Type and Box # fields. If the vendor is subject to 1099 Reporting, you must now manually enter those values.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
