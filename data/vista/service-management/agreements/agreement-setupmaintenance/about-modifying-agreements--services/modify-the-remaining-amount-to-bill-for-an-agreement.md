---
title: "Modify the Remaining Amount to Bill for an Agreement | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-modifying-agreements--services/modify-the-remaining-amount-to-bill-for-an-agreement"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-modifying-agreements--services/modify-the-remaining-amount-to-bill-for-an-agreement"
---

# Modify the Remaining Amount to Bill for an
 Agreement

Whether you are adding, amending, or renewing an agreement, you can modify the amount remaining to bill without affecting the total price of the agreement, amendment, or renewal.
A typical use for this might be when you are adding new services to an agreement amendment that will increase the agreement's price, but will only be performed for the remaining portion of the term. In this case, you will generally only bill for the portion of the service that you actually perform. For new agreements, you might use this feature to discount the agreement price for the first term of an agreement.
If you are using the revenue amortization feature
 (that is, the agreement's Revenue Recognition drop-down is set to S-Amortize), the system adjusts the Total Remaining amount for the agreement
 amortization schedule based on the modified total remaining to bill. For example, if
 you increased the agreement price by $1500, but decreased the amount remaining to
 bill by $500 (leaving a new total remaining to bill of $1000), the new Total
 Remaining for the amortization schedule will also be $1000. You will need to update
 the existing amortization entries until the Total Remaining is 0.00.

1. Open the SM Agreements form.

1. In the Agreement field, select the agreement, amendment, or renewal
 quote to work with.

1. In the Billing
 Reduction field (below the Agreement Price), enter the amount by
 which to reduce the remaining amount to bill.

1. Click on the Billing
 Schedule tab.The Total Remaining field (above
 the grid) displays the amount remaining to bill for the agreement, less the
 billing reduction amount. If the billing reduction created a negative Total
 Remaining balance, you must adjust the existing billing sequences until
 the Total Remaining is 0.00. If the Total Remaining is greater than 0.00, you
 must either adjust existing entries or add new entries until the Total
 Remaining is 0.00.

1. Save the record.

Related information

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)
