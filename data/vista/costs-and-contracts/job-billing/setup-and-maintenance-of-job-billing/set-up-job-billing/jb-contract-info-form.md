---
title: "JB Contract Info Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form"
---

# JB Contract Info Form

Use this form (accessed from the JB Programs folder or the JB Contract Info tab on the JC Contracts form) to enter additional information for contracts set up in JC Contracts.
 You cannot enter new contracts using this form; however, information entered here will update JC Contracts.
Processing groups gather contracts together that are billed at the same time. In the Processing Group section, you can assign a processing group for a contract here or use the JB Processing Group form to assign contracts to a processing group. If you assign or delete a processing group here, it will automatically update JB Processing Group.
Use the AIA Info section to enter additional information (i.e., the architect's name and project number, contract description, and contract date) that prints in the heading of the JB AIA Continuation and JB AIA Summary Change Order Form reports. This data is informational only and is not used anywhere else in the system.

## Override Billing Information

You will typically only need to enter information here when you need to override the standard billing address for the customer. The address entered here will default when entering progress and/or T&M billings and will print on JB invoices for the contract (if not overridden during bill entry).Tip: Billings (Progress and T&M) default each address field separately; any field left blank here will be pulled from AR Customers. If you use the Add’l Address field to enter ‘Attention’ information (e.g. Attn: Mary), and you have multiple contracts pointing to a single customer, you can leave the override address information blank and enter only the ‘Attention’ information here. The system will pull the billing address from AR Customers, but will pull the Add’l Address for each contract from here.

## JB Delivery History

The JB Delivery History tab allows you to track the delivery history for Progress and T&M invoices associated with the contract. This display-only tab shows you the delivery ID, bill month, bill number, the date the invoice was sent (delivered), delivery method, delivery status (Delivered or Failed), and the recipient, as well as the recipient's email and/or address information (depending on the delivery method).
