---
title: "Labor Billing Rate Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-hierarchies/labor-billing-rate-hierarchy"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-hierarchies/labor-billing-rate-hierarchy"
---

# Labor Billing Rate Hierarchy

When multiple rates exist, Spectrum uses the following
 hierarchy to determine the appropriate billing rates.

1. First it looks to see if this billing code has rates set up by Service Contract. If so, it uses that rate.

1.  If none are found, it then looks to see if the billing code has been set up by Site. If so, it uses that rate.

1. Next, it looks to see if this billing code has special Customer rates defined. If it finds one, it uses that rate.

1.  If no rates are found, then Spectrum uses the standard labor billing rates.

1.  Next, it must determine the level number:

- If a contract does not exist on the transaction, Spectrum looks to Customer
 File Maintenance to find the labor billing number.

- If the transaction has a service contract code entered onto it, it looks to
 Service Contract Maintenance to find the labor billing number.

1. The combination of the billing code and level determine the appropriate billing rate.
