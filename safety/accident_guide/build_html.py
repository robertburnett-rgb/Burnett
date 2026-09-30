#!/usr/bin/env python3
"""Assemble guide.html: original pages 01-02 plus the injury-specific guides (03+)."""
from html import escape
from pathlib import Path

HERE = Path(__file__).parent

GUIDES = [
    {
        "num": "05",
        "title": "Manual Handling",
        "sub": "Injury Guide 1 of 5 — Pain, strain or sprain reported",
        "label": "Someone reports pain",
        "cells": [
            ("Onset", "How it started", "Did the pain start and get worse, or just appear? What were they handling at that exact moment?"),
            ("Hands", "Small items", "Handling small items: both hands or just one? One-handed picking overloads the same arm, shoulder and back."),
            ("Body Position", "Posture", "Facing the load and turning with the feet, or twisting at the waist? Twisting is a key factor in back pain."),
            ("History", "Same area", "Any problem in the same area before? When, what happened, was it reported? Ask without judgement."),
            ("The Load", "What was handled", "Weight, size, shape, grip. Awkward or unstable? Was the weight known or labelled?"),
            ("Heights &amp; Reach", "Where", "Picked up and put down at floor, waist, shoulder or overhead height? Any stooping or stretching?"),
            ("Pace &amp; Repetition", "How often", "Lifts per hour, targets, rotation, breaks taken. Start or end of shift: was fatigue a factor?"),
            ("Aids &amp; Help", "Support", "Was a trolley, tilter or second person available? Trained and following the WBI?"),
        ],
        "centre": ("What have they been lifting or handling over the last 60 minutes?",
                   "Rule: Go back the full hour. The cause is often not the last lift."),
        "evidence": [
            ("CCTV of the full hour", "how they lifted, carried and turned"),
            ("Weights handled", "weigh a sample, don't trust the label"),
            ("Pick-up and put-down heights", "measured and photographed"),
            ("WBI and training record", "current, task-specific, matches the job"),
            ("Task data", "units per hour, rotation plan, breaks taken"),
            ("Pain score log", "number and time, re-asked through the shift"),
        ],
        "factors": [
            ("People", "Rushing? Skipping the team lift? Is the same technique normal for others here?"),
            ("Equipment", "Trolleys, tilters or lift aids available, working and within reach?"),
            ("Environment", "Cold stiffens muscles. Work height, floor, congestion, space to turn the feet."),
            ("Method", "Does the WBI match the real task? Can the layout remove the twist or reach?"),
            ("Training", "Recent and task-specific? Do they know to turn their feet, not their waist?"),
            ("Systems", "Do targets drive the pace? Is job rotation in place? Similar reports here?"),
        ],
        "red": "Stop the task and get a first aider. Call 999 for chest pain, difficulty breathing or loss of bladder or bowel control. Urgent medical help for numbness, pins and needles, limb weakness or pain spreading down a leg.",
        "follow": "Pain often worsens overnight. Re-check at the end of the shift and before the next one. If they call in sick, treat it as a potential LTI and tell the safety team (page 04).",
    },
    {
        "num": "06",
        "title": "Slip, Trip &amp; Fall",
        "sub": "Injury Guide 2 of 5 — Slip, trip or fall on the same level or from height",
        "label": "Someone slips, trips or falls",
        "cells": [
            ("Slip", "Loss of grip", "Wet, oily, dusty, icy, condensation or film? Where did the foot lose grip? When was it last cleaned?"),
            ("Trip", "Foot caught", "What did the foot catch on: pallet, wrap, cable, step, threshold, damaged floor or loose stock?"),
            ("Fall", "Height &amp; landing", "Same level, or from steps, ladder, platform, dock edge or vehicle? How far? What did they land on?"),
            ("Footwear", "Grip", "What were they wearing? Soles worn? Right type for wet or chilled areas? Photograph the soles."),
            ("Carrying", "Hands &amp; view", "Carrying, pushing or pulling? Could they see their feet and the route? A hand free for the rail?"),
            ("Attention &amp; Pace", "Focus", "Rushing? On a phone or wearing headphones? Looking where they were going? No blame."),
            ("Lighting &amp; View", "Visibility", "Light levels, glare, shadow, moving from bright to dark. Was the hazard marked or visible?"),
            ("Health", "Before the fall", "Dizzy, unwell or unsteady beforehand? Did they hit their head or black out, even briefly?"),
        ],
        "centre": ("What did they slip on, trip over or fall from — and had it been there before?",
                   "Rule: Make it safe, then photograph before it is cleaned or moved."),
        "evidence": [
            ("Photos of the surface or obstruction", "wide and close-up, with scale"),
            ("Footwear", "photos of soles, policy and what was issued"),
            ("Cleaning and inspection records", "last clean, spill reports"),
            ("Floor, steps or ladder", "damage, gradient, inspection tag, handrail"),
            ("CCTV", "direction, pace, what they carried, the lead-up"),
            ("Lighting and weather", "light levels; wet or ice brought in"),
        ],
        "factors": [
            ("People", "Shortcuts across wet or cluttered areas? Are others working round the same hazard?"),
            ("Equipment", "Right steps or ladder for the job? Handrails, edge protection, non-slip treads?"),
            ("Environment", "Floor finish, leaks, condensation, chiller doors, weather brought in, lighting."),
            ("Method", "Spill procedure: who cleans, how fast, cordon and signs? Clean-as-you-go in place?"),
            ("Training", "Footwear rules, safe use of steps, reporting spills and near misses."),
            ("Systems", "Housekeeping standard and inspection frequency. Any trend for this location?"),
        ],
        "red": "Do not move them if they hit their head, have neck or back pain, cannot bear weight or a limb looks deformed. First aider now; 999 for loss of consciousness, confusion, vomiting or a fall from height.",
        "follow": "Bruising and stiffness show up the next day, so check in again. Fix the hazard and re-inspect before reopening the area, and look for the same hazard elsewhere on site.",
    },
    {
        "num": "07",
        "title": "MHE Collision",
        "sub": "Injury Guide 3 of 5 — Forklift, reach truck or pallet truck collision",
        "label": "Material handling equipment hits a person, truck or structure",
        "cells": [
            ("Who &amp; What", "People and asset", "Driver, pedestrian or second truck. Truck type and asset ID. Is the driver authorised on this truck?"),
            ("Direction &amp; Speed", "Movement", "Forward or reversing? Speed? Turning or at a junction? Was the horn or warning used?"),
            ("Load &amp; View", "Visibility", "What was carried, at what fork height? Could the driver see past the load? Should they have been reversing?"),
            ("Pedestrian", "Why there", "Why were they there? In a walkway or crossing? Phone or headphones? Did they see the truck?"),
            ("Layout", "Traffic routes", "Segregation, barriers, crossing points, blind corners, mirrors, speed limits, floor marking."),
            ("Truck Condition", "Pre-use check", "Check done? Brakes, horn, lights, beacon or blue spot, seat belt. Any earlier defects?"),
            ("Driver Condition", "Fit to drive", "Alert and fit? Hours on the truck, breaks, pace and targets. Post-incident checks per policy."),
            ("Damage", "Property", "Racking, doors, stock or other trucks hit? Damaged racking must be inspected before use."),
        ],
        "centre": ("Were the truck and the pedestrian ever meant to be in the same place at the same time?",
                   "Rule: Take the truck out of use, keep the key, preserve the truck data."),
        "evidence": [
            ("Truck isolated", "key removed, tagged out until inspected"),
            ("Truck data", "telematics, impact, speed, key or PIN log"),
            ("CCTV from several angles", "approach, impact and aftermath"),
            ("Scene photos and measurements", "positions, sight lines, marks"),
            ("Pre-use check and service history", "that shift, that truck"),
            ("Driver authorisation", "training on this truck type, refresher"),
        ],
        "factors": [
            ("People", "Pedestrians using truck routes as a shortcut? Horn used at junctions? What is normal here?"),
            ("Equipment", "Blue spots, beacons, mirrors, collision detection, speed limiters fitted and working?"),
            ("Environment", "Congestion, blind corners, noise, lighting, floor condition, peak periods."),
            ("Method", "Does the traffic plan (segregation, crossings, priority) match how the site runs?"),
            ("Training", "Authorised on this truck type? Refresher current? Pedestrian awareness covered?"),
            ("Systems", "Do targets drive speed? Are MHE near misses here reported and reviewed?"),
        ],
        "red": "Anyone struck by a truck needs a first aider or medical check, even if they walked away. 999 for crush injuries, head, neck or back pain, unconsciousness or heavy bleeding. If trapped, follow the site emergency plan.",
        "follow": "Tell the safety team the same day and check whether it is reportable. Keep the truck and driver out of service until checks are done. Inspect racking, and check for similar risks elsewhere.",
    },
    {
        "num": "08",
        "title": "Cart &amp; Cage Collision",
        "sub": "Injury Guide 4 of 5 — Roll cage, trolley or tugger cart movement resulting in a collision",
        "label": "A moving cart or cage hits, traps or crushes",
        "cells": [
            ("What Moved", "Equipment", "Roll cage, trolley, tugger cart or stacked pallet? Pushed or pulled? By how many people?"),
            ("The Load", "Weight and view", "Weight and height. Stable and secured? Overloaded? Could they see over or round it?"),
            ("Wheels &amp; Brakes", "Condition", "Castors turning freely, or damaged and seized? Brakes working? Which wheels led?"),
            ("Route &amp; Floor", "Surface", "Ramp, slope, dock plate, threshold, damaged or dirty floor? Did the cage run away?"),
            ("Hands &amp; Body", "Contact", "Where were hands and feet? Trapped between cage and rack, wall, door or another cage? Foot run over?"),
            ("Speed &amp; Pace", "Movement", "How fast? Rushing, targets, peak-time congestion? Two-way traffic in the same aisle?"),
            ("Visibility", "Crossings", "Blind corners, doorways, crossing points, mirrors. Could they see the person, and the person them?"),
            ("Parking", "At rest", "Parked with brakes on, out of the walkway, not on a slope? Did it move by itself?"),
        ],
        "centre": ("What did the cage hit or trap — and was it under control at the time?",
                   "Rule: Tag the cage out before it goes back into circulation."),
        "evidence": [
            ("Cage or cart tagged out", "asset number; wheels and brakes photographed"),
            ("Load weight and loading", "measure it; photograph how it was loaded"),
            ("Route and floor", "gradient, ramps, thresholds, dock plates"),
            ("CCTV", "speed, direction, who was pushing, their view"),
            ("Inspection and maintenance records", "plus defect reports"),
            ("Cage handling rules", "max load and height, push not pull, WBI"),
        ],
        "factors": [
            ("People", "Pulling cages backwards or overloading to save trips? Are others doing the same?"),
            ("Equipment", "Wheel type suited to the floor? Brakes fitted? Does defect reporting work?"),
            ("Environment", "Ramps, thresholds, narrow aisles, congestion, worn floor, lighting."),
            ("Method", "Max load and height, route, push or pull, right of way, parking rules."),
            ("Training", "Cage handling and pushing technique. Pre-use inspection covered?"),
            ("Systems", "Targets that reward speed? Maintenance schedule? Near misses reported?"),
        ],
        "red": "Call a first aider for crushed or trapped hands, fingers or feet. Call 999 for heavy bleeding, deformity, inability to move a limb or bear weight, or any blow to the head or neck.",
        "follow": "Swelling and bruising can build over hours, so check in again before the end of the shift. Check the rest of the cage fleet for the same fault, and share the learning (no names).",
    },
    {
        "num": "09",
        "title": "Struck Into Injury",
        "sub": "Injury Guide 5 of 5 — Someone has bumped or walked into something",
        "label": "Someone bumps into a fixed or protruding object",
        "cells": [
            ("What Was Hit", "The object", "Racking beam, pallet corner, forks, door, guard, cage, low structure or sharp edge? Fixed, or moved there?"),
            ("Body Part", "Force", "Which part of the body, and how hard? Head, face or eyes need a medical check even if they look minor."),
            ("Movement", "Direction", "Walking, turning, bending or reaching? Forwards, backwards or sideways? How fast?"),
            ("Attention", "Focus", "Looking where they were going? Carrying, on a phone, wearing headphones, talking? No blame."),
            ("Route", "Path taken", "Normal route or a shortcut? Was the route blocked, forcing them through a gap?"),
            ("Should It Be There?", "Object status", "Left out, moved or protruding? Temporary or permanent? Has anyone hit it before?"),
            ("Visibility", "Lighting", "Lighting, glare, colour or contrast marking, warning signs. Could they see the hazard at all?"),
            ("Space", "Housekeeping", "Clearance height and width. Stock stored in the aisle? Was the area congested or busy?"),
        ],
        "centre": ("What did they hit — and would the next person hit it too?",
                   "Rule: If the hazard is still there, guard or mark it now."),
        "evidence": [
            ("Photos of the object", "position and clearance; measure it"),
            ("View from their eye line", "photograph along their direction of travel"),
            ("CCTV", "route, pace, what they carried, who left it there"),
            ("First aid record", "body part and mechanism"),
            ("Housekeeping and inspection records", "when last checked"),
            ("Near-miss log", "earlier bumps at this location"),
        ],
        "factors": [
            ("People", "Regular route or shortcut? Is weaving round hazards seen as normal here?"),
            ("Equipment", "Rack protectors, guarding, padding, edge protection or mirrors fitted?"),
            ("Environment", "Lighting, contrast marking, congestion, narrow gaps, low structure."),
            ("Method", "Are pallets, forks or cages left standing in walkways? Where should they go?"),
            ("Training", "Aware of the hazard zone? Site layout covered in induction?"),
            ("Systems", "Hazard reporting, inspection frequency, previous bumps, layout change control."),
        ],
        "red": "First aider for any strike to the head, face, eyes or neck. 999 for unconsciousness, confusion, vomiting, drowsiness, blurred vision, heavy bleeding or a suspected fracture. Never leave a head injury alone.",
        "follow": "Head bumps can show symptoms later. Check again during the shift and before the next one. If they call in sick, treat it as a potential LTI and tell the safety team (page 04).",
    },
]

NEEDS = [
    ("A small break", "Sit, stretch, have a drink. Check again soon."),
    ("Different work", "Lighter, lower-risk duties for now."),
    ("First aid", "A first aider assesses, treats and records."),
    ("Rest", "Time off the floor in a quiet place."),
    ("A medical check", "GP, occupational health, urgent care or A&amp;E."),
]


def cell(n, title, sub, desc):
    return f"""
      <div class="ig-cell">
        <div class="ig-header">
          <div class="ig-num">{n}</div>
          <div><div class="ig-title">{title}</div><span class="ig-sub">{sub}</span></div>
        </div>
        <div class="ig-desc">{desc}</div>
      </div>"""


def guide(g, idx, total):
    cells = [cell(i + 1, *c) for i, c in enumerate(g["cells"])]
    q, rule = g["centre"]
    centre = f"""
      <div class="ig-center">
        <div class="ig-center-q">{q}</div>
        <div class="ig-center-rule">{rule}</div>
      </div>"""
    grid = "".join(cells[:4]) + centre + "".join(cells[4:])

    ev = "".join(
        f'\n        <div class="ev"><div class="ev-box"></div><span><strong>{a}</strong> — {b}</span></div>'
        for a, b in g["evidence"]
    )
    fcs = "".join(
        f'\n        <div class="fcl"><div class="fcl-label">{a}</div><p>{b}</p></div>'
        for a, b in g["factors"]
    )
    scale = "".join(
        f'<div class="{"lo" if i <= 3 else "mid" if i <= 6 else "hi"}">{i}</div>' for i in range(1, 11)
    )
    needs = "".join(f'\n        <div class="need"><b>{a}</b><p>{b}</p></div>' for a, b in NEEDS)

    return f"""
<!-- ═══════════════════════════════════════════
     PAGE {g['num']} — {g['title'].upper()}
     ═══════════════════════════════════════════ -->
<div class="page guide">

  <div class="ph">
    <div>
      <div class="ph-eyebrow">HelloFresh · Safety &amp; Operations · Injury Guide</div>
      <div class="ph-title">{g['title']}</div>
      <div class="ph-sub">{g['sub']}</div>
    </div>
    <div class="ph-num">{g['num']}</div>
  </div>

  <div class="use-band"><b>Use with pages 01–04</b> Welfare first, make it safe, secure CCTV, separate witnesses, then ask "What do you think caused this?"</div>

  <div class="sec">
    <div class="sec-label">{g['label']}</div>
    <div class="sec-title">Ask and note in the first 60 minutes</div>
    <div class="info-grid">{grid}
    </div>
  </div>

  <div class="two-col">
    <div class="sec">
      <div class="sec-label">What We Know 100%</div>
      <div class="sec-title">Evidence to Secure</div>
      <div class="ev-list">{ev}
      </div>
    </div>
    <div class="sec">
      <div class="sec-label">Look Wider — Not Just the Person</div>
      <div class="sec-title">Contributing Factors</div>
      <div class="fc-list">{fcs}
      </div>
    </div>
  </div>

  <div class="bq needs-band">
    <div class="bq-headline">"On a scale of 1 to 10, how bad is the pain right now?"</div>
    <div class="bq-rule">Write down the number and the time. Ask again later — a rising number means it is getting worse.</div>
    <div class="scale">{scale}</div>
    <div class="scale-key"><span>Mild</span><span>Moderate</span><span>Severe — first aider or medical check now</span></div>
    <div class="needs-title">Then ask: what do you need?</div>
    <div class="needs">{needs}
    </div>
  </div>

  <div class="bar-row">
    <div class="bar"><div class="bar-head">Red flags — act now</div>{g['red']}</div>
    <div class="bar"><div class="bar-head">Follow-up</div>{g['follow']}</div>
  </div>

  <div class="pf">
    <div class="pf-brand"><strong>HelloFresh</strong> &nbsp;·&nbsp; Safety &amp; Operations</div>
    <div class="pf-note">Injury guide {idx} of {total} &nbsp;·&nbsp; Manager reference only</div>
  </div>

</div><!-- /page {g['num']} -->
"""


def main():
    fonts = (HERE / "fonts" / "fonts.css").read_text()
    css = (HERE / "styles.css").read_text()
    base = (HERE / "pages_01_02.html").read_text()
    guides = "".join(guide(g, i + 1, len(GUIDES)) for i, g in enumerate(GUIDES))
    html = f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Accident Investigation Guide</title>
<style>
{fonts}
{css}
</style></head><body>
{base}
{guides}
</body></html>
"""
    (HERE / "guide.html").write_text(html)
    print("wrote guide.html", len(html))


if __name__ == "__main__":
    main()
