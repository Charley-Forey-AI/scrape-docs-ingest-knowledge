---
title: "Modify the Remaining Amount to Bill for an Agreement Service | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-modifying-agreements--services/modify-the-remaining-amount-to-bill-for-an-agreement-service"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-modifying-agreements--services/modify-the-remaining-amount-to-bill-for-an-agreement-service"
---

# Modify the Remaining Amount to Bill for an
 Agreement Service

Whether you are adding, amending, or renewing an agreement, you can modify the amount remaining to bill for periodic agreement services without affecting the total price of the service.
For example, say you are amending an agreement and adding a new periodic service for $4,000. However, you are already 6 months into the term, so you want to only bill for the remaining portion of the term. In this case, you can reduce the billing amount by $2,000 for the remainder of the term, without affecting the agreement service price. When you renew the agreement, the system updates the new billing schedule to reflect the total amount of the service (in our example, $4.000).
If you are using the revenue amortization feature (that is, the agreement's Revenue Recognition drop-down is set to S-Amortize), the system adjusts the Total Remaining amount for the agreement service's deferral schedule based on the modified total remaining to bill. For example, if you increased the agreement price by $1500, but decreased the amount remaining to bill by $500 (leaving a new total remaining to bill of $1000), the new Total Remaining for the deferral schedule will also be $1000. You must update the existing deferral entries until the Total Remaining is 0.00.

1. Open the SM Agreements form.

1. In the Agreement field, select the agreement, amendment, or renewal quote to work with.

1. Click on the Work Schedule tab and double-click in the grid to open the SM Service form.

1. In the Service Seq field, select the periodic service to update.

1. In the Billing Reduction field (below the service Price), enter the amount by which to reduce the remaining amount to bill.

1. Click on the Billing Schedule tab. The Total Remaining field (above the grid) displays the amount remaining to bill for the agreement service, less the billing reduction amount. If the billing reduction created a negative Total Remaining balance, adjust the existing billing sequences until the Total Remaining is 0.00. If the Total Remaining is greater than 0.00, adjust existing entries or add new entries until the Total Remaining is 0.00.

1. Save the record.

Related information

- [SM Service Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form)

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)
