---
title: "Material Rate Hierarchy - Agreement Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy/material-rate-hierarchy---agreement-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy/material-rate-hierarchy---agreement-work-orders"
---

# Material Rate Hierarchy - Agreement Work Orders

When capturing materials on agreement work orders, the system
 uses a specific hierarchy to determine the markup and discount rates to use for calculating
 billable rates
For agreement-related work orders, the system uses a similar
 hierarchy to determine material rates. However, for these work orders, the system will
 only use the agreement service, agreement, or work order scope template. This hierarchy
 is determined as follows:

- If the work completed line is for a preventative
 maintenance work order (those generated via SM Generate PM Work Orders) and the
 agreement service has a Pricing
 method of T-Time of Service, the system will use the rate template defined for
 the service in SM Service. The system will follow the same overrides hierarchy
 discussed above; however, in this case, it will start with the Effective Date
 overrides defined for the agreement service rate template. If the date specified
 for the work completed line does not fall within the effective date range or no
 effective dates are defined, it will use the rate template overrides and finally
 the rate template rates (if overrides are not found). No further rate search is
 performed.

- For manually entered work order scopes associated an
 agreement, if the Price Method
 is T-Time and Material and you check the Agreement Rates box, the system will use the rate template
 assigned to the agreement in SM Agreements (using the same hierarchy specified
 above for preventative maintenance work orders).

- If you did not assign a rate template to the agreement
 or if you did not check the Agreement
 Rates box, the system will use the rate template assigned to the
 work order scope, following the same hierarchy specified above for preventative
 maintenance agreements.

- If you do not associate a work order scope with an
 agreement, but you associate the work completed line with an agreement, and you
 check the Agreement Rates box,
 the system will use the rate template assigned to the agreement in SM Agreements
 (following the same hierarchy specified above for preventative maintenance work
 orders).

- If you did not assign a rate template to the agreement
 or if the Agreement Rates box
 is unchecked, the rate template specified for the work order scope will be used,
 following the same hierarchy indicated for preventative maintenance work orders
 above.

Related concepts

- [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy)

- [About Setting up Material Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides)
