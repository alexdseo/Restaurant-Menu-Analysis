import pandas as pd
# import difflib
from tqdm import tqdm
import string


def preprocessing(menu):
    # Find the restaurant names that are actually the same restaurant
    # These lists can be found via `difflib` which is commented below
    same_names = ['christies', 'cooks', 'country_kitchen', 'dell_alpe', 'drews', 'dukes', 'earls', 'elmans', 'emerils',
                  'henrynlisa', 'kaizen', 'maninis', 'mi_familia', 'quaker_snl', 'rachael_ray', 'rushing_waters',
                  'sail', 'sea_pak', 'sobeys', 'perfect_pita', 'toms', 'whiteys_icecream', 'wild_oats']
    # Restaurants with multiple names
    christies = ['Christie\'s', 'Christie\'s Crispies', 'Christies']
    cooks = ['Cook\'s', 'Cooks']
    country_kitchen = ['Country Kitchen', 'Country Kitchens']
    dell_alpe = ['Dell\' Alpe', 'Dell \' Alpe', 'Dell Alpe']
    drews = ['Drew\'s', 'Drew\'s Organics', 'Drews', 'Organic Drew\'s']
    dukes = ['Duke\'s', 'Dukes']
    earls = ['Earl\'s', 'Earls']
    elmans = ['Elman\'s', 'Elmans']
    emerils = ['Emeril\'s', 'Emeril', 'Emerils']
    henrynlisa = ['Henry & Lisa\'s', 'Henry & Lisa\'s Natural Seafood']
    kaizen = ['Kaizen', 'Kaizen Naturals']
    maninis = ['Manini\'s', 'Maninis']
    mi_familia = ['Mi Familia', 'Mi-Familia']
    quaker_snl = ['Quaker Steak & Lube', 'Quaker Steak & Lube Grocery']
    rachael_ray = ['Rachael Ray', 'Rachael Ray Stock-in-a-box']
    rushing_waters = ['Rushing Waters', 'Rushing Waters Fisheries']
    sail = ['Sail', 'Sail Brand Products']
    sea_pak = ['Sea Pak Shrimp Co.', 'Sea Pak Shrimp Company']
    sobeys = ['Sobey\'s', 'Sobeys']
    perfect_pita = ['The Perfect Pita', 'The Perfect Pita Grocery']
    toms = ['Tom\'s', 'Toms']
    whiteys_icecream = ['Whitey\'s Ice Cream', 'Whitey\'s Ice Cream Grocery']
    wild_oats = ['Wild Oats Marketplace', 'Wild Oats Marketplace Organic', 'Wild Oats Organic', 'Wild Oats']

    # Check if there are any restaurants that have multiple names
    # similar_names = []
    # for name in restaurants:
    #    if len(difflib.get_close_matches(name, restaurants)) >= 2:
    #        print(difflib.get_close_matches(name, restaurants))
    #        similar_names.append(name)

    # Preprocessing part 1: Unify restaurant names that have multiple names
    for i in tqdm(range(len(menu)), desc='Data Preprocessing 1/3'):
        for k in range(len(same_names)):
            if menu['Restaurant Name'][i] in eval(same_names[k]):
                menu['Restaurant Name'][i] = eval(same_names[k] + '[0]')

    # Save all the unique names
    restaurants = menu['Restaurant Name'].unique()

    # Preprocessing part 2: Remove commas in the menu item and reverse the order
    # i.e. Coke, Regular ==> Regular Coke
    for i in tqdm(range(len(menu)), desc='Data Preprocessing 2/3'):
        temp = menu['Original food Item'][i].split(', ')
        temp.reverse()
        temp = ' '.join(temp).translate(str.maketrans('', '', string.punctuation))
        menu['Original food Item'][i] = ' '.join(temp.split())

    # Define new Dataframe to store cleaned dataset
    col_name = ['Restaurant Name', 'Original food Item']
    menu_cleaned = pd.DataFrame(columns=col_name)
    # Group original data by their restaurant name
    menu_t = menu.groupby('Restaurant Name', sort=False)

    # Preprocessing part 3: Concat every menu item for each restaurant to one data
    for i in tqdm(range(len(restaurants)), desc='Data Preprocessing 3/3'):
        t = menu_t.get_group(restaurants[i])
        x = ' '.join(t['Original food Item'].to_list())
        temp = [[restaurants[i], x]]
        temp_df = pd.DataFrame(temp, columns=col_name)
        menu_cleaned = pd.concat([menu_cleaned, temp_df], ignore_index=True)

    return menu_cleaned


if __name__ == '__main__':
    # Read csv file
    df = pd.read_csv('MenuItem.csv')
    # Perform data preprocessing
    df_cleaned = preprocessing(df)
    # Write csv file
    df_cleaned.to_csv('MenuItem_cleaned.csv', encoding='utf-8', index=False)