---
title: "PO Batch Creation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-batch-creation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-batch-creation"
---

# PO Batch Creation

Generating purchase orders is the final step in the
 requisition process. Once requisitions are approved for purchase, they are eligible for
 initialization to a purchase order.
The initialization process (PO Initialization)
 allows you to generate purchase orders based on a set of criteria (i.e. IN location,
 material category, job, line type, requisition ID, etc.). The system adds all eligible
 requisition lines meeting the specified criteria to a purchase order based on vendor and
 shipping address; that is, all requisition lines with the same vendor and shipping
 address will be added as (separate) items on the same purchase order.
Examples:
Eligible Requisition Lines
Req #
Line #
Line Type
Material
Vendor
Ship Address

120
1
Job
21000
2503
222 W 10th Ave  Any
 City, OR

121
1
Exp
22000
1694
1122 SE Grand Ave 
 Any City, WA

121
2
Inv
23000
1694
2300 SW Franklin
 Blvd  Any City, CA

122
1
Job
24000
2503
222 W 10th Ave  Any
 City, OR

After Initialization to a Purchase Order
PO #
Vendor
Ship Address
PO Item
RQ #
RQ Line #

30100
2503
222 W 10th Ave  Any
 City, OR
1
120
1

2
122
1

30101
1694
122 SE Grand Ave 
 Any City, WA
1
121
1

30102
1694
2300 SW Franklin
 Blvd  Any City, CA
1
121
2
