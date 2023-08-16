# OrganizationとAPI keyを.envから読み込む関数
# 依存ライブラリ: python-dotenv
# .envファイルの中身:
# OPENAI_ORGANIZATION = org-xxxxxxxxxxxxxxxxxxxxxxxx
# OPENAI_API_KEY = sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def get_openai_vars():
    # .envファイルから環境変数を読み込む
    import os
    from dotenv import load_dotenv
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    # 環境変数から値を取得する
    organization = os.environ.get("OPENAI_ORGANIZATION_ID")
    api_key = os.environ.get("OPENAI_API_KEY")
    return organization, api_key

# 初期化
import openai
organization, api_key = get_openai_vars()
openai.organization = organization
openai.api_key = api_key

# Modelをすべて出力
l = openai.Model.list()
print('Model ----------------------------------')
for idx, item in enumerate(l["data"]):
    print('{}: {}'.format(idx, item["id"]))
# アカウントの問題でgpt-4はまだ有効になっていない(2023/8/17時点)

print('') # 改行

# openai.ChatCompletionのテスト
print('ChatCompletion -------------------------')
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "あなたは平成一桁年代のJ-POPのマニアとしてふるまってください。"},
        {"role": "user", "content": "1990年のヒット曲はなんですか？"},
        {"role": "assistant", "content": "米米CLUBの「浪漫飛行」です。"},
        {"role": "user", "content": "その頃の米米CLUBの他の代表曲を3つ挙げてください。"}
    ]
)
print(response)

print('') # 改行

# チャット本文だけ抜粋する
print('content --------------------------------')
content = response["choices"][0]["message"]["content"].strip()
print(content)
print('----------------------------------------')
