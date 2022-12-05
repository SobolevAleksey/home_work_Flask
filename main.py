from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def page_all_candidates():
    """
    :return: главную страничку со всеми кандидатами и ссылкой на их страницу.
    """
    candidates = utils.load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:x>")
def page_candidate_by_id(x):
    """
    :param x: id кандидата
    :return: страницу кандидата по id
    """
    candidate = utils.get_candidate(x)
    if len(candidate) == 0:
        return "Такого кандидата нет"

    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search_candidate(candidate_name):
    """
    :param candidate_name: Имя кандидата.
    :return: количество кандидатов по имени и ссылки на их страницы
    """
    candidates = utils.get_candidates_by_name(candidate_name)
    count = len(candidates)
    if len(candidates) == 0:
        return "Такого кандидата нет"
    return render_template("search.html", count=count, candidates=candidates)


@app.route("/skill/<skill_name>")
def candidate_skills(skill_name):
    """
    :param skill_name: умения кандидатов
    :return: всех кандидатов у которых есть skill_name, и ссылки на их странички
    """
    candidates = utils.get_candidates_by_skill(skill_name)
    count = len(candidates)
    if len(candidates) == 0:
        return "Такого кандидата нет"
    return render_template("search.html", count=count, candidates=candidates)


if __name__ == "__main__":
    app.run()
