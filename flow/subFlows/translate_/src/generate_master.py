# This is used at the begining to generate the master
# Afterwords the master is manually updated

import sys
from pathlib import Path

import yaml
from more_itertools import flatten, partition


def read_yml(yml_path):
    assert yml_path.suffix.lower() in ('.yml', '.yaml')
    yml_path = Path(yml_path)
    return yaml.load(yml_path.read_text(), Loader=yaml.FullLoader)


def process_names(names_yml, output_path):
    def is_initial(name):
        return name.isupper() or name[-1] == '.'

    names_dict = read_yml(names_yml)
    names = [o['name'] for o in names_dict['officers']]

    initials, no_initials = [], []
    for name in names:
        n_noinitials, n_initials = partition(is_initial, name.split())
        n_noinitials, n_initials = list(n_noinitials), list(n_initials)
        initials.extend(n_initials)
        no_initials.append(' '.join(n_noinitials))
        # print(f'{name}: {" ".join(n_noinitials)}')
    # end for

    output_path = output_dir / 'names.master.txt'
    if output_path.exists():
        pass
    else:
        output_path.write_text('\n'.join(no_initials))


depts_trlit = (
    "Raj=Homoeopathy=Bengal=Unani=Kashmir=Jammu=Siddha=Ganga="
    "Ayurveda=Petroleum=Naturopathy=Non-Ferrous=Panchayati=Yoga"
)


def process_depts(depts_yml, output_dir):
    dept_dict = read_yml(depts_yml)
    depts = [d['name'] for d in dept_dict['ministries']]
    depts += [dd['name'] for d in dept_dict['ministries'] for dd in d.get('departments', [])]

    output_path = output_dir / 'dept.master.txt'
    if output_path.exists():
        pass
    else:
        output_path.write_text('\n'.join(depts))

    dept_words = set(flatten(d.replace(',', '').split() for d in depts))

    ignore_words = depts_trlit.split('=') + ['of', 'the']
    dept_words = sorted(d for d in dept_words if d not in ignore_words)

    output_words_path = output_dir / 'dept.words.master.txt'
    if output_words_path.exists():
        pass
    else:
        output_words_path.write_text('\n'.join(dept_words))


if __name__ == '__main__':

    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    # process_names(input_dir / 'names.yml', output_dir)
    # process_depts(input_dir / 'dept.yml', output_dir)
    # process_roles(input_dir / 'role.yml', output_dir)
