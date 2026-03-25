---
title: "Labor Rate Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides/labor-rate-hierarchy"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides/labor-rate-hierarchy"
---

# Labor Rate Hierarchy

When capturing labor for work orders (in SM Work Orders, Work Completed tab), the system uses a specific hierarchy to determine the labor rates to use for calculating billable rates for work completed labor lines.
The following table identifies the levels and search order used
 by the system to find a default labor rate in the labor overrides table (SM Advanced
 Labor Overrides). The “Xs” denote that a value has been supplied and a blank indicates
 that no value has been supplied.
The first row represents the minimum set of information
 required for a labor rate. Each successive row provides more specific information, and
 overrides all preceding levels. For example, rates defined by call type and pay type
 will override rates defined by call type.
Technician
PRCo
Craft
Class
Call Type
Pay Type

X

X

X

X

X

X
X

X
X

X
X

X

X
X

X
X

X
X
X

X
X
X
X

X
X
X
X
X

X
X

X
X
X

X
X
X
X

X
X
X
X

X
X
X
X
X

X
X
X
X
X
X

Note: If the system does not find a match in the SM Advanced Labor Overrides
 table, it will use the standard labor rate. However, because you can set up labor
 overrides by rate template, effective date template, customer, and/or service site, the
 system will use the following hierarchy to pull the labor rate:

## Customer and Job Work Orders

The hierarchy described below is used only when the work order scope referenced on
 the work completed labor line has a Price
 Method of Time and Material. Billable rates are not calculated for
 work completed labor lines associated with Flat Price or Non-Billable work order
 scopes

1. Service Site

- The system will first look in the SM Advanced Labor Overrides table
 at the service site level. If overrides exist and a match is found,
 that rate will be used. If a match is not found, the system will use
 the override labor rate defined in SM Rate Override Base for the
 service site.

- If no override labor rate is defined in SM Rate Override Base (i.e.
 the Rate field is
 blank) and this is a customer work order, the system will then look
 for overrides at the Customer level (#2 below). If this is a Job
 work order, the system will then look for overrides at the scope
 rate template level (#4 below).

1. Customer

- The system will look for advanced labor overrides using the same
 hierarchy described above. If a match is found, that rate will be
 used. If a match is not found, the system will use the override
 labor rate defined in SM Rate Override Base for the customer.

1. Effective Date

- If override rates are not found at the Service Site level (job work
 orders) or Customer level (customer work orders), the system will
 then look for Effective Date overrides using the rate template
 specified for the work order scope. If Effective Date overrides
 exist, the system will compare the Date specified on the work
 completed line to the Effective Dates specified for the rate
 template. If the work completed date falls within any of the
 effective date ranges, the system will then use the appropriate
 effective date template to determine the labor rate to use.

- The system will look in the SM Advanced Labor Overrides table for
 the effective date. If overrides exist and a match is found, that
 rate will be used. If a match is not found, the system will use the
 override labor rate defined in SM Rate Template Effect Dates for the
 effective date template. No other rate search will be
 performed.

1. Rate Template

- If the work completed date does not fall within any of the effective
 date ranges or no effective dates are defined, the system will then
 look for advanced labor overrides at the basic rate template level.
 If a match is found in the overrides table, that rate will be used.
 If a match is not found, the system will use the standard labor rate
 defined for the rate template (in SM Rate Templates).Important: If you enter a 0.00 value in a rate field, the
 system assumes this is the desired rate and no further attempts
 will be made to locate a rate at a lower level. This applies to
 rates entered in the SM Advanced Labor Overrides table at the
 service site, customer, and rate template levels, as well as the
 standard labor rates entered in SM Rate Override Base for the
 service site and customer levels, and in SM Rate Template at the
 rate template level.To ensure that the system will follow the
 hierarchy to the next level when a match is not found in the
 SM Advanced Labor Overrides table, leave the standard rate
 field blank at the service site and customer levels. This
 will allow the system to go to the lowest level (standard
 labor rate at the rate template level) when no match is
 found in the overrides table at any of the levels. You will
 only set a value of 0.00 or greater in the standard labor
 rate field for the service site or customer levels if you do
 not want the system to use the rates at the lower levels
 (i.e. setting the standard labor rate for a service site to
 0.00 or greater will cause the system to only use that
 site's override and standard labor rates when entering work
 completed labor for a work order referencing that service
 site).

## Quote-Related Work Orders

For work orders generated from a work order quote, the system uses a similar
 hierarchy to determine labor rates. However, for these work orders, the system will
 use only the rate overrides/rate template defined for the quote sequence. Overrides
 defined at the customer or service site level are not used.Note: The hierarchy
 described below is used only when the work order scope referenced on the work
 completed labor line has a Price
 Method of Time and Material. Billable rates are not calculated
 for work completed labor lines associated with Flat Price or Non-Billable work
 order scopes

1. Quote Override Rates

- The system will first look in the SM Advanced Labor Overrides table
 defined at the quote sequence Override Rates level. If overrides
 exist and a match is found, that rate will be used. If a match is
 not found, the system will use the override labor rate defined in SM
 Rate Override Base at the quote sequence Override Rates level.

1. Effective Date

- If override rates are not found at the quote sequence Override Rates
 level, the system will then look for Effective Date overrides using
 the rate template specified for the quote sequence. If Effective
 Date overrides exist, the system will compare the Date specified on
 the work completed line to the Effective Dates specified for the
 rate template. If the work completed date falls within any of the
 effective date ranges, the system will then use the appropriate
 effective date template to determine the labor rate to use.

- The system will first look in the SM Advanced Labor Overrides table
 for the effective date. If overrides exist and a match is found,
 that rate will be used. If a match is not found, the system will use
 the override labor rate defined in SM Rate Template Effect Dates for
 the effective date template. No other rate search will be
 performed.

1. Rate Template

- If the work completed date does not fall within any of the effective
 date ranges or no effective dates are defined, the system will then
 look for advanced labor overrides at the quote rate template level.
 If a match is found in the overrides table, that rate will be used.
 If a match is not found, the system will use the standard labor rate
 defined for the rate template (in SM Rate Templates).Note: If you
 enter a 0.00 value in a rate field, the system assumes this is
 the desired rate and no further attempts will be made to locate
 a rate at a lower level. This applies to rates entered in the SM
 Advanced Labor Overrides tables, as well as the standard labor
 rates entered in SM Rate Override Base (quote override or quote
 rate template levels) or SM Rate Template Effect Dates (quote
 effective date level).To ensure that the system will follow
 the hierarchy to the next level when a match is not found in
 the SM Advanced Labor Overrides table, leave the labor rate
 field blank in SM Override Rate Base or SM Rate Template
 Effect Dates. This will allow the system to go to the next
 level when no match is found in the overrides tables. You
 will only set a value of 0.00 or greater in the labor rate
 field if you do not want the system to use the rates at the
 next level.

## Agreement Work Orders

For agreement-related work orders, the system uses a
 similar hierarchy to determine labor rates. However, for these work orders, the
 system will only use the agreement service, agreement, or work order scope template.
 This hierarchy is determined as follows:

- If the work completed line is for a preventative
 maintenane work order (those generated via SM Generate PM Work Orders) and
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
