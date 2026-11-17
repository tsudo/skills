<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2026 Keith Crawford. Ships with the council skill, github.com/tsudo/skills -->

# Persona Card

A persona card is a perspective written for one decision, confirmed by the user before dispatch, and given to a seat as its identity. It simulates a perspective; it does not speak for a real person.

## Fields

| Field | Content |
| --- | --- |
| `name` | A role, never a real person's name: "first-year customer", "opposing counsel", "the CFO" |
| `represents` | Whose perspective this is, in one line |
| `stake` | What this seat gains or loses from the decision |
| `knows` | What someone in this position would know |
| `cannot_know` | What they would not know or see |
| `blind_spots` | Where this perspective tends to go wrong |
| `simulated` | Always `true` |

## Rules

- **No stance in the card.** "Skeptical of price rises" steers the answer. "Pays monthly, has switched providers twice" lets the seat reach its own view.
- **Show the user every card before dispatch.** They edit or drop it.
- **Cards must be able to disagree.** Two cards whose `stake` and `knows` overlap heavily will not. Merge them or change one.
- **A card is not a person.** Do not name a real individual, and do not present a card's view as what that person would say.

## Example

```yaml
name: long-time client
represents: a client who has bought from the firm for two years
stake: loses a known contact if the service changes hands; gains if response times improve
knows: current pricing, turnaround, who answers the phone
cannot_know: margins, staffing, what competitors charge
blind_spots: weighs familiarity over price; assumes today's service level is fixed
simulated: true
```
