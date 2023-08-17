# openai-test

OpenAI APIのサンプルコードを試すためのテストプロジェクト。
ChatCompletion、Imageを試している。
API keyは実行環境の.envに保存したものを読み込む。

## 環境構築

```sh
conda create -n openai python=3.10
conda activate openai
conda install openai python-dotenv
# 生成した画像をPythonから表示する場合
conda install opencv
```
