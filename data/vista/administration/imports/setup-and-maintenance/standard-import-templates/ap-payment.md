---
title: "AP Payment | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/ap-payment"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/ap-payment"
---

# AP Payment

It is strongly recommended that you set up a separate CM Account when using this template to import payment history information.
This helps avoid running into check validation problems (e.g., the same check number was used in both the third-party application and in Vista™).
When using this import template, the system pulls
 information into an AP payment batch. If you pull imported transactions into AP Payment
 Posting prior to posting the batch, the system will default the Check Type
 field to I-Import, and you will be unable to make any changes to the transaction, as it
 is a previously paid transaction. You can add additional transactions from the system
 into the batch and process them alongside the imported transactions, however.
Note: When importing amounts that are less than the open-to-pay amount of the invoice, the system will display an error message. The import process will not split payments.
