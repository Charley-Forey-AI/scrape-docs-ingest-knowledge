---
title: "Information Flow | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-hierarchies/use-tax-management---accounts-payable-hierarchy/information-flow"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-hierarchies/use-tax-management---accounts-payable-hierarchy/information-flow"
---

# Information Flow

Follow the hierarchies below to see how Spectrum determines the tax default by comparing the settings shown here with your company's settings.
IF ->
AND ->
AND ->
= THEN

Vendors = No tax code
Job Cost Installation Utilize tax classification? = No
Not applicable
Non-taxable.

Vendors = No tax code
Job Cost Installation Utilize tax classification? = Yes
Job File Maintenance = Yes, tax classification code entered
Use the A/P tax code in Tax Classification File Maintenance unless exemptions exist (see hierarchy shown below).

Vendors = No tax code
Job Cost Installation Utilize tax classification? = Yes
Job File Maintenance = No tax classification code
Non-taxable.

Vendors = Yes, tax code entered
Job Cost Installation Utilize tax classification? = No
Not applicable
Use the tax code from Vendors.

Vendors = Yes, tax code entered
Job Cost Installation Utilize tax classification? = Yes
Job File Maintenance = No tax classification code
Use the tax code from Vendors

Vendors = Yes, tax code entered
Job Cost Installation Utilize tax classification? = Yes, and Tax class default = Byvendor
Job File Maintenance = Yes, tax classification code entered
Use the tax code from Vendors.

Vendors = Yes, tax code entered
Job Cost Installation Utilize tax classification? = Yes, and Tax class default = Byjob
Job File Maintenance = Yes, tax classification code entered
Use the A/P tax code in Tax Classification File Maintenance unless exemptions exist (see hierarchy shown below).
