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

    expected_party = []
    for _ in range(max_searts-sum(searts_numbers)):
        next_index = sorted(zip(range(num_parties), [votes[j]/(searts_numbers[j]+1) for j in range(num_parties)]), key=lambda x: -x[1])[0][0]
        expected_party.append(party_names[next_index])
        searts_numbers[next_index] += 1

    print(expected_party)


if __name__ == '__main__':
    analyze()
