---
title: "A/P Payment Selection | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/ap-payment-selection"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/ap-payment-selection"
---

# A/P Payment Selection

The A/P Payment Selection screen is accessed from the [A/P Payment Processing](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing) screen and is used to begin the check cycle and allows you to build a list of outstanding invoices and then select which ones you want to pay.

- You may wish to select invoices for payment based solely on job number. When this is the case, it is recommended that only one job be charged in the expense distribution portion of A/P Vendor Invoice Entry. Because payment selection is done on the header of the invoice, not the distribution, there is only one field for a job. It uses the job from the first line when the invoice is updated into the open item file. Most users do not mix jobs on the invoices, or if they do (such as for gas cards or delivery services) they do not attempt to pay these invoices partially based on each job.

- Payment Selection performs the [Document Tracking Item Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance) as part of the invoice selection process, thereby disallowing invoices to be selected for payment if any open items exist for the invoice or an associated subcontract. If open items exist, the Status column will display as 'Pymt disallowed' for these rows.

- If sub-tier vendor tracking is being used, this screen will disallow selection of subcontract invoices whenever any of pertinent sub-tier vendors are flagged to prevent payment (triggered by Document Tracking action #4). Payment is disallowed if even one sub-tier vendor triggers this action.

- If two (or more) separate checks should be issued to a single vendor, all appropriate items should first be selected using this screen. To indicate multiple checks on a single check run, use [Alternate Payee Entry](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/alternate-payee-entry).

- In the unusual case where the 'Comdata payable' setting is changed in the Vendor Payment Setup page while payment processing is in progress, items already selected in this page will still be paid based on the setting when they were added.

Related information

- [Removing a Hold from an Invoice or Vendor](/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/invoice-and-credit-memo-procedures/removing-a-hold-from-an-invoice-or-vendor)

- [New Processing Group](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/ap-payment-selection/new-processing-group)
