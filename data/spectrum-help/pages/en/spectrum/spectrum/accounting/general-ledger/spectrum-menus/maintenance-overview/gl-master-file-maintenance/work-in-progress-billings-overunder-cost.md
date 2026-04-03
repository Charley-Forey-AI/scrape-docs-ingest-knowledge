---
title: "Work-in-Progress: Billings Over/Under Cost | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-master-file-maintenance/work-in-progress-billings-overunder-cost"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-master-file-maintenance/work-in-progress-billings-overunder-cost"
---

# Work-in-Progress: Billings Over/Under Cost

According to G.A.A.P., construction industry accounting standards call for use of several General Ledger accounts to handle the situations of "Billings in excess of Costs" and "Costs in excess of Billings." This occurs in the construction industry because jobs extend across accounting periods. Work on jobs in progress across accounting periods requires this special handling in order to appropriately match the period's income to expense.
The following General Ledger accounts should be created:

- Costs in Excess of Billings (Asset is an element of the balance sheet normally carrying a debit balance and represents a probable future economic benefits obtained or controlled by a particular entity and a result of past transactions or events.) Based on the account type, when the Opening Forward Balance Update is performed, the beginning balance of the future year is set equal to the ending balance of the prior year. The same is true for liability and capital. The same is not true for income and expense accounts, which are closed automatically each year end to retained earnings. Each year, the user will start expenses at "0".)

- Billings in Excess of Costs (Normally a credit balance in the liability account represents the probable future sacrifices of economic benefits arising from present obligations of a particular entity to transfer assets or provide services to other entities in the future as a result of past transactions or events. (Like asset amounts, liability amounts are not cleared during the year-end processing. Instead, the ending balance is carried over to the new year's beginning balance.))

- Net Over / Under Billings (Revenue is the same as income; revenue is the term used in Spectrum. Income closes at year-end to retained earnings during year-end processing.)

At each period-end, the company will determine the amounts of over- and under-billings using a work-in-progress schedule. In order for the schedule to be accurate, all costs and billings must be posted. In addition, estimates or projections must be up-to-date in order to produce accurate results.
After the figures for the period have been updated, print the Contract
 Status Report on the Job Cost Reports menu. This report computes the percent complete for
 jobs in progress, and then determines the amounts of over- or under-billings based on the
 percent of work complete.
The total over-billing figure is determined by summing over-billing amounts for all the jobs in which progress billings-to-date exceed the associated costs.
The under-billing amount is computed by totaling the under-billing amounts for all jobs for which costs-to-date exceed the associated billings.
Two journal entries would typically be required at period-end. One journal entry would bring the asset account (Costs in Excess of Billings) into agreement with the under-billing figure determined above. The amount of the journal entry would be the net difference between the current balance in the asset account and the under-billing amount computed on the Contract Status Report.
The other journal entry would correspondingly adjust the liability account (Billings in Excess of Cost) to agree with the over-billing figure. In both cases, the other side of the journal entry would be to the new revenue account (Net Over /Under Billing).
Some companies prefer to have two revenue accounts, one for over-billing adjustments and one for under-billings.
