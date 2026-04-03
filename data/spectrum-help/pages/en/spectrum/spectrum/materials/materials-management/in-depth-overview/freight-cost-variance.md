---
title: "Freight Cost Variance | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/in-depth-overview/freight-cost-variance"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/in-depth-overview/freight-cost-variance"
---

# Freight Cost Variance

The A/P invoice created for freight is for the actual freight charge that is paid to the vendor. There may be a variance between this and what has posted to Job Cost or Order Processing in the scale ticket update. Instead of creating one invoice line for the actual freight charge, the software creates at least two invoice lines:

- One line for estimated freight

- Another line, or as many as needed, to distribute actual variance to Job Cost or Order Processing
The first line will debit the freight liability account that was originally credited during the Scale Ticket Update. This is debited for the estimated freight charge.
The second line is created as a direct cost A/P invoice detail line. This is to credit the job/phase/cost type associated with the ticket.
When the A/P invoice is posted, the end result is a wash in the freight liability (net $0.00) and the freight variance posting to job cost, which results in the actual freight charge being applied to the job. For Order Processing customer invoices, the variance is applied to the "Cost of Goods Sold" G/L freight account charged on the original invoice.

For example, assume that the total estimated freight for a group of tickets is $60. The actual freight charge turns out to be $80. the software creates an A/P invoice line for $60 and another line for $20. The $60 balances against the $60 posted in the ticket update. The $20 A/P invoice line is created for a direct cost account, posted to the same job/phase/cost type as the original estimated freight.
