---
title: "Material Purchase Tracking | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/in-depth-overview/material-purchase-tracking"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/in-depth-overview/material-purchase-tracking"
---

# Material Purchase Tracking

The Outside Material Purchases Reconciliation process accounts for variances between the original job cost transaction and the actual Accounts Payable invoice when the A/P invoice is updated. This is similar to the Freight Reconciliation process to track freight variances. As the invoice is updated using the Outside Material Purchase Update, the difference between the estimated and actual material cost is now allocated in General Ledger and Job Cost History.
The scale tickets are imported on a daily basis. The Scale Ticket Update is also done on a daily basis to get the information to job cost. Since the actual material costs may not be known at this time, it is posted to an outside material purchase reconciliation holding file. When the invoice comes in from the vendor, the tickets are reconciled and an A/P invoice is automatically created to pay the vendor. This process potentially creates a variance between the estimate charged to Job Cost and the actual amount of the invoice.
To account for this, a variance is posted to the job when the A/P Invoice is processed. This will result in estimated outside material purchases going to the job on a daily basis, and on a more periodic basis the actual material purchases will be reflected in job cost.
When the invoice comes in from the vendor, the tickets are grouped together and an A/P invoice is created. This A/P invoice contains adjustments for the outside materials purchase variance. These are posted to Job Cost during the A/P invoice update. This results in the actual outside materials cost being posted to Job Cost after the A/P invoices have been created and update (not necessarily paid).
