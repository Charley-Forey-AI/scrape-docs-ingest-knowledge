---
title: "How can I disconnect subcontract change orders from change requests? | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/troubleshooting/frequently-asked-questions/how-can-i-disconnect-subcontract-change-orders-from-change-requests"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/troubleshooting/frequently-asked-questions/how-can-i-disconnect-subcontract-change-orders-from-change-requests"
---

# How can I disconnect subcontract change orders from change requests?

Problem: We want to increase our estimates and projections by one amount, but we want to issue a subcontract change order for a completely different amount. How can we make this happen in Spectrum?
Solution: Prior to version 10, there were two separate processes to modify a project's estimate and to create a subcontract change order. To eliminate duplicate entries, version 10 introduced the change request concept. Unfortunately, you could not create a subcontract change order for a different amount from the actual change request. Some people like to issue subcontract change orders for a lower amount, in essence creating a "slush fund" in their estimates. Here is a strategy to make this happen.

## Setup

1. Go to the Accounts Receivable Installation - Properties tab.

1. Select the Cost-reimbursable CR's post to Job Cost checkbox.

1. Clear the Non-cost reimbursable CR's post to Job Cost checkbox.

1. Select the Contractor pricing update projected costs checkbox and then click OK.

## New Procedure

1. Use the cost-reimbursable version of the change request to record the changes to estimates and revenue. Use contractor pricing to record these changes to estimates and projections.

1. Use a non-cost reimbursable change request to record the amount of the subcontract change order. Here, you will want to use subcontractor pricing.

1. Navigate to the SubcontractChange Order Log and finish setting up the subcontract change order. This will update open commitments, but will not affect estimates or projected costs.
