#!/usr/bin/env python3
"""Generate a scheduler-import CSV for the CAG social launch week.

Source of truth = the content files in content/social/. This script holds the
final per-platform copy as structured data so the CSV is RFC-4180 valid
(captions contain commas, quotes, emoji, and newlines).

Columns are chosen to map cleanly onto Metricool / Publer / Buffer bulk import:
  date, time, platform, title, text, first_comment, link, media, status

- title         -> Pinterest pin title + YouTube title (blank for IG/FB/TikTok)
- text          -> the post body / caption / YouTube+Pinterest description
- first_comment -> IG hashtags (best practice: hashtags in first comment, clean caption)
- media         -> file to attach (Reels/TikTok/Shorts need the 9:16 reframe first)

Re-run safe: overwrites content/social/cag-social-schedule.csv.
"""
import csv, pathlib

OUT = pathlib.Path("content/social/cag-social-schedule.csv")

IG_TAGS = ("#africangrey #africangreyparrot #congoafricangrey #talkingparrot "
           "#africangreysofinstagram #greyparrot #parrotsofinstagram #parrotlove "
           "#parrotlife #birdsofinstagram #parrotbreeder #captivebred #dnasexed "
           "#ethicalbreeder #usdalicensed #citesappendixI #handraised #parrottok "
           "#smartbird #midlandtx #texasparrots #africangreytexas")
IG_TAGS_DIET = ("#africangrey #congoafricangrey #africangreysofinstagram "
                "#parrotsofinstagram #parrotlife #parrotcare #parrotdiet #captivebred "
                "#dnasexed #ethicalbreeder #handraised #birdsofinstagram #greyparrot #midlandtx")

POSTS = [
    # ---- 2026-06-09 : Maxy talking HERO (vertical reframe needed) ----
    {
        "date": "2026-06-09", "time": "18:00", "platform": "Instagram", "title": "",
        "text": ("Meet Maxy. He started \"talking\" back to us at about a year old — and now he "
                 "runs commentary on the whole house from his perch.\n\n"
                 "Here at C.A.Gs, this is the part nobody warns you about: an African Grey doesn't "
                 "just mimic, he files away the sounds that matter to your family and gives them back "
                 "at the worst (best) possible moment. Maxy learned the microwave beep before \"hello.\"\n\n"
                 "Every grey we raise is hand-fed from hatch, fully weaned, DNA-sexed, and goes home "
                 "with full CITES Appendix I + health paperwork. Family aviary in Midland, TX since 2014.\n\n"
                 "Comment or DM us \"AVAILABLE\" and we'll send you who's looking for a home right now. 👇"),
        "first_comment": IG_TAGS, "link": "https://congoafricangreys.com/african-grey-parrot-for-sale/",
        "media": "talking-african-grey-parrots-video.mp4 (REFRAME to 9:16 first)", "status": "draft",
    },
    {
        "date": "2026-06-09", "time": "19:00", "platform": "TikTok", "title": "",
        "text": ("Maxy is 100% certain he's a person. 🗣️ Our hand-raised Congo African Greys are talkers "
                 "— and this is just a Tuesday. Follow for weekly parrot updates from our Midland, TX "
                 "aviary. #africangrey #talkingparrot #parrottok #fyp #congoafricangrey #parrotsoftiktok"),
        "first_comment": "", "link": "https://congoafricangreys.com/african-grey-parrot-for-sale/",
        "media": "talking-african-grey-parrots-video.mp4 (REFRAME to 9:16 first)", "status": "draft",
    },
    {
        "date": "2026-06-09", "time": "17:00", "platform": "YouTube", "title": "Our African Grey Maxy Won't Stop Talking 🗣️ #shorts",
        "text": ("Maxy is one of our hand-raised Congo African Greys here at C.A.Gs in Midland, TX. "
                 "African Greys are the best talkers in the parrot world — and Maxy proves it daily. "
                 "Every bird we raise is captive-bred, DNA-sexed, and placed with full CITES Appendix I "
                 "documentation. See available greys → https://congoafricangreys.com/african-grey-parrot-for-sale/\n"
                 "#africangrey #talkingparrot #congoafricangrey #shorts"),
        "first_comment": "", "link": "https://congoafricangreys.com/african-grey-parrot-for-sale/",
        "media": "talking-african-grey-parrots-video.mp4 (REFRAME to 9:16 first)", "status": "draft",
    },
    # ---- 2026-06-10 : Maxy story on Facebook ----
    {
        "date": "2026-06-10", "time": "09:00", "platform": "Facebook", "title": "",
        "text": ("Some mornings Maxy greets us before the coffee's even on. ☕\n\n"
                 "He's one of our hand-raised Congo African Greys, and if you've never lived with a "
                 "talking grey, this is what you're signing up for: a feathered family member who learns "
                 "your routines, your phrases, and exactly which sound gets your attention.\n\n"
                 "We've raised greys as a family here in Midland, TX since 2014. Every bird is captive-bred "
                 "in the USA, DNA-sexed, vet-checked, and goes home with full CITES Appendix I and hatch "
                 "paperwork. We ship nationwide — $185 airport pickup or $350 home delivery.\n\n"
                 "See who's available → https://congoafricangreys.com/african-grey-parrot-for-sale/\n#africangrey #congoafricangrey #talkingparrot"),
        "first_comment": "", "link": "https://congoafricangreys.com/african-grey-parrot-for-sale/",
        "media": "talking-african-grey-parrots-video.mp4", "status": "draft",
    },
    # ---- 2026-06-11 : Pinterest "do greys talk?" ----
    {
        "date": "2026-06-11", "time": "20:00", "platform": "Pinterest",
        "title": "Do African Greys Really Talk? Meet Maxy (Congo African Grey)",
        "text": ("African Greys are widely considered the best talking parrots in the world — and our "
                 "hand-raised Congo, Maxy, is proof. Here at C.A.Gs in Midland, TX we've raised talking "
                 "African Greys since 2014. Curious whether a Congo or a Timneh is the better talker for "
                 "your home, what they cost, and how talking training actually works? We break it all down. "
                 "Every grey is captive-bred, DNA-sexed, and placed with full CITES Appendix I documentation."),
        "first_comment": "", "link": "https://congoafricangreys.com/congo-african-grey-for-sale/",
        "media": "graphics/pinterest-pin-congo-vs-timneh.html (screenshot to PNG) or Maxy still", "status": "draft",
    },
    # ---- 2026-06-12 : Pair eating (diet/care) on FB + Pinterest + IG ----
    {
        "date": "2026-06-12", "time": "09:00", "platform": "Facebook", "title": "",
        "text": ("Breakfast for two. 🥣\n\nThese two share everything — including the good almonds. A big "
                 "part of raising healthy African Greys is the diet they start on: here at C.A.Gs we wean "
                 "every chick onto a varied fresh diet (pellets, sprouted seed, veg, and yes, the occasional "
                 "almond) before they ever go home, so they arrive eating well and confident.\n\n"
                 "Family-raised in Midland, TX since 2014. Captive-bred, DNA-sexed, CITES Appendix I "
                 "documented, shipped nationwide. Curious what a healthy grey diet looks like? Ask us below. 👇\n"
                 "https://congoafricangreys.com/african-grey-parrot-guide/\n#africangrey #congoafricangrey #parrotcare"),
        "first_comment": "", "link": "https://congoafricangreys.com/african-grey-parrot-guide/",
        "media": "African-grey-pair-eating.mp4", "status": "draft",
    },
    {
        "date": "2026-06-12", "time": "20:00", "platform": "Pinterest",
        "title": "What Do African Greys Eat? A Healthy Congo Grey Diet",
        "text": ("Wondering what to feed an African Grey? A healthy diet is one of the biggest factors in a "
                 "long, happy life for a Congo or Timneh grey. Here at C.A.Gs we wean every chick onto a "
                 "varied fresh diet — quality pellets, sprouted seed, vegetables, and limited nuts — before "
                 "placement, so your grey arrives eating well. Learn what we feed, what to avoid (chocolate, "
                 "avocado, and more), and how to transition a new bird. Every grey is captive-bred, DNA-sexed, "
                 "and CITES Appendix I documented."),
        "first_comment": "", "link": "https://congoafricangreys.com/african-grey-parrot-guide/",
        "media": "African-grey-pair-eating.mp4", "status": "draft",
    },
    {
        "date": "2026-06-12", "time": "18:00", "platform": "Instagram", "title": "",
        "text": ("Sharing is caring (mostly). 🥜 These two greys grew up together in our home and it shows. "
                 "The way a grey eats — curious, two-footed, a little dramatic — tells you everything about "
                 "how socialized they are.\n\nHere at C.A.Gs we hand-raise and fully wean every chick on a "
                 "fresh, varied diet before they go home. Family aviary, Midland TX, since 2014 · captive-bred "
                 "· DNA-sexed · CITES Appendix I.\n\nDM us \"AVAILABLE\" to meet our current greys. 👇"),
        "first_comment": IG_TAGS_DIET, "link": "https://congoafricangreys.com/african-grey-parrot-for-sale/",
        "media": "African-grey-pair-eating.mp4", "status": "draft",
    },
    # ---- 2026-06-16 : Flock trust on YouTube (main) + FB ----
    {
        "date": "2026-06-16", "time": "17:00", "platform": "YouTube",
        "title": "Meet Our Hand-Tame African Greys | C.A.Gs Midland, TX",
        "text": ("Step-up, gentle, and curious — this is what \"hand-tame\" actually looks like. Meet four of "
                 "our hand-raised Congo African Greys.\n\nHere at C.A.Gs we're a family aviary in Midland, TX, "
                 "raising African Greys since 2014. Every bird in this video was hand-fed from hatch, fully "
                 "weaned, and socialized to people.\n\nWhen you bring a grey home from us, you get:\n"
                 "• A captive-bred, DNA-sexed bird (Appendix I CITES documentation per bird)\n"
                 "• Avian-vet health certificate + hatch certificate + leg band\n"
                 "• Hand-raised, fully weaned temperament (placed at 12–16 weeks)\n"
                 "• Nationwide shipping — $185 airport pickup or $350 home delivery\n\n"
                 "Looking for an African Grey near you? We ship to all 50 states. "
                 "See who's available → https://congoafricangreys.com/african-grey-parrot-for-sale/\n"
                 "Questions? Info@congoafricangreys.com · +1-281-545-3169\n"
                 "#africangrey #congoafricangrey #africangreyparrot #talkingparrot #parrotbreeder"),
        "first_comment": "", "link": "https://congoafricangreys.com/african-grey-parrot-for-sale/",
        "media": "buy-african-grey-parrot-near-me.mp4", "status": "draft",
    },
    {
        "date": "2026-06-16", "time": "12:00", "platform": "Facebook", "title": "",
        "text": ("This is the moment that tells you everything. 🤝\n\nFour of our greys, and not one hesitates "
                 "to step up to a hand. That's not luck — it's what happens when every chick is hand-fed from "
                 "hatch, fully weaned, and socialized to people before it ever leaves our home.\n\nWe're a "
                 "family aviary here in Midland, TX, raising African Greys since 2014. Every bird goes home "
                 "captive-bred, DNA-sexed, vet-checked, and with full CITES Appendix I + hatch documentation. "
                 "We ship nationwide — $185 airport pickup or $350 home delivery, to all 50 states.\n\n"
                 "If you've been searching for an African Grey \"near me,\" near is wherever you are. "
                 "Come meet our flock → https://congoafricangreys.com/african-grey-parrot-for-sale/\n#africangrey #congoafricangrey #parrotbreeder"),
        "first_comment": "", "link": "https://congoafricangreys.com/african-grey-parrot-for-sale/",
        "media": "buy-african-grey-parrot-near-me.mp4", "status": "draft",
    },
]

FIELDS = ["date", "time", "platform", "title", "text", "first_comment", "link", "media", "status"]

def main():
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for p in POSTS:
            w.writerow(p)
    print(f"wrote {len(POSTS)} rows -> {OUT}")

if __name__ == "__main__":
    main()
