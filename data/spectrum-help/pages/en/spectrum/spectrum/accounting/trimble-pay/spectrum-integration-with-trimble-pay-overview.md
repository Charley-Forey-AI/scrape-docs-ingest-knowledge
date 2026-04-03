---
title: "Spectrum Integration With Trimble Pay Overview | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/trimble-pay/spectrum-integration-with-trimble-pay-overview"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/trimble-pay/spectrum-integration-with-trimble-pay-overview"
---

# Spectrum Integration With Trimble Pay Overview

Learn how the integration with Trimble Pay works
Trimble Pay's integration
 with Spectrum simplifies the
 subcontractor pay application process.

1. Initial job import - when
 you perform the one-time import of an ActiveSpectrum job into Trimble Pay, a job-specific connection
 is established.

1. Ongoing automated sync

- Subcontracts - As new subcontracts reach the
 Active
 status in Spectrum,
 Trimble Pay pulls them
 in automatically, including the assigned vendor and vendor member(s).
 The subcontract phase details are imported as section headers in the
 subcontract schedule of values (SOV).

- Change Orders - When subcontract change orders are
 Executed, they flow into Trimble Pay, updating the contract amount and adding
 new lines to the schedule of values. This allows the subcontractor to
 invoice for the change orders.

1. Schedule of Values & Phase
 Detail Management - Both general contractors and subcontractors can
 break out the schedule of values in Trimble Pay to match up with the phase details created in
 Spectrum. Trimble Pay supports your choice of
 single or multiple AP subcontract phase detail lines in Spectrum.

1. Payment Application Approval
 Process & Export: Applications for Payment submitted by
 subcontractors follow the defined approval workflow in Trimble Pay. After all approvers sign
 off, the pay application can be exported (or auto-exported, if you've enabled
 that setting) to Spectrum as
 an approved AP invoice, where it shows up within about 5-10 minutes. All billing
 backup submitted with the invoice is attached to the AP invoice as an Invoice
 Image in Spectrum.

## Records Exchanged in the Import Process

A depiction of
 the data flow between Trimble Pay and
 Spectrum.
Note: The integration does not support subcontracts that use bill
 item numbers in the AP Subcontract Phase Detail. If you use subcontracts with bill
 items, costs from the exported invoices will not be properly allocated to the
 correct bill items, causing issues for your financial records.

## Spectrum Records Import Requirements

Spectrum recordImported to Trimble Pay if
JC JobStatus is Active (A)
AP SubcontractStatus is Active (A)
AP Subcontract Change OrderStatus is Executed (E)
AP VendorAssociated to the AP Subcontract
 record
AP Subcontract Phase Details Associated to the AP Subcontract
 record

Trimble Pay exports
 AP Invoices and AP Invoice Images to Spectrum.
