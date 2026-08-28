# LeetCode AI Code Analyzer

An AI-powered Chromium browser extension designed to act as your personal coding assistant and reviewer. When you're stuck on a LeetCode problem or want to know how your solution stacks up, this extension provides instant, highly-structured feedback directly in your browser.

**Live Backend API**: (https://leetcode-code-anaylzer.vercel.app/)

## Features

*   **Native LeetCode Integration:** Automatically scrapes the problem description and your code from the active LeetCode tab. No copy-pasting required!
*   **Deep Code Analysis:** Powered by the Gemini AI model, the analyzer provides insights into:
    *   Overall Score (out of 10)
    *   Correctness & Edge Cases
    *   Time & Space Complexity (Big-O)
    *   Readability Feedback
    *   Optimization & Modularity Recommendations
    *   Alternative Algorithms

## How to Install and Use (Developer Mode)

Since this extension interacts with your active browser tabs, you can easily load it into Google Chrome, Microsoft Edge, or Brave by following these steps:

1.  **Clone or Download this repository** to your local machine.
2.  Open your browser and navigate to the Extensions page:
    *   Chrome: `chrome://extensions/`
    *   Edge: `edge://extensions/`
3.  Turn on **"Developer mode"** (usually a toggle in the top right corner).
4.  Click the **"Load unpacked"** button.
5.  Select the **`extension`** folder located inside this repository.
6.  *Optional:* Pin the extension to your toolbar for easy access!

### Testing it out:
1.  Navigate to any problem on [LeetCode](https://leetcode.com/problemset/all/).
2.  Open the extension popup from your toolbar.
3.  Watch as your problem statement and code are automatically filled in!
4.  Click **"Analyze Code"** to get your AI evaluation.

## Architecture

*   **Frontend:** Vanilla HTML, CSS (Tailwind), and JS inside a Manifest V3 Chrome Extension architecture.
*   **Backend:** Python FastAPI server hosted on Vercel.
*   **AI Engine:** Google Gemini SDK (`gemini-3.6-flash`).
