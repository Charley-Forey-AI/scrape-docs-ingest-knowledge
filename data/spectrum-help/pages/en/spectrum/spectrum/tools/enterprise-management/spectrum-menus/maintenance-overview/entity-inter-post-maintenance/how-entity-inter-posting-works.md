---
title: "How Entity Inter-posting Works | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/entity-inter-post-maintenance/how-entity-inter-posting-works"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/entity-inter-post-maintenance/how-entity-inter-posting-works"
---

# How Entity Inter-posting Works

Updates throughout Spectrum utilize an 'inter-post' G/L
 account when posting transactions to General Ledger when Cost Centers are enabled. The
 Inter-post G/L account is specified in the respective Installation screen.
Users may also elect to set up "Cost Center Override" accounts for
 certain cost centers. Regardless of the particular assigned 'inter-post' account, the
 software will automatically reclassify portions of the 'inter-post' amount pertaining to a
 different entity.
While the processing details may vary depending upon the particular
 update, in general, the software will look to setup in [Entity Inter-Post Maintenance](/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/entity-inter-post-maintenance) in order to
 reclassify inter-post entries to G/L accounts for the proper entity. The G/L Transaction
 Report will show the Debits and Credits to be posted to G/L based on any inter-entity
 transactions in the batch and then the update to General Ledger will write the applicable
 inter-post amounts to the designated entity-specific G/L accounts.
In order to determine the alternate 'inter-post' G/L account, the software looks to the 'From/To' entity combination for each half of the 'inter-post' transaction:

- For the CREDIT side of the inter-post transaction, the entity associated with the Credit Cost Center is the 'FROM ENTITY', and the entity associated with Debit cost center of the related inter-post entry is the 'TO ENTITY'. The software reads the Entity Inter-Post Table for this 'FROM/TO' entity combination to determine the G/L account to assign to the CREDIT side of the inter-post transaction.

- For the DEBIT side of the inter-post transaction, the entity associated with the Debit Cost Center is the 'FROM ENTITY', and the entity associated with Credit cost center of the related inter-post entry is the 'TO ENTITY'. The software reads the Entity Inter-Post Table for this 'FROM/TO' entity combination to determine the G/L account to assign to the DEBIT side of the inter-post transaction.

Inter-entity records will appear on the transaction registers just like the existing 'inter-post' lines.
Note: Inter-post "Overrides" are not supported, and no modifications
 will be provided for the case where a user posts an inter-company transaction from a
 non-entity company to a company with entity tracking.
