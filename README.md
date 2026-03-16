# Gwangju

## Pickleball Round Robin – Doubles

A single-file HTML app for organizing a pickleball doubles tournament with rotating partners, score tracking, and standings.

Open `pickleball-round-robin.html` in any web browser. No installation or internet connection required.

---

## How to Use

### 1. Tournament Setup

Choose three values and click **Set Players & Courts**:

| Field | Description |
|---|---|
| **Number of Players** | Total players joining the tournament (4 – 16) |
| **Number of Courts** | Available pickleball courts |
| **Number of Rounds** | How many rounds to play (1 – 10) |

> **Doubles rule:** Each court needs exactly 4 players (2 per side).
> The courts dropdown automatically disables options that require more players than you have.

| Courts | Minimum Players Needed |
|---|---|
| 1 | 4 |
| 2 | 8 |
| 3 | 12 |
| 4 | 16 |

The **Number of Rounds** field pre-fills with the full round-robin count (everyone plays against everyone once). You can reduce it for a shorter tournament. The hint next to the label shows both values, e.g. `(full round-robin = 7, max 10)`.

---

### 2. Enter Player Names

A numbered input appears for each player. Type each player's name.

- Click **Fill Demo Names** to auto-populate sample names for testing.
- Click **Generate Schedule** when all names are entered.

---

### 3. Match Schedule

The schedule is displayed round by round. Each round shows:

- **Court cards** – which two teams play on each court:
  ```
  Court 1
  Alice & Bob
      VS
  Carol & Dave
  ```
- **Sitting Out panel** – players who rest this round (appears when players exceed courts × 4).
- **Idle courts** – courts with no match this round.

Partners rotate every round automatically using a circle-rotation algorithm, so everyone plays with and against different people each round.

**Buttons in the schedule header:**
- **🖨 Print** – opens the browser print dialog for a clean hard copy.
- **🔀 Shuffle** – randomises player seeding and regenerates the entire schedule.

---

### 4. Score Entry

Below the schedule, a score table lists every match:

| Column | Description |
|---|---|
| Match | Round and court reference (e.g. `R1 · C1`) |
| Team 1 | Names of the two players on the first team |
| Score 1 | Points scored by Team 1 |
| Score 2 | Points scored by Team 2 |
| Team 2 | Names of the two players on the second team |

Enter scores after each round or at the end of the tournament. Click **Calculate Standings** when done.

---

### 5. Standings

Players are ranked individually by wins, then point differential as a tiebreaker.

| Column | Meaning |
|---|---|
| # | Rank (🥇 🥈 🥉 for top 3) |
| Player | Individual player name |
| W | Matches won (as a team) |
| L | Matches lost (as a team) |
| +Pts | Total points scored by the player's team |
| −Pts | Total points scored against the player's team |
| Diff | Point differential (+Pts minus −Pts) |

Wins and losses are shared between both partners on a team for each match.

---

## Round Count Reference

| Players | Full Round-Robin |
|---|---|
| 4 | 3 rounds |
| 6 | 5 rounds |
| 8 | 7 rounds |
| 10 | 9 rounds |
| 12 – 16 | 10 rounds (capped) |

Rounds beyond the full round-robin count repeat the rotation with new partner combinations.
