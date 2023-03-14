import csv
import subprocess
import csv
from datetime import datetime

file_path = 'test.csv'


def parse_csv(file_path):
    data = []
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def run_git_command(command):
    return subprocess.check_output(['git'] + command.split()).decode('utf-8')


def get_commits():
    commit_hashes = run_git_command('rev-list --all').splitlines()
    commits = []
    for commit_hash in commit_hashes:
        timestamp = run_git_command(f'show -s --format=%ct {commit_hash}').strip()
        date = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
        data = parse_csv('test.csv')
        commits.append({'timestamp': date, 'data': data})
    return commits


commits = get_commits()


def export_csv(file_path, data):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['city', 'temperature', 'timestamp'])
        for commit in data:
            for row in commit['data']:
                writer.writerow([row['city'], row['temperature'], commit['timestamp']])


export_csv('data_history.csv', commits)