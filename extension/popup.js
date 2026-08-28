document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('analyze-btn');
    const btnText = document.getElementById('btn-text');
    const btnSpinner = document.getElementById('btn-spinner');
    const resultsSection = document.getElementById('results-section');

    // Auto-fill from LeetCode
    if (typeof chrome !== 'undefined' && chrome.tabs) {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            const activeTab = tabs[0];
            if (activeTab.url && activeTab.url.includes("leetcode.com/problems/")) {
                chrome.scripting.executeScript({
                    target: { tabId: activeTab.id },
                    func: () => {
                        let problemText = "";
                        // Try to get LeetCode problem description
                        const descEl = document.querySelector('[data-track-load="description_content"]') || document.querySelector('.elfjS') || document.querySelector('meta[name="description"]');
                        if (descEl) {
                            problemText = descEl.content || descEl.innerText;
                        }
                        
                        let codeText = "";
                        // Try to get Monaco editor lines
                        const lineNodes = document.querySelectorAll('.view-line');
                        if (lineNodes.length > 0) {
                            codeText = Array.from(lineNodes).map(line => line.textContent).join('\n');
                        }
                        return { problem: problemText, code: codeText };
                    }
                }, (results) => {
                    if (results && results[0] && results[0].result) {
                        const data = results[0].result;
                        if (data.problem) document.getElementById('problem').value = data.problem;
                        if (data.code) document.getElementById('code').value = data.code;
                    }
                });
            }
        });
    }

    analyzeBtn.addEventListener('click', async () => {
        const language = document.getElementById('language').value;
        const problem = document.getElementById('problem').value;
        const code = document.getElementById('code').value;

        if (!problem || !code) {
            alert("Please enter both a problem statement and source code.");
            return;
        }

        // 1. Change button state
        btnText.textContent = 'Analyzing...';
        btnSpinner.classList.remove('hidden');
        analyzeBtn.disabled = true;
        analyzeBtn.classList.add('opacity-80', 'cursor-not-allowed');
        resultsSection.classList.add('hidden-result');
        resultsSection.style.display = 'none';

        try {
            // 2. Fetch data from backend
            const response = await fetch('https://leetcode-code-anaylzer.vercel.app/api/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    problem_statement: problem,
                    source_code: code,
                    language: language
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            // 3. Populate data
            document.getElementById('score-display').innerText = `${data.overall_score}/10`;
            document.getElementById('score-circle').setAttribute('stroke-dasharray', `${data.overall_score * 10}, 100`);
            
            document.getElementById('correctness-display').innerText = data.correctness_assessment;
            document.getElementById('time-complexity-display').innerText = data.time_complexity;
            document.getElementById('space-complexity-display').innerText = data.space_complexity;
            document.getElementById('readability-display').innerText = data.readability_feedback;

            const populateList = (id, items) => {
                const list = document.getElementById(id);
                list.innerHTML = '';
                if (items && items.length > 0) {
                    items.forEach(item => {
                        const li = document.createElement('li');
                        li.innerText = item;
                        list.appendChild(li);
                    });
                } else {
                    list.innerHTML = '<li>None</li>';
                }
            };

            populateList('issues-list', data.detected_issues);
            populateList('optimizations-list', data.optimization_recommendations);
            populateList('modularity-list', data.modularity_recommendations);
            populateList('alternatives-list', data.alternative_algorithms);

            // 4. Reveal Results
            resultsSection.style.display = 'flex';
            resultsSection.classList.remove('hidden-result');
            
            requestAnimationFrame(() => {
                resultsSection.classList.add('fade-in');
            });
            
            resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });

        } catch (error) {
            alert("Error analyzing code. Is the backend running? " + error);
        } finally {
            // 5. Reset button
            btnText.textContent = 'Analyze Code';
            btnSpinner.classList.add('hidden');
            analyzeBtn.disabled = false;
            analyzeBtn.classList.remove('opacity-80', 'cursor-not-allowed');
        }
    });
});
