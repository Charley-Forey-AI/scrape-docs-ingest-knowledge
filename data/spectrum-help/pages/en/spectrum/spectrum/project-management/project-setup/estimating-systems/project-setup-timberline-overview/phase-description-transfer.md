---
title: "Phase Description Transfer | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/estimating-systems/project-setup-timberline-overview/phase-description-transfer"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/estimating-systems/project-setup-timberline-overview/phase-description-transfer"
---

# Phase Description Transfer

Some Timberline Estimating users wish to transfer phase
 code descriptions from the estimating package.
This is possible, but requires careful setup. There is a fine point in the Job Cost Export
 file. Precision can only create "P" type records and include the corresponding Precision
 phase description in the export file when each Job Cost Phase code used in the Precision
 Estimating database has an EXACTLY MATCHING Estimating Phase code. Any difference
 (including suffix or punctuation, leading zeros, etc.) and Precision will not be able to
 look up a matching description to place in the JCE file. The Job Cost phase code and
 Estimating Phase code are both in the Timberline estimating software. The estimator has to
 set up both of these to be the same in the estimating package in order for the transfer to
 succeed.
