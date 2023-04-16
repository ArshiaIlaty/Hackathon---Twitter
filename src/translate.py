from deep_translator import GoogleTranslator
import pandas as pd

def translate(text: str):
    to_translate = text
    translated = GoogleTranslator(source='fa', target='en').translate(to_translate)
    print(translated)
    return translated

def run_translate():
    username = 'arshiailaty'
    full_path = './users/' + username + '.csv'
    df = pd.read_csv(full_path)
    # df.columns = ['date', 'name', 'id', 'text', 'target']

    df = df.dropna()
    df = df[df['Tweet_id'] != '[empty]']
    df['transalted'] = df['Content'].apply(lambda x: translate(x))

    df.to_csv('your.csv')

    df['transalted'].to_csv('your.csv')
