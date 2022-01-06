import pandas as pd


def clean_animes(animes_df):
  animes_df['score'] = animes_df['score'].astype(str)

  animes_df['synopsis'].fillna('None', inplace=True)
  animes_df['genre'].fillna('None', inplace=True)
  animes_df['episodes'].fillna(0, inplace=True)
  animes_df['score'].fillna('-', inplace=True)
  animes_df['img_url'].fillna('https://i.postimg.cc/fL9WXt0H/Capture.png', inplace=True)

  animes_df['episodes'] = animes_df['episodes'].astype(int)
  return animes_df


animes = pd.read_csv('data/filtered_animes.csv')
animes = clean_animes(animes)


def animes_as_list(target_animes):
    animes_dict = target_animes.T.to_dict()

    anime_list = []
    [anime_list.append(animes_dict[anime]) for anime in animes_dict]

    return anime_list

def get_anime_list(n=20):
    anime_list = animes_as_list(animes)
    return [anime_list[i] for i in range(n)]



def animes_by_seasons(target_animes):
    animes_dict = target_animes.T.to_dict()
    seasons = list(animes['release_date'].astype(int).sort_values(ascending=False).unique())

    seasoned_anime_list = {}
    for season in seasons:
        seasoned_anime_list[season] = []

    for anime in animes_dict:
        season = animes_dict[anime]['release_date']
        season = int(season)
        seasoned_anime_list[season].append(animes_dict[anime])

    return seasoned_anime_list


def get_n_seasoned_animes(seasoned_animes, num_of_animes, target_season=None):
    new_seasoned_animes = {}
    for season in seasoned_animes:
        new_seasoned_animes[season] = []
        for anime in range(num_of_animes):
          try:
            new_seasoned_animes[season].append(seasoned_animes[season][anime])
          except:
            pass

    filtered_seasoned_animes = {}
    for season in new_seasoned_animes:
      if season != target_season:
        filtered_seasoned_animes[season] = new_seasoned_animes[season]
      else:
        break

    return filtered_seasoned_animes

def get_seasoned_animes(season=None, num_of_animes=20, target_season=None):
    seasoned_animes = animes_by_seasons(animes)

    if season:
        return get_n_seasoned_animes({season: seasoned_animes[season]}, num_of_animes)
    else:
        return get_n_seasoned_animes(seasoned_animes, num_of_animes, target_season)



def get_anime(uid):
    uid_mask = animes['uid'] == uid
    anime = animes[uid_mask].iloc[0]
    return anime


def get_animes_by_category(category=None, n=-1):
    category_mask = animes['genre'].str.contains(category, case=False)
    target_animes = animes[category_mask]

    anime_list = animes_as_list(target_animes)

    if n == -1:
        return anime_list
    else:
        return [anime_list[i] for i in range(n)]



def get_recommended(uid):
    pass
