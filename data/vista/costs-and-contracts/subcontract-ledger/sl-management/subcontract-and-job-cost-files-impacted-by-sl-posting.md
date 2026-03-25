---
title: "Subcontract and Job Cost Files Impacted by SL Posting | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/subcontract-and-job-cost-files-impacted-by-sl-posting"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/subcontract-and-job-cost-files-impacted-by-sl-posting"
---

# Subcontract and Job Cost Files Impacted by SL Posting

The following illustration provides an example of how regular
 items and change order items affect Subcontract and Job Cost balances.
Subcontract Ledger
SLIT (SL Items)
 Table
Job Cost
JCCP (JC Costs By
 Period) Table

ORIGINAL 
 Units/Price/Total
CURRENT 
 Units/Price/Total
INVOICED 
 Units/Price/Total
TOTAL COMMTD 
 Units/Total
REMAIN COMMTD 
 Units/Total
ACTUAL  Units/Total

1.
10/$100/$1000
10/$100/$1000
0/$0
10/$1000
10/$1000
0/$0

2.
10/$100/$1000
10/$100/$1000
8/$800
10/$1000
2/$200
8/$800

3.
10/$100/$1000
15/$100/$1500
8/$800
15/$1500
7/$700
8/$800

4.
10/$100/$1000
15/$100/$1500
18/$1800
15/$1500
-3/$-300
18/$1800

5.
10/$100/$1000
18/$100/$1800
18/$1800
18/$1800
0/$0
18/$1800

1.  SL Entry: A subcontract is set up
 with one item.       10 units @ $100 each = $1000
2.  AP Transaction Entry: An AP
 transaction to pay a portion of this subcontract is
 entered.        8 units @$100 = $800
3.  SL Change Order Entry: A change
 order is entered for additional units.         5 units @
 $100 each = $500
4.  AP Transaction Entry: An AP
 transaction to pay a portion of this subcontract is entered.      10
 units @$100 = $1000
  Note that this overpays the
 subcontract, causing negative remaining committed costs until the next transaction is
 entered.
5.  SL Change Order Entry: A change
 order is entered for additional units.        3 units @
 $100 each = $300
