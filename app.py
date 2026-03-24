from flask import Flask, render_template, send_from_directory, request, redirect
from datetime import datetime

app = Flask(__name__)

# ==================== 博客数据 ====================
BLOG_POSTS = [
    {
        'id': 1,
        'title': '初心者向け投資ガイド：安全な株式投資の始め方',
        'slug': 'beginners-guide-safe-stock-investment',
        'excerpt': '株式投資の基礎知識を学び、初心者が安全に投資を開始するための完全なステップバイステップガイド。',
        'meta_description': '初心者向けの安全な株式投資ガイド。投資の基本原則とリスク管理を解説',
        'content': '''
        <h2>投資を始める前に知るべき基礎知識</h2>
        <p>株式投資は長期的な資産構築の有力な手段です。しかし、投資を始める前に、基本的な概念と原則を理解することが重要です。</p>

        <h3>1. 投資の基本原則</h3>
        <p>投資の成功は、明確な目標設定とリスク管理に基づいています。以下の要素を考慮することが推奨されます：</p>
        <ul>
            <li><strong>財政目標の明確化：</strong>あなたが投資で何を達成したいのかを明確にする必要があります。リタイアメント、住宅購入、教育資金など。</li>
            <li><strong>リスク許容度の評価：</strong>あなたがどの程度のリスクを受け入れられるかを理解することが重要です。</li>
            <li><strong>投資期間の決定：</strong>短期投資と長期投資では戦略が異なります。</li>
            <li><strong>投資額の決定：</strong>余裕資金で投資することが推奨されます。</li>
        </ul>

        <h3>2. リスク管理の重要性</h3>
        <p>すべての投資にはリスクが伴います。重要なのは、そのリスクを理解し、管理することです。分散投資とポートフォリオの管理が重要な戦略です。</p>

        <h3>3. 始める前の準備</h3>
        <p>以下の準備をしてから投資を始めましょう：</p>
        <ul>
            <li>証券会社の口座開設</li>
            <li>投資資金の確保</li>
            <li>基本的な知識の習得</li>
            <li>投資計画の作成</li>
        </ul>

        <h3>4. 最初の投資のコツ</h3>
        <p>最初��小額から始めることをお勧めします。市場の動きを観察しながら、徐々に知識と経験を積み重ねることが成功の鍵です。</p>
        ''',
        'author': '堀江貴文',
        'author_credentials': '20年以上の投資分析経験を持つ独立系投資家。CFA認定アナリスト。',
        'date': '2026-03-15',
        'category': '投資入門',
        'tags': ['投資', '初心者', 'リスク管理', '基礎知識'],
        'read_time': 12,
    },
    {
        'id': 2,
        'title': '市場変動期の投資戦略：感情的な取引を避ける方法',
        'slug': 'investment-strategy-market-volatility',
        'excerpt': '市場が大きく変動している時期の投資判断。感情的な取引を避けるための戦略を解説。',
        'meta_description': '市場変動期の投資戦略。感情的な取引を避けるプロのテクニック',
        'content': '''
        <h2>市場変動は投資の自然な現象</h2>
        <p>過去100年間の株式市場データから、市場の変動は通常の現象であり、避けられないものであることが明らかになっています。</p>

        <h3>行動経済学からの視点</h3>
        <p>行動経済学の研究によれば、投資家の3分の2は市場下落時にパニック売却を行います。この行動は長期的なリターンを著しく低下させます。</p>

        <h3>感情的な取引がもたらす悪影響</h3>
        <p>感情に基づいた投資判断は以下のような悪影響をもたらします：</p>
        <ul>
            <li>パニック売却による損失確定</li>
            <li>過度な楽観による過度な買い増し</li>
            <li>短期的な値動きへの過剰反応</li>
            <li>タイミング投資の失敗</li>
        </ul>

        <h3>プロが実践する冷静な判断</h3>
        <p>プロの投資家は、感情に左右されず、事前に定めた投資計画に従って行動します。これが安定したリターンの源です。</p>

        <h3>市場変動への対処法</h3>
        <ul>
            <li><strong>投資計画の事前設定：</strong>市場が静かなうちに戦略を決定する</li>
            <li><strong>定期的な見直し：</strong>月に1回程度、定期的にポートフォリオをチェック</li>
            <li><strong>ドルコスト平均法：</strong>定額で継続的に投資する</li>
            <li><strong>長期視点の維持：</strong>短期変動に一喜一憂しない</li>
        </ul>

        <h3>実例：過去の市場危機</h3>
        <p>2008年の金融危機、2020年のコロナ市場混乱など、市場危機は何度も発生しています。しかし、これらの危機を乗り越えた投資家は、その後の大きなリターンを享受しました。</p>
        ''',
        'author': '堀江貴文',
        'author_credentials': '行動経済学と投資心理の専門家。100以上の投資セミナーを開催。',
        'date': '2026-03-10',
        'category': '投資戦略',
        'tags': ['戦略', '市場分析', '心理学', '投資'],
        'read_time': 14,
    },
    {
        'id': 3,
        'title': 'ポートフォリオ分散投資：理論と実践ガイド',
        'slug': 'portfolio-diversification-guide',
        'excerpt': 'ポートフォリオ理論に基づいた分散投資の実践的ガイド。資産配分戦略を解説。',
        'meta_description': 'ポートフォリオ分散投資ガイド。資産配分戦略とリスク低減の方法',
        'content': '''
        <h2>分散投資の科学的根拠</h2>
        <p>ノーベル���済学賞を受賞したハリー・マーコウィッツの現代ポートフォリオ理論によれば、異なる資産への適切な配分により、全体的なリスクを低減することが可能です。</p>

        <h3>効率的フロンティア</h3>
        <p>効率的フロンティアとは、与えられたリスクレベルで最大のリターンを得られる投資ポートフォリオの集合です。この理論に基づいて、最適なポートフォリオを構築することができます。</p>

        <h3>資産クラスの相関性</h3>
        <p>異なる資産クラス（株式、債券、不動産、商品など）は、市場条件に対して異なる反応を示します。これが分散効果の源です。</p>

        <h3>実践的な配分戦略</h3>
        <p>年齢や目標に応じた適切なポートフォリオ構成が重要です：</p>
        <ul>
            <li><strong>20-30代：</strong>成長資産80%、防御資産20%</li>
            <li><strong>30-40代：</strong>成長資産70%、防御資産30%</li>
            <li><strong>40-50代：</strong>成長資産60%、防御資産40%</li>
            <li><strong>50代以上：</strong>成長資産50%、防御資産50%</li>
        </ul>

        <h3>リバランスの重要性</h3>
        <p>定期的にポートフォリオをリバランスすることで、リスクを管理しながらリターンを最適化することができます。</p>

        <h3>よくある分散投資の誤解</h3>
        <p>単に多くの銘柄を保有することが分散投資ではありません。異なる特性を持つ資産クラスへの配分が重要です。</p>
        ''',
        'author': '堀江貴文',
        'author_credentials': 'ポートフォリオ管理の専門家。資産運用会社での勤務経験あり。',
        'date': '2026-03-01',
        'category': '投資戦略',
        'tags': ['分散投資', 'ポートフォリオ', 'リスク管理'],
        'read_time': 15,
    },
    {
        'id': 4,
        'title': '配当金投資で不労所得を創造する方法',
        'slug': 'dividend-income-passive-income',
        'excerpt': '配当金を活用した継続的な収入源の構築。配当利回りと税金対策。',
        'meta_description': '配当金投資ガイド。不労所得の構築と税金対策',
        'content': '''
        <h2>配当金投資の基礎</h2>
        <p>配当金は企業が利益の一部を株主に還元する仕組みです。継続的な配当を支払う企業に投資することで、定期的な収入を得ることができます。</p>

        <h3>配当利回りの計算</h3>
        <p>配当利回り = 年間配当金 ÷ 株価 × 100</p>
        <p>例：年間配当金が100円、株価が2,000円の場合、配当利回りは5%です。</p>

        <h3>高配当企業の特徴</h3>
        <ul>
            <li>安定した利益を生み出す事業モデル</li>
            <li>キャッシュフローが豊富</li>
            <li>成熟産業での事業展開</li>
            <li>配当性向が適切（30～50%程度）</li>
        </ul>

        <h3>配当金投資のメリット</h3>
        <ul>
            <li>定期的な現金収入</li>
            <li>株価上昇による利得との二重利益</li>
            <li>インフレ対策</li>
            <li>心理的な安定感</li>
        </ul>

        <h3>税金対策</h3>
        <p>配当金には税金がかかります。以下の方法で税負担を最適化できます：</p>
        <ul>
            <li>NISA口座の活用（配当金非課税）</li>
            <li>iDeCo（確定拠出年金）への投資</li>
            <li>配当控除制度の活用</li>
        </ul>

        <h3>実例：月5万円の不労所得</h3>
        <p>年間配当利回り5%で月5万円の配当を得るには、約1,200万円の投資が必要です。段階的に構築することが重要です。</p>
        ''',
        'author': '堀江貴文',
        'author_credentials': '配当金投資の実践者。月10万円以上の配当収入を実現。',
        'date': '2026-02-28',
        'category': '投資入門',
        'tags': ['配当', '不労所得', '税金対策'],
        'read_time': 13,
    },
    {
        'id': 5,
        'title': '初心者が知るべき投資の心理学',
        'slug': 'psychology-of-investing',
        'excerpt': '投資行動に影響を与える心理的要因。バイアスと感情管理。',
        'meta_description': '投資心理学。投資決定に影響する心理的要因',
        'content': '''
        <h2>投資心理学の重要性</h2>
        <p>投資の成功には技術と同じくらい心理管理が重要です。多くの投資家は理性的な判断ではなく、感情に基づいて行動します。</p>

        <h3>よくある認知バイアス</h3>

        <h4>1. 確認バイアス</h4>
        <p>自分の信念を支持する情報ばかりを集め、反論する情報を無視する傾向です。</p>

        <h4>2. アンカリング効果</h4>
        <p>最初に見た情報に過度に影響を受ける傾向です。例：過去最高値が「本来の価値」と思い込む。</p>

        <h4>3. 損失回避</h4>
        <p>利益と同額の損失を避ける傾向が、利益を得る欲望より強いという特性です。</p>

        <h4>4. 群集心理</h4>
        <p>他の投資家の行動に追随する傾向。バブル形成の原因となります。</p>

        <h3>感情管理のテクニック</h3>
        <ul>
            <li><strong>投資計画の事前設定：</strong>冷静な時に決めた計画に従う</li>
            <li><strong>定期的な見直し：</strong>過度な頻度で見ずに、月1回程度</li>
            <li><strong>分散投資：</strong>心理的な負担を軽減</li>
            <li><strong>長期投資：</strong>短期変動に一喜一憂しない</li>
        </ul>

        <h3>プロと素人の違い</h3>
        <p>プロの投資家とアマチュアの最大の違いは、感情をコントロールする能力です。</p>
        ''',
        'author': '堀江貴文',
        'author_credentials': '行動経済学の専門家。心理学の観点から投資を研究。',
        'date': '2026-02-20',
        'category': '投資戦略',
        'tags': ['心理学', '投資', 'バイアス'],
        'read_time': 14,
    },
    {
        'id': 6,
        'title': 'テクニカル分析の基礎：チャートの読み方',
        'slug': 'technical-analysis-basics',
        'excerpt': 'テクニカル分析の基本的な考え方。チャートパターンとトレンド分析。',
        'meta_description': 'テクニカル分析ガイド。チャートの読み方とトレンド分析',
        'content': '''
        <h2>テクニカル分析とは</h2>
        <p>テクニカル分析は、過去の株価動きと取引量から将来の価格変動を予測する分析手法です。</p>

        <h3>基本的なチャートタイプ</h3>
        <ul>
            <li><strong>ローソク足チャート：</strong>始値、終値、高値、安値を表示</li>
            <li><strong>トレンドライン：</strong>価格の方向性を示す</li>
            <li><strong>移動平均線：</strong>価格の平均値の推移</li>
        </ul>

        <h3>よくあるチャートパターン</h3>
        <ul>
            <li><strong>ダブルトップ：</strong>売却シグナル</li>
            <li><strong>ダブルボトム：</strong>買い付けシグナル</li>
            <li><strong>ヘッドアンドショルダー：</strong>トレンド反転パターン</li>
        </ul>

        <h3>重要な指標</h3>
        <ul>
            <li><strong>RSI（相対力指数）：</strong>買われすぎ・売られすぎを判断</li>
            <li><strong>MACD：</strong>トレンド転換を検出</li>
            <li><strong>ボリンジャーバンド：</strong>価格の変動幅を表示</li>
        </ul>

        <h3>テクニカル分析の限界</h3>
        <p>テクニカル分析は参考情報です。100%の精度はなく、ファンダメンタル分析と併用することが重要です。</p>
        ''',
        'author': '堀江貴文',
        'author_credentials': 'テクニカル分析の経験者。チャート分析で15年の経験。',
        'date': '2026-02-15',
        'category': '投資戦略',
        'tags': ['テクニカル分析', 'チャート', '分析'],
        'read_time': 12,
    },
    {
        'id': 7,
        'title': 'ファンダメンタル分析：企業の本質的価値を理解する',
        'slug': 'fundamental-analysis-guide',
        'excerpt': '企業の本質的な価値を評価する方法。決算分析と企業評価の基礎。',
        'meta_description': 'ファンダメンタル分析ガイド。企業価値の評価方法',
        'content': '''
        <h2>ファンダメンタル分析の重要性</h2>
        <p>ファンダメンタル分析は、企業の財務状況と事業の質を評価する方法です。長期投資には欠かせません。</p>

        <h3>重要な財務指標</h3>
        <ul>
            <li><strong>PER（株価収益率）：</strong>利益に対する株価の倍率</li>
            <li><strong>PBR（株価純資産倍率）：</strong>純資産に対する株価の倍率</li>
            <li><strong>配当利回り：</strong>株価に対する配当金の割合</li>
            <li><strong>ROE（自己���本利益率）：</strong>企業の収益性</li>
            <li><strong>負債比率：</strong>企業の財務健全性</li>
        </ul>

        <h3>決算報告の読み方</h3>
        <ul>
            <li>売上高の推移</li>
            <li>営業利益の動き</li>
            <li>キャッシュフロー</li>
            <li>在庫水準</li>
        </ul>

        <h3>優良企業の特徴</h3>
        <ul>
            <li>安定した売上成長</li>
            <li>高い利益率</li>
            <li>強いキャッシュポジション</li>
            <li>競争優位性</li>
        </ul>

        <h3>企業の本質的価値の計算</h3>
        <p>本質的価値 ≈ 将来利益の現在価値</p>
        <p>株価が本質的価値より安い場合が買い時です。</p>
        ''',
        'author': '堀江貴文',
        'author_credentials': 'ファンダメンタル分析の専門家。企業評価で20年の実績。',
        'date': '2026-02-10',
        'category': '投資入門',
        'tags': ['ファンダメンタル分析', '企業評価', '決算'],
        'read_time': 13,
    },
    {
        'id': 8,
        'title': 'IPO投資の実践ガイド：新規上場銘柄で利益を出す',
        'slug': 'ipo-investment-guide',
        'excerpt': 'IPO（新規公開株）での投資方法。申し込みから売却まで。',
        'meta_description': 'IPO投資ガイド。新規上場銘柄への投資方法',
        'content': '''
        <h2>IPOとは</h2>
        <p>IPO（Initial Public Offering）は、これまで非公開だった企業が初めて株式を公開する際の新規公開株式のことです。</p>

        <h3>IPO投資の特徴</h3>
        <ul>
            <li><strong>短期で利益を出すチャンス：</strong>公開後の株価上昇が期待できます</li>
            <li><strong>成長企業への投資：</strong>将来性のある企業が多い</li>
            <li><strong>リスクも高い：</strong>公開直後は変動が大きい</li>
        </ul>

        <h3>IPO株購入の流れ</h3>
        <ol>
            <li>証券会社で口座開設</li>
            <li>IPO案件の情報収集</li>
            <li>申し込み（抽選）</li>
            <li>当選確認</li>
            <li>購入代金の振込</li>
            <li>上場初日の取引開始</li>
        </ol>

        <h3>IPO投資の成功ポイント</h3>
        <ul>
            <li><strong>企業研究：</strong>IPO企業の事業内容を十分理解する</li>
            <li><strong>タイミング：</strong>上場初日での売却も選択肢</li>
            <li><strong>資金管理：</strong>損切のルール設定</li>
            <li><strong>複数申し込み：</strong>当選確率を高める</li>
        </ul>

        <h3>注意点</h3>
        <p>IPO株も通常の株式と同じリスクを持っています。過度な期待は禁物です。</p>
        ''',
        'author': '堀江貴文',
        'author_credentials': 'IPO投資の経験者。年間50社以上のIPOを分析。',
        'date': '2026-02-05',
        'category': '投資戦略',
        'tags': ['IPO', '新規上場', '短期投資'],
        'read_time': 11,
    },
    {
        'id': 9,
        'title': '米国株投資ガイド：グローバル分散投資の入門',
        'slug': 'us-stock-investment-guide',
        'excerpt': '米国株式市場への投資方法。為替リスクと銘柄選定。',
        'meta_description': '米国株投資ガイド。グローバル投資の基本',
        'content': '''
        <h2>米国株投資の利点</h2>
        <p>米国は世界最大の株式市場です。グローバル投資の第一歩として米国株投資を検討する価値があります。</p>

        <h3>米国株の特徴</h3>
        <ul>
            <li><strong>���引量が多い：</strong>流動性が高く取引しやすい</li>
            <li><strong>優良企業が多い：</strong>Apple、Microsoft、Amazonなど</li>
            <li><strong>配当が高い：</strong>多くの企業が安定した配当を提供</li>
            <li><strong>為替リスク：</strong>ドル円相場の影響を受ける</li>
        </ul>

        <h3>有名な米国企業指数</h3>
        <ul>
            <li><strong>S&P 500：</strong>米国の500大企業</li>
            <li><strong>ナスダック100：</strong>成長企業が多い指数</li>
            <li><strong>ダウ平均：</strong>米国の代表的な30企業</li>
        </ul>

        <h3>米国株購入の流れ</h3>
        <ol>
            <li>米国株対応の証券口座開設</li>
            <li>円をドルに両替</li>
            <li>企業研究と銘柄選定</li>
            <li>注文（ADRまたは直接取引）</li>
        </ol>

        <h3>為替ヘッジの考え方</h3>
        <p>ドル上昇は利益を増幅し、ドル下落は利益を減少させます。長期投資では為替変動を気にしない人も多いです。</p>

        <h3>初心者向けの米国企業</h3>
        <ul>
            <li>Apple（AAPL）</li>
            <li>Microsoft（MSFT）</li>
            <li>Amazon（AMZN）</li>
            <li>Coca-Cola（KO）</li>
        </ul>
        ''',
        'author': '堀江貴文',
        'author_credentials': '米国株投資の専門家。米国企業への投資経験20年以上。',
        'date': '2026-02-01',
        'category': '投資入門',
        'tags': ['米国株', 'グローバル投資', '為替'],
        'read_time': 12,
    },
    {
        'id': 10,
        'title': 'ETF投資の完全ガイド：手軽な分散投資',
        'slug': 'etf-investment-complete-guide',
        'excerpt': 'ETF（上場投資信託）を利用した分散投資。メリットとデメリット。',
        'meta_description': 'ETF投資ガイド。上場投資信託による分散投資',
        'content': '''
        <h2>ETFとは</h2>
        <p>ETF（Exchange Traded Fund）は、上場投資信託で、株式のように証券取引所で取引できます。手軽な分散投資が実現できます。</p>

        <h3>ETFの特徴</h3>
        <ul>
            <li><strong>分散効果：</strong>一つのETFで複数の銘柄に投資</li>
            <li><strong>低コスト：</strong>手数料が安い</li>
            <li><strong>流動性：</strong>いつでも売却可能</li>
            <li><strong>透明性：</strong>保有銘柄が公開されている</li>
        </ul>

        <h3>主なETFの種類</h3>
        <ul>
            <li><strong>インデックスETF：</strong>日経平均やTOPIXに連動</li>
            <li><strong>セクターETF：</strong>特定の業界に集中投資</li>
            <li><strong>国際ETF：</strong>海外株式に投資</li>
            <li><strong>債券ETF：</strong>債券に投資</li>
        </ul>

        <h3>ETF vs 個別株投資</h3>
        <table>
            <tr>
                <td>要素</td>
                <td>ETF</td>
                <td>個別株</td>
            </tr>
            <tr>
                <td>リスク</td>
                <td>低い（分散）</td>
                <td>高い</td>
            </tr>
            <tr>
                <td>リターン</td>
                <td>中程度</td>
                <td>高い可能性</td>
            </tr>
            <tr>
                <td>手間</td>
                <td>少ない</td>
                <td>多い</td>
            </tr>
            <tr>
                <td>手数料</td>
                <td>安い</td>
                <td>通常</td>
            </tr>
        </table>

        <h3>人気のETF</h3>
        <ul>
            <li>iShares MSCI Japan ETF（EWJ）</li>
            <li>Vanguard S&P 500 ETF（VOO）</li>
            <li>iShares ACWX</li>
        </ul>
        ''',
        'author': '堀江貴文',
        'author_credentials': 'ETF投資の推奨者。ポートフォリオ構築にETFを活用。',
        'date': '2026-01-28',
        'category': '投資入門',
        'tags': ['ETF', '分散投資', '投資信託'],
        'read_time': 12,
    },
]

# ==================== 首页卡片 ====================
FEATURE_CARDS = [
    {
        'title': '投資経験ゼロでも理解できる',
        'description': '段階的なカリキュラムで、基礎から実践まで体系的に学べます。',
        'icon': '📚'
    },
    {
        'title': '実例をもとにした失敗しない考え方',
        'description': '20年以上の投資経験からプロが実際に活用する方法を公開。',
        'icon': '💡'
    },
    {
        'title': 'LINEでいつでも相談・質問',
        'description': '専門家に直接相談でき、すぐに疑問が解決します。',
        'icon': '💬'
    }
]


# ==================== 路由 ====================

@app.route("/")
def home():
    posts = BLOG_POSTS[:6]  # 首页显示前6篇
    return render_template("index.html", posts=posts, features=FEATURE_CARDS)


@app.route("/blog")
def blog_list():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    start = (page - 1) * per_page
    paginated_posts = BLOG_POSTS[start:start + per_page]
    total_pages = (len(BLOG_POSTS) + per_page - 1) // per_page

    return render_template("blog_list.html",
                           posts=paginated_posts,
                           page=page,
                           total_pages=total_pages)


@app.route("/blog/<slug>")
def blog_post(slug):
    post = next((p for p in BLOG_POSTS if p['slug'] == slug), None)
    if not post:
        return render_template("404.html"), 404
    related_posts = [p for p in BLOG_POSTS if p['id'] != post['id']][:2]
    return render_template("blog_post.html", post=post, related_posts=related_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")


@app.route("/learning")
def learning():
    # 按分类组织学习内容
    categories = {}
    for post in BLOG_POSTS:
        cat = post['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(post)

    return render_template("learning.html", categories=categories, posts=BLOG_POSTS)


@app.route("/category/<name>")
def category(name):
    posts = [p for p in BLOG_POSTS if p['category'] == name]
    return render_template("category.html", category_name=name, posts=posts)


@app.route("/tag/<tag>")
def tag(tag):
    posts = [p for p in BLOG_POSTS for t in p['tags'] if t == tag]
    return render_template("tag.html", tag_name=tag, posts=posts)


@app.route("/sitemap")
def sitemap():
    return render_template("sitemap.html", posts=BLOG_POSTS)


@app.route("/robots.txt")
def robots_txt():
    return send_from_directory(app.root_path, "robots.txt")


@app.route("/sitemap.xml")
def sitemap_xml():
    return send_from_directory(app.root_path, "sitemap.xml")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)python-3.11.7