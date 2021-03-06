# genetic-algorithm-sample

# 概要

- 遺伝的アルゴリズム（GA, Genetic Algorithm）のサンプルを実装しました。
- 基本的には[Qiita の記事](https://qiita.com/Azunyan1111/items/975c67129d99de33dc21)を参考にしながら実装しました。

# 実装上の変更点

- params.py でパラメータを変更(.env のようなものです。)
- gene クラス内関数 set_evl（引数なしで self.genes から直接評価値を計算しています）-> よって main.py の evaluation 関数削除
- 内包表記に変更（コードの見通しは良くなったと思う）

# 今後の改良

- gene クラス内関数 set_genes 実行で self.evl も更新されるように変更
- 選択や交叉にも色々な手法があるようなので、それらも実装できると面白そう。(本実装では、選択->優秀な N 件(params.SELECT_GENE)を選択(エリート選択)、交叉->2 点交叉)
- バイナリの遺伝情報ではなく、幅のある遺伝情報でチャレンジしたい。

# gene.py

- gene_status --- 遺伝子の二値情報(\[0,1,1,0,0,0,1,...\])とその評価値(各遺伝子情報の平均値)を持つクラス

# params.py

- GENE_LENGTH --- 1 遺伝子の情報の長さ
- MAX_GENE_GROUP --- 1 世代の遺伝子集団規模
- SELECT_GENE --- 選択で選ばれる遺伝子の数(次世代に受け継ぐ優秀な遺伝子の数)
- INDIVIDUAL_MUTATION --- 1 遺伝子に起こる突然変異の確率
- GENE_MUTATION --- 1 遺伝子の中の 1 ステータスに起こる突然変異の確率
- MAX_GENERATION --- 世代交代の最大数

# main.py

1. 初代の遺伝子集団（第一世代）をランダムに作成
2. 遺伝子集団の中からエリート選択と 2 点交叉を行う
3. 現在の遺伝子集団から下位 N 件（エリート選択数とエリートによる交叉が集団に入るのに必要な数）を削除
4. 遺伝子集団にエリートと交叉遺伝子を追加し 2 に戻る
