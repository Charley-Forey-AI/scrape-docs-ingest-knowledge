---
title: "Service Request Alerts | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/in-depth-overview/service-request-alerts"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/in-depth-overview/service-request-alerts"
---

# Service Request Alerts

The heading section of the [Service Request - W.O. History](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/service-request/service-request---w.o.-history) window displays a series of alerts. The following explains what triggers the alerts to display. Each of these alerts has a hyperlink that will provide you with more information.

## Credit Limit Alert

The system calculates the customer's credit limit minus their outstanding receivables. Leaving the credit limit field blank or at zero indicates that there are no credit limits for this customer. To reflect a pre-paid only status, enter $1 be entered as the credit limit in the customer file.
The alert message will change to explain how close the customer is to reaching the credit limit.

- Over Credit Limit: Exceeded by <outstanding balance less credit limit>

- Near Credit Limit: Available balance <outstanding balance less credit limit> (Near Credit Limit is defined when the outstanding balance is 90% or more of the credit limit.)

- At Credit Limit: Available balance $0

- Under Credit Limit: Available balance <outstanding balance less credit limit>

Clicking the hyperlink displays the Credit Check tab.

## Collections Monitor Alert

This alert will display when the customer has a positive overdue Accounts Receivable balance. Retention is not considered a past due receivable.
Clicking the hyperlink displays the Credit Check tab.

## Site Alert

This alert will display when Alert notes are entered in Site File Maintenance > Notes.
Clicking the hyperlink displays the View Site window.

## Service Contract Alert

Appears when there is a service contract for the selected site.

- Service Contract: Active MM/DD/YY to MM/DD/YY (Only one active contract available.)

- Service Contract: Multiple active contracts (Two or more active contracts.)

- Service Contract: Next service contract begins on MM/DD/YY (Only one contract and it starts in the future.)

- Service Contract: Last service contract expired on MM/DD/YY (Only one contract and it has expired within the last 365 days. Contracts with expiration dates greater than one year do not trigger this alert.)

Clicking the hyperlink displays the Service Contracts tab.

## Purchase Order Alert

The fifth alert will only appear when there are one or more outstanding purchase orders with quantity due for work orders for the selected site. This alert will not appear when there are no open purchase orders for this site.

- Purchase Order: Waiting for P.O. items-on-order

Clicking the hyperlink displays the Purchase Order tab.

## Customer Status Alert

This alert appears when text has been entered in the WO
 Warning button on Customer File Maintenance > Other.
Clicking the hyperlink displays the View Customer window.

## Site Status Alert

This alert only appears when the site is set to a status of
 Inactive or Not Used.
Clicking the hyperlink displays the View Site window.

## Customer Status

This alert only appears when the customer is set to a status of
 Inactive or Not Used.
Clicking the hyperlink displays the View Customer window.
