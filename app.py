from flask import Flask, render_template, request, redirect, url_for
from data.event_info import EVENT_TITLE, EVENT_DESC
from data.options import GROUP_OPTIONS, DIRECTION_OPTIONS
from data.page_text import FORM_HINT, RESULT_TITLE
from data.registrations import DEFAULT_REGISTRATIONS

app = Flask(__name__)

# 内存中保存报名数据（Vercel 无持久存储，使用内存列表）
registrations = list(DEFAULT_REGISTRATIONS)


@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        event_title=EVENT_TITLE,
        event_desc=EVENT_DESC,
        group_options=GROUP_OPTIONS,
        direction_options=DIRECTION_OPTIONS,
        form_hint=FORM_HINT,
    )


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    group = request.form.get("group", "").strip()
    direction = request.form.get("direction", "").strip()
    note = request.form.get("note", "").strip()

    if name and group and direction:
        registrations.append({
            "name": name,
            "group": group,
            "direction": direction,
            "note": note,
        })

    return redirect(url_for("result"))


@app.route("/result")
def result():
    total = len(registrations)

    # 统计各活动方向人数
    direction_count = {}
    for r in registrations:
        d = r["direction"]
        direction_count[d] = direction_count.get(d, 0) + 1

    recent = registrations[-10:][::-1]

    return render_template(
        "result.html",
        result_title=RESULT_TITLE,
        total=total,
        direction_count=direction_count,
        recent=recent,
    )


if __name__ == "__main__":
    app.run(debug=True)
