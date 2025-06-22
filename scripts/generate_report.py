import pandas as pd

# Load data
df = pd.read_csv('data/netflix_titles.csv')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = df['date_added'].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['genre_list'] = df['listed_in'].str.split(',')

# Insights
type_counts = df['type'].value_counts()
top_country = df['country'].value_counts().head(5)
df_exploded = df.explode('genre_list')
df_exploded['genre_list'] = df_exploded['genre_list'].str.strip()
top_genres = df_exploded['genre_list'].value_counts().head(5)

# Generate text report
with open('output/stakeholder_report.md', 'w') as f:
    f.write("# 📊 Netflix Content Insights Report\n\n")
    f.write("## Content Type Trends:\n")
    f.write(f"- TV Shows: {type_counts.get('TV Show', 0)}\n")
    f.write(f"- Movies: {type_counts.get('Movie', 0)}\n\n")
    
    f.write("## Top Content-Producing Countries:\n")
    for country, count in top_country.items():
        f.write(f"- {country}: {count}\n")
    f.write("\n")
    
    f.write("## Top Genres:\n")
    for genre, count in top_genres.items():
        f.write(f"- {genre}: {count}\n")
    f.write("\n")
    
    f.write("## Recommendations:\n")
    f.write("- Expand TV Show content (binge-friendly)\n")
    f.write("- Increase localized content for emerging markets\n")
    f.write("- Leverage Docuseries and Reality TV\n")
    f.write("- Improve metadata quality\n\n")
    
    f.write("_Generated automatically via Python script._\n")

