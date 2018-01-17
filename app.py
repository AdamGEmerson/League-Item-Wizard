import json
from requests import get
from bs4 import BeautifulSoup

data = json.load(open('championdata.json'))
cdata = data['data']


def generate_url(champ):
    url = 'http://champion.gg/champion/' + champ
    return url


def generate_builds(url):
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    build_wrappers = soup.find_all('div', class_='build-wrapper')
    champ_builds = []
    block = {}
    block['items'] = []

    for build in build_wrappers:
        block = {}
        block['items'] = []
        build_items = build.find_all('img')
        for item in build_items:
            block['items'].append({'id': item['data-id'], 'count': 1})
        if build == build_wrappers[0]:
            block['type'] = "Most Frequent Build"
        elif build == build_wrappers[1]:
            block['type'] = "Highest Win Rate Build"
        elif build == build_wrappers[2]:
            block['type'] = "Starters"
        else:
            break

        champ_builds.append(block)
    champ_builds.insert(0, champ_builds.pop(2))

    return champ_builds


def generate_json(cdata, consumables=True):

    for key, value in cdata.iteritems():
        name = value['name']
        key = value['key']
        champ_id = value['id']
        print("Working on Items for {}".format(name))
        url = generate_url(champ_id)
        builds = generate_builds(url)

        output = {}
        output['title'] = "{} Items".format(name)
        output['associatedMaps'] = [11, ]
        output['associatedChampions'] = [int(key), ]
        output['blocks'] = builds

        if consumables:
            consume_items = {}
            consume_items['items'] = []
            consume_items['items'].append({'id': '2003', 'count': 1})
            consume_items['items'].append({'id': '2055', 'count': 1})
            consume_items['items'].append({'id': '2140', 'count': 1})
            consume_items['items'].append({'id': '2138', 'count': 1})
            consume_items['items'].append({'id': '2139', 'count': 1})
            consume_items['type'] = "Consumables"
            output['blocks'].append(consume_items)

        with open('item_sets/{}.json'.format(name), 'w') as outfile:
            json.dump(output, outfile)

if __name__ == '__main__':
    generate_json(cdata)
