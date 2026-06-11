# 班级活动报名与统计网页

> 第15周实验课小组协作项目 · Flask 动态网页 · Vercel 部署

## 项目简介

本项目是一个基于 Flask 的班级活动报名网页，支持：

- **首页**：填写姓名、小组、活动方向、一句话说明并提交报名
- **结果页**：实时显示报名总人数、各活动方向人数及最近报名列表

---

## 五人分工

| 角色 | 分支名 | 负责文件 | 对应 Issue |
|------|--------|----------|-----------|
| **组长** | `main` | `README.md`、Vercel 部署 | — |
| 组员 A | `member-a-event-info` | `data/event_info.py` | Issue #1 |
| 组员 B | `member-b-options` | `data/options.py` | Issue #2 |
| 组员 C | `member-c-page-text` | `data/page_text.py` | Issue #3 |
| 组员 D | `member-d-sample-data` | `data/registrations.py` | Issue #4 |

> **重要规则**：每位组员**只改自己负责的 data 文件**，不修改 `app.py`、`templates/` 或 `static/`。

---

## 项目文件结构

```
class_event_signup/
├── app.py                  # Flask 程序入口
├── requirements.txt        # Python 依赖
├── vercel.json             # Vercel 部署配置
├── README.md               # 项目说明（本文件）
├── data/
│   ├── event_info.py       # 活动标题和说明（组员 A 修改）
│   ├── options.py          # 小组和活动方向选项（组员 B 修改）
│   ├── page_text.py        # 表单提示和结果页标题（组员 C 修改）
│   └── registrations.py   # 默认报名记录（组员 D 修改）
├── templates/
│   ├── index.html          # 首页表单
│   └── result.html         # 统计结果页
└── static/
    └── style.css           # 网页样式
```

---

## 本地运行

```powershell
# 进入项目根目录
cd class_event_signup

# 创建并激活虚拟环境
python -m venv .venv
.\.venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 启动
python app.py
```

打开浏览器访问：
- 首页：http://127.0.0.1:5000
- 结果页：http://127.0.0.1:5000/result

---

## GitHub 协作流程

### 组长操作步骤

1. 在 GitHub 创建空仓库 `class_event_signup`（不要自动生成 README）
2. 在本地初始化并推送：

```powershell
git init
git branch -M main
git add .
git commit -m "initial Flask event signup app"
git remote add origin https://github.com/你的用户名/class_event_signup.git
git push -u origin main
```

3. 在 GitHub 创建 4 个 Issue（内容见下方）
4. 等组员 Fork → 创建分支 → 提交 PR
5. 审核每个 PR 的 Files changed，写 review/comment 后 merge
6. 所有 PR 合并后部署到 Vercel

### 4 个 Issue 内容

#### Issue #1：修改活动标题和说明
```
## 任务说明
请在你的 Fork 仓库中，创建分支 member-a-event-info，
修改 data/event_info.py 中的 EVENT_TITLE 和 EVENT_DESC，
改为你们小组自定义的活动标题和说明文字。
完成后提交 Pull Request，在 PR 描述中注明"完成 Issue #1"。
```

#### Issue #2：修改小组选项和活动方向
```
## 任务说明
请在你的 Fork 仓库中，创建分支 member-b-options，
修改 data/options.py 中的 GROUP_OPTIONS 和 DIRECTION_OPTIONS，
改为你们班级实际的小组名称和活动方向列表。
完成后提交 Pull Request，在 PR 描述中注明"完成 Issue #2"。
```

#### Issue #3：修改表单提示和结果页标题
```
## 任务说明
请在你的 Fork 仓库中，创建分支 member-c-page-text，
修改 data/page_text.py 中的 FORM_HINT 和 RESULT_TITLE，
改为你们小组自定义的提示语和标题。
完成后提交 Pull Request，在 PR 描述中注明"完成 Issue #3"。
```

#### Issue #4：修改默认报名记录
```
## 任务说明
请在你的 Fork 仓库中，创建分支 member-d-sample-data，
修改 data/registrations.py 中的 DEFAULT_REGISTRATIONS，
加入 3~5 条有意义的示例报名记录（使用虚构姓名即可）。
完成后提交 Pull Request，在 PR 描述中注明"完成 Issue #4"。
```

---

## 组员 Fork 流程

```powershell
# 1. 在 GitHub 点击 Fork，将组长仓库 Fork 到自己账号
# 2. 克隆自己的 Fork
git clone https://github.com/自己的用户名/class_event_signup.git
cd class_event_signup

# 3. 添加组长仓库为 upstream
git remote add upstream https://github.com/组长用户名/class_event_signup.git
git remote -v

# 4. 创建自己的任务分支（以组员A为例）
git checkout -b member-a-event-info

# 5. 修改指定文件，完成后提交
git add data/event_info.py
git commit -m "update event title and description (Issue #1)"
git push -u origin member-a-event-info

# 6. 在 GitHub 创建 Pull Request
```

---

## Vercel 部署

1. 打开 [https://vercel.com](https://vercel.com)，用 GitHub 账号登录
2. 点击 **Add New... → Project**
3. 导入 `class_event_signup` 仓库
4. **Framework Preset** 选择 `Other`
5. Root Directory 保持默认
6. 点击 **Deploy**

确认仓库根目录包含：
```
app.py
requirements.txt
vercel.json
templates/
static/
data/
```

---

## 最终提交清单

- [ ] GitHub 主仓库链接
- [ ] Issue #1 ~ #4 截图或链接
- [ ] PR #1 ~ #4 截图或链接
- [ ] 至少 1 条 review/comment 记录
- [ ] 本地 Flask 首页截图
- [ ] 本地 Flask 结果页截图
- [ ] Vercel 线上网址
- [ ] Vercel 首页截图
- [ ] Vercel 结果页截图
