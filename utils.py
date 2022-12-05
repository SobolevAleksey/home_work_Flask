import json


def load_candidates_from_json():
    """
    :return: Список кондидатов
    """
    with open("candidates.json", encoding="utf-8") as file:
        return json.load(file)


def get_candidate(candidate_id):
    """
    :param candidate_id:
    :return: возвращает словарь кондидата по его id
    """
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    :param candidate_name:
    :return: Возвращает список с кандидатами по candidate_name
    """
    candidates_by_name = []
    for candidate in load_candidates_from_json():
        if candidate_name.lower() in candidate['name'].lower().split(" "):
            candidates_by_name.append(candidate)

    return candidates_by_name


def get_candidates_by_skill(skill_name):
    """
    :param skill_name:
    :return: Возвращает список с кандидатами по skill_name
    """
    candidates_by_skills = []
    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate['skills'].lower().split(", "):
            candidates_by_skills.append(candidate)

    if len(candidates_by_skills) > 0:
        return candidates_by_skills
    else:
        return "Такого кандитата нет"
