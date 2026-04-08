# Blog 升级计划

---

## 第零阶段：修理现有文章 & 搞清结构

在动任何升级之前，先把现状整理干净。

### 需要修的问题

1. **`articles.json` 不完整** — 08/09/10 三篇文章没有加进去，分类页面找不到它们
2. **`index.html` 目录手动维护** — 和 `articles.json` 脱节，现在是两套数据
3. **`style.css` 有拼写错误** — `figurecaption` 应该是 `figcaption`（第 173 行），导致图片说明文字样式失效
4. **03/05/06/08/09/10 文章内容是空的** — 占位符状态，要么补内容要么明确标注"未完成"

### 需要搞懂的结构

在改代码之前，确保理解以下几件事：

- **Flask 路由怎么工作** — `@app.route('/articles/01')` 和函数名的关系，`url_for()` 为什么用函数名而不是 URL
- **Jinja2 模板继承** — `base.html` 里的 `{% block %}` 是怎么被各文章模板填充的
- **`articles.json` 目前的用途** — 只被分类页面 `/category/<name>` 用到，首页目录没有用它

---

## 第一阶段：小工作（JS 强化）

### 1. 阅读进度条
**作用：** 页面顶部一条细横线随滚动增长，让读者知道文章读到哪了，长文（04 皮肤纪念那篇）体验好很多。

**需要会：**
- JS 的 `scroll` 事件监听
- `window.scrollY` / `document.documentElement.scrollHeight` 这两个属性
- CSS 的 `position: fixed`

**改动范围：** `script.js` 加约 10 行，`style.css` 加约 5 行

---

### 2. 图片 Lightbox
**作用：** 点击图片弹出全屏查看，特别适合皮肤/牌图展示，不用眯着眼看小图。

**需要会：**
- JS 的 DOM 操作（`querySelector`, `addEventListener`）
- CSS 的 `position: fixed` 和 `z-index`（做遮罩层）
- `createElement` / `appendChild`

**改动范围：** `script.js` 加约 30 行，`style.css` 加约 20 行

---

### 3. 首页动态渲染
**作用：** 现在加新文章要手动改 `index.html`，改完之后只改 `articles.json` 就能自动出现在首页目录，不会漏更也不会忘。

**需要会：**
- Jinja2 的 `{% for %}` 循环
- Flask 里怎么把 JSON 数据传进模板（`render_template` 传参）

**改动范围：** 改 `app.py` 约 5 行，重写 `index.html` 目录部分约 10 行

---

## 第二阶段：中等工作（架构优化）

### 4. Markdown 驱动文章内容
**作用：** 现在写文章要在 `app.py` 里改 Python 字符串，非常反人类。改完之后在 `articles/` 文件夹里新建一个 `.md` 文件就能写文章，格式清晰，支持标题/加粗/列表/链接。

**需要会：**
- Markdown 基本语法
- Flask 里读取文件（`open()`）
- `markdown` 库的 `markdown.markdown()` 调用（已经 import 了）
- Jinja2 的 `{{ content | safe }}` 过滤器（渲染 HTML 字符串）

**改动范围：** 新建 `articles/` 目录放 `.md` 文件，改 `app.py` 路由逻辑，改相关模板。工作量最大，但一旦做完写文章会轻松很多。

---

### 5. 统一展示模板
**作用：** 07/08/09/10 这几篇结构完全一样（介绍段落 + 一堆图），现在每篇都有独立的 `.html` 模板，维护麻烦。合并成一个通用模板，减少重复代码，改样式只改一处。

**需要会：**
- Jinja2 的 `{% for %}` 循环和条件判断
- 设计一个简单的数据结构（列表套字典）来描述"段落 + 图片"

**改动范围：** 新建一个通用模板，改 `app.py` 里 4 个路由的数据格式

---

### 6. 客户端搜索
**作用：** 首页加一个搜索框，输入关键字实时过滤文章列表，文章多了之后找起来方便。

**需要会：**
- JS 的 `input` 事件监听
- 字符串的 `.includes()` / `.toLowerCase()` 方法
- DOM 的 `style.display` 控制显隐

**改动范围：** `index.html` 加搜索框 HTML，`script.js` 加约 15 行

---

## 建议顺序

```
第零阶段（先做，打好基础）：
  修 articles.json → 修 figcaption 拼写 → 理解 Flask/Jinja2 结构

第一阶段（互相独立，任意顺序）：
  进度条 → Lightbox → 首页动态渲染

第二阶段（有依赖，按顺序）：
  Markdown 驱动 → 统一展示模板 → 客户端搜索
```

Markdown 驱动建议在统一模板之前做，因为模板改了之后内容管理方式也会跟着变。
