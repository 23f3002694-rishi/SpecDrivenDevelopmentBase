# Proposal

## Motivation

Clients currently fetch all reports and filter client-side to find one record.

Direct lookup reduces payload and improves usability.

## Changes

ADD:

GET /reports/{id}

Behavior:

- Return report if found
- Return 404 if missing

## Non-goals

- Existing routes unchanged
- No authentication changes
- No changes to PublicReport model