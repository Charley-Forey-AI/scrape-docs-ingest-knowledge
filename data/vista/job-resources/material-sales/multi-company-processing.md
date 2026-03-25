---
title: "Multi-Company Processing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/multi-company-processing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/multi-company-processing"
---

# Multi-Company Processing

The Material Sales module, like the majority of the accounting modules, has multi-company and cross-company processing capabilities.
These features enable you to process data in one specific MS company and interface the information to a different company in a related module.
Multi-company processing allows the
 currently active company to interface to any valid company in another related module. In
 MS, this applies to interfaces with EM, IN, and JC. The company that will be updated
 with transaction detail is specified at the time of transaction entry. For example, in
 MS Ticket Entry, the JC Co# is specified for Job sales, the IN Co# is specified for
 Inventory sales, and the EM Co# is specified when hauling materials with your own
 equipment.

## Cross Company Processing

Cross-company processing occurs when the
 currently active company can only interface with one specified company in another
 related module. In MS, this applies to interfaces with AP and AR. Unlike
 multi-company processing, you do not specify the company at the time of transaction
 entry; therefore, you must define which companies will be updated in MS Company
 Parameters. Updates to AR occur only when processing customer and intercompany
 sales, and updates to AP only occur when processing intercompany sales or hauler
 payments posted to a haul vendor.
Note: The GL company you specify for the MS company
 must be the same GL company specified for the corresponding IN company.

## One to One Processing

One-to-one processing means that the
 currently active company can only interface with the same company in another module.
 In MS, this applies to IN for the selling company. Although an MS company can sell
 materials to any valid Inventory company, it can only sell materials from the same
 IN company (i.e. MS Co# 1 can only sell materials stocked in IN Co# 1).
If you plan to use multi-company or
 cross-company processing, your Viewpoint representative will work closely with you
 to ensure that all appropriate coordinating setups are made to accommodate your
 specific accounting needs.
