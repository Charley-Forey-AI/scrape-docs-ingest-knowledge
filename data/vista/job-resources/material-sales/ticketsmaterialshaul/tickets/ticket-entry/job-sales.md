---
title: "Job Sales | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/ticket-entry/job-sales"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/ticket-entry/job-sales"
---

# Job Sales

This type of sale is used to record materials and hauling posted to jobs within your own company or to a sister-company.
When a job sale is posted, the JC Cost Detail (JCCD) table is updated with both material and haul units and costs.
Job quotes can be used to set pricing for each job. Like customer quotes, job quotes allow you to define special pricing on materials, as well as override haul and pay rates. You also have the option to set up phase and cost type defaults to use when entering job tickets. If you do not define phase/cost type defaults on the quote, the system uses the standard phase and cost type defaults in HQ Materials.
Pricing and haul rates follow the standard
 hierarchy.

## General Ledger Implications

When posting job sales, the General
 Ledger entries are determined by whether you are posting job sales in the same
 company, or whether you are posting sales to a sister-company, and if so, whether
 intercompany invoices are used. If selling to jobs in the same company, or
 cross-company and not using intercompany invoices, all of the necessary accounting
 is made to relieve inventory, post job expenses, and record sales revenue. If you
 are selling the materials to a sister-company, additional journal entries are made
 to the intercompany AR and AP accounts. If using intercompany invoices,
 cross-company sales are treated as a customer sale. An invoice is created, and the
 journal entries will be the same as those made for a customer sale. Job costs will
 not be recorded until the intercompany invoice is updated in AP. See Intercompany
 Invoicing in Related Topics below for information about creating invoices for sales
 to sister companies.
Override GL accounts can be defined for
 the Cost of Goods, Inventory, and Job Sales accounts (by company, category, and/or
 company/category). The system will use a hierarchical search to determine which
 account to use. If no overrides exist, the accounts specified in the IN Locations
 are used. For more information, refer to the online help for Inventory.
If you are posting tax and freight with
 job sales, the debit to the job expense entry is determined by the following:

- Material Phase (MS Ticket Entry)
 – Material expense account is determined by the phase/cost type specified
 when posting the ticket (Material Phase/CT will default from the quote or
 from HQ Materials if no quote exists).

- Haul Phase (MS Ticket Entry) –
 Haul phase expense account is determined by the haul phase/cost type
 specified when posting the ticket (Haul Phase/CT will default from the quote
 or from HQ Materials if no quote exists).

- Tax Phase (HQ Tax Codes) - The
 tax expense account is determined by the tax phase/cost type specified when
 posting the ticket. (Tax phase is determined by the JC Tax Phase and JC Cost
 Type specified in HQ Tax Codes for the tax code.) If no tax phase specified,
 the material phase is used.

The following diagrams illustrate the GL
 entries for both sales to your own jobs and those to a sister company.

## GL Implications for Value Added Tax Transactions

If you are posting Goods and Services
 Tax (GST) and/or Provincial Sales Tax (PST), the update to GL will credit the
 appropriate GST and/or PST tax payable accounts (i.e, the Credit GL Account defined
 in HQ Tax Codes). If you are tracking Income Tax Credits (ITC), the GST amount is
 deducted from the job expense and debited to the Debit GL Account specified for the
 GST tax code in HQ Tax Codes. If not tracking ITC, the GST amount is included in the
 job expense and no update to the Debit GL Account occurs.
