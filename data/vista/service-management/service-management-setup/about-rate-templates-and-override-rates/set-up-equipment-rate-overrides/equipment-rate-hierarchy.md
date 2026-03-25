---
title: "Equipment Rate Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides/equipment-rate-hierarchy"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides/equipment-rate-hierarchy"
---

# Equipment Rate Hierarchy

When you capture equipment costs for work orders (in SM Work Orders,
 Work Completed tab), the system uses a specific hierarchy to determine the equipment rates
 to use for calculating billable rates for work completed equipment lines.

## Customer and Job Work Orders

1. Service Site Overrides

- The system will first look for rate overrides by equipment/revenue
 code rate (in SM Rate Equipment Overrides) at the service site
 level. If a match is found for the equipment/revenue code specified
 on the work completed line, the associated markup or flat rate will
 be used.

- If an override does not exist for the specified equipment/revenue
 code, the system will then use the Markup rate defined in SM Rate
 Override Base.

- If no rate is defined in SM Override Base (i.e. the Markup field is blank) and
 this is a customer work order, the system will then look for
 overrides at the Customer level (see Step 3). If this is a Job work
 order, the system will then look for overrides at the scope rate
 template level (see Step 4).

1. Customer Overrides (Customer WOs only)

- The system will look for rate overrides by equipment/revenue code.
 If a match is found (in SM Rate Equipment Overrides) for the
 equipment/revenue code at the customer level, the associated markup
 or flat rate will be used.

- If an override does not exist for the specified equipment/revenue
 code, the system will then use the override standard markup rate
 defined for the customer in SM Rate Override Base.

1. Effective Date

- If override rates are not found at the Service Site level (job work
 orders) or Customer level (customer work orders), the system will
 then look for Effective Date overrides using the rate template
 specified for the work order scope. If Effective Date overrides
 exist, the system will compare the Date specified on the work
 completed line to the Effective Dates specified for the rate
 template. If the work completed date falls within any of the
 effective date ranges, the system will then use the appropriate
 effective date template to determine equipment rates.

- The system will first look for rate overrides by equipment/revenue
 code rate (in SM Rate Equipment Overrides). If a match is found for
 the equipment/revenue code specified on the work completed line, the
 associated markup or flat rate will be used.

- If an override does not exist for the specified equipment/revenue
 code, the system will then use the override standard markup rate
 defined for the effective date template in SM Rate Template Effect
 Dates. No further rate search will be performed.

1. Rate Template

- If the work completed date does not fall within any of the effective
 date ranges or no effective dates are defined, the system will then
 look for rate overrides by equipment/revenue code at the basic rate
 template level. If a match is found for the equipment/revenue code
 at the rate template level, the associated markup or flat rate will
 be used.

- If an override does not exist for the specified equipment/revenue
 code, the system will then use the standard equipment markup rate
 defined for the rate template in SM Rate Templates.

Note: If you enter a 0.00 value in a rate field, the system assumes this is
 the desired rate and no further attempts will be made to locate a rate at a lower
 level. This applies to rates entered in SM Rate Equipment Overrides, SM Rate
 Override Base, and SM Rate Templates.

## Quote-Related Work Orders

For work orders generated from a work order quote, the system uses a similar
 hierarchy to determine equipment rates. However, for these work orders, the system
 will use only the rate overrides/rate template defined for the quote sequence.
 Overrides defined at the customer or service site level are not used.Note: The
 hierarchy described below is used only when the work order scope referenced on
 the work completed equipment line has a Price Method of Time and Material. Billable rates are not
 calculated for work completed lines associated with Flat Price or Non-Billable
 work order scopes.

1. Quote Override Rates

- The system will first look in the SM Rate Equipment Overrides table
 defined at the quote sequence Override Rates level. If overrides
 exist and a match is found, that rate will be used.

- If a match is not found, the system will use the override equipment
 rate defined in SM Rate Override Base at the quote sequence Override
 Rates level.

1. Effective Date

- If override rates are not found at the quote sequence Override Rates
 level, the system will then look for Effective Date overrides using
 the rate template specified for the quote sequence. If Effective
 Date overrides exist, the system will compare the Date specified on
 the work completed line to the Effective Dates specified for the
 rate template. If the work completed date falls within any of the
 effective date ranges, the system will then use the appropriate
 effective date template to determine the labor rate to use.

- The system will first look in the SM Rate Equipment Overrides table
 for the effective date. If overrides exist and a match is found,
 that rate will be used. If a match is not found, the system will use
 the override equiment rate defined in SM Rate Template Effect Dates
 for the effective date template. No other rate search will be
 performed

1. Rate Template

- If the work completed date does not fall within any of the effective
 date ranges or no effective dates are defined, the system will then
 look for override rates at the quote rate template level. If a match
 is found in the overrides table, that rate will be used. If a match
 is not found, the system will use the standard equipment rate
 defined for the rate template (in SM Rate Templates).Important: If you enter a 0.00 value in a rate field, the
 system assumes this is the desired rate and no further attempts
 will be made to locate a rate at a lower level. This applies to
 rates entered in SM Rate Equipment Overrides, SM Rate Override
 Base, SM Rate Tempate Effect Dates, and SM Rate
 Templates

## Agreement Work Orders

For agreement-related work orders, the system uses a
 similar hierarchy to determine equipment rates. However, for these work orders, the
 system will only use the agreement service, agreement, or work order scope template.
 This hierarchy is determined as follows:

- If the work completed line is for a preventative
 maintenance work order (those generated via SM Generate PM Work Orders) and
 the agreement service has a Pricing method of T-Time of Service, the system will use
 the rate template defined for the service in SM Service. The system will
 follow the same overrides hierarchy discussed above; however, in this case,
 it will start with the Effective Date overrides defined for the agreement
 service rate template. If the date specified for the work completed line
 does not fall within the effective date range or no effective dates are
 defined, it will use the rate template overrides and finally the rate
 template rates (if overrides are not found). No further rate search is
 performed.

- For manually entered work order scopes associated
 an agreement, if the Price
 Method is T-Time and Material and you check the Agreement Rates box, the system
 will use the rate template assigned to the agreement in SM Agreements (using
 the same hierarchy specified above for preventative maintenance work
 orders).

- If you did not assign a rate template to the
 agreement or if you did not check the Agreement Rates box, the system will use the rate template
 assigned to the work order scope, following the same hierarchy specified
 above for preventative maintenance agreements.

- If you do not associate a work order scope with an
 agreement, but you associate the work completed line with an agreement, and
 you check the Agreement
 Rates box, the system will use the rate template assigned to
 the agreement in SM Agreements (following the same hierarchy specified above
 for preventative maintenance work orders).

- If you did not assign a rate template to the
 agreement or if the Agreement
 Rates box is unchecked, the rate template specified for the
 work order scope will be used, following the same hierarchy indicated for
 preventative maintenance work orders above.
