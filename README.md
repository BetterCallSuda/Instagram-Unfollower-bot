# Instagram-Unfollower-bot
A robust, human-like Instagram unfollow automation script designed with safety mechanisms to minimize detection risks. This tool helps manage your following list by unfollowing users with configurable delays, error handling, and anti-detection patterns.


Key Features:
✅ Human-like interaction patterns (randomized delays, scroll behavior)
✅ Comprehensive error handling (stale elements, intercepts, timeouts)
✅ Configurable safety limits (max unfollows, delay ranges)
✅ Modular architecture following Python best practices
✅ Detailed logging instead of print statements
✅ Explicit XPath selectors with fallback strategies
✅ Modal scrolling for dynamic content loading
✅ Safety-focused defaults (conservative unfollow limits)
🗂️ Project Structure
1234567891011
instagram-unfollower-bot/
├── instagram_bot/               # Core package
│   ├── __init__.py
│   ├── bot.py                   # Main bot logic & InstagramBot class
│   ├── config.py                # Configuration management
│   └── utils.py                 # Helper functions (scrolling, delays)
├── main.py                      # Entry point script
├── requirements.txt             # Dependencies
├── .gitignore                   # Git ignore rules
├── README.md                    # This file

🚀 Installation & Setup
Prerequisites
Python 3.8+
Chrome browser installed
Instagram account (logged-in session recommended)
Steps
Clone the repository:
bash
12
git clone https://github.com/your-username/instagram-unfollower-bot.git
cd instagram-unfollower-bot
Create virtual environment (recommended):
bash
12
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies:
bash
1
pip install -r requirements.txt
Configure your environment:
Rename instagram_bot/config.py.example to instagram_bot/config.py
Update TARGET_ACCOUNT and safety parameters
Configure ChromeDriver path in config.py (see comments)
CRITICAL SAFETY STEP:
Before first run:
Manually log into Instagram in Chrome
Save cookies/session (use browser profile persistence)
Verify you can access https://instagram.com/your_target_account manually
⚙️ Configuration (instagram_bot/config.py)
python
12345678910111213141516
# TARGET ACCOUNT (username only - NO slashes/spaces)
TARGET_ACCOUNT = "ghiliboiz"  # ← CHANGE THIS

# SAFETY LIMITS (ADJUST CONSERVATIVELY)
MAX_UNFOLLOWS_PER_SESSION = 15  # Instagram's soft limit: ~20/hour
MIN_DELAY_BETWEEN_ACTIONS = 10  # Seconds (min)
MAX_DELAY_BETWEEN_ACTIONS = 20  # Seconds (max)
SCROLL_DELAY_MIN = 4            # Seconds
SCROLL_DELAY_MAX = 6            # Seconds


▶️ Usage
bash
1
python main.py
Expected Workflow:
Bot navigates to target account's profile
Opens "Following" list modal
Unfollows users with human-like delays:
Randomized wait between actions (10-20s)
Smooth modal scrolling
Automatic stale element recovery
Stops after reaching MAX_UNFOLLOWS_PER_SESSION
Generates detailed log output
Sample Output:
1234567
[INFO] 2026-01-30 14:22:10 - Navigating to @ghiliboiz profile...
[INFO] 2026-01-30 14:22:16 - Following list modal opened successfully
[INFO] 2026-01-30 14:22:22 - ✓ Unfollowed user_123 (1/15)
[INFO] 2026-01-30 14:22:45 - ✓ Unfollowed travel_blogger (2/15)
[WARNING] 2026-01-30 14:23:10 - Stale element encountered - recovering...
[INFO] 2026-01-30 14:23:18 - ✓ Unfollowed photo_enthusiast (3/15)
[INFO] 2026-01-30 14:26:44 - ✅ Session complete: 15 unfollows performed
🔒 Safety & Best Practices
Recommendation
Why It Matters
Max 15 unfollows/session
Instagram's undocumented limit is ~20/hour; exceeding triggers flags
Run during active hours
Mimics human behavior (9 AM - 8 PM local time)
Never run daily
Allow 48-72 hours between sessions
Use dedicated account
Never automate your primary/personal account
Monitor account
Check for "action blocked" notifications after each session
Respect users
Avoid unfollowing accounts you genuinely engage with
💡 Pro Tip: Combine with manual engagement (likes/comments) on remaining follows to maintain healthy account activity patterns.
🌐 Ethical Considerations
✋ DO NOT use for mass-unfollowing campaigns
✋ DO NOT target accounts that follow you back
✅ DO use to clean inactive/non-reciprocating accounts
✅ DO prioritize authentic relationship building
✅ ALWAYS comply with Instagram's Community Guidelines
🤝 Contributing
Contributions focused on safety improvements are welcome:
Fork the repository
Create feature branch (git checkout -b safe-enhancement)
Add tests for new functionality
Submit pull request with detailed safety rationale
⚠️ PRs that:
Increase unfollow speed/rate
Bypass Instagram protections
Remove safety delays
...will be rejected.
