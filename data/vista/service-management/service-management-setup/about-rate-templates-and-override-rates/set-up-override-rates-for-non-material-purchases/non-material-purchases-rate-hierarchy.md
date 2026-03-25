---
title: "Non-Material Purchases Rate Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-override-rates-for-non-material-purchases/non-material-purchases-rate-hierarchy"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-override-rates-for-non-material-purchases/non-material-purchases-rate-hierarchy"
---

# Non-Material Purchases Rate Hierarchy

When capturing non-material purchases on a work order (via work completed purchase and work complete miscellaneous lines), the system uses a specific hierarchy to determine the markup rate to use.
 The following explains how the system determines the markup rate for non-material purchases based on your rate setup.
If the work order scope associated with the work completed line was not created from a work order quote:

1. Service Site Overrides - The system first checks the cost type overrides defined for the service site to determine if a cost type exists matching the cost type specified on the work complete line. If a match is found, the system compares the work completed lines total cost to the cost type rate break points. If the total cost falls within a break point range, the system uses the appropriate rate. If the total cost is less than the first break point, the system uses the markup rate defined for the cost type.
If an override is not defined for the cost type, the system checks the rate break points defined for the service site's base non-material markup rate. If the total cost falls within a defined rate break point, that markup rate is used. If the total cost is less than the first break point, the system uses the non-material base rate specified for the service site.

1. Customer Overrides - If no overrides are defined for the service site, the system starts with the cost type rate break points defined for the customer, and then follows the same process as described for service site overrides..

1. Effective Date - If no overrides are defined for the customer, the system then checks for an Effective Date for the rate template assigned to the work order scope. If an effective date is found that is less than the work completed date, it starts with the cost type rate break points defined for the Effective Date, and then follows the same process as described for service site overrides.

1. Rate Template - If no overrides are defined by Effective Date, the system starts with the cost type rate break points defined for the work order scope's rate template, and then follows the same process as described for service site overrides.

## Agreement Work Orders

For work orders created from a Time of Service agreement, the system checks for override rates at the service site level, then moves on to the customer level if no override rates are defined for the service site. If no override rates are found at the customer level, it then checks for an Effective Date for the rate template assigned to the agreement service or agreement (respectively). If an effective date is found that is less than the work completed date, it starts with the cost type rate break points defined for the Effective Date, and then follows the same process described above. If no overrides are defined by Effective Date, the system uses the rate template assigned to the agreement service or agreement.
