import configparser
import os


def analyze():
    parser = configparser.ConfigParser()
    parser.read('./config.ini', encoding='utf-8')
    config = parser['ANALYZE']

    max_searts = int(config.get('MAX_SEARTS'))
    num_parties = int(config.get('NUM_PARTIES'))

    party_names = []
    searts_numbers = []
    votes = []

    log_list = sorted(os.listdir('./log/'))
    with open('./log/'+log_list[-1], mode='r') as f:
        for line in f.readlines():
            party_name, num_searts, vote = line.rstrip('\n').split('-')
            party_names.append(party_name)
            searts_numbers.append(int(num_searts))
            votes.append(int("".join(vote.split(','))))

    print(party_names)
    print(searts_numbers)
    print(votes)


if __name__ == '__main__':
    analyze()
