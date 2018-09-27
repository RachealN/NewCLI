import click

import requests




prompt_test = "Enter the news source. Options are: BBC, CNN, DAILY-MAIL,ABC"



@click.command()
@click.option('--source', prompt=prompt_test)
def cli(source):
    if source.lower() == 'bbc':
        url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=6ec52193c4974fd68ca3c25e7c33a950&pageSize=10'

    elif source.lower() == 'cnn':
        url = 'https://newsapi.org/v2/top-headlines?sources=cnn&apiKey=6ec52193c4974fd68ca3c25e7c33a950&pageSize=10'

    elif source.lower() == 'daily-mail':
        url = 'https://newsapi.org/v2/top-headlines?sources=daily-mail&apiKey=6ec52193c4974fd68ca3c25e7c33a950&pageSize=10'

    elif source.lower() == 'abc':
        url = 'https://newsapi.org/v2/top-headlines?sources=abc-news&apiKey=6ec52193c4974fd68ca3c25e7c33a950&pageSize=10'

    # elif input('exit') == 'n':
    #     print (exit)
        
    
    else:
        source.lower() != 'bbc', 'cnn', 'daily-mail', 'abc'
        message = print('source not found')
        return message

    news_request = requests.get(url)
    main_dict = news_request.json()
    article_dict = main_dict['articles']

# def new():

#     click.echo("articles")
#     new()

    for articles in article_dict:
        click.echo(click.style('TITLE: ' + articles['title'], fg='red'))
        click.echo(click.style('DESCRIPTION: ' +
                               articles['description'], fg='blue'))
        click.echo(click.style('URL: ' +
                               articles['url'], fg='red'))
        click.echo('\n')
        click.echo(click.wrap_text(articles['description'], 100))
        click.echo('\n')
        click.echo('-' * 100)
        # click.echo('test%s!' % sources)
        cli()
        

def url_exists(url):
    r = requests.get(url)
    if r.status_code == 200:
        return True

    elif r.status_code == 404:
        return False

cli()

