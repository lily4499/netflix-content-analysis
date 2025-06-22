# netflix-content-analysis

---

## 🚀 Project: Netflix Content Analysis & Insight Generation

### 🎯 Business Question:

👉 *What trends can Netflix leverage to optimize their global content strategy?*
👉 *Which genres or content types are popular by region and over time?*
👉 *What is the ideal release strategy for new content?*

---

## 🗂 Final Project Structure:

```
netflix-content-analysis/
│
├── README.md
├── requirements.txt
├── data/
│   └── netflix_titles.csv
├── notebooks/
│   └── 01_netflix_content_analysis.ipynb
├── output/
│   ├── genre_trend.png
│   ├── top_countries.png
│   └── release_trend.png
├── scripts/
│   └── clean_data.py
└── venv/
```

---

# ✅ Step-by-step Guide:

---

### Step 1️⃣ — Setup Project

**Purpose:** Prepare isolated Python environment to avoid version conflicts
**Skills:** CLI, Python venv, Git version control

**CLI:**

```bash
# 1. Create project folder
mkdir netflix-content-analysis
cd netflix-content-analysis

# 2. Initialize Git repo
git init

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# .\venv\Scripts\activate  # Windows

# 4. Create requirements file
touch requirements.txt
```

**requirements.txt**:

```txt
pandas
numpy
matplotlib
seaborn
jupyter
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

---

### Step 2️⃣ — Download & Place Dataset

**Purpose:** Acquire raw data for analysis
**Skill:** Data collection, managing CSV files

**CLI:**

```bash
mkdir data
# Download 'netflix_titles.csv' from Kaggle and place it in ./data
```

---

### Step 3️⃣ — Start Jupyter Notebook

**Purpose:** Interactive EDA
**Skill:** Notebook usage, reproducible analysis

```bash
jupyter notebook
# Create notebook: notebooks/01_netflix_content_analysis.ipynb
```

---

### Step 4️⃣ — Data Cleaning & Exploration

**Purpose:** Ensure data quality for analysis
**Skill:** Python, Pandas, data cleaning best practices

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('../data/netflix_titles.csv')

# Check missing values
df.isnull().sum()

# Fill missing 'country' with 'Unknown'
df['country'] = df['country'].fillna('Unknown')

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'])

# Extract year
df['year_added'] = df['date_added'].dt.year

# Example save cleaned data (optional)
df.to_csv('../output/cleaned_netflix_titles.csv', index=False)
```

---

### Step 5️⃣ — Exploratory Data Analysis (EDA)

**Purpose:** Find insights from the data
**Skill:** Pandas, Numpy, visualization (Matplotlib, Seaborn)

#### 5.1 Top content countries:

```python
import matplotlib.pyplot as plt
import seaborn as sns

top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title('Top 10 Content-Producing Countries on Netflix')
plt.xlabel('Number of Titles')
plt.savefig('../output/top_countries.png')
plt.show()
```

#### 5.2 Genre trends:

```python
# Split genres
df['genre_list'] = df['listed_in'].str.split(',')

# Explode genres
df_exploded = df.explode('genre_list')
df_exploded['genre_list'] = df_exploded['genre_list'].str.strip()

top_genres = df_exploded['genre_list'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title('Top 10 Genres on Netflix')
plt.xlabel('Number of Titles')
plt.savefig('../output/genre_trend.png')
plt.show()
```

#### 5.3 Content release trend:

```python
release_trend = df['year_added'].value_counts().sort_index()

plt.figure(figsize=(12,6))
sns.lineplot(x=release_trend.index, y=release_trend.values, marker='o')
plt.title('Content Added to Netflix Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.savefig('../output/release_trend.png')
plt.show()
```

---

### Step 6️⃣ — Insight Generation & Recommendations

**Purpose:** Translate analysis into actionable insights
**Skill:** Critical thinking, storytelling, business acumen

#### Example insights:

* 📈 Netflix has steadily increased content from India and Korea in the past 3 years. Opportunity: Double down on Asian content markets.
* 🎭 Top genre is "Dramas," but **under-served segments** like "Documentaries" are trending upwards — potential growth market.
* 🗓️ Most content drops in Q4 — opportunity to spread releases more evenly for retention.

---

### Step 7️⃣ — Automate / Refactor

**Purpose:** Modularize for reusability
**Skill:** Python scripting, version control

```bash
mkdir scripts
touch scripts/clean_data.py
```

**scripts/clean\_data.py** (example):

```python
import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path)
    df['country'] = df['country'].fillna('Unknown')
    df['date_added'] = pd.to_datetime(df['date_added'])
    df['year_added'] = df['date_added'].dt.year
    return df
```

---

### Final CLI Wrap-up:

```bash
# Stage files
git add .
git commit -m "Initial Netflix Content Analysis project"

# Create GitHub repo and push
# Example using GitHub CLI
gh repo create netflix-content-analysis --public --source=. --push
```

---

## 🚀 Summary: Skills Demonstrated

| Step                       | Skill demonstrated                       |
| -------------------------- | ---------------------------------------- |
| Setup project              | CLI, Git, Python environment             |
| Data download & management | Data acquisition, CSV management         |
| Notebook usage             | Jupyter, reproducible analysis           |
| Data cleaning              | Pandas, missing value handling           |
| EDA                        | Pandas, Numpy, Matplotlib, Seaborn       |
| Insight generation         | Critical thinking, business storytelling |
| Automation & scripting     | Python scripting, reusable code          |
| Version control            | Git workflow                             |

---




