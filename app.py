import textwrap
from flask import Flask, render_template
from datetime import datetime
import markdown
import json

app = Flask(__name__)

@app.route('/')
def index():
    post_data = {
        "heading": "Neo's Blog Index Page | 根目录页"
    }
    return render_template('index.html', post=post_data)

@app.route('/articles/00')
def testing_page():
    post_data = {
        "title": "Neo's Blog 测试页面",
        "heading": f"This is the blog testing page | 测试页面",
        "author": "NeoNought",
        "categories": ["Computer Science"], 
        "date": "June 30, 2025",
        "content": 
        '''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        blog的测试/演示页面blog的测试/演示页面blog的测试/演示页面blog的测试/演示页面blog的测试/演示页面blog的测试/演示页面blog的测试/演示页面
        blog的测试/演示页面blog的测试/演示页面blog的测试/演示页面blog的测试/演示页面blog的测试/演示页面
        ''',
        "image_url": "/static/testPic.png"
    }
    return render_template('testing_page.html', post=post_data)

@app.route('/articles/01')
def death_stranding1():
    post_data = {
        "heading": "一年前在死亡搁浅留下的建筑和指示牌",
        "author": "NeoNought",
        "categories": ["Video Games"], 
        "date": "June 30, 2025",

        "content1": textwrap.dedent("""\
            刚开始玩死亡搁浅1的时候建了一些发电机和雨亭，前几天看到都有一千多赞了
        """).strip(),

        "image_url1": "/static/ds1/ds3.jpg",

        "content2": textwrap.dedent("""\
            给摩托加速的指示牌:
        """).strip(),

        "image_url2": "/static/ds1/ds2.jpg",
        "image_url3": "/static/ds1/ds4.jpg",

        "content3": textwrap.dedent("""\
            半衰期系列的 lambda 标志指示牌（才发现）
        """).strip(),

        "image_url4": "/static/ds1/ds1.jpg",
    }
    return render_template("death_stranding1.html", post=post_data)

@app.route('/articles/02')
def gamma_doppler():

    def info_text(phase):
        return str(phase) + ''' 模版推荐(reference: The Complete Gamma Doppler Patterns Guide by korenevskiy and NIKI)<br>
                            <a href="/articles/claw-knife">爪子刀</a>，
                            <a href="/articles/butterfly-knife">蝴蝶刀</a>，
                            <a href="/articles/m9-bayonet">M9刺刀</a>，
                            <a href="/articles/bayonet">刺刀</a>，
                            <a href="/articles/falchion">折叠刀</a>，
                            <a href="/articles/huntsman">猎杀者匕首</a>，
                            <a href="/articles/bowie">鲍伊猎刀</a>，
                            <a href="/articles/gut">穿肠刀</a>，
                            <a href="/articles/glock18">格洛克18</a>'''
    
    post_data = {
        "heading": "CS2 多普勒&伽马多普勒款式挑选指南",
        "author": "NeoNought",
        "date": "June 31 2025",
        "categories": ["Video Games"],

        "content0": """多普勒和伽马多普勒都有款式(phase)之分，不同款式之间都有着一些差异。
        而相同款式之间还有很多不同的模版(pattern template)。
        这篇文章详细的展示了不同款式的特点，价位，和好模版推荐。""",

        "heading2": "多普勒（Doppler）",
        "content1": """多普勒分为7个款式：\nphase 1, 2, 3, 4, 红宝石(ruby)，蓝宝石(sapphire)，黑珍珠(black pearl)。
        价格比较（此比较刀型为蝴蝶刀，不同刀型可能会有差异）: \n红宝石 > 黑珍珠 > 蓝宝石 > p2 > p4 > p1 > p3
        有多普勒皮肤的刀型：\n求生匕首，流浪者匕首，刺刀，M9刺刀，蝴蝶刀，骷髅匕首，爪子刀，折叠刀，熊刀，穿肠刀，短剑，系绳匕首，折刀，锯齿爪刀，暗影双匕，猎杀者匕首，弯刀，鲍伊猎刀""",

        "heading3_1": "phase 1",
        "content2": "phase 1 颜色由(浅)红和(浅)蓝组成，呈现出一种渐变粉紫色。",
        "image_url_dopplerp1_1": "/static/gamma_doppler/m91.jpg",
        "image_url_dopplerp1_2": "/static/gamma_doppler/kara1.jpg",

        "heading3_2": "phase 2",
        "content3": "phase 2 整体来看是浅粉色",
        "image_url_dopplerp2_1": "/static/gamma_doppler/m92.jpg",
        "image_url_dopplerp2_2": "/static/gamma_doppler/kara2.jpg",

        "heading3_3": "phase 3 和 phase 4",
        "content4": "phase 3 和 4 看起来都是蓝色，只不过深浅度和上面的斑颜色不同。",
        "image_url_dopplerp3": "/static/gamma_doppler/m93.jpg",
        "image_url_dopplerp3_kara": "/static/gamma_doppler/kara3.jpg",
        "image_url_dopplerp4": "/static/gamma_doppler/m94.jpg",
        "image_url_dopplerp4_kara": "/static/gamma_doppler/kara4.jpg",

        "heading3_4": "红宝石",
        "content5": "红宝石是多普勒特殊模版之一，通体亮红色。",
        "image_url_ruby_1": "/static/gamma_doppler/m9ruby.jpg",
        "image_url_ruby_2": "/static/gamma_doppler/kara_ruby.jpg",

        "heading3_5": "蓝宝石",
        "content6": "蓝宝石是多普勒特殊模版之一，通体亮蓝色。但是由于CS2画质和光影效果，蓝宝石热度和价格直线下降。此外因为蓝宝石还和p3/p4过于相似，导致很多人不选择这个款式。",
        "image_url_sap_1": "/static/gamma_doppler/m9sap.jpg",
        "image_url_sap_2": "/static/gamma_doppler/kara_sap.jpg",

        "heading3_6": "黑珍珠",
        "content7": "黑珍珠是多普勒特殊模版之一，通体深紫色。",
        "image_url_bp_1": "/static/gamma_doppler/m9black.jpg",
        "image_url_bp_2": "/static/gamma_doppler/kara_black.jpg",

        "heading2_gd": "伽马多普勒（Gamma Doppler）",
        "content8": 
        '''
        伽马多普勒分为5个款式：\nphase 1, 2, 3, 4, 绿宝石(emerald)。
        价格比较（此比较刀型为蝴蝶刀，不同刀型可能会有差异）: \n绿宝石 > p2 > p3 > p1 > p4 
        有多伽马普勒皮肤的刀型：\n刺刀，M9刺刀，蝴蝶刀，爪子刀，折叠刀，穿肠刀，暗影双匕，猎杀者匕首，弯刀，鲍伊猎刀。
        此外，格洛克18型也有此皮肤。
        伽马多普勒的款式区别没有多普勒那么大，看起来大概都是绿色。
        ''',
        "heading3_7": "phase 1",
        "content9": "phase 1 主体是浅蓝色加上一点绿色和紫色渐变。部分模版会呈现纯浅蓝色(diamond gem)",
        "image_url_gd_1": "/static/gamma_doppler/m9g1.jpg",
        "image_url_gd_2": "/static/gamma_doppler/karag1.jpg",
        "content9_1": info_text('P1'),

        "heading3_8": "phase 2",
        "content10": "phase 2 是除了绿宝石款式外绿色最多的，通体浅绿色",
        "image_url_gd_3": "/static/gamma_doppler/m9g2.jpg",
        "image_url_gd_4": "/static/gamma_doppler/karag2.jpg",
        "content9_2": info_text('P2'),

        "heading3_9": "phase 3",
        "content11": "phase 3 是浅蓝和浅绿混合，但是和phase 1 还是有明显区别。具体可以对照图片。",
        "image_url_gd_5": "/static/gamma_doppler/m9g3.jpg",
        "image_url_gd_6": "/static/gamma_doppler/karag3.jpg",
        "content9_3": info_text('P3'),

        "heading3_10": "phase 4",
        "content12": "phase 4 以深绿色为主，加上一些浅蓝色。但是会有一些暗斑。",
        "image_url_gd_7": "/static/gamma_doppler/m9g4.jpg",
        "image_url_gd_8": "/static/gamma_doppler/karag4.jpg",
        "content9_4": info_text('P4'),

        "heading3_11": "绿宝石",
        "content13": "绿宝石为稀有的特殊模版，整体是像翡翠一样的亮绿色。",
        "image_url_gd_9": "/static/gamma_doppler/m9emer.jpg",
        "image_url_gd_10": "/static/gamma_doppler/kara_em.jpg",
        "content9_5": info_text('绿宝石'),

        "heading2_notice": "关于刀身上的斑",
        "content14": "伽马多普勒皮肤刀身上会出现一些白/黑色的斑。其中白斑会导致刀在光的照射下失去反射，一般出现在非宝石模版上面。在购买前最好去社区服光线下看看效果",
        "image_url_gd_11": "/static/gamma_doppler/white1.jpeg",
        "content15": "宝石刀的黑斑主要影响整体观感。",
        "image_url_gd_13": "/static/gamma_doppler/black1.jpg",
    }
    return render_template("gamma_doppler.html", post=post_data)

#### 文章03 05 06 都没开始写
@app.route('/articles/03')
def blue_farm_primer():
    post_data = {
        "heading": "万智牌 cEDH Blue Farm 套牌指南",
        "author": "NeoNought",
        "categories": ["Magic the Gathering", "Trading Card Games"],
        "date": "July 3, 2025",
        "content_intro":
        '''
        这是一套以织命使·堤谟娜(Tymna the Weaver)和卢德维佳作寇姆(Kraum, Ludevic's Opus)为指挥官的cEDH套牌指南。
        本文将详细介绍套牌的核心策略、关键单卡以及对局思路。
        ''',
        "content_section1": "## 1. 套牌简介",
        "content_body1":
        '''
        Blue Farm 是一套中速控制套牌，主要通过以下策略获胜：
        <br>• 利用 Tymna 抽牌积累资源优势
        <br>• 通过康咒和去除控制场面
        <br>• 寻找时机完成combo取胜
        <br><br>
        牌表链接：https://moxfield.com/decks/NkkFb-Gv6Uy3cVATGKHOdg
        ''',
        "content_section2": "## 2. 核心策略",
        "content_body2":
        '''
        套牌有两个主要的游戏计划：
        <br><br>
        <strong>中速计划：</strong>
        <br>• 1-3回合出 Tymna 开始抽牌
        <br>• 保持手牌优势，用康咒保护自己
        <br>• 等待最佳时机完成combo
        <br><br>
        <strong>快速计划：</strong>
        <br>• 遇到理想起手时可以尝试快速combo
        <br>• 需要评估对手的应对能力
        ''',
        "content_section3": "## 3. 关键单卡",
        "content_body3":
        '''
        <strong>指挥官：</strong>
        <br>• Tymna the Weaver - 主要抽牌引擎
        <br>• Kraum, Ludevic's Opus - 提供额外抽牌和飞行威胁
        <br><br>
        <strong>Combo单卡：</strong>
        <br>• Thassa's Oracle + Demonic Consultation
        <br>• Underworld Breach 相关combo
        <br><br>
        <strong>保护/交互：</strong>
        <br>• Force of Will, Force of Negation
        <br>• Mental Misstep
        <br>• Swords to Plowshares
        ''',
        "content_conclusion":
        '''
        <br><br>
        本文持续更新中，更多详细内容将陆续补充...
        '''
    }
    return render_template("blue_farm_primer.html", post=post_data)

@app.route('/articles/04')
def neos_cs2_inv():
    post_data = {
        "heading": "2025年CS2自用主战武器皮肤纪念",
        "author": "NeoNought",
        "categories": ["Video Games"],
        "date": "July 5 2025",

        "content_neo_cs_skins_0": 
        '''
        由于皮肤早晚都要卖，所以纪念一下准备长期用的皮肤。
        ''',
        "img_url_sh0": "/static/cs_skin_hist/arti4_inv.jpg",
        "heading2_knife": "匕首皮肤",
        "content_article4_1": 
        '''
        准备长用的皮肤是P3伽马多普勒蝴蝶刀。
        2025年4月左右发现去年买的P3伽马多普勒爪子刀涨了7000多，就直接卖了换成了ADHD喜欢的蝴蝶刀。
        使用历史：人工染色爪子刀，P1多普勒爪子刀，P3伽马多普勒鲍伊猎刀，P3伽马多普勒爪子刀，黑色层压板刺刀，原皮蝴蝶刀，传说M9刺刀（玩了半年多换了这么多刀，这就是为什么写了这篇文章😅）
        ''',
        "img_url_sh1": "/static/cs_skin_hist/arti4_knife.jpg",
        "content_article4_1.5": "仔细看上面其实还有一些白斑，但是好在模版还可以。",
        # 手枪皮肤
        "heading2_pistols": "手枪皮肤",
        "content_article4_2": "平时常用的手枪有：USP-S, 格洛克-18, FN57, P250",
        "content_article4_3": "最常用的USP-S是凯门鳄，握把上还有一个科隆2014全息小眼(Team Dignitas)贴纸。其实当时就是因为这个贴纸买的，后来因为没什么特别喜欢的USP皮肤就一直用这个了。",
        "img_url_sh2": "/static/cs_skin_hist/arti4_usps1.jpg",
        "content_article4_4": "另一把USP-S是刚玩游戏的时候买的脑洞大开，感觉很好看就偶尔也会拿出来看看。",
        "img_url_sh3": "/static/cs_skin_hist/arti4_usps2.jpg",
        "content_article4_5": "警的ECO局有时起一把FN57，随便选了一把绿的。",
        "img_url_sh4": "/static/cs_skin_hist/arti4_fn57.jpg",
        "content_article4_6": "几乎不起P250。",
        "img_url_sh5": "/static/cs_skin_hist/arti4_p250.jpg",
        "content_article4_7": "现在的格洛克就一把伽马多普勒绿宝石，买不起宝石刀可以买个手枪体验一下😅",
        "img_url_sh6": "/static/cs_skin_hist/arti4_glock.jpg",
        "content_article4_8": "ECO神器tec-9，带了科隆2016一个全息小眼贴纸",
        "img_url_sh7": "/static/cs_skin_hist/arti4_tec9.jpg",
        # smg皮肤
        "heading2_smg": "冲锋枪皮肤",
        "content_article4_9": "平时常用的冲锋枪只有Mac-10, MP9, 偶尔买MP7",
        "content_article4_10":"Mac-10随便买了一把绿的，贴了几张便宜的贴纸。（这个绿枪好像还是新皮肤）",
        "img_url_sh8":"/static/cs_skin_hist/arti4_smg1.jpg",
        "content_article4_11": "在之前没想凑全绿套装的时候还用过一把Saibā Oni，有点像黎明杀机里我最常玩的屠夫。",
        "img_url_sh9":"/static/cs_skin_hist/arti4_smg2.jpg",
        "content_article4_12": "MP9最常用的是四个全息贴纸改装的富士山，虽然看不到富士山图案，但是能看到渐变色也可以。",
        "img_url_sh10": "/static/cs_skin_hist/arti4_smg3.jpg",
        "content_article4_13": "2024年11月刚玩的时候看有人往这个枪上面贴了三个全息独角兽，那时候还没怎么见过这种贴纸，感觉很好看就买了一把，但是好像因为那个独角兽贴纸太贵了就买了一张🤔。",
        "img_url_sh11": "/static/cs_skin_hist/arti4_smg4.jpg",
        "content_article4_14": "这是一把平平无奇开出来的绿枪，偶尔起一把。",
        "img_url_sh12": "/static/cs_skin_hist/arti4_smg5.jpg",
        # 步枪皮肤
        "heading2_rifles": "步枪皮肤",
        # 步枪皮肤 - AK-47
        "content_article4_15": "最近在 Somnium 手里买的淬火，感觉很蓝。还是暗金的，感觉可以一直用，记录一下用它鲨了多少人。",
        "img_url_sh13": "/static/cs_skin_hist/arti4_r1.jpg",
        "content_article4_16": "这把也是刚玩的时候买的，感觉很简洁，加上 AK 平滑的表面，适合贴贴纸（特别是 Virtus Pro 和 Neo 的橙白色贴纸）。",
        "img_url_sh14": "/static/cs_skin_hist/arti4_r2.jpg",
        "content_article4_17": "三联泰坦贴纸，但是似乎这个很难卖🤬",
        "img_url_sh15": "/static/cs_skin_hist/arti4_r3.jpg",
        "content_article4_18": "莫言（墨岩）似乎每人都有一把，刚玩 CS 的时候也迷上了半衰期系列，正好有联动的贴纸就随便贴了一把。这个全息 Lambda 还是之前一发开出来的。",
        "img_url_sh16": "/static/cs_skin_hist/arti4_r4.jpg",
        # M4A1-S
        "content_article4_19": "冒险家乐园是我觉得最好看的 A1 皮肤，感觉还不是特别吃磨损。我这个站痕累累看着也没太影响上面的图案。枪名玩了个合金装备 Les Enfants Terribles 的梗（字数竟然正好）",
        "img_url_sh17": "/static/cs_skin_hist/arti4_r5.jpg",
        "content_article4_20": "这把似乎是 CSGO 饰品理财的第一步🤔（第二步是买了把爪子刀）刚玩的时候朋友说这把枪是绝版皮肤比较保值，用一用卖了也不会降价。现在看还是很好看的，上面那个小挂件也是当时武库开出来的。",
        "img_url_sh18": "/static/cs_skin_hist/arti4_r6.jpg",

        # M4A4
        "content_article4_21": "贴了四个 2015 卡托维兹泰坦贴纸的二希莫夫 M4A4，但是我并不怎么用这把枪，即使是游戏内降价之后。",
        "img_url_sh19": "/static/cs_skin_hist/arti4_r7.jpg",

        # Galil AR
        "content_article4_22": "donk 同款小绿枪。没钱的时候起一把。刚玩的时候还觉得这个相比 AK 更好压。",
        "img_url_sh20": "/static/cs_skin_hist/arti4_r9.jpg",

        # SG 553
        "content_article4_23": "平时也不太起这把枪，感觉性价比很低。但是当时看那个意式拉力很像我在《地平线》里保时捷的涂装，就买了把玩玩。",
        "img_url_sh21": "/static/cs_skin_hist/arti4_r10.jpg",
        "content_article4_24": "这把 SG553 是我收藏里最彩的几把枪之一，但是很少用。贴了点便宜贴纸图个乐。",
        "img_url_sh22": "/static/cs_skin_hist/arti4_r11.jpg",

        # AWP
        "content_article4_25": "买这个皮肤就是为了镜上面的那个全息 2015 卡托维兹 Virtus.pro 贴纸。颜色也很配，后来自己贴上了一个 Neo、卡托泰坦和 NAVI。",
        "img_url_sh23": "/static/cs_skin_hist/arti4_r12.jpg",

        # 结尾
        "heading2_ending": "纪念相册里那些被卖掉的枪皮",
        "heading3_first_knife": "我的第一把刀",
        "content_article4_26": "刚玩的第一个月听他们说 CS 里匕首还有手感一说，当时就动了买一把的念头。研究过后发现似乎只有刀型影响手感（但是现在看来似乎颜色也影响），听说三幻神（M9，爪子刀，蝴蝶刀）是手感最好的，然后就在 skinport 上找了一把颜色能看的（纯色）爪子刀。记得当时好像才花了 600 多美元。虽然当时没有很贪婪，但是还是给欲望膨胀开了一个头😅",
        "img_url_sh24": "/static/cs_skin_hist/o6.png",
        "content_article4_26_note": "（图片拍摄于 2024-12-24）",




    }
    return render_template("neos_cs2_inv.html", post=post_data)

@app.route('/articles/05')
def kinnan_cedh_primer():
    post_data = {
        "heading": "万智牌 cEDH Kinnan 套牌指南",
        "author": "NeoNought",
        "categories": ["Magic the Gathering", "Trading Card Games"],
        "date": "Oct 12 2025",
        "content_kinnan_cedh_0": 
        ''' 
        这是一套以 Kinnan, Bonder Prodigy 为指挥官的 cEDH 套牌指南。还没开始的
        ''',
    }
    return render_template("kinnan_cedh.html", post=post_data)

@app.route('/articles/06')
def cs_market_crash():
    post_data = {
        "heading": "2025年CS2饰品市场崩盘分析",
        "author": "NeoNought",
        "categories": ["Video Games"],
        "date": "Oct 23 2025",
        "content_cs_market_crash_0": 
        ''' 
        2025年10月末，CS2饰品市场经历了一次大规模的价格崩盘，本文将分析其原因和影响。
        ''',
    }
    return render_template("cs_market_crash.html", post=post_data)

@app.route('/articles/07')
def shorikai_stax_1_show():
    post_data = {
        "heading": "万智牌EDH(8分/Challenge/Optimised)创机胜利械套牌展示",
        "author": "NeoNought",
        "categories": ["Magic the Gathering", "Trading Card Games", "Neo's Collection"],
        "date": "Nov 20 2025",

        "content_shorikai_stax_1_0": textwrap.dedent('''\
        全套一张生物（碎船惊惧兽）的高达控锁组合技套牌，在国内外牌店折磨了不少路人。
        牌表链接：<a href="https://moxfield.com/decks/C8zsmmszGUCdzB9UMDSKuQ" target="_blank">https://moxfield.com/decks/C8zsmmszGUCdzB9UMDSKuQ</a>
        primer有空补上
        好像是当时在学校社团抄的邮差的牌表
        剩下的就是展示/纪念一下玩了三年多的版本
        ''').strip(),


        "content_shorikai_stax_1_1": "指挥官",
        "img_url_shorikai_stax_1_1": "/static/shorikai_stax_1_show/shorkai_commander.jpg",

        "content_shorikai_stax_1_2": "法术力基础",
        "img_url_shorikai_stax_1_2": "/static/shorikai_stax_1_show/shorikai_mana.jpg",
        "img_url_shorikai_stax_1_5": "/static/shorikai_stax_1_show/shorikai_mana2.jpg",

        "content_shorikai_stax_1_3": "神器&结界锁&赚牌引擎",
        "img_url_shorikai_stax_1_3": "/static/shorikai_stax_1_show/shorkai_draw.jpg",

        "content_shorikai_stax_1_4": "控制咒语",
        "img_url_shorikai_stax_1_4": "/static/shorikai_stax_1_show/shorkai_counter.jpg",

        "content_shorikai_stax_1_7": "实用法术&导师",
        "img_url_shorikai_stax_1_7": "/static/shorikai_stax_1_show/shorkai_tutor.jpg",

        "content_shorikai_stax_1_8": "生物&鹏洛客",
        "img_url_shorikai_stax_1_8": "/static/shorikai_stax_1_show/shorkai_creature.jpg",

        "content_shorikai_stax_1_9": "值得纪念的版本",
        "img_url_shorikai_stax_1_9": "/static/shorikai_stax_1_show/shorkai_mox_opal.jpg",
        "img_url_shorikai_stax_1_10": "/static/shorikai_stax_1_show/shorkai_tezz.jpg",
        }
    return render_template("shorikai_stax_1.html", post=post_data)

@app.route('/articles/08')
def hottoys_berserker():
    post_data = {
        "heading": "Hot Toys 1/6 Berserker Predator Figure",
        "author": "NeoNought",
        "categories": ["Hot Toys", "Neo's Collection"],
        "date": "Dec 10 2025",

        "content_hottosys_berserker_0": textwrap.dedent('''\
        ''').strip(),
    }

    return render_template("hottosys_berserker.html", post=post_data)

@app.route('/articles/09')
def cedh_kinnan_show():
    post_data = {
        "heading": "万智牌cEDH持绊逸才季宁套牌展示",
        "author": "NeoNought",
        "categories": ["Magic the Gathering", "Trading Card Games", "Neo's Collection"],
        "date": "Dec 15 2025",

        "content_cedh_kinnan_show_0": textwrap.dedent('''\
        ''').strip(),
    }
    return render_template("cedh_kinnan_show.html", post=post_data)

@app.route('/articles/10')
def cedh_blue_farm_show():
    post_data = {
        "heading": "万智牌cEDH堤谟娜/寇姆(Blue Farm)套牌展示",
        "author": "NeoNought",
        "categories": ["Magic the Gathering", "Trading Card Games", "Neo's Collection"],
        "date": "Dec 15 2025",

        "content_cedh_blue_farm_show_0": textwrap.dedent('''\
        ''').strip(),
    }
    return render_template("cedh_blue_farm_show.html", post=post_data)










# 分类页面
@app.route('/category/<category_name>')
def show_category(category_name):
    post_data = {
        "heading": f"{category_name} | 分类",
    }
    '''
    param category_name: 用户点击一个分类，展示所有属于这个分类的文章

    '''
    # 从 JSON 文件读取文章列表
    with open('articles.json', 'r', encoding='utf-8') as f:
        all_articles = json.load(f)

    # 筛选出属于这个分类的文章
    filtered_articles = [
        a for a in all_articles
        if (category_name == a.get('category', '')) or (category_name in a.get('categories', []))
    ]
    return render_template('category.html', articles=filtered_articles, category=category_name, post=post_data)




if __name__ == '__main__':
    app.run(debug=True)

