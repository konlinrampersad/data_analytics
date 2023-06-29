declaration_of_hr = {}

with open('un_declaration_hr_text_data.txt', 'r') as file:
    content = file.read()
    articles = content.split('Article')

    for article in articles[1:]:
        article_num, article_content = article.split('\n', 1)
        declaration_of_hr[f'Article {article_num.strip()}'] = article_content.strip()

# Print the declaration
for article, content in declaration_of_hr.items():
    print(f"{article}\n{content}\n")
