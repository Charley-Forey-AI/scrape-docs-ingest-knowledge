---
title: "About the CM Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-company-setup/about-the-cm-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-company-setup/about-the-cm-company-parameters-form"
---

# About the CM Company Parameters Form

Use the CM Company Parameters form to set up the various control options for each CM company on your system before you begin processing in CM.
 You must have the same company number set up in the HQ and GL modules before you can access and set up a company in CM. Each CM company set up on this system may be customized using this program.
It is suggested that this program be restricted so that only the System Administrator has access to it.

## GL Interaction

CM is directly linked to General Ledger for updates and company/account
 verification.
For each CM company on your system, you
 must specify the GL company number that will be updated. The GL Interface Level
 controls the type of detail that is sent to GL from posting outstanding checks,
 deposits, and adjustments in Cash Management.
Note: The GL company that you specify here must first
 be set up in GL before it can be accessed in CM.

## Implementation

During the initial setup stage, you may wish to check the Allow
 Changes to Statement Beginning Balance option box and set the GL Interface Level to
 ‘No Update’. This will allow you to enter your first statement beginning balances
 and to post dummy outstanding entries for cleared checks and deposits prior to those
 entered live on the system. Remember to change these fields after the first
 statement is reconciled.

## Audit Options

The audit options determine when entries will be added to the HQ Audit Master (HQMA)
 table. See [Audit Options](/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-company-setup/about-the-cm-company-parameters-form/field-definitions-cm-company-parameters-form#ID-00009903--en__ID-00009903) for more
 information.
