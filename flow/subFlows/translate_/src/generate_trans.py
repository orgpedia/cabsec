import sys
from itertools import zip_longest
from pathlib import Path

import yaml

# ISO 639 language codes
# Bodo/Boro: brx,
LANG_CODES = [
    'as',
    'bn',
    'brx',
    'doi',
    'gu',
    'hi',
    'kn',
    'ks',
    'gom',
    'mai',
    'mni',
    'ml',
    'mr',
    'ne',
    'or',
    'pa',
    'sa',
    'sat',
    'sd',
    'ta',
    'te',
    'ur',
]

LANG_SCRIPT_DICT = {
    'as': 'as',
    'bn': 'bn',
    'brx': 'hi',
    'doi': 'hi',
    'gu': 'gu',
    'hi': 'hi',
    'kn': 'kn',
    'ks': 'ur',
    'gom': 'hi',
    'mai': 'hi',
    'mni': 'mni',
    'ml': 'ml',
    'mr': 'hi',
    'ne': 'hi',
    'or': 'or',
    'pa': 'pa',
    'sa': 'hi',
    'sat': 'sat',
    'sd': 'hi',
    'ta': 'ta',
    'te': 'te',
    'ur': 'ur',
    'en': 'en',
}

TRANSLATIONS_DIR = Path('hand')
STUBS = ['names', 'initials', 'dept', 'dept.words', 'digits', 'role', 'labels', 'ministry']


def split_initials(name):
    name = name.strip()
    if 'Md.' in name:
        name = name.replace('Md.', 'Mohammad')

    if 'Mohd.' in name:
        name = name.replace('Mohd.', 'Mohammad')

    if 'Ch.' in name:
        name = name.replace('Ch.', 'Choudhary')

    if 'Prof.' in name:
        name = name.replace('Prof.', '')

    initials, name_words = [], []
    name_str = ''
    for c, cn in zip_longest(name, name[1:]):
        if c == ' ':
            name_words += [name_str] if name_str else []
            name_str = ''
        elif c.isupper() and (cn.isupper() or cn == ' ' or cn == '.'):
            initials.append(c)
        elif c == '.':
            initials[-1] += '.'
        else:
            name_str += c

    name_words += [name_str] if name_str else []
    return initials, ' '.join(name_words)


def read_yml(yml_path):
    yml_path = Path(yml_path)
    return yaml.load(yml_path.read_text(), Loader=yaml.FullLoader)


def load_translations(trans_dir, stub):
    en_path = Path(trans_dir) / f'{stub}.master.txt'
    en_texts = en_path.read_text().strip().split('\n')

    en_texts_dict = dict((n.strip(), {}) for n in en_texts)
    for (lang, script_lang) in LANG_SCRIPT_DICT.items():
        lang_text_path = Path(trans_dir) / f'{stub}.{lang}.txt'
        if not lang_text_path.exists():
            if stub in ('names', 'digits', 'initials'):
                lang_text_path = Path(trans_dir) / f'{stub}.{script_lang}.txt'
            else:
                print(f'Unable to find file {str(lang_text_path)}')
                continue
        lang_texts = lang_text_path.read_text().rstrip().split('\n')

        assert len(lang_texts) == len(
            en_texts
        ), f'Mismatch {stub} {lang}:{len(lang_texts)} en:{len(en_texts)}'
        for idx, text in enumerate(lang_texts):
            en_texts_dict[en_texts[idx]][lang] = text.strip()

    return en_texts_dict


def read_hierarchy_names(hier_dict):
    def get_children(yml_dict):
        def is_not_child_field(field):
            return field in ["name", "alias"] or field.startswith("_")

        child_fields = [f for f in yml_dict.keys() if not is_not_child_field(f)]
        if child_fields:
            assert len(child_fields) == 1
            return yml_dict[child_fields[0]]
        else:
            return []

    def get_names(yml_dicts):
        if not yml_dicts:
            return []

        names = []
        for yml_dict in yml_dicts:
            child_dicts = get_children(yml_dict)
            names.append(yml_dict['name'])
            names.extend(get_names(child_dicts))
        return names

    h_field_dict = {
        "__department__": "ministries",
        "__role__": "roles",
    }

    h_field = h_field_dict[hier_dict["name"]]
    names = get_names(hier_dict[h_field])
    return names


def process_depts(depts_yml, trans_dict):
    depts_dict = read_yml(depts_yml)
    depts = read_hierarchy_names(depts_dict)

    for dept in depts:
        for d in dept.split():
            if d != 'of' and d.strip(', .') not in trans_dict['dept.words']:
                print('Missing: ', d)

    for dept in depts:
        for lang in ['brx', 'ks', 'sat']:
            lang_dept_words = [
                trans_dict['dept.words'][d.strip(' ,.')][lang]
                for d in dept.split()
                if d not in ('of', '-')
            ]
            lang_dept = ' '.join(lang_dept_words)
            if dept not in trans_dict['dept']:
                print(f'Missing Dept: {dept}')
            else:
                trans_dict['dept'][dept][lang] = lang_dept
    # end for

    result_dict = {}
    for dept in depts:
        if dept not in trans_dict['dept']:
            continue
        trans_dict['dept'][dept]['en'] = dept
        result_dict[dept] = trans_dict['dept'][dept]
    return result_dict


def process_names(names_yml, trans_dict):
    def is_initial(name):
        return name.isupper() or name[-1] == '.'

    names_dict = read_yml(names_yml)
    result_dict = {}
    initials = [], []
    for officer in names_dict['officers']:
        name = officer['name']
        initials, split_name = split_initials(name)

        lang_words_list = []
        for initial in initials:
            clean_initial = initial.rstrip(' .').lstrip(' ')
            initial_words = trans_dict['initials'][clean_initial]
            if '.' in initial:
                initial_lang_words = dict((l, f'{i}.') for (l, i) in initial_words.items())  # noqa
            lang_words_list.append(initial_lang_words)

        if split_name in trans_dict['names']:
            lang_words_list.append(trans_dict['names'][split_name])
        else:
            print(f'* Missing: {split_name}')

        name_lang_dict = {}
        for lang in LANG_CODES:
            lang_words = [twd[lang] for twd in lang_words_list]
            name_lang_dict[lang] = ' '.join(lang_words)

        name_lang_dict['en'] = name
        # result_dict[officer['officer_id']] = name_lang_dict
        result_dict[name] = name_lang_dict
        # pprint.pprint(name_lang_dict)
    # end for
    return result_dict


def process_digits(trans_dict):
    result_dict = {}
    for digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        lang_dict = trans_dict['digits'][str(digit)]
        lang_dict['en'] = str(digit)
        result_dict[digit] = lang_dict
    return result_dict


def process_roles(roles_yml, trans_dict):
    roles_dict = read_yml(roles_yml)
    roles = read_hierarchy_names(roles_dict)

    result_dict = {}
    for role in roles:
        if role not in trans_dict['role']:
            print('Role not found in translations: {role}')
        role_trans_dict = trans_dict['role'][role]
        role_trans_dict['en'] = role
        result_dict[role] = role_trans_dict
    return result_dict


def process_ministry(ministry_yml, trans_dict):
    ministry_dict = read_yml(ministry_yml)
    ministry_infos = ministry_dict['ministries']
    ministries = [m['name'] for m in ministry_infos]

    result_dict = {}
    for ministry in ministries:
        if ministry not in trans_dict['ministry']:
            print('Ministry not found in translations: {ministry}')
        ministry_trans_dict = trans_dict['ministry'][ministry]
        result_dict[ministry] = ministry_trans_dict
    return result_dict


def process_labels(labels_master, trans_dict):
    labels = labels_master.read_text().strip().split('\n')

    result_dict = {}
    for label in labels:
        if label not in trans_dict['labels']:
            print('Label not found in translations: {label}')
        label_trans_dict = trans_dict['labels'][label]
        result_dict[label] = label_trans_dict
    return result_dict


if __name__ == '__main__':
    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    trans_dict = {}
    for stub in STUBS:
        trans_dict[stub] = load_translations(TRANSLATIONS_DIR, stub)
    # end for

    depts_dict = process_depts(input_dir / 'dept.yml', trans_dict)
    names_dict = process_names(input_dir / 'names.yml', trans_dict)

    # digits_dict = process_digits(trans_dict)
    # roles_dict = process_roles(input_dir / 'role.yml', trans_dict)
    # ministry_dict = process_ministry(input_dir / 'ministries.yml', trans_dict)
    # labels_dict = process_labels(TRANSLATIONS_DIR / 'labels.master.txt', trans_dict)

    output_path = output_dir / 'trans.yml'
    output_path.write_text(
        yaml.dump(
            {
                'names': names_dict,
                'dept': depts_dict,
                'digits': trans_dict['digits'],
                'role': trans_dict['role'],
                'labels': trans_dict['labels'],
                'ministry': trans_dict['ministry'],
            }
        )
    )
