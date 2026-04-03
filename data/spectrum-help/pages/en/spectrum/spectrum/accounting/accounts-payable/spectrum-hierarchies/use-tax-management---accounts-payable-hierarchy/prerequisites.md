---
title: "Prerequisites | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-hierarchies/use-tax-management---accounts-payable-hierarchy/prerequisites"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-hierarchies/use-tax-management---accounts-payable-hierarchy/prerequisites"
---

# Prerequisites

When trying to determine what the tax default is, Spectrum considers the following:

- The Utilize tax
 classification setting and the Tax class default setting (is it
 set to job or vendor?) in the Job Cost Installation
 screen.

- The vendor tax setup (is there a tax code present?).

- The job tax setup (is there a tax class code present in Job Cost > Job File Maintenance?).

- The tax classification setup (what is the A/P tax code and are there any cost
 type or phase overrides in Job Cost > Tax Classification File Maintenance?).

Spectrum allows you to set up all tax information in either the vendor
 or the job, but you can also use both sources and even overrides. Furthermore, if the
 Utilize tax classification
 checkbox is selected in the Job Cost Installation screen, this
 allows you to set the exemption flags in Tax Classification File
 Maintenance that will be used when processing A/P invoices.
