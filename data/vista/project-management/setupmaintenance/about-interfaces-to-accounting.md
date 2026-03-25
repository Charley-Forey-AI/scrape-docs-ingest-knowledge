---
title: "About Interfaces to Accounting | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/about-interfaces-to-accounting"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/about-interfaces-to-accounting"
---

# About Interfaces to Accounting

Once you have entered all the appropriate project detail and made any necessary modifications to the estimate, use PM Interface to update the accounting system for further processing.
Note:All modifications made to a project after it has been interfaced to accounting must be made through the entry of approved change orders in order for the changes to be updated to accounting.

The following accounting modules are updated with data from Project Management:

- Inventory (IN) – Material orders

- Job Cost (JC) – Jobs, original estimates, committed costs, contracts, and change orders

- Material Sales (MS) – Material quotes

- Purchase Order (PO) – Purchase orders and change orders

- Subcontract Ledger (SL) – Subcontracts and change orders

The following table illustrates which accounting tables are affected by the interface from Project Management to Accounting. Tables shown in blue are shared tables (PM/JC):
PM Files
JC
SL
PO
IN
MS

Project Master
Job Master (JCJM)
—
—
—
—

Phase/Cost Type Detail
Cost by Period (JCCP) 
Cost Header (JCCH) 
Cost Detail (JCCD) 
ACO Items (JCOD)
—
—
—
—

Phase Header
Job Phases (JCJP)
—
—
—
—

Contract Master
Contract Master (JCCM)
—
—
—
—

Contract Items
Contract Items (JCCI)
—
—
—
Contract Item by Period (JCIP)  Contract Item
 Detail  (JCID)

Material Detail
Cost by Period (JCCP)
—
PO Header (POHD) 
PO Items (POIT) 
Change Order Detail 
 (POCD)
Material Order Header  (INMO) 
Material Order Item 
 (INMI) 
IN Materials (INMT)
MS Quote Header  (MSQH) 
MS Quote Detail (
 MSQD)

Subcontract Detail
Cost by Period (JCCP)
SL Header (SLHD) 
SL Items (SLIT) 
Change Order Detail 
 (SLCD)
—
—
—

ACO Header
Change Order Header  (JCOH)
—
—
—
—

ACO Items
Contract Items (JCCI) 
Change Order Items 
 (JCOI)
—
—
—
—

[](/en/vista/vista/project-management/shared-tables)Shared Tables
[](/en/vista/vista/project-management/setupmaintenance/pm-interface-form)PM Interface
