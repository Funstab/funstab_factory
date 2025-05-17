<!-- README.md – Funstab Factory -->
<p align="center">
  <img src="https://img.buymeacoffee.com/button-api/?text=Buy&nbsp;me&nbsp;a&nbsp;coffee&emoji=&slug=funstab&button_colour=FFDD00&font_colour=000000&font_family=Inter&outline_colour=000000&coffee_colour=ffffff" alt="Buy Me A Coffee">
</p>

# Funstab Factory ☕️📈🎬  
**Your always-on, server-hosted clip factory** — it hunts trending topics, grabs legal footage, writes a punchy script, generates voice-over, and renders a 60-second, caption-ready 9 × 16 video every 30 minutes.

> **Status**: early proof-of-concept. Google-trend scraping is under repair, Reddit front-page scraping works today.  
> **License**: *All Rights Reserved* – look, learn, don’t reuse without permission.

---

## What it does 🚀
| Stage | Action | Tech |
|-------|--------|------|
| 1. Trend Hunt | Fills a backlog with fresh topics (Reddit r/news + Google Trends feed). | `pytrends`, `feedparser`, `requests`, `sqlite-utils` |
| 2. Asset Fetch | Pulls 3 royalty-free vertical clips per topic. | Pexels API (fallback to YouTube CC) |
| 3. Story Engine | Writes **hook + 3 facts + CTA** JSON. | OpenAI `gpt-4o-mini` |
| 4. Video Edit | Rescales, concatenates, colour-bumps, adds ElevenLabs voice-over, exports 1080 × 1920 MP4. | MoviePy, FFmpeg, ElevenLabs TTS |
| 5. (Opt.) Upload | Drops draft straight into TikTok Drafts; YouTube Shorts & Reels coming. | `tiktok-uploader` CLI |
| 6. Scheduler | Windows Task Scheduler fires every 30 min. | `cron_loop.bat` |

All raw files auto-prune; finished clips land in **`storage/ready/`** ready for drag-and-drop (or automatic upload).

---

## Folder layout  📂

C:\funstab_factory
 ├─ pipeline\              # Python modules (trend_hunt, asset_fetch…)
 ├─ storage\
 │   ├─ backlog.db         # SQLite queue
 │   ├─ raw\{topic}\       # temp clips + script.json + vo.mp3
 │   └─ ready\             # final MP4s
 ├─ .env                   # ← add your API keys here (never commit!)
 └─ LICENSE                # All Rights Reserved

## Contributing 🤝

Pull requests welcome for bug fixes only; feature PRs require prior e-mail approval.
Commercial forks / redistributions are strictly forbidden under the current license.

**E-mail** | contact@najjacomputers.be
**Donate** | https://buymeacoffee.com/funstab

Copyright © 2025 NAJJA COMPUTERS

Funstab Factory is provided “AS IS” without warranty.  
See LICENSE for full terms. Commercial use is prohibited.

