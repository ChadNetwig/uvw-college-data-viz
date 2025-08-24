# 🎓 UVW College — Data Visualization Project

Data visualizations and analysis created for UVW College to identify demographic factors associated with earning ≤$50,000 vs >$50,000 (U.S. Census "Adult" dataset). Delivered as part of CSE 578 (Data Visualization). Python analysis code is included; Tableau was used for some production-quality visuals.

---

## 📖 Overview

UVW College wants to use salary as a key demographic (threshold = $50,000) to build marketing profiles and target enrollment outreach. This project analyzes the U.S. Census “Adult” dataset to explore how attributes — such as education, age, occupation, marital status, sex, native country, capital gain, and hours-per-week — relate to the income threshold.

The analysis follows visualization best practices (legibility, labeling, color, and aspect ratio) and produces one univariate and four multivariate visualizations that answer targeted user stories for the marketing team. All code used to generate the Python visualizations is contained in `Final-report-uvw-analysis.py`. Tableau-produced charts are exported and included as static images in `/assets`.

### The project delivers:
- One univariate visualization and four multivariate visualizations, each addressing a **user story** shaped with the marketing team in mind.
- Insights into how key demographics correlate with the $50K income threshold, enabling tailored enrollment strategies.
- Visualizations designed according to best practices (legibility, labeling, aspect ratio, color, and annotation) to ensure they are both **instructive and actionable**.

By providing these insights, the UVW College marketing team can design outreach campaigns aligned to the needs of specific demographics (e.g., education level or age/occupation segments), ultimately helping them increase enrollment while allocating marketing resources more effectively.

---

## ✨ Key Features

- Exploratory data cleaning and preprocessing (handling missing `?` entries, grouping categories).
- Univariate and multivariate visualizations addressing five user stories (education, age & occupation, marital status & sex, education-num & hours-per-week, capital gain vs age & country).
- Visual design choices: grouped categories, annotated bar counts, color palettes optimized for contrast and readability.
- Outputs suitable for the marketing team and a separate Python code PDF for submission.

---

## 🖼️ Screenshots

**1) Impact of Education Level on Income**  
Shows counts by education level separated by income (<=50K vs >50K).  
<img src="./assets/chart-1-bar chart-education vs income.png" alt="Education vs Income" width="500"/>

**2) Impact of Age and Occupation on Income**  
Stacked bar showing occupation breakdown by age-groups and income. Useful to find occupations where younger/older groups skew above/below $50K.  
<img src="./assets/chart-2-age & occupation vs income.png" alt="Age and Occupation vs Income" width="500"/>

**3) Distribution of Income Across Marital Status and Sex**  
A mosaic/treemap-style chart showing combined effect of marital status and sex on income buckets. Highlights big segments (e.g., married-civ-spouse) and their income skew.  
<img src="./assets/chart-3-Distribution of Income Across Marital Status and Sex.png" alt="Marital Status and Sex vs Income" width="500"/>

**4) Education-Num & Hours-per-week vs Income**  
Line chart aggregating weekly hours across education-num levels and income buckets — helps detect workload patterns correlated with higher earnings.  
<img src="./assets/chart-4-Distribution of Aggregated Weekly Work Hours Across Education Number and Income.png" alt="Education-Num and Hours vs Income" width="500"/>

**5) Avg Capital-Gain vs Avg Age by Native Country and Income**  
Scatterplot with regression annotations showing how capital gain varies with age and country groups (split by income). Useful for identifying country/age cohorts with high capital gains.  
<img src="./assets/chart-5-Distribution of Average Capital-Gain Across Average Age-Native Country-and Income.png" alt="Capital Gain vs Age and Country" width="500"/>

**6) Notebook / README snippet (markdown code block example)**  
A screenshot showing where markdown can "jump out" if triple backticks are not closed — included to remind contributors to close code fences.  
<img src="./assets/8d05fb5a-36d8-4798-8273-1a66577a867c.png" alt="Markdown snippet reminder" width="500"/>

---

## 🧰 Technologies Used

- Python 3.x — Pandas, Matplotlib, Seaborn, statsmodels  
- Tableau — high-quality multivariate visuals  
- Jupyter Notebook — development & exploratory plotting  
- U.S. Census / UCI Adult dataset

---

## 📂 Project Structure

Key files in this repository:

- `Final-report-uvw-analysis.py` — primary Python analysis script (data cleaning, grouping, and Matplotlib/Seaborn plots).  
- `ChadNetwig_CSE 578_Course Project Final Report.pdf` — final written report.  
- `/assets/` — exported visualization PNGs created in Tableau or Matplotlib.  
- Raw data: `adult.data.txt`, `adult.names.txt` (download from UCI and place in repo root).

---

## ⚙️ How to Build and Run

1. **Install dependencies** (recommended in a virtualenv):
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows PowerShell
```

pip install pandas matplotlib seaborn statsmodels

2. **Place data files**
Ensure adult.data.txt and adult.names.txt are present in the repo root.

3. **Run analysis**
**Jupyter recommended:**
```bash
jupyter notebook Final-report-uvw-analysis.py
```

** Or run as script:
```bash
python Final-report-uvw-analysis.py
```

### ⚠️ Important note — running notebook cells in a plain `.py` script

If you copy/paste notebook-oriented cells (which often rely on the Jupyter display) into a standalone `.py` script, make sure Matplotlib uses a file (non-interactive) backend — or remove the notebook magic (`%matplotlib inline`). Otherwise your script may fail to display or hang on headless systems.

**Recommended approaches**

1. **Set a non-interactive backend (before importing `pyplot`)**
```python
import matplotlib
matplotlib.use('Agg')   # non-interactive backend that writes files
import matplotlib.pyplot as plt

# create and save figure
plt.plot([1,2,3], [4,5,6])
plt.xlabel('x'); plt.ylabel('y')
plt.savefig('figure.png')   # write to file instead of display
```

2 **Remove Jupyter magic**
Delete any lines like:
```text
%matplotlib inline
```

from the .py script. These are Jupyter-only “magic” commands and will cause syntax errors in plain Python.

3. **Conditional backend selection (useful for headless servers)**
```bash
import os
if os.environ.get('DISPLAY', '') == '':
    # no X11 display — choose file backend
    import matplotlib
    matplotlib.use('Agg')

import matplotlib.pyplot as plt
```

4. **If you want an interactive display when available**
```python
import matplotlib.pyplot as plt

# show the plot only when running interactively
plt.plot([1,2,3], [4,5,6])
plt.savefig('figure.png')   # always save
if os.environ.get('DISPLAY', ''):
    plt.show()              # show on systems with a display
```

### 📌 Summary

Either remove `%matplotlib inline` when converting notebook code to a script **or** set a non-interactive backend (e.g., `Agg`) before importing `matplotlib.pyplot`, and use `plt.savefig()` to persist figures. This ensures your script runs correctly in both notebook and non-notebook environments.

---

## 📊 Conclusion

This project successfully analyzed the U.S. Census “Adult” dataset to identify demographic attributes influencing income levels with respect to the $50K threshold. By creating one univariate and four multivariate visualizations, the analysis provided UVW College’s marketing team with actionable insights into education, age, occupation, marital status, sex, native country, capital gain, and weekly work hours.

The findings highlight clear demographic trends:
- High school graduates and individuals with “some college” form the largest ≤$50K segments.  
- Married-civ-spouse males dominate both income categories, while never-married adults form another large ≤$50K group.  
- Occupations such as admin-clerical, craft-repair, other-service, and sales show strong ≤$50K representation across ages 21–50.  
- Weekly work hours between education numbers 8–11 are associated with disproportionately high total hours in the ≤$50K group.  
- Average capital gains are higher in specific country groups (e.g., Asia, Middle East) for younger age brackets in the >$50K group.

For UVW College, these results provide a **data-driven foundation for marketing decisions**. Enrollment strategies can now be tailored to specific demographics by adjusting tuition, program delivery, and messaging to match the needs and constraints of each group. This alignment of demographic insights with institutional goals supports UVW’s overarching mission: to **increase student enrollment through informed, targeted outreach**.

---

## ⚠️ Important Notes

- **Data cleaning:** The dataset contains `?` values for several categorical fields; those are handled in the script (replaced/aggregated).  
- **Category grouping:** Education and native-country are aggregated for readability (per the design objective).  
- **Reproducibility:** The Python script reads local files — confirm the `adult.data.txt` and `adult.names.txt` files exist and are named correctly.  
- **Markdown caution:** When showing shell or code in the README, wrap it with triple backticks (for example ```bash or ```python) and **close** the block with matching triple backticks to avoid rendering issues.  

---

## 📝 License

This project is provided for **educational and portfolio use** under the **MIT License**.  
If you reuse major parts for academic submission, cite appropriately.

